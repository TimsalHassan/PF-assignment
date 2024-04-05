#Name : Timsal Hassan
#Roll Number : 1129
#Semester : 1st 
#Section : 3M
while True:
    def same_or_not(a):
        if a[0] == a[len(a)-1]:
            print('\033[42m',"Palindrome Number!",'\033[0m')
        elif a.isdigit() == False:
            print('\033[43m','Uexpected value','\033[0m')
        else:
            print('\033[41m',"Not a Palindrome Number!",'\033[0m')
    a=(input("Your List please; "))
    same_or_not(a)
