import pickle
import gzip
import os
import threading

def save_data_threaded(students, courses, marks, filename="students.dat"):
    """
    Starts a new thread to serialize and compress the data.
    """
    thread = threading.Thread(target=save_data, args=(students, courses, marks, filename))
    thread.start()
    return thread

def save_data(students, courses, marks, filename="students.dat"):
    """
    Serializes and compresses the student, course, and marks data into a file.
    """
    with gzip.open(filename, 'wb') as f:
        pickle.dump((students, courses, marks), f)

def load_data(filename="students.dat"):
    """
    Loads and deserializes data from the specified file.
    Returns (students, courses, marks) if the file exists, otherwise (None, None, None).
    """
    if os.path.exists(filename):
        with gzip.open(filename, 'rb') as f:
            return pickle.load(f)
    return None, None, None
