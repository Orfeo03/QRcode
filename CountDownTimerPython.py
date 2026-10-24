import time  #import përdoret për të importuar një modul në Python.


#CountDownTimer in Python

my_time = int(input("Enter the time in seconds: "))

for x in reversed ( range(0,my_time)):
    print(x)
    time.sleep(1)   #Ky funksion e ndalon përkohësisht ekzekutimin e programit për 1 sekondë.

print ("Time'S Up")


# #CountDownTimer in Python
#
# my_time = int(input("Enter the time in seconds: "))
#
# for x in  range(my_time,0,-1):
#     print(x)
#     time.sleep(1)   #Ky funksion e ndalon përkohësisht ekzekutimin e programit për 1 sekondë.
#
# print ("Time'S Up")
#
