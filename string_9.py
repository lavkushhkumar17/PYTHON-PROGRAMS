#to demonstrate string performance in python
# we can use both type ("") , ('') to create string in python

# single line string  ("") ('')
'''name="lavkush"
friend='hassan'
anotherfriend="salim"
print("hello "+name)
print("hello "+friend)
print("hello "+anotherfriend)'''

"""apple1="he said,"i want to eat apple"  they give syntax error because of double quotes inside double quotes
print(apple1)"""
'''apple2="he said,\"i want to eat apple"
apple3='he said,i want to eat apple'
print(apple2)
print(apple3)'''


#multi line string ('''  ''') ("""  """)
"""intro='hello my name is lavkush 
i am a python developer
i am pusuing my career in python programming'
print(intro)      this give syntax error"""


#intro1='''hello my name is lavkush 
#i am a python developer
#i am pusuing my career in python programming'''
#print(intro1)

#intro2="""hello my name is lavkush 
#i am a python developer
#i am pusuing my career in python programming"""
#print(intro2)   


# {ACCESSING STRING CHARACTERS}
# we can access string characters by using index number

"""name="lavkush"
print(name[0])  # prints the first character
print(name[1])  # prints the second character
print(name[2])  # prints the third character
print(name[3])  # prints the fourth character
print(name[4])  # prints the fifth character
print(name[5])  # prints the sixth character
print(name[6])  # prints the seventh character
print(name[7])  # prints the eighth character #"lavkush" has only 7 characters so index 7 will give error"""

'''name="lavkush"
print(name[0])  # prints the first character
print(name[1])  # prints the second character
print(name[2])  # prints the third character
print(name[3])  # prints the fourth character
print(name[4])  # prints the fifth character
print(name[5])  # prints the sixth character
print(name[6])  # prints the seventh character'''


#{LOOPING THROUGH STRING}
'''name1="lavkush"
for i in name1:
    print(i)'''


'''name2="my name is lavkush"
for i in name2:
    print(i)'''

#{STRING SLICING}=OPERATION ON STRING TO GET SUBSTRING
'''name="my name is , lavkush"
print(name[0])
print(name[0:5])
print(name[11])
print(len(name))'''

"""fruit="mango"
len1=len(fruit)
print("mango is a", len1, "letter word")
print(type(fruit))"""


# SLICING = 
"""fruit="mango"
print(fruit[0:3])
print(fruit[1:4])
print(fruit[:])
print(fruit[0])
print(fruit[0:-3]) #[0:len(fruit)-3] = [0:5-3] = [0:2] = ma
mangolen=len(fruit)
print(mangolen)
print(len(fruit))
print(fruit[-1:-3]) #[5=1:5-3]=[4:2] not executable
print(fruit[-3:-1])  #[5-3:5-1]= [2:4]=ng"""

'''nm="kumar"
print(nm[-4:-2])'''

#{STRING METHODS}=string is immutable
'''a="lavkush"
print(len(a))
print(a.upper())
print(a.lower())
str1="abcDeFGHijKL"
print(str1.lower())
print(str1.upper())'''

'''a="lavkush!!!!"
a1="!!lavkush!!!lavkush!!!!"
b="!!!kumar!!!"
print(a.rstrip("!"))
print(b.rstrip("!"))  #only for last not for initial
print(a.replace("lavkush","gupta"))
print(a1.replace("lavkush","gupta"))
c="$lav !kush! @gup %ta!!!"
print(c.split())'''


'''a="lavkush"
print(a.capitalize())
b="introduction tO jS"
print(b.capitalize())
print(len(a))
print(len(b))'''


'''a="!!!lavkush $lavkush !!!kumar"
print(a.count("lavkush"))
print(a.endswith("kumar"))
b="welcome to the console"
print(b.endswith("to",4,10))'''

'''a="!!!lavkush $lavkush !!!kumar"
print(a.find("$"))
print(a.find("$a"))
print(a.find("lavkush"))
print(a.find("ar!!")) # value error'''


#{true or false type(is)}=
'''a="WelcomeToTHEcONSOLE"
print(a.isalnum())  #A-Z,a-z,0-9
print(a.isalpha())  #A-Z,a-z

b="hello"
print(b.islower())
print(b.isprintable())
c="hello\n"
print(c.isprintable())'''


"""a="   "
b=" "
print(a.isspace())
print(b.isspace())"""

"""a="World Health Organization"
print(a.istitle())
b="WORLD"
print(b.isupper())"""


'''a="World Health Organization"
print(a.startswith("World"))


b="pYTHON"
c="Python"
print(b.swapcase())
print(c.swapcase())


d="lifestyle consultancy private limited"
print(d.title()) '''