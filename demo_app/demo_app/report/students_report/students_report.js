// Copyright (c) 2024, hopeson and contributors
// For license information, please see license.txt

frappe.query_reports["Students report"] = {
    "filters": [
        {
            "fieldname": "regno",
            "label": __("Reg No."),
            "fieldtype": "Link",
            "options":"Student",
            "reqd": 0,
            "hidden": 0
        },
        {
            "fieldname": "name1",
            "label": __("Name"),
            "fieldtype": "Data",
            "reqd": 0,
            "hidden": 0
        },
        {
            "fieldname": "gender",
            "label": __("Gender"),
            "fieldtype": "Select",
            "options": ["Female", "Male", "Others",""],
            "reqd": 0,
            "hidden": 0
        },
        {
            "fieldname": "email_id",
            "label": __("Email"),
            "fieldtype": "Data",
            "reqd": 0,
            "hidden": 0
        },
        {
            "fieldname": "phone",
            "label": __("Phone"),
            "fieldtype": "Data",
            "reqd": 0,
            "hidden": 0
        },
        {
            "fieldname": "department",
            "label": __("Department"),
            "fieldtype": "Data",
            "reqd": 0,
            "hidden": 0
        },
        {
            "fieldname": "course",
            "label": __("Course"),
            "fieldtype": "Data",
            "reqd": 0,
            "hidden": 0
        },
        {
            "fieldname": "dob",
            "label": __("DOB"),
            "fieldtype": "Date",
            "reqd": 0,
            "hidden": 0
        }
    ]
};

