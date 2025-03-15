# Student Management System

A Python-based command-line application for managing student records with file saving capabilities and data export features.

## Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Export Features](#export-features)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Student Management**
  - Add new students with their details (name, age, gender, ID)
  - View all student records with complete information
  - Update existing student information
  - Remove students from the system
  - Search for students by name or ID

- **Course Management**
  - Enroll students in courses
  - Remove students from courses
  - Track courses for each student

- **Data Persistence**
  - Automatically save student records to a text file (JSON format)
  - Load existing student data on startup

- **Data Export**
  - Export student data to CSV format
  - Export student data to Excel format (requires openpyxl)

- **User-Friendly Interface**
  - Menu-driven command-line interface
  - Input validation for error prevention
  - Clear success/error messages

## Project Structure

```
student_management/
│
├── main.py         # Entry point with menu system and user interface
├── models.py       # Contains Person, Student, and Admin classes
├── database.py     # Handles file operations (save/load/export)
├── students.txt    # Student data storage (JSON format, created on first run)
└── README.md       # This file
```

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/student-management-system.git
cd student-management-system
```

2. No additional dependencies are required for basic functionality.

3. For Excel export functionality, install openpyxl:
```bash
pip install openpyxl
```

## Usage

1. Run the application:
```bash
python main.py
```

2. Follow the on-screen menu to:
   - Add students
   - View all students
   - Update student information
   - Remove students
   - Search for students
   - Export data
   - Save and exit

### Sample Workflow

1. Add a new student (Option 1)
   - Enter name, age, gender, and student ID
   
2. Add courses to the student (Option 3)
   - Select the student by ID
   - Choose option to add courses
   
3. View all students (Option 2)
   - See a list of all students with their details
   
4. Export data (Option 6)
   - Choose CSV or Excel format
   - Find the exported file in the project directory

## Export Features

### CSV Export
Exports student data to a comma-separated values (CSV) file that can be opened in any spreadsheet software.

### Excel Export
Exports student data to a formatted Excel file with proper column widths and header styling. Requires the openpyxl library.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
