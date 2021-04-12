#! python3
"""
(10 points) 
Create a class object for a student.
It should have the following properties
str name
str studentNumber
int grade
list courses - to corresepond with course names
list grades - to correspond with grades

It should have the following methods:
average()       - determines the mathematical average of all course grades
getHonorRoll()  - determines the average of the top 5 courses if there are at least 5 courses.
                  returns True if the average is 86 or higher (on the honor roll)
                  returns False if not on the honor roll
showCourses()   - prints a list of all courses
showGrade(int)  - takes 1 parameter, the index of the list
                - displays the course name and grade
getCourses(list)- Receives a list of courses and stores that in the class property
getGrades(list) - Receives a list of grades and stores that in the class property
constructor     - should require the student name, studentNumber and grade (in that order)
"""

class student:
    name = ""
    studentnumber = ""
    gradelevel = 0
    courses = []
    grades = []
    # properties should be listed first

    def __init__(self, name, studentnumber, gradelevel, grades = [], courses = []): # You will need to create your own input parameters for all methods
        self.name = name
        self.studentnumber = studentnumber
        self.gradelevel = gradelevel
        self.grades = grades
        self.courses = courses


    def __del__(self):
        pass

    def average(self, grades):
            Sum = sum(self.grades)
            x = Sum/len(self.grades)
            print(x)

    def getHonorRoll(self):
        a = self.grades

        a.sort()
        honornumber = a[-1] + a[-2] + a[-3] + a[-4] + a[-5]
        honornumber = honornumber / 5
        honornumber = int(honornumber)
        if honornumber >= 86:
            return True

        else: 
            return False
    def getGrades(self, grades):
        grades = self.grades
        return
    def getCourses(self, courses):
        courses = self.courses
        return 
    def showCourses(self,grades):
        print(self.courses)
    def showGrades(self, courses):
        print(self.grades)
def main():
    # This contains test data that will be used by the autograder.
    # do not modify this function

    st1 = student("Anita Bath","91334",11)
    st1.getCourses( ["English","Math","PE","Computers","History","Biology","Japanese"] )
    st1.getGrades( [91, 94, 87, 99, 82, 100, 73])

    st2 = student("Joe Lunchbox","12346", 11)
    st2.getCourses( ["English","Math","Physics","Computers","Geography","Chemistry","French"] )
    st2.getGrades( [71, 98, 93, 95, 68, 81, 71])






    



main() 