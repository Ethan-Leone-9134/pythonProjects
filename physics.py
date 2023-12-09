def print_all_variables_in_global_scope():
    global_vars = globals()
    for var_name, var_value in global_vars.items():
        if not var_name.startswith("__"):  # Exclude system variables
            print(f"{var_name}: {var_value}")

def clear_global_variables():
    global_vars = globals()
    vars_to_delete = [var_name for var_name in global_vars if not var_name.startswith("__")]
    for var_name in vars_to_delete:
        del global_vars[var_name]


def clear():
    clear_global_variables()

#%%%# Running code #%%%#
# Example usage:
a = 5
c = [1, 2, 3]
de = 124 * 124 / 95
b = 1298345




#%%%# End of Script #%%%#
print_all_variables_in_global_scope()