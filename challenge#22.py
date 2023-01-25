def checkStepNumbers(system_names, step_numbers):
    system_steps = {}
    for system, step in zip(system_names, step_numbers):
        if system in system_steps:
            if step <= system_steps[system][-1]:
                return False
            system_steps[system].append(step)
        else:
            system_steps[system] = [step]
    return True

# Test case 1: Expected output: True
system_names = ["tree_1", "tree_2", "house", "tree_1", "tree_2", "house"]
step_numbers = [1, 33, 10, 2, 44, 20]
print(checkStepNumbers(system_names, step_numbers))

# Test case 2: Expected output: False
system_names = ["tree_1", "tree_1", "house"]
step_numbers = [2, 1, 10]
print(checkStepNumbers(system_names, step_numbers))