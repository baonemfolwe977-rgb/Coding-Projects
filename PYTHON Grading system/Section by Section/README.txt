# Student Grading System

A comprehensive Python-based student grading management system that allows educators to track, manage, and analyze student performance across multiple subjects.

## Description

This project implements a modular grading system that evolves from basic grade management to a fully-featured application with persistent storage, robust error handling, and comprehensive testing. The system is designed to handle student records for three core subjects: Maths, English, and Science.

## Project Structure

The project is organized into six main sections (A-F), each building upon the previous:

### Section A
- Basic grade input and validation
- Single grade per student
- Simple class statistics (average, highest, lowest)

### Section B
- Multi-subject grade management
- Enhanced grade validation
- Per-subject statistics

### Section C & D
- Menu-driven interface
- Advanced error handling
- Student management (add/remove)
- Detailed grade reporting

### Section E & F
- Object-oriented implementation
- JSON-based data persistence
- Comprehensive testing suite
- Search and sort functionality
- Robust error handling with custom exceptions

## Key Features

- Data persistence using JSON storage
- Grade validation (0-100 range)
- Detailed student and subject reports
- Support for multiple subjects (Math, English, Science)
- Student management (add/remove students)
- Search functionality for student records
- Sort students by grade performance
- Comprehensive error handling
- Interactive menu-driven interface

## Technologies Used

- Python 3.x
- Built-in libraries:
  - `json` for data persistence
  - `statistics` for mathematical calculations
  - `sys` for system operations

## Installation Requirements

1. Python 3.13.0 installed on your system
2. No additional external packages required
3. Minimum 50MB free disk space for storing data 

## Installation Instructions

1. Clone or download the project files
2. Ensure Python 3.13.0 or any earlier version is installed on your system
3. Navigate to the project directory
4. Run the section file  `Mfolwe_Baone_SectionE+F.py.py` which contains all the sections and is more robust and stable. 

## Basic Usage

1. Start the program:
   ```bash
   python Mfolwe_Baone_SectionE+F.py.py
   ```

2. Main Menu Options:
   - Add New Student
   - Remove Student
   - Enter Grades
   - View Student Report
   - View Subject Grades
   - Exit

### Example Input/Output

```
=== Grade Management System ===
1. Add New Student
2. Remove Student
3. Enter Grades
4. View Student Report
5. View Subject Grades
6. Exit

Enter your choice (1-6): 1
Enter student name: John Doe
Successfully added John Doe

Enter your choice (1-6): 3
Enter student name: John Doe
Enter John Doe's grade for Math (0-100): 85
Enter John Doe's grade for English (0-100): 92
Enter John Doe's grade for Science (0-100): 88
Grades entered successfully
```

## Configuration Options

- Subject list can be modified in the `SUBJECTS` constant in the code
- Grade range validation (0-100) can be adjusted in the `validate_grade` method
- Data storage location can be configured in the save/load data methods

## Troubleshooting

Common Issues and Solutions:
1. **Data Not Saving:**
   - Ensure write permissions in the program directory
   - Check for available disk space

2. **Invalid Grade Inputs:**
   - Ensure grades are numbers between 0 and 100
   - Don't use special characters or letters

3. **Student Not Found:**
   - Verify correct spelling of student name
   - Check if student was properly added to the system

## Contributing Guidelines

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request
6. Follow the existing code style
7. Add appropriate comments and documentation
8. Update test cases as needed

## License

Copyright © 2025 Baone Hail Mfolwe

This project is licensed under the MIT License. Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files, to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

## Author

Baone Hail Mfolwe
For any queries or to provide collaboration opportunities kindly contact  developer on LinkedIN: https://www.linkedin.com/in/baonemfolwe  

---
Last Updated: November 2, 2025