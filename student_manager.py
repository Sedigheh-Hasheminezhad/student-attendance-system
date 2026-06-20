students = []
def add_student(student_id, name):
  students.append({
    "id": student_id,
    "name": name
  })
  def show_students():
    for student in students:
      print(student)
      def remove_student(student_id):
        global students
        students = [
        s for s in students
        if s["id"] != student_id
        ]
