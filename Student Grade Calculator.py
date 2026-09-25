
while True:
    print("===== STUDENT GRADE CALCULATOR =====")
    print("Press 1. for calculating studnet grade ")
    print("Press anything else for exit")
    choice=int(input("Enter your choice(1/2)"))
    if choice==1:
        subjects = ["Python", "DSA", "DBMS", "Maths"]
        marks = {}
        n=len(subjects)
        name=str(input("Enter Student name :- "))
        for items in subjects:
            mark=float(input(f"Enter the marks of {items} :- "))
            marks[items]=mark
        total=sum(marks.values())
        percentage=(total/(n*100))*100
        if percentage>=90:
            Grade="Grade : A "
        elif percentage>=80:
            Grade="Grade : B "
        elif percentage>=70:
                Grade="Grade : C "
        elif percentage>=60:
                Grade="Grade : D "
        elif percentage>=45:
                Grade="Grade : E "
        else:
            Grade="Grade : Fail"
        print("===== RESULT =====")
        print("Student :",name)
        print(marks)
        print("")
        print("")
        print("Total :",total)
        print("Percentage : ",percentage)
        print(Grade)
    else:
        print("Program is extting ")
        print("Thank you for choosing us ")
        break
