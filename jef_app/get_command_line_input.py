# print("before input call")
# input()
# print("after calling input")

import datetime








def jefson(param):
    print("inside jefson : ",param)
    if 1 == 2:
        return "RRRRRRRRRRRRRRRR"
    if 1 == 3:
        return 1
    return "default return"

def jefsonPrint(message):
    datetime_object = datetime.datetime.now()
    print(datetime_object)
    print(datetime_object, message)

jefsonPrint("before jefson call")
jef = (jefson("passing data to jefson"))
print(jef)
print("after jefson call")

