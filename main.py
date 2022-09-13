print("Hi, I am so excited to talk to you today!")

user_input = input()
bot_name = "Jack"
name1 = input("What is your name? ") 
if user_input ==  bot_name:
  print("Wow! We have the same name, what a chance")
print("Nice to meet you " + name1 + ", my name is Jack")
user_input = input("How are you feeling today " + name1 + "?")
print("it is nice to feel " + user_input)
age1 = input("How many years it has been since you born? ")
if user_input == "18":
  print("Wow , now you are a young person")
elif user_input == "16":
  print("Wow, You are eligible to drive now")
else:
  print(age1 + " is a good age")
country = input("Where are you from?")
if user_input == "Turkey":
  print("You can't be serious, I am from" + country + " too")
else:
  print("I have been in " + country + " for once.")
Q = input("Do you have any questions or have something to say? ")
if user_input == "no":
  breakpoint
elif user_input == "yes":
  print("But it is timeto live, bay bay")