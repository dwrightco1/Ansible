# Ansible
Here are some projects I've built over the last year or so working with Ansible

##IAC Organization Module

The module code is located in modules/iac_org/
* iac_org.py is the module

The playbook code is located in playbooks/iac_org.yml
* iac_org.yml is a sample playbook that calls the module

This module creates and deletes organizations in Raindance IAC
* It uses proper Ansible semantics for modules
* It is idempotent

To run:

$ ansible-playbook -i inventory/hosts playbooks/iac_org.yml

Sample output is in modules/iac_org/sampleRun.txt
