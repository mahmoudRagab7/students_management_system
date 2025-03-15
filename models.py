class Person:
    """Base class for all persons in the system."""
    
    def __init__(self, name, age, gender):
        """Initialize a Person object with basic attributes."""
        self.name = name
        self.age = age
        self.gender = gender
    
    def display_info(self):
        """Display basic information about the person."""
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"


class Student(Person):
    """Student class that inherits from Person."""
    
    def __init__(self, name, age, gender, student_id):
        """Initialize a Student object with person attributes and student-specific ones."""
        super().__init__(name, age, gender)
        self.student_id = student_id
        self.courses = []
    
    def enroll_course(self, course_name):
        """Add a course to the student's record."""
        if course_name not in self.courses:
            self.courses.append(course_name)
            return f"{course_name} has been added to {self.name}'s courses."
        return f"{self.name} is already enrolled in {course_name}."
    
    def remove_course(self, course_name):
        """Remove a course from the student's record."""
        if course_name in self.courses:
            self.courses.remove(course_name)
            return f"{course_name} has been removed from {self.name}'s courses."
        return f"{self.name} is not enrolled in {course_name}."
    
    def display_info(self):
        """Display information about the student including their courses."""
        basic_info = super().display_info()
        courses_info = f"Student ID: {self.student_id}, Courses: {', '.join(self.courses) if self.courses else 'None'}"
        return f"{basic_info}, {courses_info}"
    
    def to_dict(self):
        """Convert student object to dictionary for saving to file."""
        return {
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'student_id': self.student_id,
            'courses': self.courses
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create a Student object from a dictionary."""
        student = cls(data['name'], data['age'], data['gender'], data['student_id'])
        student.courses = data['courses']
        return student


class Admin:
    """Admin class to manage students."""
    
    def __init__(self, db_handler):
        """Initialize Admin with a database handler."""
        self.db_handler = db_handler
        self.students = []
        self.load_students()
    
    def load_students(self):
        """Load students from the database."""
        self.students = self.db_handler.load_students()
    
    def save_students(self):
        """Save students to the database."""
        self.db_handler.save_students(self.students)
    
    def add_student(self, name, age, gender, student_id):
        """Add a new student to the system."""
        # Check if student_id already exists
        for student in self.students:
            if student.student_id == student_id:
                return f"Student with ID {student_id} already exists."
        
        # Create and add new student
        new_student = Student(name, age, gender, student_id)
        self.students.append(new_student)
        self.save_students()
        return f"Student {name} with ID {student_id} has been added."
    
    def view_students(self):
        """View all students in the system."""
        if not self.students:
            return "No students found in the system."
        
        result = []
        for i, student in enumerate(self.students, 1):
            result.append(f"{i}. {student.display_info()}")
        
        return "\n".join(result)
    
    def find_student_by_id(self, student_id):
        """Find a student by their ID."""
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None
    
    def update_student(self, student_id, name=None, age=None, gender=None):
        """Update a student's information."""
        student = self.find_student_by_id(student_id)
        if not student:
            return f"No student found with ID {student_id}."
        
        if name:
            student.name = name
        if age:
            student.age = age
        if gender:
            student.gender = gender
        
        self.save_students()
        return f"Student with ID {student_id} has been updated."
    
    def delete_student(self, student_id):
        """Remove a student from the system."""
        student = self.find_student_by_id(student_id)
        if not student:
            return f"No student found with ID {student_id}."
        
        self.students.remove(student)
        self.save_students()
        return f"Student with ID {student_id} has been removed."
    
    # Bonus feature: Search for students by name
    def search_students(self, query):
        """Search for students by name or ID."""
        results = []
        for student in self.students:
            if query.lower() in student.name.lower() or query == student.student_id:
                results.append(student)
        
        if not results:
            return f"No students found matching '{query}'."
        
        output = []
        for i, student in enumerate(results, 1):
            output.append(f"{i}. {student.display_info()}")
        
        return "\n".join(output)