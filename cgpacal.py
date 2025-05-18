def grade_to_points(percentage):
    """Convert numerical grade to GPA points based on a 4.0 scale."""
    if 70 <= percentage <= 100:
        return 5.0
    elif 60 <= percentage < 70:
        return 4.0
    elif 50 <= percentage < 60:
        return 3.0
    elif 45 <= percentage < 50:
        return 2.0
    elif 0 <= percentage < 45:
        return 0.0
    else:
        return None  # Invalid percentage


def calculate_gpa():
    total_points = 0.0
    total_credits = 0.0
    num_courses = 6

    
    print("Enter the grade percentages and credit hours for each of your 6 courses:")

    for i in range(1, num_courses + 1):
        while True:
            try:
                # Get the grade and credit hours for each course
                percentage = float(input(f"Course {i} percentage (0-100): "))
                credits = float(input(f"Course {i} credit hours: "))

                # Ensure valid input for credit hours
                if credits <= 0:
                    print("Credit hours must be a positive number. Please enter a valid number of credit hours.")
                    continue

                points = grade_to_points(percentage)
                
                if points is not None:
                    # Calculate the weighted points for the course
                    weighted_points = points * credits
                    total_points += weighted_points
                    total_credits += credits
                    print(f"Course {i}: Grade: {percentage}% | GPA Points: {points} | Weighted Points: {weighted_points}")
                    break
                else:
                    print("Invalid percentage. Please enter a valid grade between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter valid numbers for both percentage and credit hours.")

    # Calculate the weighted GPA
    if total_credits > 0:
        gpa = total_points / total_credits
        print(f"\nYour overall GPA is: {gpa:.2f}")
    else:
        print("Error: Total credits cannot be zero.")

# Run the program
calculate_gpa()
