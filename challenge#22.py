def checkStepNumbers(systemNames, stepNumbers):
    systemSteps = {}
    for system, step in zip(systemNames, stepNumbers):
        if system in systemSteps:
            if step <= systemSteps[system][-1]:
                return False
            systemSteps[system].append(step)
        else:
            systemSteps[system] = [step]
    return True

# True
system_names = ["tree_1", "tree_2", "house"]
step_numbers = [1, 33, 10]
print(checkStepNumbers(system_names, step_numbers))

# False
system_names = ["tree_1", "tree_1", "house"]
step_numbers = [2,1,10]
print(checkStepNumbers(system_names, step_numbers))