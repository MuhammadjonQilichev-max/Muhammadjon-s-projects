def calculate_average(score1, score2, score3):
    average = (score1+score2+score3)/3
    return average
def drop_lowest(score1, score2, score3):
    scores = [score1, score2, score3]
    lowest = min(scores)
    average_high2 = (sum(scores)-lowest)/2
    return average_high2
def calculate_weighted(assignments, midterm, final):
    assignments_f = assignments * 0.30
    midterm_f = midterm * 0.30
    final_f = final * 0.40
    weighted_average = assignments_f + midterm_f + final_f
    return weighted_average
def determine_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"
def needs_improvement(current_avg, target_grade):
    if target_grade == 'A':
        return current_avg < 90
    elif target_grade == 'B':
        return current_avg < 80
    elif target_grade == 'C':
        return current_avg < 70
    elif target_grade == 'D':
        return current_avg < 60
def grade_calculator():
    score1 = int(input("Enter the 1st Assignment score: "))
    score2 = int(input("Enter the 2nd Assignment score: "))
    score3 = int(input("Enter the 3rd Assignment score: "))
    midterm_score = int(input("Enter the midterm score: "))
    final_score = int(input("Enter the final score: "))
    avg_assignment_score = calculate_average(score1, score2, score3)
    avg_with_lowest_dropped = drop_lowest(score1, score2, score3)
    better_avg = max(avg_assignment_score, avg_with_lowest_dropped)
    avg_weighted = calculate_weighted(better_avg, midterm_score, final_score)
    grade = determine_grade(avg_weighted)

    improvement_for_a = needs_improvement(avg_weighted, 'A')


# Test Data
assignment_scores = (85, 78, 92)
midterm = 88
final = 82

# Calculations
regular_avg = calculate_average(*assignment_scores)
dropped_avg = drop_lowest(*assignment_scores)
better_avg = max(regular_avg, dropped_avg)

weighted_avg = calculate_weighted(better_avg, midterm, final)
letter_grade = determine_grade(weighted_avg)
improvement_needed, points_needed = needs_improvement(weighted_avg, 'A')

print("STUDENT GRADE CALCULATOR")
print("========================================")
print(f"Assignment Scores: {assignment_scores[0]}, {assignment_scores[1]}, {assignment_scores[2]}")
print(f"Midterm Score: {midterm}")
print(f"Final Score: {final}")
print("----------------------------------------")
print(f"Regular Assignment Average: {regular_avg:.2f}")
print(f"Average with Lowest Dropped: {dropped_avg:.2f}")
print(f"Using Better Average: {better_avg:.2f}")
print()
print(f"Weighted Course Average: {weighted_avg:.2f}")
print(f"Letter Grade: {letter_grade}")
print()
if improvement_needed:
    print(f"Needs improvement for an 'A': Yes")
    print(f"Points needed: {points_needed:.2f}")
else:
    print(f"Needs improvement for an 'A': No")
print(f"Already meets or exceeds 'B' grade requirement")

    


    
