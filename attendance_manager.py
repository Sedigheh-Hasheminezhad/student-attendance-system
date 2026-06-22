attendance = {}

def mark_present(student_id):
    attendance[student_id] = "Present"

def mark_absent(student_id):
    attendance[student_id] = "Absent"

def show_attendance():
    print(attendance)
