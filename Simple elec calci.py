ask=int(input("Enter value of voltage: "))
ask2=int(input("Enter value of Resistance: "))
ask3=int(input("Enter value of Current: "))



def resistance(ask,ask3):
    resistance=(ask/ask3)
    
    return resistance
    

print("Value of resistance is",resistance(ask,ask3))

def voltage(ask3,ask2):
    voltage=(ask3*ask2)
    

    return voltage
  
print("Value of voltage is",voltage(ask3,ask2))

def current(ask,ask2):
    current=(ask/ask2)
    

    return current
print("Value of current is",current(ask,ask2))


    