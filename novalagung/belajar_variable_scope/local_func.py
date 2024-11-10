my_var = 12

def task_two():
    another_var = "Hello Python"

    all_local_vars = locals()
    print(type(all_local_vars))
    print(all_local_vars.get('another_var'))

    try:
        print(all_local_vars.get['my_var'])
    except Exception as err:
        print(f"error {err}")

task_two()