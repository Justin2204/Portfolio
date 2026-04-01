COMMON_PASSWORDS = [
    "password", "123456", "123456789", "qwerty", "abc123",
    "password1", "111111", "iloveyou", "letmein", "monkey",
    "dragon", "master", "sunshine", "princess", "welcome",
]

SPECIAL_CHARS = set("!@#$%^&*()-_=+[]{}|;:',.<>?/`~\"\\")


def check_password(password):
    score = 0
    feedback = []

    # (a) Length check — worth up to 3 points
    n = len(password)
    if n <= 8:
        score += 0
        feedback.append("[-] Length is too short (<=8 characters) — aim for at least 9")
    elif n <= 11:
        score += 1
        feedback.append("[~] Length is fair (9-11 characters) — consider 12 or more")
    elif n <= 15:
        score += 2
        feedback.append("[+] Length is good (12-15 characters)")
    else:
        score += 3
        feedback.append("[+] Length is strong (16+ characters)")

    # (b) Uppercase letters — 1 point
    if any(c.isupper() for c in password):
        score += 1
        feedback.append("[+] Contains uppercase letter(s)")
    else:
        feedback.append("[-] Missing uppercase letter — add at least one (e.g. A-Z)")

    # (c) Lowercase letters — 1 point
    if any(c.islower() for c in password):
        score += 1
        feedback.append("[+] Contains lowercase letter(s)")
    else:
        feedback.append("[-] Missing lowercase letter — add at least one (e.g. a-z)")

    # (d) Digits — 1 point
    if any(c.isdigit() for c in password):
        score += 1
        feedback.append("[+] Contains digit(s)")
    else:
        feedback.append("[-] Missing digit — add at least one number (0-9)")

    # (e) Special characters — 1 point
    if any(c in SPECIAL_CHARS for c in password):
        score += 1
        feedback.append("[+] Contains special character(s)")
    else:
        feedback.append("[-] Missing special character — add one (e.g. !@#$%^&*)")

    # (f) Common password check — worth 3 points, hard fail if common
    if password.lower() in COMMON_PASSWORDS:
        score = 0  # override entire score; common passwords are always weak
        feedback.append("[-] This is a known common password — choose something unique!")
    else:
        score += 3
        feedback.append("[+] Not a common password")

    # Determine strength label
    if score <= 2:
        label = "Weak"
    elif score <= 5:
        label = "Fair"
    elif score <= 8:
        label = "Good"
    else:
        label = "Strong"

    return score, label, feedback


def main():
    print("=" * 45)
    print("       PASSWORD STRENGTH CHECKER")
    print("=" * 45)

    password = input("Enter a password to check: ")

    score, label, feedback = check_password(password)

    print(f"\nScore   : {score}/10")
    print(f"Strength: {label}")
    print("\nFeedback:")
    for line in feedback:
        print(f"  {line}")
    print()


if __name__ == "__main__":
    main()
