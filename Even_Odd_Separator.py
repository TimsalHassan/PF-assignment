#Name : Timsal Hassan
#Roll Number : 1129
#Semester : 1st 
#Section : 3M
Even = []
Odd = []
String = []
while True :
    Your_input = input("Enter your data: ")
    input_type = type(Your_input)
    if Your_input.isdigit():
        number = int(Your_input)

        if number %2 == 0:
            Even.append(number)
            print('\033[30m','\033[41m', "Even :" , Even ,'\033[0m')
        else:
            Odd.append(number)
            print('\033[43m',"Odd: " , Odd ,'\033[0m')
    elif input_type == str:
        String.append(Your_input)
        print('\033[44m', "String: ", String,'\033[0m')

    else:
        print("Unsupported data type.")
        break
