class universityresults:
    name=""
    physics=0
    maths=0
    def showresults(self):

        total = self.physics + self.maths
        print("student :",self.name)
        print("the result is:",total)

student1 = universityresults()
student1.name="shafeeq"
student1.physics=100
student1.maths=80
student1.showresults()