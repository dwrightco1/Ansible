#!/usr/bin/python
################################################################################
# Cloud-Manager: a simple wrapper around Ansible for managing
#                virtual infrastructure accross many public and privte clouds.
#                CM provides a common CLI syntax to desribe virtual infrastructure
#                regardless of the underlying virtualization or cloud technology.
#
# @author:       dan@raindanceit.com
# @contributors: eric@raindanceit.com
# @copyright:    Fast Access Technologies, LLC (dba Raindance) 2015, 2016
# @license:      GPL
################################################################################

# import ansible module
from ansible.module_utils.basic import AnsibleModule
import requests
import json

# function to create IAC organization
def iac_org_present(data):  
  # invoke api to create organization (which is anynchronous api method)
  url = data['cm_api']
  headers = { "Content-Type": "application/json"}
  url = "{}{}" . format(url, '/v0.1/organizations')
  result = requests.post(url, json.dumps(data), headers=headers)

  # handle HTTP 201
  if result.status_code == 201:
    meta = { "msg": "job submitted (asynchronous method)", "result": result.status_code}
    return False, True, meta

  # handle HTTP 400
  if result.status_code == 400:
    meta = { "msg": "HTTP 400: request body invalid", "result": result.status_code}
    return False, False, meta

  # handle HTTP 409
  if result.status_code == 409:
    meta = { "msg": "HTTP 409: organization already exists", "result": result.status_code}
    return False, False, meta

  # handle HTTP 201
  if result.status_code == 500:
    meta = { "msg": "HTTP 500: internal server error", "result": result.status_code}
    return False, False, meta

  # handle unknown HTTP status code2
  meta = {
    "msg": "unknown return code from api call",
    "result": result.status_code,
    "module.params": data,
    "iac_endpoint": url
  }
  return (False, False, meta)

# function to remove IAC organization
def iac_org_absent(data):  
  # initialize org_id
  org_id = 0

  # invoke api to lookup organization ID
  url = data['cm_api']
  headers = { "Content-Type": "application/json"}
  url = "{}{}" . format(url, '/v0.1/organizations/')
  result = requests.get(url)

  # parse result
  jdata = result.json()
  for r in jdata:
    if r['name'] == data['name']:
      org_id = r['id']

  # validate organization was found
  if org_id == 0:
    meta = { "msg": "organization not found" }
    return (False, False, meta)

  # invoke api to delete organization (by ID)
  url = data['cm_api']
  url = "{}{}{}" . format(url, '/v0.1/organizations/', org_id)
  result = requests.delete(url)

  # handle HTTP 204
  if result.status_code == 204:
    meta = { "msg": "organization deleted successfully" }
    return (False, True, meta)

  # handle HTTP 404
  if result.status_code == 404:
    meta = {
      "msg": "organization not found, id = {}".format(org_id),
      "url": url
    }
    return (False, False, meta)

  # handle HTTP 500
  if result.status_code == 500:
    meta = { "msg": "internal server error" }
    return (False, False, meta)

  # handle unknown HTTP status code2
  meta = {
    "msg": "unknown return code from api call",
    "result": result.status_code,
    "module.params": data,
    "iac_endpoint": url
  }
  return (False, False, meta)

# entry point into the module
def main():
  # define required/optional fields for module
  fields = {
    "name": {"required": True, "type": "str" },
    "cm_api": {"required": True, "type": "str" },
    "fullName": {"required": True, "type": "str" },
    "vSpheres": { "required": True, "type": "dict" },
    "state": {
      "default": "present",
      "choices": ['present', 'absent'],  
      "type": 'str' 
    },
  }

  # map ansible states to functions
  choice_map = {
    "present": iac_org_present,
    "absent": iac_org_absent, 
  }

  # instantiate ansible module
  module = AnsibleModule(argument_spec=fields)

  # call state-dependent function to create/delete IAC organization
  is_error, has_changed, result = choice_map.get(module.params['state'])(module.params)

  # return response to caller
  if not is_error:
    module.exit_json(changed=has_changed, meta=result)
  else:
    module.fail_json(msg="An error occured", meta=result)

# call main (if running standalone)
if __name__ == '__main__':  
  main()

