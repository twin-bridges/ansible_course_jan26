#!/usr/bin/python
import requests
import urllib3
import json
from ansible.module_utils.basic import AnsibleModule

# Ignore self-signed certificate warnings (note, this is a security issue)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def chkpnt_login(base_url, user, password, ssl_verify=False):
    """Login to the Mgmt API."""

    endpoint = "login"

    # Use "read-only" to avoid locking the database
    login_payload = {"user": user, "password": password, "read-only": True}
    response = chkpnt_api(base_url=base_url, endpoint=endpoint, payload=login_payload, ssl_verify=ssl_verify)
    return response
    # session_id = login_data.get("sid")


def chkpnt_api(base_url, endpoint, payload, session_id=None, ssl_verify=False):
    """
    ssl_verify=False is a security issue (ensure this is appropriate in your context).
    """
    url = f"{base_url}/{endpoint}"
    headers = {"Content-Type": "application/json"}
    if session_id:
        headers["X-chkp-sid"] = session_id

    # CheckPoint uses POST even for information retrieval operations
    response = requests.post(
        url, data=json.dumps(payload), headers=headers, verify=ssl_verify
    )
    return response


def run_module():

    # Define the arguments
    module_args = dict(
        host=dict(type="str", required=True),
        api_user=dict(type="str", required=True, no_log=False),
        api_password=dict(type="str", required=True, no_log=True),
    )

    # Initialize AnsibleModule object with the arguments
    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)

    # Logic for interfacing to checkpoint management API
    mgmt_host = module.params["host"]
    base_url = f"https://{mgmt_host}/web_api"

    user = module.params["api_user"]
    password = module.params["api_password"]

    #module.fail_json(msg="DEBUG DUMP", data=str(f"{user}\n{password}\n{base_url}"))
    response = chkpnt_login(base_url=base_url, user=user, password=password)
    # module.fail_json(msg="DEBUG DUMP", data=str(f"{response.json()}"))

    results = {
        "changed": False,  # mandatory
        "failed": False,  # optional
        "msg": response.json()
    }
    # response = [user]
    # results["msg"] = response

    #module.fail_json(msg="DEBUG DUMP", data=str(response))
    # module.fail_json(msg="DEBUG DUMP", data=str('test'))
    module.exit_json(**results)


def run_python():
    mgmt_host = "chkpnt-pod1.lasthop.io"
    user = "admin"
    password = "INVALID"

    base_url = f"https://{mgmt_host}/web_api"

    response = chkpnt_login(base_url=base_url, user=user, password=password)
    print(response)


def main():
    run_module()
    # run_python()


if __name__ == "__main__":
    main()
