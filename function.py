def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcom to our company")


print("start")
greet_user("The ceo of OpenAI", "Seen jirawin")
print("finish")





# Function for another way
def attack(i, p):
    print(f'target is {i} and {p}')

url = "10.10.10.10"
ip = "Domain.com"
attack(url, ip)



# Create program that calculate the sqft of a room
# make a function that calculates two parameters that are passed in
# take an input for width and height as variables
# mutiple w * h 
# print the final sqft




print("Please enter the dimensions of the room in s qft")

def calculate_area(w, h):
    area_sqft = w * h
    print(f'The total is {area_sqft}')


width = int(input("Take your room width: "))
height = int(input("Take your room hight: "))

calculate_area(width, height)