import re
def evaluate_password_strength(password):

    length_criteria = False
    upper_case_criteria = False
    lower_case_criteria = False
    number_criteria = False
    special_char_criteria = False

    if len(password) >= 8:
        length_criteria = True


    if re.search(r'[A-Z]', password):
        upper_case_criteria = True


    if re.search(r'[a-z]', password):
        lower_case_criteria = True

    if re.search(r'[0-9]', password):
        number_criteria = True

    if re.search(r'[@$!%*?&]', password):
        special_char_criteria = True

    strength_score = sum([length_criteria, upper_case_criteria, lower_case_criteria, number_criteria, special_char_criteria])
    if strength_score == 5:
        strength = "Very Strong"
    elif strength_score == 4:
        strength = "Strong"
    elif strength_score == 3:
        strength = "Medium"
    else:
        strength = "Weak"

    return strength


def main():
    print("Password Strength Evaluation Tool")
    print("-------------------------------")
    password = input("Enter a password to evaluate: ")
    strength = evaluate_password_strength(password)
    print(f"Password Strength: {strength}")

if __name__ == "__main__":
    main()
