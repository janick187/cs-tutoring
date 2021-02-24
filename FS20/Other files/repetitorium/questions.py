from functools import reduce
import random


# Question 1: What is the output of the following code snippet?

'''
def getNumbers(number1, number2, number3):
    
    # range(0,4) -> 0,1,2,3
    for i in range(len(number1)-1):
        # i = 2
        
        # number1 = 3, number2 = 4
        # FLASE
        
        # number3 = 3
        # TRUE, FALSE -> FALSE
        
        # FALSE or FALSE -> False
        if (number1[i] == 2 and number2[i+1] == 2) or (not number3[i] == 2 and not number3[i] == 3):
            continue
        
        num1 = number1[i] # 3
        num2 = number2[-i] # 4
        
        length = len(number3) # 5
        
        num3 = number3[list(map(lambda x: random.randrange(0, x), [length]))[0]]

        print("{},{},{}".format(num1, num2, num3))
        break
    
getNumbers([2,1,3,4,5],
           [1,2,3,4,5],
           [1,4,3,2,5])

'''

# Question 2: What is the output of the following code snippet?

'''
def getElements(elements):
    
    my_set = set()
  
    for item in elements:
        if elements.index(item) % 2 == 0:
            if isinstance(item, str):
                my_set.add(elements[::2][2])
        else:
            my_set.add(elements[::-2][1])
    
    return my_set

print(getElements(["a",1,1,"a","b","b"]))

'''

# Question 3: What is the output of the following code snippet?

'''
# What is the output of the following code snippet?

def reduceNumbers(numbers):
    
    result = []
    while len(numbers) >= 2:
        result.append(reduce(lambda a,b: a // b if a < b else a+b, numbers))
        del numbers[-1]
    
    return sorted(filter(lambda x: x >= 2 and x < 84, result))

print(reduceNumbers([4,1,3,10,4]))
'''

# Question 4: What is the output of the following code snippet?

'''
# What is the output of the following code snippet?

def iterateDict(dictionary):
    
    counter = 0
    
    for key, value in dictionary.items():
        
        if type(value) == dict:
            
            for sub_key, sub_value in value.items():
                counter += 1
        else:
            try:
                int(value)
                counter += 1
            except ValueError:
                continue
                counter += 1
        
        counter -= 1
    
    return counter
        
dictionary = {
        'key1':5,
        'key2':{
            'a':2,
            'b':7,
            'o':99
            },
        'key3':'hello',
        'key4':'goodlife',
        'key5' :22,
        'key6':{
            'onemore':
            {
                'last':999
            }
        }
    }

print(iterateDict(dictionary))
'''