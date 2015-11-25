### Ansible Modules to Configure Jenkins

Currently one module is implemented which uses the jenkinsapi python library to idempotently manage Jenkins jobs. See the playbook jobs_example.yaml for usage example.

###### Example output:

```
$ ansible-playbook job_example.yml
PLAY [jenkins] ****************************************************************

TASK: [jenkins_job ] **********************************************************
changed: [127.0.0.1]

TASK: [jenkins_job ] **********************************************************
ok: [127.0.0.1]

TASK: [jenkins_job ] **********************************************************
changed: [127.0.0.1]

TASK: [jenkins_job ] **********************************************************
changed: [127.0.0.1]

PLAY RECAP ********************************************************************
127.0.0.1                  : ok=4    changed=3    unreachable=0    failed=0
```
