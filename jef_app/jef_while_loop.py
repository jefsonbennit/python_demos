
def while_1():
  i=10
  while i<50:
    print (i)
    if i == 25:
      break 
    i+=1

while_1()    

def while_2():
  i=100
  print ("value of i after while : ",i,i<50)
  while i<50:
    print ("while 2",i,((i == 25)))
    if i == 25:
      break 
    i+=1

while_2()


def while_true():
  while False:
    print ("while true")

while_true()