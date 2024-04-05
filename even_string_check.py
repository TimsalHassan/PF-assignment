#Name : Timsal Hassan
#Roll Number : 1129
#Semester : 1st 
#Section : 3M
while True:
    str=input("Give your str: ")
    for a in range(0,len(str)) :
        if a %2==0:
            print('\033[43m',str[a],'\033[0m')
        else:
            continue
