#Name : Timsal Hassan
#Roll Number : 1129
#Semester : 1st 
#Section : 3M
while True:
    def strings_remover(Str,x):
        xstr=int(x)
        x1=int(len(Str))
        x2=x1-xstr
        str2=Str[-x2::]
        print('\033[44m',str2,'\033[0m')
    String=(input("Place your string here \n"))
    chr=input("number characters you want to remove \n")
    strings_remover(String,chr)
