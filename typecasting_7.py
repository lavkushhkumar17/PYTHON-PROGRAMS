# Type Casting in Python


#general
"""a="1"
b="2"
print(a+b) 
c=1
d=2
print(c+d)"""


"""TYPECASTING= conversion of one datatype into another datatype.
  * python support wide variety of functions like:- int(), float(), str(), hex(), oct(), tuple(), dict(), etc."""

"""a="1"
b="2"
print(int(a)+int(b))"""


#TWO TYPES :-
"""1{EXPLICIT TYPECASTING}=conversion of one datatype into another datatype done via developer or programmers.
   functions support = int(),float(),hex(),oct(),str()  etc."""
"""a="15"  #throws an error if the string is not a valid integer
num=7
a_num=int(a)
sum=num+a_num
print("the sum of both the numbers is:",sum)"""

"""2{IMPLICIT TYPECASTING}=conversion of one datatype into another datatype done via PYTHON interpreter itself(automatically)
   * but in order= from small datatype into higher datatype"""
"""c=1.9
d=8
print(c+d)
  int and float gives float beacause to prevent data loss"""

