"""
KRZYSZTOF THE SH!T-TALKING ROBOT

Author: Benji Gifford
Class: CSI-160-02
Assignment: Conversation with a Computer
Due Date: 9/13/2021

Certification of Authenticity:
I certify that this is entirely my own work, except where I have given
fully-documented references to the work of others. I understand the definition
and consequences of plagiarism and acknowledge that the assessor of this
assignment may, for the purpose of assessing this assignment:
- Reproduce this assignment and provide a copy to another member of academic
- staff; and/or Communicate a copy of this assignment to a plagiarism checking
- service (which may then retain a copy of this assignment on its database for
- the purpose of future plagiarism checking)
"""

name = input('What is your name?\n')
print('Hi, %s.' % name)
print("My name is Krzysztof") 

while True:
    try:
        age=eval(input("How old is your dad? ")) #the machine begins sh!t-talking
        print ("Your dad's age in centuries is",age)
        break;
    except NameError:
        print ("Invalid input, jackass")
print('Absolute fossil of a man. You got an old ass dad, %s.' %name)  #reusing the user's name
print("I could beat his",age)
print("century old ass.") 

word = input('Guess how long my name is. I bet its longer than yours') #the 2nd operation
word_len = len(word)
if (word_len > 9 or word_len < 9):
    print('Nope forehead its not '+ word + ' letters long. You buggin bro.')
else:
    print('Yeah thats right i got a long ass name')

base = float(input('Whats your shoe size, nerd?')) #another mathematical demonstration, area of a triangle
height = float(input('How tall are you in inches?'))
area = (base * height) / 2
print('If you were a triangle, you would have an area of', area, 'square inches. Pathetic.')

if (base < 14):
    print('Your shoe size is ', base,'. My mom could eat you for breakfast.') #one final insult
else:
    print('Damn bro you walk around with them ', base,'size ass flippers? Flip flopping all over the place and shi. Bet you can use them sh!ts as snowshoes.')
print("Aight im done see ya later pinhead")
