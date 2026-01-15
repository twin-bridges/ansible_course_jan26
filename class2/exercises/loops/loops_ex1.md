### Loops Exercise 1

Create a playbook and uses a host of 'localhost'.
1. Create a task1 with a name of 'Simple loop' use 'ansible.builtin.debug' and a loop structure to print out the name of four firewalls (for example, 'fw1, fw2, fw3, fw4').
2. Create a variable in the vars section with a name of 'my_firewalls'. This 'my_firewalls' variable should be a list of four firewall names. Create a task2 that loops over 'my_firewalls' and prints out the names of the four firewalls ('debug' module).
3. In the vars section create the following dictionary named 'firewall_dict':

   ```yaml
   firewall_dict:
     name: fw1 
     location: Munich
     ip_address: 1.1.1.1
     sw_version: R82
   ```

   Create a task3 that loops over this dictionary and prints out both the 'key' and the 'corresponding' value for each key-value pair in the dictionary.
4. In the vars section of the playbook create a variable named 'fw_list' which is a list of dictionaries and looks as follows:

   ```yaml
   fw_list:
     - {name: fw1, location: Munich, ip_address: 1.1.1.1, sw_version: R82 }
     - {name: fw2, location: Munich, ip_address: 1.1.1.2, sw_version: R82 }
     - {name: fw3, location: Cologne, ip_address: 10.1.1.1, sw_version: R81.10 }
     - {name: fw4, location: Cologne, ip_address: 10.1.1.2, sw_version: R81.10 }
   ```

   Create a task that loops over this list and prints out the name, location, IP address, and software version. Use 'loop_control' and 'label: " "' to reduce the clutter in the output.

