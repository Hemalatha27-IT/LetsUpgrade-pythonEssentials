alt=int(input("Enter the altitude :"))#getting input from user(altitude)
if(alt<1000):
    print("You are safe to land")
elif(alt<5000 and alt>1000):
    print("Come down to 1000ft")
elif(alt>5000):
    print("go around and try after some time")
else:
    print("Enter the valid altitude")
