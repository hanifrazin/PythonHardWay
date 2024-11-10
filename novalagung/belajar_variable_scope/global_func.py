my_var = 12

def task_one():
    all_global_vars = globals()
    print(type(all_global_vars))
    print(all_global_vars.get('my_var'))

task_one()