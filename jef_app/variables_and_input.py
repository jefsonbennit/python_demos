from tkinter import Variable


def variables():
    print("Inside variables function")
    # print("Enter input : ",input())
    print("Enter input : ")
    entered_input = input()
    entered_input = int(entered_input)
    print("Entered input : ", entered_input, type(entered_input))

variables()