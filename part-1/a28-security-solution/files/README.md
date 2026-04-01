# Password Strength Checker

A command-line tool that evaluates the strength of a password across six security criteria and returns a score out of 10, a strength label, and specific feedback for any failed checks.

---

## How to Run

```
python password_checker.py
```

You will be prompted to enter a password. The tool will then display your score, strength label, and feedback instantly.

---

## Scoring Breakdown

The tool scores passwords out of **10 points** across six checks:

| Check | Criteria | Points |
|---|---|---|
| (a) Length | ≤8 characters | 0 |
| | 9–11 characters | 1 |
| | 12–15 characters | 2 |
| | 16+ characters | 3 |
| (b) Uppercase letters | At least one A–Z | +1 |
| (c) Lowercase letters | At least one a–z | +1 |
| (d) Digits | At least one 0–9 | +1 |
| (e) Special characters | At least one e.g. !@#$%^&* | +1 |
| (f) Not a common password | Not in the known weak password list | +3 (or forces score to 0 if common) |

**Strength labels:**

| Score | Label |
|---|---|
| 0–2 | Weak |
| 3–5 | Fair |
| 6–8 | Good |
| 9–10 | Strong |

---

## Example Output

```
=============================================
       PASSWORD STRENGTH CHECKER
=============================================
Enter a password to check: MySecure#Pass2025

Score   : 10/10
Strength: Strong

Feedback:
  [+] Length is strong (16+ characters)
  [+] Contains uppercase letter(s)
  [+] Contains lowercase letter(s)
  [+] Contains digit(s)
  [+] Contains special character(s)
  [+] Not a common password
```

---

## Security Rationale

**(a) Length**
Length is the single most important factor in password strength. Every additional character exponentially increases the number of possible combinations an attacker must try in a brute-force attack. A password of 16+ characters is considered strong because even modern hardware would take an impractical amount of time to crack it through exhaustive search.

**(b) Uppercase letters**
Mixing uppercase and lowercase letters increases the character set from 26 to 52 possibilities per character. This directly raises the cost of both brute-force and dictionary attacks, which often target all-lowercase passwords first.

**(c) Lowercase letters**
Passwords composed entirely of uppercase letters are uncommon and are therefore targeted in certain attack patterns. Using both cases together maximises unpredictability and resists pattern-based cracking strategies.

**(d) Digits**
Adding digits (0–9) expands the character set further and breaks up letter-only patterns. Many dictionary attack wordlists consist of words without numbers, so their inclusion forces attackers to use larger, slower attack sets.

**(e) Special characters**
Special characters such as `!@#$%^&*` dramatically increase the keyspace. Passwords with mixed character types require significantly more computation to crack and are typically excluded from simple dictionary wordlists entirely.

**(f) Common password check**
No matter how long or complex a password appears, if it appears on a known password list it can be cracked instantly using a lookup attack — no guessing required. Lists of breached passwords are publicly available and are the first thing attackers use. This check is treated as a hard fail: a common password scores 0 regardless of other criteria.

---

## Common Passwords List

The tool checks against the following known weak passwords:

`password`, `123456`, `123456789`, `qwerty`, `abc123`, `password1`, `111111`, `iloveyou`, `letmein`, `monkey`, `dragon`, `master`, `sunshine`, `princess`, `welcome`
