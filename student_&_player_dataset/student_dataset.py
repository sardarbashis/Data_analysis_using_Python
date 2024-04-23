import csv

def process_student_marks(input_file, output_file):
    with open(input_file, 'r') as f:
        reader = csv.DictReader(f)
        students = []

        for row in reader:
            # Initialize total marks and count of subjects
            total_marks = 0
            subjects_count = 0
            # Iterate over each subject
            for subject in reader.fieldnames[3:]:  # Skip the first three columns which are not subjects
                # Check if the mark is not empty
                if row[subject].strip():
                    # Add to total marks and increment subject count
                    total_marks += int(row[subject])
                    subjects_count += 1
            # Calculate average marks
            average_marks = total_marks / subjects_count if subjects_count else 0
            # Add total and average marks to the row
            row['total_marks'] = total_marks
            row['Average'] = average_marks
            students.append(row)

    with open(output_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=reader.fieldnames + ['total_marks', 'Average'])
        writer.writeheader()
        writer.writerows(students)

process_student_marks('student_marks.csv', 'processed_student_marks.csv')
