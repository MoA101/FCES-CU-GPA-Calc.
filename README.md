# GPA Calculator for FCES students 

This is a project done with Python 3 to help students calculate their GPA easily at Faculty of Commerce English section at Cairo University.

The input() function is used to prompt the user for the number of courses and their corresponding letter grades. To ensure accurate processing, the strip() function cleans up any extra spaces in the user's input, while the upper() function converts the input to uppercase, making it consistent with the grading scale defined in the script.

The int() function is employed to convert the user's input for the number of courses from a string to an integer, allowing for numerical calculations. The print() function is used throughout the script to display prompts and the final calculated GPA, providing clear feedback to the user.

The project uses a for loop to go through each course one by one. For each course, the loop asks the user to enter their letter grade. It then checks if the grade is valid. If it is, the corresponding grade points are added to the total. If the grade is not valid, it assigns 0.0 grade points. This loop helps gather all the grade points needed to calculate the GPA at the end.
