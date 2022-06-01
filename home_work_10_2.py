def function(a, b):
    try:
        result = int((a**2)/b)
        print(result)
    except (TypeError, ZeroDivisionError):
            print("You make mistake, plese, try again")
#Second function. You can have two notification about mistake, the name of notifaction depend from type of error, if it`s another type wiil be 3 type of except

def function_2(a,b):
    try:
        result = int((a**2)/b)
        print(result)
    except TypeError:
        print("Please, put a numbers")
    except ZeroDivisionError:
        print("You can't divide by zero")
    except:
        print("Opps")


function(12,1)

function_2("hi","no")

