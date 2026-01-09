### Role exercise

Create a role named 'address_range'. 

In this role you should configure three address ranges. The address ranges should be stored as a variable(s) in ./vars/main.yml (in the role).

The 'tasks/main.yml' should contain only two tasks: 

```yaml
- name: Configure Address Ranges
  ansible.builtin.import_tasks: cfg_address_ranges.yml
- name: Display Address Ranges
  ansible.builtin.import_tasks: display_address_ranges.yml
```

The tasks specified in 'cfg_address_ranges.yml' should configure the three address ranges that are stored in ./vars/main.yml. The three address ranges should be:

```yaml
 name: Test Address Range 1
 ip_address_first: 192.168.201.1
 ip_address_last: 192.168.201.10
```

```yaml
 name: Test Address Range 2
 ip_address_first: 192.168.202.1
 ip_address_last: 192.168.202.10
```

```yaml
 name: Test Address Range 3
 ip_address_first: 192.168.203.1
 ip_address_last: 192.168.203.10
```

The format and arguments of the 'cp_mgmt_address_range' module is:

```yaml
- name: Add address ranges
  check_point.mgmt.cp_mgmt_address_range:
    color: dark green   # Some valid color
    ip_address_first: 10.1.1.1
    ip_address_last: 10.1.1.10
    name: My Address Range
    state: present
```

The tasks specified in 'display_address_ranges.yml' should retrieve and display the currently configured address ranges.

The format of 'cp_mgmt_address_range_facts' is:

```yaml
- name: Get address range objects
  check_point.mgmt.cp_mgmt_address_range_facts:
  register: address_range_out
```

You should create and use a handler in 'handlers/main.yml' to execute a publish action if the 'cfg_address_ranges.yml' results in a change.

