def log_decorator(func):
    def new_func(*args):
        if args:
            func(*args)
        else:
            print("Avant l'exécution de la fonction")
            func()
            print("Après l'exécution de la fonction")
    return new_func
 
@log_decorator
def function_test():
    print("Cette fonction ne prend pas d'arguments.")

@log_decorator
def function_test2(a, b, c):
    print("Cette fonction prend des arguments.")

function_test()
print("\n")
function_test2(1, 2, 3)
