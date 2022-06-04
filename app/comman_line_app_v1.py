

def factorial():
    fact = 1
    n = int(input("Enter a number for finding factorial : "))
    if n > 100:
        print("Please enter a number less than 100")
        print("You have come here for playing. You don't need this app!!")
        return
    if n == 0:
        fact = 1
    else:
        for i in range(1, n+1):
            print("fact : ",fact, ", i : ",i)
            fact = fact * i
    print("Factorial of the given number : ",n," is ",fact)

def sum_of_series():
    n = int(input("Enter a value of n : "))
    sum = 0
    for i in range(1, n+1):
        print("Sum : ",sum, ", i : ",i)
        a = float(i**i)/i
        sum = sum + a
    print("The sum of the series is ",sum)

print("===================================== COMMAND LINE APP ================================")
print("1. Factorial")
print("2. Sum of Series")

while True:
    print("Please enter the app code : ")
    app_code = int(input())
    print("================== Your entered the app code : ",app_code, type(app_code))
    
    try:
        if app_code == 1:
            factorial()
        elif app_code == 2:
            sum_of_series()
        else:
            print("You entered an invalid app code : ",app_code)
    except:
        print("problem with my code")


