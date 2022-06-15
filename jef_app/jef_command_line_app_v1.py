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

def welcome():
  print("===================================== COMMAND LINE APP ================================")
  print("1. Factorial")
  print("2. Sum of Series")
     
welcome()

while True:
  print("please enter the app code: ")
  app_code=int(input())
  print("you entered the app code: ",app_code)

  try:
    # print ("hello")
    if app_code==1:
       factorial()
    elif app_code==2:
       sum
       sum_of_series() 
    else :
      print ("you have entered an invalid code")
  except:
      print("an exception occured") 


