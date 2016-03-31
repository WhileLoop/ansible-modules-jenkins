## Intro

An ansible module which uses the jenkinsapi python library to idempotently manage Jenkins jobs. See the playbook jobs_example.yaml for usage example.

## Getting Started

Simply run 'vagrant up' to get started with a with Ubuntu VM with Jenkins and ansible installed. The provisioning script will execute the example playbook. Point your browser to http://localhost:8080 to access the Jenkins application.

## Example Output:

```
$ ansible-playbook job_example.yml
PLAY [jenkins jobs] ***********************************************************

TASK: [create job1] ***********************************************************
changed: [localhost]

TASK: [check job1 idempotency] ************************************************
ok: [localhost]

TASK: [modify job1] ***********************************************************
changed: [localhost]

TASK: [delete job1] ***********************************************************
changed: [localhost]

TASK: [create job2] ***********************************************************
changed: [localhost]

PLAY RECAP ********************************************************************
localhost                  : ok=5    changed=4    unreachable=0    failed=0
```
