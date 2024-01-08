# Code to descramble a scrambled input into the different bits of information it contains so the information is understandable
# Dylan Friedman
# FRDDYL002
# 10 April 2022
def location(block):
    # Your code here
    reverse = ''
    for i in block[len(block)-5:block.find('S'):-1]:
        reverse = reverse + i
    return reverse.title()

def temperature(block):
    # Your code here
    temp = block[block.find(' ')+1:block.find('_')]
    return float(temp)

def x_coordinate(block):
    # Your code here
    x = block[block.find(':')+1:block.find(',')]
    return x

def y_coordinate(block):
    # Your code here
    newblock = block[block.find(' ')+1:]
    y = newblock[newblock.find(',')+1:(newblock.find(' '))]
    return y

def pressure(block):
    # Your code here
    pressure = block[block.find('_')+1:block.find(':')]
    return float(pressure)


def get_block(data):
    # Your code here
    block = data[data.find('BEGIN'): data.find('END')+3]
    return block


def main():
    data = input('Enter the raw data:\n')
    block = get_block(data)
    print('Site information:')
    print('Location:', location(block))
    print('Coordinates:', y_coordinate(block), x_coordinate(block))
    print('Temperature: {:.2f} C'.format(temperature(block)))
    print('Pressure: {:.2f} hPa'.format(pressure(block)))

if __name__=='__main__':
    main()
