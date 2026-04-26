secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print("You woun!")
        break
    else:
        print("You failed!!!")

    weight = int(input('Weight: '))
    unit = input('(L)bs or (K)g: ')
    if unit.upper() == "L":
        converted = weight * 0.45
        print(f"you are {converted} kilos")
    else:
        converted = weight / 0.45
        print(f"you are {converted} pounds")


        is_hot = True
        is_cold = False
        if is_hot:
            print("it's a hot day")
            print("get some drinks")
        elif is_cold:
            print("it's a cold day")
            print("wear war clothes")
        print("enjoy our day:) ")