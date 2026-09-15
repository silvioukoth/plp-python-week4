# Grade Classifier
# This program validates a score and assigns a grade.

score = int(input("Enter your score (0-100): "))

# Check if the score is outside the valid range.
if score < 0 or score > 100:
    print("Invalid score. Please enter a score between 0 and 100.")

# Check if the score is 80 or above.
elif score >= 80:
    print(f"A score of {score} earns grade: A")

# Check if the score is between 70 and 79.
elif score >= 70:
    print(f"A score of {score} earns grade: B")

# Check if the score is between 60 and 69.
elif score >= 60:
    print(f"A score of {score} earns grade: C")

# Check if the score is between 50 and 59.
elif score >= 50:
    print(f"A score of {score} earns grade: D")

# Any remaining valid score is below 50.
else:
    print(f"A score of {score} earns grade: F")