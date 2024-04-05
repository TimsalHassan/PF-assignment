#Name : TimsaL Hassan
#Roll Number : 1129
#Semester : 1st 
#Section : 3M
def List_merge(ls1,ls2):
    Merged_list=[]
    for num in ls1:
        if num %2 != 0:
            Merged_list.append(num)
    for num in ls2:
        if num %2 == 0:
            Merged_list.append(num)
    print('\033[44m',Merged_list,'\033[0m')
ls1=[1,2,3,4,5,6,7,8]
ls2=[10,11,12,13,14,15,16]
List_merge(ls1,ls2)
