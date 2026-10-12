#Indentation
'''
Python uses Indentation to define structure and hierachy of code. 
Consisten use of spaces (commonly 4) or a tab is required.
Unlike manyother programming languages that use braces {} to delimit blocks of code,
python uses indentation to determine the grouping of statements.
'''

age = 32

if age>32:
    print(age)

if True:
    print("Correct Indentation")
    if False:
        print("This Wont Print")
    print("This will print")
print("Outside the if block")