# Coding the functions that return a input (integer) to work out the factorial and thus a second input to determine the number of periatations
# Dylan Friedman
# FRDDYL002
# 6 April 2022

def get_integer(s): # sent "n"
   # Code here
   s = input ("Enter " + s + ":\n")
   while not s.isdigit ():
      s = input ("Enter " + s + ":\n")  
   s = eval(s)   
   n = s
   return(n)
   

def calc_factorial(n):
   # Code here
   nfactorial = 1
   for i in range (1, int(n)+1):
      nfactorial *= i
      
   return nfactorial
    


   
