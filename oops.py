class student():
    def __init__(self,name,age,R_no,branch,grade):
        self.name=name
        self.age=age
        self.R_no=R_no
        self.branch=branch
        self.grade=grade

    def SD(self):
        print("name: ",self.name)
        print("Age: ",self.age)
        print("Registration no: ",self.R_no)
        print("Grade: ",self.grade)
        print("Branch: ",self.branch)

#creating object for class
student1= student("Aashu",18,"R5432","Infomatik","A")
student1.SD()
