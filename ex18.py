# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")
    
# ok, that *args is actually pointless, we ca just do this 
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")
    
# this just takes one argument 
def print_one(arg1):
    print(f"arg1: {arg1}")
    
# this one takes no arguemnt
def print_none():
    print(" i got nothin'.")
    
    
    print_two("zed","Shaw")
    print-two_again("Zed","Shaw")
    print-ONE("first!")
    print_none()