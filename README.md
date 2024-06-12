# Enrollment Manager Application

## Problem Statement

The Enrollment Manager application aims to address the challenges faced by both students and educational institutions in managing enrollment processes efficiently. For students, applying to institutions can be complex, while institutions may struggle with organizing enrollment data effectively, leading to potential errors and inefficiencies.

## Solution

The Enrollment Manager app provides a solution by offering a user-friendly interface to manage student-course relationships and update information across different tables. By centralizing enrollment data and streamlining processes, the app enhances the enrollment experience for both students and institutions.

## Tables

### Students Table
- `Student id`: Integer, Primary key
- `Name`: String
- `Age`: Integer
- `Course_name`: String, Foreign key from course table
- `Instructor_name`: String, Foreign key from instructors table

### Courses Table
- `Course id`: Integer, Primary key
- `Name`: String
- `Description`: String

### Instructors Table
- `Instructor id`: Integer, Primary key
- `Name`: String
- `Course id`: Integer, Foreign key from students table

### Enrollment Table
- `Enrollment_id`: Integer, Primary key
- `Course name`: String, Foreign key from courses table
- `Student_name`: String, Foreign key from students table
- `Instructor_name`: String, Foreign key from instructors table

The `course_name`, `student_name`, and `instructor_name` are composite keys in the enrollment table.

## Relationships

### One-to-Many Relationship (Instructors to Courses)
One instructor can teach many courses, establishing a one-to-many relationship between instructors and courses. This relationship is represented by a foreign key in the courses table, referencing the primary key (Instructor ID) of the instructors table.

### Many-to-Many Relationship (Students to Courses)
Many students can enroll in many courses, creating a many-to-many relationship between students and courses. This relationship is facilitated by the enrollment table, which serves as a junction table containing composite keys referencing both the student and course tables.

## Functionality

- **Add Student**: Allows administrators to add new students to the database, providing their personal details.
- **Add Course**: Enables administrators to add new courses to the system, including course names, descriptions, and other relevant information.
- **Add Instructor**: Allows administrators to add new instructors to the database, providing their contact details and other pertinent information.
- **Enroll Student**: Enables administrators to enroll students in courses, specifying the student ID and course ID.
- **List Students/Courses/Instructors**: Provides functionality to view lists of students, courses, and instructors stored in the database.
- **Update Information**: Allows administrators to update information in different tables, such as modifying student details, course information, or instructor contact information.
- **Delete Information**: Allows administrators to delete records in different tables, such as removing students, courses, instructors, or enrollments.

## Usage

Upon running the application, you will be presented with a menu to perform various operations:

1. **List students**
2. **List courses**
3. **List instructors**
4. **List enrollments**
5. **Add student**
6. **Add course**
7. **Add instructor**
8. **Enroll student**
9. **Update student**
10. **Update course**
11. **Update instructor**
12. **Update enrollment**
13. **Delete student**
14. **Delete course**
15. **Delete instructor**
16. **Delete enrollment**
17. **Exit**

### Example Operations

1. **Add Student**

    - Select option `5` and follow the prompts to enter student details.

2. **List Students**

    - Select option `1` to view all students.

3. **Update Student**

    - Select option `9` and follow the prompts to update a student's details.

4. **Delete Student**

    - Select option `13` and follow the prompts to delete a student.

## Exiting the Application

To exit the application, select option `17` from the menu. The application will display a goodbye message.


