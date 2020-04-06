# my_lambdata/my_mod.py

def enlarge(n):
    """
    Param n is a number
    Function will enlarge the number
    """
    return n * 100

# if in our global scope, this will mess up our ability to import other
## functions from this file. So we need to nest it under the main

# # x = 5
# x = int(input("Please choose a number (like 5): "))
# result = enlarge(x)
# print(result)

if __name__ == "__main__":
    # only invoke the code below if running this file from the command line,
    ## not if import from another file
    x = int(input("Please choose a number (like 5): "))
    result = enlarge(x)
    print(result)