# Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".
# Author: John Royce Punay
# Date created: March 29, 2020 9:50 AM
# hello_name('Bob') → 'Hello Bob!'
# hello_name('Alice') → 'Hello Alice!'
# hello_name('X') → 'Hello X!'

def hello_name(name):
	return "Hello {}!".format(name)

def hello_name2(name):
	return "Hello" + " " + name + "!"

a = hello_name("Royce")
print(f"Solution 1 output {a}")
a = hello_name2("Royce")
print("Solution 2 output {}".format(a))

