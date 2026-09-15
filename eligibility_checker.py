# Eligibility Checker
# This program checks whether a person can join a coding club.

age = int(input("Enter your age: "))

# Adults aged 18 or older are automatically eligible.
if age >= 18:
    print("Welcome to the club!")

# Teenagers aged 13-17 need parental consent.
elif age >= 13:
    consent = input("Do you have parental consent? (yes/no): ").strip().lower()

    # A teenager is eligible when they have consent and are within the allowed age range.
    if age >= 13 and (consent == "yes" or consent == "y"):
        print("Welcome to the club!")
    else:
        print("Sorry, you are not eligible yet.")

# Anyone under 13 is not eligible.
else:
    print("Sorry, you are not eligible yet.")