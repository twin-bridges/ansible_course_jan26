### Loops Exercise 2

Create a playbook that connects to your Check Point mgmt host.

1. The first task of this playbook should execute 'check_point.mgmt.cp_mgmt_simple_gateway_facts' and register the output from this task. This module will require a `name: "{{ fw_name }}"` argument.
2. From this output, extract the '.ansible_facts.simple_gateway.interfaces' which will be a list of interfaces. Save this list of interfaces to a new variable.
3. Add a task that loops over this list of interfaces and prints out the 'name', 'ipv4-address', and 'ipv4-network-mask' fields for 'eth0'. 

   Note, you should only print out the 'eth0' interface. The other interfaces should all be skipped. You should use a conditional to accomplish this.

