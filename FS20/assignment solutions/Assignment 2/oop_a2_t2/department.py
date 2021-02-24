# -*- coding: utf-8 -*-
"""
oop_a2_t2.department
XX-YYY-ZZZ
<Your name>
"""
from .course import Course

# The Department class. A Department should have a name, a code, and a list of courses.

class Department:
    def __init__(self, name, code):
        # your code here
        self.name = name
        self.code = code
        self.courses = list() 

    # A method to add a given course to the list of courses of the department.
    def add_course(self, course):
        # your code here
        self.courses.append(course)