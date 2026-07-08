#OPERATOR'S= special symbol used perform operations on variable and values

""" 1{ARITHMETIC OPERATORS}=
    + (Addition)
    - (Subtraction)
    * (Multiplication)
    / (Division)
    % (Modulus)
    ** (Exponentiation)
    // (Floor Division)"""
"""a=20
b=3
print("Addition of a and b is:",a+b)
print("Subtraction of a and b is:",a-b)
print("Multiplication of a and b is:",a*b)
print("Division of a and b is:",a/b)
print("Modulus of a and b is:",a%b)
print("Exponentiation of a and b is:",a**b)
print("Floor Division of a and b is:",a//b)"""


""" 2{COMPARISON OPERATORS(relational)}=
    == (Equal to)
    != (Not equal to)
    > (Greater than)
    < (Less than)
    >= (Greater than or equal to)
    <= (Less than or equal to)"""
"""a=10
b=30
print("Is a equal to b:",a==b)
print("Is a not equal to b:",a!=b)
print("Is a greater than b:",a>b)
print("Is a less than b:",a<b)
print("Is a greater than or equal to b:",a>=b)
print("Is a less than or equal to b:",a<=b)"""

""" 3{ASSIGNMENT OPERATORS}=
    = (Assign)
    += (Add and assign)
    -= (Subtract and assign)
    *= (Multiply and assign)
    /= (Divide and assign)
    %= (Modulus and assign)
    **= (Exponentiation and assign)
    //= (Floor division and assign)"""
"""a=10
b=20
print("Value of a is:",a)
print("Value of b is:",b)
a+=b
print("Value of a after addition and assignment is:",a)
a-=b
print("Value of a after subtraction and assignment is:",a)
a*=b
print("Value of a after multiplication and assignment is:",a)
a/=b
print("Value of a after division and assignment is:",a)
a%=b
print("Value of a after modulus and assignment is:",a)
a**=b
print("Value of a after exponentiation and assignment is:",a)
a//=b
print("Value of a after floor division and assignment is:",a)"""


""" 4{LOGICAL OPERATORS}=
    and (Logical AND)
    or (Logical OR)
    not (Logical NOT)"""
"""a=10
b=20
print(a<b and b>15)
print(a>b or b>15)
print(not(a>b))"""

""" 5{BITWISE OPERATORS}=
    & (Bitwise AND)
    | (Bitwise OR)
    ^ (Bitwise XOR)
    ~ (Bitwise NOT)
    << (Left Shift)
    >> (Right Shift)"""

"""a=10
b=20
print("Bitwise AND of a and b is:",a&b)
print("Bitwise OR of a and b is:",a|b)
print("Bitwise XOR of a and b is:",a^b)
print("Bitwise NOT of a is:",~a)
print("Left Shift of a by 2 is:",a<<2)
print("Right Shift of a by 2 is:",a>>2)"""

""" 6{MEMBERSHIP OPERATORS}=
    in (Membership in)
    not in (Membership not in)"""

"""a=[10,20,30,40,50]
print("Is 10 a member of list a?",10 in a)
print("Is 60 a member of list a?",60 in a)
print("Is 30 a member of list a?",30 in a)
print("Is 60 not a member of list a?",60 not in a)
print("Is 20 not a member of list a?",20 not in a)
print("Is 50 not a member of list a?",50 not in a)"""



""" 7{IDENTITY OPERATORS}=
    is (Identity is)
    is not (Identity is not)"""
"""a=10
b=10
c=20
print("Is a identical to b?",a is b)
print("Is a identical to c?",a is c)
print("Is a not identical to b?",a is not b)
print("Is a not identical to c?",a is not c)"""


""" OPERATORS PRECEDENCE=
    1. Parentheses ()
    2. Exponentiation **
    3. Multiplication *, Division /, Floor Division //, Modulus %
    4. Addition +, Subtraction -
    5. Bitwise Shift <<, >>
    6. Bitwise AND &
    7. Bitwise XOR ^
    8. Bitwise OR |
    9. Comparison Operators ==, !=, >, <, >=, <=
    10. Logical NOT not
    11. Logical AND and
    12. Logical OR or
    13. Assignment Operators =, +=, -=, *=, /=, %=, **=, //=
    14. Membership Operators in, not in
    15. Identity Operators is, is not"""