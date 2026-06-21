def generate_report(attendance):
    present = 0
    absent = 0
    for status in attendance.values():
        if status == "Present":
            present += 1
        else:
            absent += 1
    print("Present:", present)
    print("Absent:", absent)
