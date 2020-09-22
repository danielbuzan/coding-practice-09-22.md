]name = input("What is your name? ")
age = int(input("How old are you? "))
print(f"Your name is {name}")
print(f"You are {age} years old")

age = int(input("what is your age? "))
if age < 18:
  print("you cannot vote at this age")
else:
    print("You can vote at this age")

cost = float(input("What is the cost of an apple?  $"))
quantity = int(input("How many apples do you wish to purchase? "))
Total = cost * quantity
print(f"Your total cost is ${Total}")



w = input("Enter Word ")
i = 0
while i < len(w):
  char = w[i]
  print(char)
  i += 1

i = len(w)
while i <= len(w):
 if w[i] == 'e':
    print(f"found an e at index {i}")
