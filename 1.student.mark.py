students = []
courses = []
marks = {}

def input_students():
    for _ in range(int(input("Number of students: "))):
        students.append({
            "id": input("Student id: "),
            "name": input("Student name: "),
            "dob": input("Student DoB: ")
        })

def input_courses():
    for _ in range(int(input("Number of courses: "))):
        courses.append({
            "id": input("Course id: "),
            "name": input("Course name: ")
        })

def list_students():
    print("Students:")
    for s in students:
        print(s["id"], "|", s["name"], "|", s["dob"])

def list_courses():
    print("Courses:")
    for c in courses:
        print(c["id"], "|", c["name"])

def input_marks():
    if not students or not courses:
        print("Need students and courses first!")
        return
    list_courses()
    cid = input("Course id: ")
    if cid not in [c["id"] for c in courses]:
        print("Course not found!")
        return
    for s in students:
        m = float(input(f"Mark for {s['id']} - {s['name']}: "))
        marks[(cid, s["id"])] = m

def show_marks():
    if not students or not courses:
        print("Need students and courses first!")
        return
    list_courses()
    cid = input("Course id: ")
    if cid not in [c["id"] for c in courses]:
        print("Course not found!")
        return
    print("Marks for", cid)
    for s in students:
        m = marks.get((cid, s["id"]))
        print(s["id"], s["name"], ":", m if m is not None else "no mark")

def main():
    while True:
        print("\n1.Input students  2.Input courses  3.List students")
        print("4.List courses   5.Input marks    6.Show marks  0.Exit")
        c = input("Choice: ")
        if c == "1": input_students()
        elif c == "2": input_courses()
        elif c == "3": list_students()
        elif c == "4": list_courses()
        elif c == "5": input_marks()
        elif c == "6": show_marks()
        elif c == "0": break
        else: print("Invalid!")

if __name__ == "__main__":
    main()
