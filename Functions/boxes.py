# Code creating functions to output different shapes according to the users input
# Dylan Friedman
# FRDDYL002
# 6 April 2022

def print_square():
 #result = '* '*5, '\n', '*', '       ', '*', '\n',  '*', '       ', '*', '\n' '*', '       ', '*', '\n', '* '*5, "sep=''"
  beg = '* '*5
  middle = '* ' + ' '*6 + '*'
  end = '* '*5
  return str(beg + '\n' + (middle + '\n') * 3 + end)
  

def print_rectangle (width, height):
  ln1 = ('* '*width) # * * * * = 7 = 5 ... * * * = 5 = 3 ... * * * * * = 9 = 7 ... * * = 3 = 1
  print(ln1)
  for i in range(1, height-1):
    print('*', ' '*(len(ln1)-3), '*', sep='')
  print('* '*width)
   
def get_rectangle(width, height):
  beg = '* ' * width
  middle = '*' + ' ' * (len(beg)-3) + '*'
  end = beg
  
  return str(beg + '\n' + (middle + '\n')* (height-2) + end)
