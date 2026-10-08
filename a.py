# example 1: boolean evaluation (corrected)
#0, none, false, [], '': false

a = 10 #true
b = 12 #true
c = 0 #false


if a and b and c: #T and T and F : T and F : F
    print("Hello")
else:
    print("Bye")

if a or b or c:#T or T or F : T or F : T
    print("Hello")
else:
    print("Bye")
if a and b and c: #T and T and F : T and F : F
    print("Hello")
else:
    print("Bye")

if a or b or c:#T or T or F : T or F : T
    print("Hello")
else:
    print("Bye")

if a and b or c:##T and T or F : T or F : T
    print("Hello")
else:
    print("Bye")

if a or b and c:##T or T and F : T or F : T
    print("Hello")
else:
    print("Bye")

