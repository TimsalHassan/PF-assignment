#Name : Timsal Hassan
#Roll Number : 1129
#Semester : 1st 
#Section : 3M
while True:
    def same_or_not(a):
        if a[0] == a[len(a)-1]:
            print('\033[42m',"Numbers of list are same!",'\033[0m')
        else:
            print('\033[41m',"Numbers of list are not the same!",'\033[0m')
    a=list(input("Your List please; "))
    same_or_not(a)
