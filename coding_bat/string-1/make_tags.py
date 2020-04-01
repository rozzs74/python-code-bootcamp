#The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. In this example, 
# the "i" tag makes <i> and </i> which surround the word "Yay". 
# Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".

# Author: John Royce Punay
# Date created: March 30, 2020 7:00 PM

# make_tags('i', 'Yay') → '<i>Yay</i>'
# make_tags('i', 'Hello') → '<i>Hello</i>'
# make_tags('cite', 'Yay') → '<cite>Yay</cite>'


def make_tags1(tag, content):
	front_delimeter = "<{}>".format(tag)
	end_delimiter = "/<{}>".format(tag)
	return front_delimeter + content + end_delimiter

a = make_tags1("i", "john")
print("Make tags solution 1: ", a)

def make_tags2(tag, content):
	return "<{}>{}</{}>".format(tag ,content ,tag)

b = make_tags2("script", "royce")
print("Make tags solution 2: ", b)

def make_tags3(tag, content):
	return f"<{tag}>{content[:]}</{tag}>"
c  = make_tags3("i", "punay")
print("Make tags solution 3: ", c)