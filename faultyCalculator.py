#In this program I created a faulty calculator which gives correct answers except for three of them.
#These are the faulty calcutations: 45*3=555 , 56+9=77, 56/6=4


vinput1=int(input("Please input the first number: "))
print("First number is recorded as: ", vinput1)
vop=input("Please input your first operator: ")
print("Your operator is recorded as: ", vop)
vinput2=int(input("Please input the second number: "))
print("Second number is recorded as: ", vinput2)

if (vop == "-"):
    vsofar = vinput1 - vinput2
    print(vsofar)
elif (vop == "+" and vinput1 == 45 and vinput2 == 9):
    vsofar = 555
    print(vsofar)
elif (vop == "+"):
    vsofar = vinput1 + vinput2
    print(vsofar)
elif (vop == "/" and vinput1 == 56 and vinput2 == 6):
    vsofar = 4
    print(vsofar)
elif (vop == "/"):
    vsofar = vinput1 / vinput2
    print(vsofar)
elif (vop == "*" and vinput1 == 45 and vinput2 == 3):
    vsofar = 555
    print(vsofar)
elif (vop == "*"):
    vsofar = vinput1 * vinput2
    print(vsofar)
else:
    print("Invalid operator entered.")