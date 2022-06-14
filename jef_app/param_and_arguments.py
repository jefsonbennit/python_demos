def factorial(input_number = 8):
    print("Going to find factorial for the input_number : ",input_number)
    fact = 1
    if input_number == 0:
        fact = 1
    else:
        for i in range(1, input_number+1):
            print("fact : ",fact, ", i : ",i)
            fact = fact * i
    print("Factorial of the given number : ",input_number," is ",fact)

def pure_function_square(sq_param = 223):
    return sq_param * sq_param

def impure_function_square(sq_param = 223):
    sq_param+=1
    return sq_param * sq_param


def main():
    n = int(input("Enter a number for finding factorial : "))
    if n > 100:
        print("Please enter a number less than 100")
        print("You have come here for playing. You don't need this app!!")
        return
    else:
        factorial()
        return_val = pure_function_square(n)
        print("Square of the given number : ",n,return_val)
        impure_return_val = impure_function_square(n)
        print("Impure function Square of the given number : ",n,impure_return_val)


main()