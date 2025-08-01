# Module 2 Literals, strings, floats, and integers

"""Through this example, you encounter two different types of literals:

a string, which you already know,
and an integer number, something completely new.
"""

print("2")
print(2)

""" If an integer number is preceded by an 0O or 0o prefix (zero-o), it will be treated as an octal value. 
This means that the number must contain digits taken from the [0..7] range only.

0o123 is an octal number with a (decimal) value equal to 83."""

print(0o123)  # 83

""" The second convention allows us to use hexadecimal numbers. Such numbers should be preceded by the 
prefix 0x or 0X (zero-x).

0x123 is a hexadecimal number with a (decimal) value equal to 291. The print() function can manage these values too. 
Try this:"""

print(0x123)  # 291

"""Coding floats
Let's see how this convention is used to record numbers that are very small (in the sense of their absolute value, 
which is close to zero).

A physical constant called Planck's constant (and denoted as h), according to the textbooks, has the value 
of: 6.62607 x 10-34.

If you would like to use it in a program, you should write it this way:"""

6.62607e-34

"""For example, let's say you've decided to use the following float literal:"""

0.0000000000000000000001
print(0.0000000000000000000001)  # 1e-22


"""Strings
Strings are used when you need to process text (like names of all kinds, addresses, novels, etc.), not numbers.

You already know a bit about them, e.g., that strings need quotes the way floats need points.

This is a very typical string: "I am a string."

However, there is a catch. The catch is how to encode a quote inside a string which is already delimited by quotes.

Let's assume that we want to print a very simple message saying:

I like "Monty Python"

How do we do it without generating an error? There are two possible solutions."""

print('I like "Monty Python"')
# -or-
print('I like "Monty Python"')

print("I'm Monty Python")
# -or-
print("I'm Monty Python")


"""  Boolean values
To conclude with Python's literals, there are two additional ones.

They're not as obvious as any of the previous ones, as they're used to represent a very abstract value - truthfulness.

Each time you ask Python if one number is greater than another, the question results in the creation of some 
specific data - a Boolean value.

The name comes from George Boole (1815-1864), the author of the fundamental work, The Laws of Thought, which 
contains the definition of Boolean algebra - a part of algebra which makes use of only two distinct values: 
True and False, denoted as 1 and 0

A programmer writes a program, and the program asks questions. Python executes the program, and provides the answers.
The program must be able to react according to the received answers.

Fortunately, computers know only two kinds of answers:

Yes, this is true;
No, this is false.

Python, then, is a binary reptile.

These two Boolean values have strict denotations in Python:

True
False

You cannot change anything - you have to take these symbols as they are, including case-sensitivity.

Challenge: What will be the output of the following snippet of code?"""

print(True > False)  # True
print(True < False)  # False

"""Lab"""

print('""I\'m""\n', '""learning""\n', '""Python""')  # Using \n to minimize print calls

""" Arithmetic operations"""
