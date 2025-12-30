import pickle
import gzip
import os

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
