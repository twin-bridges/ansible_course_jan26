
### Part a

Convert 'includes_imports1, part a' over to use "import_tasks" instead of "include_tasks". Where do you need to relocate the loop for proper execution?

### Part b

Try to convert 'includes_imports1, part b' over to use "import_tasks" instead of "include_tasks" while using a variable from inventory. 

Will you be able to do this? Why not? 

How could you use a variable for the file name while still using "import_tasks"? Hint, what are some other variable locations besides inventory where you could define the sub-tasks file name?

### Part c

Convert 'includes_imports1, part c' over to use "import_tasks" instead of "include_tasks". 

If no tags are defined in the main playbook (i.e. on the "import_tasks" task), then what happens upon ansible-playbook execution (in other words, you pass in a "tag" via ansible-playbook and that tag only exists in the sub-task file)? Does the sub-task execute or not? 

