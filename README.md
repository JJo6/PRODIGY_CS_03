# PRODIGY_CS_03
## Password Complexity Checker
This project implements a simple graphical user interface (GUI) for assessing the strength of passwords entered by users. The strength assessment is based on various criteria such as password length, presence of uppercase and lowercase letters, numbers, and special characters. Feedback on the password's strength, along with suggestions for improvement, is provided to the users.

![image](https://github.com/JJo6/PRODIGY_CS_03/assets/87189227/9038b712-38cc-4f24-80fa-e1123636d771)


**Files:**

password_strength_assessor.py: Contains the implementation of the password strength assessment algorithm and the GUI using the Tkinter library in Python. It provides a text input field for users to enter a password, a button to initiate the assessment, and a label to display the assessed strength, suggestions, and word count.
Time Complexity:
The time complexity of the password strength assessment algorithm is O(n), where n is the length of the password. This is because the algorithm iterates over each character in the password once to check for various criteria.

**How to Run:**
To run the program:

Make sure you have Python installed on your system.
Download or clone the repository containing the code.
Navigate to the directory.
Run the program by executing the command: python pass.py.
The GUI window will open, allowing users to input a password and see the assessed strength, suggestions, and word count.

![image](https://github.com/JJo6/PRODIGY_CS_03/assets/87189227/5df40c24-648e-4561-b287-f7467286aa72)


**Notes:**

The program provides suggestions for password improvement based on its assessed strength.
It displays the number of words entered in addition to the strength assessment.
Users can input any type of password, including alphanumeric and special characters.
The GUI is simple and intuitive, making it easy for users to interact with the tool.

**Additional Considerations:**

Error handling: Ensure proper handling of edge cases such as empty input or invalid characters.
Testing: Conduct thorough testing to validate the accuracy of the password strength assessment algorithm.
Documentation: Include comments within the code to explain its functionality and usage, making it easier for other developers to understand and contribute.
