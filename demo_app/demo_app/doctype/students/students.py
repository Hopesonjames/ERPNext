# Copyright (c) 2024, hopeson and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Students(Document):
	pass
class Student(Document):
    def before_save(self):
        self.calculate_percentages()

    def calculate_percentages(self):
        for mark in self.mark:
            if mark.total_marks and mark.marks_obtained:
                try:
                    mark.percentage = (float(mark.marks_obtained) / float(mark.total_marks)) * 100
                except ValueError:
                    mark.percentage = 0
            else:
                mark.percentage = 0
