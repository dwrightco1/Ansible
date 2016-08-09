# Ansible
There are some projects I've built over the last year or so working with Ansible

##IAC Organization Module

The code is located in modules/iac_org
* iac_org.py is the module (place in library path)
* iac)org.yml is a sample playbook that calls the module

This module creates and deletes organizations in Raindance IAC
* It uses proper Ansible semantics for modules
* It is idempotent

Here's a Sample Run

##$ ansible-playbook -i inventory/hosts iac_org.yml

PLAY [localhost] ***************************************************************

TASK [setup] *******************************************************************
ok: [localhost]

TASK [create IAC organization] *************************************************
changed: [localhost]

TASK [debug] *******************************************************************
ok: [localhost] => {
    "create_result": {
        "changed": true,
        "meta": {
            "msg": "job submitted (asynchronous method)",
            "result": 201
        }
    }
}

TASK [delete IAC organization] *************************************************
changed: [localhost]

TASK [debug] *******************************************************************
ok: [localhost] => {
    "delete_result": {
        "changed": true,
        "meta": {
            "msg": "organization deleted successfully"
        }
    }
}

PLAY RECAP *********************************************************************
localhost                  : ok=5    changed=2    unreachable=0    failed=0
