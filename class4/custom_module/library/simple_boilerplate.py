#!/usr/bin/python

# import requests
# import json
import urllib3
from ansible.module_utils.basic import AnsibleModule

# Ignore self-signed certificate warnings (note, this is a security issue)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def run_module():

    # Define the arguments
    module_args = dict()

    # Initialize AnsibleModule object with the arguments
    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)

    # Logic for interfacing to checkpoint management API including login/auth handling

    # Return the execution results
    results = {
        "changed": False,  # mandatory
        "failed": False,  # optional
        "msg": response.json(),
    }
    module.exit_json(**results)


def run_python():
    """Alternate Python execution path that uses similar code for testing/debugging."""
    mgmt_host = "chkpnt-pod1.lasthop.io"
    user = "admin"
    password = "INVALID"

    base_url = f"https://{mgmt_host}/web_api"

    # import pdb; pdb.set_trace()

    print(response.json())


def main():
    # Toggle between Ansible code or Python code
    run_module()
    # run_python()


if __name__ == "__main__":
    main()
