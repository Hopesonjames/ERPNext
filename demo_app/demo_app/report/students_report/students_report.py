# Copyright (c) 2024, hopeson and contributors
# For license information, please see license.txt

# custom_report.py

import frappe

def execute(filters=None):
    columns = [
        {"label": "Student Name", "fieldname": "name1", "fieldtype": "Data"},
        {"label": "Status", "fieldname": "status", "fieldtype": "Data"},
        {"label": "Registration Number", "fieldname": "reg_no", "fieldtype": "Data"},
        {"label": "Gender", "fieldname": "gender", "fieldtype": "Data"},
        {"label": "Email", "fieldname": "email", "fieldtype": "Data"},
        {"label": "Phone", "fieldname": "phone", "fieldtype": "Data"},
        {"label": "Department", "fieldname": "department", "fieldtype": "Data"},
        {"label": "Course", "fieldname": "course", "fieldtype": "Data"},
        {"label": "Date of Birth", "fieldname": "dob", "fieldtype": "Date"},
        {"label": "Subject Code", "fieldname": "subject_code", "fieldtype": "Data"},
        {"label": "Subject Name", "fieldname": "subject_name", "fieldtype": "Data"},
        {"label": "Mark", "fieldname": "mark", "fieldtype": "Data"},
        {"label": "Total Mark", "fieldname": "total_mark", "fieldtype": "Data"},
        {"label": "Percentage", "fieldname": "percentage", "fieldtype": "Data"}
    ]

    data = []

    student_filters = {}
    if filters:
        if filters.get("regno"):
            student_filters["regno"] = filters.get("regno")
        if filters.get("name1"):
            student_filters["name1"] = filters.get("name1")
        if filters.get("gender"):
            student_filters["gender"] = filters.get("gender")
        if filters.get("email_id"):
            student_filters["email_id"] = filters.get("email_id")
        if filters.get("phone"):
            student_filters["phone"] = filters.get("phone")
        if filters.get("department"):
            student_filters["department"] = filters.get("department")
        if filters.get("course"):
            student_filters["course"] = filters.get("course")
        if filters.get("dob"):
            student_filters["dob"] = filters.get("dob")

    students = frappe.get_all("Students", filters=student_filters, fields=["*"])

    for student in students:
        marks = frappe.get_all("Marks D", filters={"parent": student.name}, fields=["*"])
        for mark in marks:
            row = {
                "name1": student.name1,
                "status": student.status,
                "regno": student.reg_no,
                "gender": student.gender,
                "email_id": student.email,
                "phone": student.phone,
                "department": student.department,
                "course": student.course,
                "dob": student.dob,
                "subject_code": mark.subject_code,
                "subject_name": mark.subject_name,
                "total_marks": mark.total_mark,
                "percentage": mark.percentage
            }
            data.append(row)

    return columns, data


