import curses
from domains.entities import Student, Course
import input
import output
from data import load_data, save_data_threaded

class Management:
    def __init__(self):
        loaded_students, loaded_courses, loaded_marks = load_data()
        if loaded_students is not None:
            self.__students = loaded_students
            self.__courses = loaded_courses
            self.__marks = loaded_marks
        else:
            self.__students = []
            self.__courses = []
            self.__marks = {}

    def main(self, stdscr=None):
        save_thread = None
        while True:
            choice = output.print_menu(stdscr)
            if stdscr:
                choice = stdscr.getstr().decode()
            
            if choice == "1":
                self.__students.extend(input.input_students(stdscr))
            elif choice == "2":
                self.__courses.extend(input.input_courses(stdscr))
            elif choice == "3":
                output.print_students(self.__students, stdscr)
            elif choice == "4":
                output.print_courses(self.__courses, stdscr)
            elif choice == "5":
                self.__marks.update(input.input_marks(self.__courses, self.__students, stdscr))
            elif choice == "6":
                output.print_marks(self.__courses, self.__students, self.__marks, stdscr)
            elif choice == "0":
                save_thread = save_data_threaded(self.__students, self.__courses, self.__marks)
                break
            else:
                if stdscr:
                    stdscr.addstr("Invalid choice.\n")
                else:
                    print("Invalid choice.")
            
            if stdscr:
                stdscr.addstr("Press any key to continue...")
                stdscr.getch()
                stdscr.clear()
        
        if save_thread:
            save_thread.join()


if __name__ == "__main__":
    app = Management()
    # curses.wrapper(app.main) # Commented out for now, as it requires a terminal
    app.main()
