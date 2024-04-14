class Inputs:
    def take_inputs(self):
        self.students_name = input("Enter the student's name: ")
        self.students_roll = int(input("Enter the student's roll no.: "))
        self.English_marks = int(input("Enter English marks: "))
        self.Sci_marks = int(input("Enter Science marks: "))
        self.Math_marks = int(input("Enter Mathematics marks: "))

    def __init__(self, students_name, students_roll, English_marks, Sci_marks, Math_marks):
        self.students_name = students_name
        self.students_roll = students_roll
        self.English_marks = English_marks
        self.Sci_marks = Sci_marks
        self.Math_marks = Math_marks

    def calavg(self):
        avg_marks = (self.English_marks + self.Sci_marks + self.Math_marks) / 3
        return avg_marks

    def passorfail(self):
        avg_marks = self.calavg()
        if avg_marks >= 60:
            if self.English_marks >= 30 and self.Sci_marks >= 30 and self.Math_marks >= 30:
                print("Pass")
            else:
                print("Fail")
        else:
            print("Fail")

# Example usage
students_name = input("Enter the student's name: ")
students_roll = int(input("Enter the student's roll no.: "))
English_marks = int(input("Enter English marks: "))
Sci_marks = int(input("Enter Science marks: "))
Math_marks = int(input("Enter Mathematics marks: "))

student = Inputs(students_name, students_roll, English_marks, Sci_marks, Math_marks)
student.passorfail()
