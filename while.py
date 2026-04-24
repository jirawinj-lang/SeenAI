secret_number = 5
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        break
    else:
        print("Sorry, you failed")


weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ')
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"you are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"you are {converted} pounds")
print("Seen so genious hihihaahahah")


secret_number = 9
guess_count = 0
guess_limitl = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        print("congratulation for your win!!!")
    else:
        print("Sorry, you failed!!!")


weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ')
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight * 0.45
    print(f"You are {converted} pounds")


    your_old = input('What is your birth year: ')
    print(2026 - int(your_old))





