# NumeralTree

def calc(number):
    # add 1 if odd
    if number % 2 != 0:
        number = int(number+1)
    # logic
    number1 = int(((100+number)/2) % 100)
    number2 = int((number/2) % 100)
    return Node(number1), Node(number2)
  
    
Using the function above we will iterativley create a tree diagram.
    
