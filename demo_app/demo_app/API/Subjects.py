@frappe.whitelist(allow_guest=True)
def create_item(subject_code,subject_name,total_mark):
    #Create a new Item document
    new_item = frappe.new_doc("subjects")
    new_item.subject_code = subject_code
    new_item.subject_name = subject_name
    new_item.maximum_marks = maximum_marks

    # Save the document
    new_item.insert(ignore_permissions=True)  # Use ignore_permissions=True for testing purposes; adjust as needed
    response = "inserted successfully"
    json.dumps(response)
    return response

# @frappe.whitelist(allow_guest=True)
# def sampleapi(subject_code,subject_name,total_mark):
#         url = 'http://dcode.com:8002//api/resource/Subjects'
#         # headers = {
#         #     'Content-Type': 'application/json',
#         #     'Authorization': 'Bearer YOUR_API_TOKEN'
#         # }
#         data={
#             "subject_code":subject_code,
#             "subject_name":subject_name,
#             "total_mark":total_mark

#         }
#         response = requests.post(url,params=data)
            

#         if response.status_code == 200:

#             data={
#                 "success": True,
#                 "message": "Inserted successfully"
#             }
        
#         else:
#             data=json.dumps("FAILED")
#         return data