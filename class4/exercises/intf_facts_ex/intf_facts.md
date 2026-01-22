### Interface Facts and GW UID Retrieval

Construct a playbook that connects to your podX-mgmt host. This playbook will execute the 'cp_mgmt_interface_facts' module.

This module requires both the interface name and the firewall UID.

```yaml
check_point.mgmt.cp_mgmt_interface_facts:
  name: eth0
  gateway_uid: "{{ gw_uid }}"
```

Consequently, you will need to retrieve the gw_uid. You should accomplish this using include_tasks or import_tasks.

In order to retrieve the 'gw_uid' execute the 'check_point.mgmt.cp_mgmt_show_gateways_and_servers'. For the purposes of this example assume that you might have multiple gateways connected connected to the Mgmt Server.

Loop over the returned gateways and search for the gateway whose 'name' matches the existing 'fw_name' variable. Once you match the gateway save the gateway's uid into the 'gw_uid' variable.

Now back in your main playbook execute the 'cp_mgmt_interface_facts' using the 'gw_uid' variable and save the result.

From this returned 


    - name: Interface output
      ansible.builtin.debug:
        msg: "{{ intf_out }}"
