# -*- coding: utf-8 -*-
"""
oop_a2_t2.course
XX-YYY-ZZZ
<Your name>
"""
from .student import Student

# The Course class. A course should have a name, a code, a number of credits, and a student limit.
class Course:
    def __init__(self, name, code, credit, student_limit):
        # your code here
        self.name = name
        self.code = code
        self.credit = credit
        self.student_limit = student_limit
        self.students = list()
        
    # A method to add a given student to the list of students of the course. Before adding a student to the list,
    # check if the maximum number of students has already been reached. Raise a CourseCapacityFullError if this is the case.
    def add_student(self, student):
        # your code here
        if len(self.students) == self.student_limit:
            raise CourseCapacityFullError
        else:
            self.students.append(student)

    # A method to remove a student from the list of students given only his/her student number. Iterate over all students
    # in the list and check if the student number of each student corresponds to the number given as input value for the
    # method. Raise a StudentNotEnrolledError if the student cannot be found in the list.
    def remove_student_by_number(self, student_number):
        # your code here
        FlagRemoved = False
        
        for studi in self.students:
            if studi.number == student_number:
                self.students.remove(studi)
                FlagRemoved = True
                
        if FlagRemoved == False:
            raise StudentNotEnrolledError

    # A method to create a nicely formatted string representation of a course including its name, code, maximum number
    # of students as well as the details for each enrolled student. Refer to the example output given on the assignment
    # sheet, which should be created when executing the client_2.py file.
    def to_string(self):

        # build string
        return_string = "==Course information==\nName: {}\nCode: {}\nMaximum students: {}\nNumber of Students erolled: {}\nEnrolled stuents:".format(self.name, str(self.code), str(self.student_limit), str(len(self.students)))
        
        # build list of all students enrolled
        for student in self.students:
            add_string = "\n- {} <{}>".format(student.name, str(student.number))
            return_string += add_string
        
        return return_string
        

class CourseCapacityFullError(Exception):
    """Raised when adding a student to the course and it is already full"""
    pass

class StudentNotEnrolledError(Exception):
    """Raised when removing a student from the course and the student is not enrolled"""
    pass
