# project 1 : School administration tool
import csv

def write_into_csv(info_list):
    with open('student_info.csv','a',newline='') as csv_file:
        writer=csv.writer(csv_file)
        
        if csv_file.tell()==0:
           writer.writerow(["Name","Age","Phone Number","Email- Id"])
        writer.writerow(info_list)
if __name__=='__main__':
    condition =True
    student_num=1
    while (condition):
        student_info=input("Enter  student information for student-{} ".format(student_num))
    
    #split function
        student_info_list=student_info.split(' ')
        print("\n The Entered info is :\nName:{}\nAge:{}\nContact_Number:{}\nEmail id:{}"
              .format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
        choice_check=input("Is the entered information correct ?(yes/No) ")
        if choice_check=="yes":
            write_into_csv(student_info_list)
    
            condition_check = input("Enter (Yes/NO) if you want to enter information for another student : ")
            if condition_check=="yes":
                condition=True
                student_num+=1
            elif condition_check=="no":
                condition=False
        elif choice_check=="no":
            print("\n Please re enter the values:")     