import math

def calcPHI():
    return (math.sqrt(5)-1)/2

print(calcPHI())

'''
def identCar(car, color):
    print("Car %s has color %s"%(car, color))
    
identCar(color='red', car = 'honda')
'''

def identCar(car=None, color='red'):
    if car == None:
        print("You have to give me a car name")
        return 
    print("Car %s has color %s"%(car, color))

identCar(color='blue')
identCar(car='toyota')

def addAll(*args):
    sum = 0
    for num in args:
        sum += num
    return sum

print(addAll(1, 2))

print(addAll(1, 2, 3, 4, 5, 6, 7, 8, 9))