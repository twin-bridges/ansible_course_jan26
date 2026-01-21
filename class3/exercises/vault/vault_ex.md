### Ansible Vault Exercise

Create a group_vars/gaia/secrets.yml file that contains the following:

```yaml
---
admin_pass: some_pass
expert_pass: expert_credentials
grub_pass: low_level_pass
```

Use 'ansible-vault' to encrypt this group_vars/gaia/secrets.yml file.

Verify using 'cat' that the secrets.yml is now encrypted.

Create a simple playbook using host podX-gaia (where 'X' is your pod). The playbook should have a single task which does the following:

```yaml
    - ansible.builtin.debug:
        msg: |
          Admin Password: "{{ admin_pass }}"
          Expert Password: "{{ expert_pass }}"
          Grub Password: "{{ grub_pass }}"
```

Verify that your playbook executes and properly displays those three variables (even though they have been encrypted in the groups_vars file).

I recommend that you specify the following in your 'defaults' section of your .ansible.cfg file.

```bash
vault_password_file = ~/.vault_pass
```

You will then need to create this ~/.vault_pass file using your editor. For example, my ~/.vault_pass looks as follows:

```bash
$ cat ~/.vault_pass 
mytestpass
```

