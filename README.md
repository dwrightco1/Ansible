# Ansible
Here are some projects I've built over the last year or so working with Ansible

##IAC Organization Module

The code is located in modules/iac_org/
* iac_org.py is the module (place in library path)
* iac_org.yml is a sample playbook that calls the module

This module creates and deletes organizations in Raindance IAC
* It uses proper Ansible semantics for modules
* It is idempotent

You can view a sample run in modules/iac_org/samleRun.txt

##Component Manager

The code is located in component-manager/
* The main executable is iac-component-mgr
* Here is the usage statement

usage: ./iac-component-mgr <start [bootOnly]|stop|destroy|status> -g <all>|<group [group ...]>

  - <start>    : start IAC cluster component VMs (build VMs if needed)
  - <stop>     : suspend one or more components in an IAC cluster
  - <destroy>  : stop IAC cluster and destroy component VMs
  - <status>   : show status of component VMs

You can view a sample run in component-manager/samleRun.txt
