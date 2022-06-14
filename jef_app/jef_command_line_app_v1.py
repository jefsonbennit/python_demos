def welcome():
  print("===================================== COMMAND LINE APP ================================")
  print("1. Factorial")
  print("2. Sum of Series")
     
welcome()

while True:
  print("please enter the app code: ")
  app_code=int(input())
  print("you entered the app code: ",app_code, type(app_code))
  

  try:
    if app_code==1:
      print("enter the number of series:",int, input())
    elif app_code==2:
      print("enter the number of factorial:",int, input())
    else :
      print ("you have entered an invalid code")
  except:
      print("an exception occured") 


