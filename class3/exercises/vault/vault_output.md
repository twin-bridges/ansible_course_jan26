```bash
$ cat group_vars/gaia/secrets.yml 
---
admin_pass: some_pass
expert_pass: expert_credentials
grub_pass: low_level_pass
```

```bash
# Use vault to encrypt the file
$ ansible-vault encrypt group_vars/gaia/secrets.yml 
Encryption successful
```

```bash
# Verify 'group_vars' file is now encrypted
$ cat group_vars/gaia/secrets.yml 
$ANSIBLE_VAULT;1.1;AES256
32613238313234343937623035356335656663383864356536323563616638643962373932333366
3161626564653137643265653632633539316362383133330a656431343461666533653034636365
36333432393836393065363564653439666133656331663732643536353638353366316662633730
3030333565373139300a303665383838373537356434306561613166373961356134643561623866
64383332303832633937346266353435616236323838363334316566613032306164363134303030
61393164663639393664383635346131346630376237346434353837376630653661343838373830
34303630646461623763646437386630653133306562333733393636356563623733326433653036
33306134643766313138333631303963626630303635653361663865373466306537646661333535
3965
```

```bash
# Verify playbook runs properly (even with encrypted 'group_vars' file)
$ ansible-playbook vault_ex.yml 

PLAY [Basic Gaia Playbook] *********************************

TASK [ansible.builtin.debug] *******************************
ok: [pod99-gaia] => {
    "msg": "Admin Password: \"some_pass\"\nExpert Password: \"expert_credentials\"\nGrub Password: \"low_level_pass\"\n"
}

PLAY RECAP *************************************************
pod99-gaia                 : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```
