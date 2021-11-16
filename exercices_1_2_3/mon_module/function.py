def add(a, b):

    result = a + b
    return result 

def divide(a, b):

    try:
        result = a / b

    except ZeroDivisionError:
        #result = 'Handling run-time error:' + str(err)
        raise Exception("Sorry, you can't divide by 0")
    
    return result

def concatenation(a,b):
    
    if (type(a) != str) | (type(b) != str):
        raise TypeError("Not str")

    result = a + b
    return result


    