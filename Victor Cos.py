def get_grade(score):
    if 70 <= score <= 100:
        return "A"
    elif 60 <= score <= 69:
        return "B"
    elif 50 <= score <= 59:
        return "C"
    elif 45 <= score <= 49:
        return "D"
    elif 40 <= score <= 44:
        return "E"
    elif 0 <= score <= 39:
        return "F"
    else:
        return "Invalid score"

def main():
    user_input = input("Enter student score (0–100): ")

    if user_input.isdigit():
        score = int(user_input)
        grade = get_grade(score)
        print("Grade:", grade)
    else:
        print("Invalid input. Please enter a number between 0 and 100.")

main()