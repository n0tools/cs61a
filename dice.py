"""Functions that simulate dice rolls.

A dice function takes no arguments and returns a number from 1 to n
(inclusive), where n is the number of sides on the dice.

Types of dice:

 -  Dice can be fair, meaning that they produce each possible outcome with equal
    probability. Examples: four_sided, six_sided

 -  For testing functions that use dice, deterministic test dice always cycle
    through a fixed sequence of values that are passed as arguments to the
    make_test_dice function.
"""

from random import randint

def make_fair_dice(sides):
    """Return a die that returns 1 to SIDES with equal chance."""
    assert type(sides) == int and sides >= 1, 'Illegal value for sides'
    def dice():
        return randint(1,sides)
    return dice

four_sided = make_fair_dice(4)
six_sided = make_fair_dice(6)

def make_test_dice(*outcomes):
    """Return a die that cycles deterministically through OUTCOMES.

    >>> dice = make_test_dice(1, 2, 3)
    >>> dice()
    1
    >>> dice()
    2
    >>> dice()
    3
    >>> dice()
    1
    >>> dice()
    2

    This function uses Python syntax/techniques not yet covered in this course.
    The best way to understand it is by reading the documentation and examples.
    """
    assert len(outcomes) > 0, 'You must supply outcomes to make_test_dice'
    for o in outcomes:
        assert type(o) == int and o >= 1, 'Outcome is not a positive integer'
    index = len(outcomes) - 1
    def dice():
        nonlocal index
        index = (index + 1) % len(outcomes)
        return outcomes[index]
    return dice
    
""" To rebind variables found outside of the innermost scope, 
the nonlocal statement can be used; 
if not declared nonlocal, those variables are read-only 
(an attempt to write to such a variable will simply create a new 
local variable in the innermost scope, leaving the identically 
named outer variable unchanged). >>> so their value is bound only in
that def scope

SYNTAX nonlocal *identiier*
e.g. nonlocal x
     nonlocal somename

*** Basically you cant re-assign a value to a outer variable if 
trying to bind it within a inner environemnt. With nonlocal *name* the
program access the first instance of that variable outside the inner function,
i.e. looking for it as soon as it appears then it rebinds it, like so: """

def outer():
    x = 1
    def inner():
        nonlocal x
        x = 0
    inner() # must call inner to rebind x
    return x

""" The above rebinds x to 0, assigning from the inner function to the
one outermost (it looks for x where is next appearing)"""

""" Try
print(outer()) <<< outer calls inner that rebinds outer x to 0 """
# see above 

""" Try
print(x) <<< x is not defined in the global space. Is possible to
assign x to global with inner by declaring *gloabl x*

print(inner()) <<< Error. Inner is not defined in the global frame

print("inner:", x)

print("outer:", x)
        
From the documentation
 1. The statement allows encapsulated code to rebind variables 
 outside of the local scope besides the global (module) scope.
 
 2. Causes the listed identifiers to refer to previously bound 
 variables in the nearest enclosing scope excluding globals. 
 This is important because the default behavior for binding is 
 to search the local namespace first """
