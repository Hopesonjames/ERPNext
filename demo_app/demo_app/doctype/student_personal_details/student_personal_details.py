# # Copyright (c) 2024, hopeson and contributors
# # For license information, please see license.txt

# import frappe
# from frappe.model.document import Document

# class Studentpersonaldetails(Document):
# 	"""def before_save(self):
# 		self.try_query_non_existing_field()
# 	def try_query_non_existing_field(self):
# 		try:
# 			result = frappe.db.sql("""SELECT email_no FROM `tabStudent personal details`;""", as_dict=true)
# 			for row in result:
# 				 print(row['email_no'])
# 		except Exception as e:
# 			frappe.throw("Error!!check log for details")
# 			frappe.log_error(frappe.get_traceback(), 'Database Query Error')
# 			print(e)		 
# 		try:
# 			result = frappe.db.sql("""SELECT email_no FROM `tabStudent`;""", as_dict=True)
#             for row in result:
# 				print(row['email_no'])
#         except Exception as e:
# 			frappe.throw("Error!!Check Log for Details")
# 			frappe.log_error(frappe.get_traceback(), 'Database Query Error')
# 			print(e)"""

# Copyright (c) 2024, hopeson and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Studentpersonaldetails(Document):
    def before_save(self):
        self.try_query_non_existing_field()

    def try_query_non_existing_field(self):
        try:
            # Attempt to execute a query with a non-existing field 'email_no'
            result = frappe.db.sql("SELECT email_no FROM `tabStudentpersonaldetails` WHERE name=%s", (self.name,))
        except Exception as e:
            # Log the error
            frappe.log_error(f"Error executing query for non-existing field 'email_no': {str(e)}", "Query Execution Error")

	