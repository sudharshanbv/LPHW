
def add(a, b):
    print(f"Adding {a} and {b}")
    return a+b

def sub(a, b):
        print(f"Subtracting {b} from {a}")
        return a - b

def mul(a, b):
        print(f"Multiplying {a} and {b}")
        return a * b

def div(a, b):
        print(f"Dividing {a} by {b}")
        return a / b


age	= add(30, 5)
height = sub(78, 4)
weight = mul(90, 2)
iq = div(100, 2)

print(f"Age: {age},	Height:	{height}, Weight: {weight},	IQ:	{iq}")

print("Here	is a puzzle.")

what = add(age, sub(height, mul(weight, div(iq, 2))))

print("That	becomes: ",	what)
