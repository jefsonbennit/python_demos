import sys

class AppImplememtation:
    def __init__(self) -> None:
        pass
    def factorial(self, input_number = 8):
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

    def sum_of_series(self):
        n = int(input("Enter a value of n : "))
        sum = 0
        for i in range(1, n+1):
            print("Sum : ",sum, ", i : ",i)
            a = float(i**i)/i
            sum = sum + a
        print("The sum of the series is ",sum)

class CommandLineApp:
    def __init__(self):
        self.print_welcome_message()

    def print_welcome_message(self):
        print("===================================== COMMAND LINE APP ================================")
        print("1. Factorial")
        print("2. Sum of Series")

    def start(self):
        app_impl = AppImplememtation()
        while True:
            try:
                print("Please enter the app code : ")
                app_code = int(input())
                print("================== Your entered the app code : ",app_code, type(app_code))
            except KeyboardInterrupt:
                print("Received command to exit the app. Bye!!")
                sys.exit(0)
            except:
                print(" Please enter a valid app code!")
                continue
            try:
                if app_code == 1:
                    app_impl.factorial()
                elif app_code == 2:
                    app_impl.sum_of_series()
                else:
                    print("You entered an invalid app code : ",app_code)
            except:
                print("problem with my code")
                

def main():
    my_app = CommandLineApp()
    my_app.start()
    
main()










