import time

print('Hello, welcome to Cody Savage Coffee!!!')
name = input('What is your name?\n')
print("Hello, " + name + ", thank you so much for coming in today!\n")

menu = "black coffee, latte, mocha, white girl drink"

print(name + ", what would you like from our menu today? Here is what we are serving.\n\n" + menu)

order = input()

print("Awesome, " + name + ". I'll get that " + order + " ready for you in a few minutes!")
time.sleep(4)
print("Thank you! Hope to see you again!")


