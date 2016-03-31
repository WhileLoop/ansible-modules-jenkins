#!/usr/bin/python
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

DOCUMENTATION = ''''
'''

try:
    import jenkinsapi
    from jenkinsapi.jenkins import Jenkins
except ImportError:
    print "failed=True msg='jenkinsapi required for this module'"
    sys.exit(1)

# TODO: try catch here
from formencode.doctest_xml_compare import xml_compare
from lxml import etree

def main():

    # TODO: specify requirements and check inputs.
    module=AnsibleModule(
        argument_spec=dict(
            host=dict(),
            state=dict(),
            name=dict(),
            template=dict(),
        )
    )

    host = module.params['host']
    state = module.params['state']
    name = module.params['name']
    template = module.params['template']

    # TODO: try catch here
    J = Jenkins(host)

    # TODO: try catch here
    # TODO: how to handle paths?
    if (template):
        txt = open(template)
        job_config = txt.read()
        job_config_xml = etree.fromstring(job_config)

    # There are 4 possible outcomes: created, updated, deleted, nochange.
    if (state == 'present'):
        # If the desired state is present we must check if the job exists and then check if the job has changed.
        if (J.has_job(name)):
            # The job exists so we must compare the XMLs for changes and update if they don't match.
            current_conf = J[name].get_config()
            current_conf = current_conf.encode('ascii','replace')
            current_conf_xml = etree.fromstring(current_conf)
            if (xml_compare(job_config_xml, current_conf_xml)):
                module.exit_json(msg="job exists", changed=False)
            else:
                J[name].update_config(job_config)
                module.exit_json(msg="job updated", changed=True)
        else:
            new_job = J.create_job(name, job_config)
            module.exit_json(msg="job created", changed=True)
    elif (state == 'absent'):
        if (J.has_job(name)):
            J.delete_job(name)
            module.exit_json(msg="job deleted", changed=True)
        else:
            module.exit_json(msg="job does not exist", changed=False)

    module.exit_json(msg=J.version, changed=False)

# import module snippets
from ansible.module_utils.basic import *
if __name__ == '__main__':
    main()
