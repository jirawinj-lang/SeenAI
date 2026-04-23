

weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ')
if unit.upper() == "L":
        converted = weight * 0.45
        print(f"You are {converted} kilos")
else:
        converted = weight / 0.45
        print(f"you are {converted} pounds")

is_hot = False
is_cold = True

if is_hot:
        print("it's a hot day")
        print("drink some water")
else:
        print("it's a cold day")
        print("wear warm clothes")
print("enjoy lovely day")