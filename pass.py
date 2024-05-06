import re
import tkinter as tk
from tkinter import messagebox

def assess_password_strength(password):
    # Define criteria
    length_criteria = len(password) >= 8
    lowercase_criteria = bool(re.search(r"[a-z]", password))
    uppercase_criteria = bool(re.search(r"[A-Z]", password))
    digit_criteria = bool(re.search(r"\d", password))
    special_char_criteria = bool(re.search(r"[!@#$%^&*()_+{}\[\]:;<>,.?/~\\-]", password))

    # Assess strength
    if length_criteria and lowercase_criteria and uppercase_criteria and digit_criteria and special_char_criteria:
        return "Strong", "Your password is strong. Good job!"
    elif length_criteria and lowercase_criteria and uppercase_criteria and digit_criteria:
        return "Moderate", "Your password is moderate. Consider adding special characters."
    elif length_criteria and lowercase_criteria and uppercase_criteria:
        return "Weak", "Your password is weak. Consider adding numbers and special characters."
    else:
        return "Very Weak", "Your password is very weak. Please improve it."

# GUI using Tkinter
def assess_strength():
    password = password_entry.get()
    strength, suggestion = assess_password_strength(password)
    char_count = len(password)
    special_char_count = sum(1 for char in password if re.match(r'[!@#$%^&*()_+{}\[\]:;<>,.?/~\\-]', char))
    result_label.config(text=f"Strength: {strength}\nSuggestions: {suggestion}\nCharacter Count: {char_count}\nSpecial Character Count: {special_char_count}")

# Create the main window
root = tk.Tk()
root.title("Password Strength Assessor")

# Create and place widgets
password_label = tk.Label(root, text="Enter Password:")
password_label.pack(pady=5)

password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

assess_button = tk.Button(root, text="Assess Strength", command=assess_strength)
assess_button.pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack(pady=5)

# Coded by Jagjot
coded_by_label = tk.Label(root, text="Coded by Jagjot")
coded_by_label.pack(pady=5)

# Run the application
root.mainloop()
