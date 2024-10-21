import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Placeholder for students' data, each check-in will add more rows
columns = [
    "Student Name", "Check-in Date", "Online Curriculum Progress (%)", 
    "Bookwork Done", "Assignment Due Date", "Assignment Marks", 
    "Midcourse Marks", "Comments", "Course Progress (%)", 
    "Mock Exams Done", "End of Chapter Questions"
]

# Creating an empty DataFrame to store check-in records
df = pd.DataFrame(columns=columns)

# Function to simulate adding check-in data
def add_checkin_data(student_name, online_curriculum_progress, bookwork_done, assignment_due_date, 
                     assignment_marks, midcourse_marks, comments, course_progress, 
                     mock_exams_done, chapter_questions):
    
    new_checkin = {
        "Student Name": student_name,
        "Check-in Date": datetime.today().strftime('%Y-%m-%d'),
        "Online Curriculum Progress (%)": online_curriculum_progress,
        "Bookwork Done": bookwork_done,
        "Assignment Due Date": assignment_due_date,
        "Assignment Marks": assignment_marks,
        "Midcourse Marks": midcourse_marks,
        "Comments": comments,
        "Course Progress (%)": course_progress,
        "Mock Exams Done": mock_exams_done,
        "End of Chapter Questions": chapter_questions
    }
    
    # Append the new check-in data to the DataFrame
    global df
    df = df.append(new_checkin, ignore_index=True)
    
    # Save to CSV for record keeping
    df.to_csv('student_checkins.csv', index=False)
    
    # Show the updated DataFrame
    print("\nUpdated Check-in Records:")
    print(df)

# Function to generate performance graphs for a student
def generate_report(student_name):
    student_data = df[df["Student Name"] == student_name]

    if student_data.empty:
        print(f"No data available for {student_name}")
        return

    # Plot student's progress over time
    plt.figure(figsize=(10, 5))
    
    # Plot Course Progress
    plt.subplot(1, 2, 1)
    plt.plot(student_data["Check-in Date"], student_data["Course Progress (%)"], marker='o')
    plt.title(f"{student_name}'s Course Progress Over Time")
    plt.xlabel("Check-in Date")
    plt.ylabel("Course Progress (%)")
    plt.xticks(rotation=45)
    
    # Plot Assignment Marks
    plt.subplot(1, 2, 2)
    plt.plot(student_data["Check-in Date"], student_data["Assignment Marks"], marker='o', color='r')
    plt.title(f"{student_name}'s Assignment Marks Over Time")
    plt.xlabel("Check-in Date")
    plt.ylabel("Assignment Marks")
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()

# Simulate adding data for a student
add_checkin_data(
    student_name="John Doe", 
    online_curriculum_progress=80, 
    bookwork_done="Yes", 
    assignment_due_date="2024-09-20", 
    assignment_marks=85, 
    midcourse_marks=90, 
    comments="Good progress", 
    course_progress=75, 
    mock_exams_done="No", 
    chapter_questions="Yes"
)

# Generate a report for the student
generate_report("John Doe")
