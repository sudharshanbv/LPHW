


def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)
print ("with a starting point of : {}".format(start_point))
print(f"we'd have {beans} beans, {jars}, jars, and {crates} crates.")

start_point = start_point / 10

print ("we can also do that this way: ")
formula = secret_formula(start_point)
print (type(formula))
print ("we'd have {} beans, {} jars, and {} crates.". format(*formula))
