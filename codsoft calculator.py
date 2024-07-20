#  Task 1 @codsoft# python intrenship
"""designing a simple calculator"""
print("welcome to the mini  calculator made by chirag miglani ")
print("1. addition")
print("2. sutraction")
print("3. multiplication")
print("4. division")
print("choose any of the above operation that you want:")
option= int(input("choose any operation:"))
if(option in [1,2,3,4]):
    digit1= int(input("enter a number of your choicee :"))
    digit2=int(input("enter the second number of your choice:"))

    if (option==1):
        finalresult=digit1+digit2
    elif(option==2):
        finalresult=digit1-digit2
    elif(option==3):
        finalresult=digit1*digit2
    elif(option==4):
        finalresult=digit1/digit2
else:
    print("The operation which user entered is inappropriate")

print(f"The result of {option} is {finalresult}")
print("The Final Result is shown to you Thanks for using my calculator:")




     