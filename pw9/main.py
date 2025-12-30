import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from domains.entities import Student, Course
from data import load_data, save_data_threaded

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Student Management System")
        self.geometry("800x600")

        self.students, self.courses, self.marks = load_data()
        if self.students is None:
            self.students = []
            self.courses = []
            self.marks = {}

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(pady=10, padx=10, fill="both", expand=True)

        self.create_student_tab()
        self.create_course_tab()
        self.create_mark_tab()

    def create_student_tab(self):
        student_frame = ttk.Frame(self.notebook)
        self.notebook.add(student_frame, text="Students")

        # Student list
        student_list_frame = ttk.LabelFrame(student_frame, text="Students")
        student_list_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.student_tree = ttk.Treeview(student_list_frame, columns=("id", "name"), show="headings")
        self.student_tree.heading("id", text="ID")
        self.student_tree.heading("name", text="Name")
        self.student_tree.pack(fill="both", expand=True)
        self.update_student_list()

        # Add student button
        add_student_button = ttk.Button(student_frame, text="Add Student", command=self.add_student)
        add_student_button.pack(pady=5)
        
    def create_course_tab(self):
        course_frame = ttk.Frame(self.notebook)
        self.notebook.add(course_frame, text="Courses")

        # Course list
        course_list_frame = ttk.LabelFrame(course_frame, text="Courses")
        course_list_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.course_tree = ttk.Treeview(course_list_frame, columns=("id", "name"), show="headings")
        self.course_tree.heading("id", text="ID")
        self.course_tree.heading("name", text="Name")
        self.course_tree.pack(fill="both", expand=True)
        self.update_course_list()

        # Add course button
        add_course_button = ttk.Button(course_frame, text="Add Course", command=self.add_course)
        add_course_button.pack(pady=5)

    def create_mark_tab(self):
        mark_frame = ttk.Frame(self.notebook)
        self.notebook.add(mark_frame, text="Marks")

        # Mark list
        mark_list_frame = ttk.LabelFrame(mark_frame, text="Marks")
        mark_list_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.mark_tree = ttk.Treeview(mark_list_frame, columns=("student_id", "course_id", "mark"), show="headings")
        self.mark_tree.heading("student_id", text="Student ID")
        self.mark_tree.heading("course_id", text="Course ID")
        self.mark_tree.heading("mark", text="Mark")
        self.mark_tree.pack(fill="both", expand=True)
        self.update_mark_list()
        
        # Add mark button
        add_mark_button = ttk.Button(mark_frame, text="Add Mark", command=self.add_mark)
        add_mark_button.pack(pady=5)

    def update_student_list(self):
        for i in self.student_tree.get_children():
            self.student_tree.delete(i)
        for student in self.students:
            self.student_tree.insert("", "end", values=(student.get_id(), student.get_name()))

    def update_course_list(self):
        for i in self.course_tree.get_children():
            self.course_tree.delete(i)
        for course in self.courses:
            self.course_tree.insert("", "end", values=(course.get_id(), course.get_name()))
            
    def update_mark_list(self):
        for i in self.mark_tree.get_children():
            self.mark_tree.delete(i)
        for (course_id, student_id), mark in self.marks.items():
            self.mark_tree.insert("", "end", values=(student_id, course_id, mark))

    def add_student(self):
        student_id = simpledialog.askstring("Add Student", "Enter student ID:")
        student_name = simpledialog.askstring("Add Student", "Enter student name:")
        if student_id and student_name:
            self.students.append(Student(student_id, student_name))
            self.update_student_list()

    def add_course(self):
        course_id = simpledialog.askstring("Add Course", "Enter course ID:")
        course_name = simpledialog.askstring("Add Course", "Enter course name:")
        if course_id and course_name:
            self.courses.append(Course(course_id, course_name))
            self.update_course_list()

    def add_mark(self):
        student_id = simpledialog.askstring("Add Mark", "Enter student ID:")
        course_id = simpledialog.askstring("Add Mark", "Enter course ID:")
        mark = simpledialog.askfloat("Add Mark", "Enter mark:")
        if student_id and course_id and mark is not None:
            self.marks[(course_id, student_id)] = mark
            self.update_mark_list()

    def on_closing(self):
        save_thread = save_data_threaded(self.students, self.courses, self.marks)
        if save_thread:
            save_thread.join()
        self.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()
