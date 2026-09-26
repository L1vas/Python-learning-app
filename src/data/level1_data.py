from sqlalchemy.orm import Session

from src.models import Lesson


LEVEL1_LESSONS = [
    {
        "title": "Introduction to Programming",
        "content": """
## Title: Introduction to Programming

**Learning Objectives:** Understand what programming is and why it matters.

**Explanation:** Explain programming as a way of giving instructions to computers. Discuss how programs are used in everyday life.

**Examples:** Simple examples of programs (e.g., calculators, games).

**Worked Examples:** None yet.

**Try It Yourself:** Write down what you think a program does based on its description.

**Guided Exercise:** Describe a simple task you would like to automate with a program.

**Independent Exercise:** Think of a real-world problem that could be solved with programming.

**Hints:** None yet.

**Common Mistakes:** None yet.

**Short Quiz:**
- What is programming?
  - A way to give instructions to computers
  - A type of art
  - A form of exercise

**Summary:** Programming is the process of creating instructions for computers to perform tasks. It can solve real-world problems and automate repetitive tasks.

**Practice/Review:** Think of a task you would like to automate with programming.

**Optional Challenge:** None yet.
""",
    },
    {
        "title": "Introduction to Python",
        "content": """
## Title: Introduction to Python

**Learning Objectives:** Understand what Python is and its uses.

**Explanation:** Explain Python as a versatile, beginner-friendly programming language. Discuss its applications in web development, data analysis, artificial intelligence, etc.

**Examples:** Simple examples of Python code (e.g., printing "Hello, World!").

**Worked Examples:** None yet.

**Try It Yourself:** Write down what you think Python is used for based on its description.

**Guided Exercise:** Describe a real-world problem that could be solved with Python.

**Independent Exercise:** Think of a task you would like to automate with Python.

**Hints:** None yet.

**Common Mistakes:** None yet.

**Short Quiz:**
- What is Python?
  - A programming language
  - A type of fruit
  - A musical instrument

**Summary:** Python is a versatile, beginner-friendly programming language used for web development, data analysis, artificial intelligence, and more. It is known for its readability and ease of use.

**Practice/Review:** Think of a task you would like to automate with Python.

**Optional Challenge:** None yet.
""",
    },
    {
        "title": "Understanding Program Flow",
        "content": """
## Title: Understanding Program Flow

**Learning Objectives:** Understand how programs execute step-by-step.

**Explanation:** Explain the concept of program flow, including input, processing, and output. Use everyday analogies to help understand these concepts.

**Examples:** Simple examples of program flow (e.g., a recipe).

**Worked Examples:** None yet.

**Try It Yourself:** Describe the steps in a simple recipe as a program.

**Guided Exercise:** Break down a simple task into input, processing, and output steps.

**Independent Exercise:** Think of a real-world process you would like to automate with programming.

**Hints:** None yet.

**Common Mistakes:** None yet.

**Short Quiz:**
- What are the three main components of program flow?
  - Input, Processing, Output
  - Start, Middle, End
  - Read, Write, Execute

**Summary:** Programs execute step-by-step, taking input, processing it, and producing output. Understanding this flow is crucial for writing effective programs.

**Practice/Review:** Break down a simple task into input, processing, and output steps.

**Optional Challenge:** None yet.
""",
    },
    {
        "title": "Writing Your First Python Program",
        "content": """
## Title: Writing Your First Python Program

**Learning Objectives:** Write and run your first Python program.

**Explanation:** Explain how to write and execute a simple "Hello, World!" program in Python. Discuss the purpose of each line of code.

**Examples:**

```python
print("Hello, World!")
```

**Worked Examples:** None yet.

**Try It Yourself:** Write a program that prints your name.

**Guided Exercise:** Write a program that prints "Welcome to Python Coach!"

**Independent Exercise:** Write a program that prints "I am learning Python."

**Hints:** Use the `print()` function to display text on the screen.

**Common Mistakes:**
- Forgetting to use quotes around strings
- Missing parentheses after print

**Short Quiz:**
- What does the `print()` function do?
  - Displays text on the screen
  - Hides text from the screen
  - Deletes text from the screen

**Summary:** The `print()` function is used to display text on the screen. Writing a simple program involves using this function and understanding its syntax.

**Practice/Review:** Write a program that prints "I am learning Python."

**Optional Challenge:** Write a program that prints your name and age.
""",
    },
    {
        "title": "Using the `print()` Function",
        "content": """
## Title: Using the `print()` Function

**Learning Objectives:** Understand how to use the `print()` function effectively.

**Explanation:** Explain the purpose of the `print()` function, including its syntax and common uses. Discuss how to format output using multiple arguments and escape characters.

**Examples:**

```python
print("Hello", "World!")
print("The answer is:", 42)
print("This is a new line.\\nAnd this is the next line.")
```

**Worked Examples:** None yet.

**Try It Yourself:** Write a program that prints your name and age on separate lines.

**Guided Exercise:** Write a program that prints "Hello, [name]! You are [age] years old."

**Independent Exercise:** Write a program that prints "Today is [day], and the weather is [weather]."

**Hints:** Use commas to separate multiple arguments in `print()`. Use `\\n` for new lines.

**Common Mistakes:** Forgetting to use quotes around strings, missing commas between arguments.

**Short Quiz:**
- What does the following code do?

```python
print("Hello", "World!")
```

  - Displays "Hello World!"
  - Displays "Hello, World!"
  - Displays "HelloWorld!"

**Summary:** The `print()` function is versatile and can display multiple pieces of information on the screen. Using commas separates arguments, and `\\n` creates new lines.

**Practice/Review:** Write a program that prints your name and age on separate lines.

**Optional Challenge:** Write a program that prints "Today is [day], and the weather is [weather]." with each piece of information on a new line.
""",
    },
    {
        "title": "Adding Comments to Your Code",
        "content": """
## Title: Adding Comments to Your Code

**Learning Objectives:** Understand how to add comments to your code.

**Explanation:** Explain what comments are, why they are used, and how to write them in Python. Discuss the difference between single-line (`#`) and multi-line (`'''` or `\"\"\"`) comments.

**Examples:**

```python
# This is a single-line comment
print("Hello, World!")  # This is an inline comment

\"\"\"
This is a multi-line comment.
It can span multiple lines.
\"\"\"
```

**Worked Examples:** None yet.

**Try It Yourself:** Write a program that prints "Hello, World!" with a single-line comment explaining what the code does.

**Guided Exercise:** Write a program that prints "Welcome to Python Coach!" with a multi-line comment explaining the purpose of the program.

**Independent Exercise:** Write a program that prints "I am learning Python." with both single-line and multi-line comments.

**Hints:** Use `#` for single-line comments. Use triple quotes (`'''` or `\"\"\"`) for multi-line comments.

**Common Mistakes:** Forgetting to use the correct comment syntax, placing comments in invalid locations.

**Short Quiz:**
- What is a comment?
  - A piece of code that is executed
  - A note for the programmer
  - A placeholder for future code

**Summary:** Comments are notes for programmers. They do not affect the execution of the program and help explain what the code does.

**Practice/Review:** Write a program that prints "Hello, World!" with a single-line comment explaining what the code does.

**Optional Challenge:** Write a program that prints "Welcome to Python Coach!" with a multi-line comment explaining the purpose of the program.
""",
    },
    {
        "title": "Working with Strings",
        "content": """
## Title: Working with Strings

**Learning Objectives:** Understand how to work with strings in Python.

**Explanation:** Explain what strings are, how to create them, and common operations you can perform on them. Discuss string concatenation, indexing, slicing, and methods like `len()`, `upper()`, and `lower()`.

**Examples:**

```python
greeting = "Hello"
name = "World"
full_greeting = greeting + ", " + name + "!"
print(full_greeting)  # Output: Hello, World!

first_letter = greeting[0]  # 'H'
last_letter = greeting[-1]  # 'o'

substring = greeting[1:3]  # 'el'

length = len(greeting)  # 5

upper_greeting = greeting.upper()  # 'HELLO'
lower_greeting = greeting.lower()  # 'hello'
```

**Worked Examples:** None yet.

**Try It Yourself:** Write a program that concatenates your first name and last name with a space in between.

**Guided Exercise:** Write a program that prints the first letter of your name.

**Independent Exercise:** Write a program that prints the length of your name.

**Hints:** Use + for string concatenation. Use square brackets (`[]`) for indexing. Use slicing to get substrings. Use methods like `len()`, `upper()`, and `lower()` to perform operations on strings.

**Common Mistakes:** Forgetting to use quotes around strings, using invalid indices or slices.

**Short Quiz:**
- What is a string?
  - A sequence of characters
  - A number
  - A boolean value
- How do you concatenate two strings in Python?
  - Using the + operator
  - Using the - operator
  - Using the * operator

**Summary:** Strings are sequences of characters. You can create them using quotes, perform operations like concatenation, indexing, and slicing, and use methods to manipulate their content.

**Practice/Review:** Write a program that concatenates your first name and last name with a space in between.

**Optional Challenge:** Write a program that prints the length of your name and converts it to uppercase.
""",
    },
    {
        "title": "Working with Numbers",
        "content": """
## Title: Working with Numbers

**Learning Objectives:** Understand how to work with numbers in Python.

**Explanation:** Explain what numbers are, how to create them, and common operations you can perform on them. Discuss arithmetic operators (+, -, *, /), the difference between integers and floats, and methods like `round()`.

**Examples:**

```python
a = 5
b = 3

sum = a + b  # 8
difference = a - b  # 2
product = a * b  # 15
quotient = a / b  # 1.666...

rounded_quotient = round(quotient, 2)  # 1.67

is_integer = isinstance(a, int)  # True
is_float = isinstance(b, float)  # False
```

**Worked Examples:** None yet.

**Try It Yourself:** Write a program that adds two numbers and prints the result.

**Guided Exercise:** Write a program that multiplies two numbers and prints the result.

**Independent Exercise:** Write a program that divides two numbers and rounds the result to two decimal places.

**Hints:** Use arithmetic operators (+, -, *, /) for basic operations. Use `round()` to round numbers. Use `isinstance()` to check the type of a number.

**Common Mistakes:** Forgetting to use parentheses around expressions, using invalid operators.

**Short Quiz:**
- What is a number?
  - A sequence of characters
  - A value representing quantity
  - A boolean value
- How do you divide two numbers in Python?
  - Using the / operator
  - Using the * operator
  - Using the - operator

**Summary:** Numbers are values representing quantities. You can create them using numeric literals, perform operations like addition, subtraction, multiplication, and division, and use methods to manipulate their content.

**Practice/Review:** Write a program that adds two numbers and prints the result.

**Optional Challenge:** Write a program that multiplies two numbers and rounds the result to two decimal places.
""",
    },
    {
        "title": "Using Variables",
        "content": """
## Title: Using Variables

**Learning Objectives:** Understand how to use variables in Python.

**Explanation:** Explain what variables are, how to create them, and common operations you can perform on them. Discuss variable naming conventions, assignment using =, and the difference between mutable and immutable data types.

**Examples:**

```python
name = "Alice"
age = 30

print(name)  # Output: Alice
print(age)   # Output: 30

name = "Bob"  # Reassigning a variable
```

**Worked Examples:** None yet.

**Try It Yourself:** Write a program that assigns your name to a variable and prints it.

**Guided Exercise:** Write a program that assigns your age to a variable and prints it.

**Independent Exercise:** Write a program that reassigns the value of a variable and prints the new value.

**Hints:** Use = to assign values to variables. Choose descriptive names for variables. Be aware that strings are immutable, while numbers can be reassigned.

**Common Mistakes:** Forgetting to use quotes around strings, using invalid variable names.

**Short Quiz:**
- What is a variable?
  - A sequence of characters
  - A value that can change
  - A boolean value
- How do you assign a value to a variable in Python?
  - Using the = operator
  - Using the - operator
  - Using the * operator

**Summary:** Variables are values that can change. You can create them using assignment (=), and they help store and manipulate data.

**Practice/Review:** Write a program that assigns your name to a variable and prints it.

**Optional Challenge:** Write a program that reassigns the value of a variable and prints the new value.
""",
    },
    {
        "title": "Assigning Values to Variables",
        "content": """
## Title: Assigning Values to Variables

**Learning Objectives:** Understand how to assign values to variables effectively.

**Explanation:** Explain the concept of assignment using =. Discuss best practices for assigning values, including choosing descriptive variable names and avoiding reserved keywords.

**Examples:**

```python
name = "Alice"
age = 30

print(name)  # Output: Alice
print(age)   # Output: 30
```

**Worked Examples:** None yet.

**Try It Yourself:** Write a program that assigns your favorite color to a variable and prints it.

**Guided Exercise:** Write a program that assigns the number of siblings you have to a variable and prints it.

**Independent Exercise:** Write a program that assigns the name of your pet (if any) to a variable and prints it.

**Hints:** Use = to assign values to variables. Choose descriptive names for variables. Avoid using reserved keywords as variable names.

**Common Mistakes:** Forgetting to use quotes around strings, using invalid variable names.

**Short Quiz:**
- What is the purpose of assignment in Python?
  - To create a new variable
  - To assign a value to an existing variable
  - To delete a variable
- How do you assign a value to a variable in Python?
  - Using the = operator
  - Using the - operator
  - Using the * operator

**Summary:** Assignment is the process of assigning a value to a variable. It helps store and manipulate data effectively.

**Practice/Review:** Write a program that assigns your favorite color to a variable and prints it.

**Optional Challenge:** Write a program that assigns the number of siblings you have to a variable and prints it.
""",
    },
    {
        "title": "Performing Arithmetic Operations",
        "content": """
## Title: Performing Arithmetic Operations

**Learning Objectives:** Understand how to perform arithmetic operations in Python.

**Explanation:** Explain the basic arithmetic operators (+, -, *, /) and their uses. Discuss order of operations (PEMDAS/BODMAS) and how to use parentheses to control it.

**Examples:**

```python
a = 10
b = 3

sum = a + b  # 13
difference = a - b  # 7
product = a * b  # 30
quotient = a / b  # 3.333...

result = (a + b) * 2  # 26
```

**Worked Examples:** None yet.

**Try It Yourself:** Write a program that adds two numbers and prints the result.

**Guided Exercise:** Write a program that multiplies two numbers and prints the result.

**Independent Exercise:** Write a program that divides two numbers and prints the result, controlling the order of operations with parentheses.

**Hints:** Use arithmetic operators (+, -, *, /) for basic operations. Use parentheses to control the order of operations.

**Common Mistakes:** Forgetting to use parentheses around expressions, using invalid operators.

**Short Quiz:**
- What are the four basic arithmetic operators in Python?
  - +, -, *, /
  - +, -, *, %
  - +, -, *, **
- What is the order of operations in arithmetic?
  - PEMDAS/BODMAS
  - MDAS/BOMA
  - DMAS/BMOD

**Summary:** Arithmetic operations involve basic mathematical calculations.

**Practice/Review:** Write a program that adds two numbers and prints the result.

**Optional Challenge:** Write a program that multiplies two numbers and rounds the result to two decimal places.
""",
    },
]


def add_or_update_lesson(db: Session, title: str, content: str) -> Lesson:
    """Create a lesson if it does not exist, otherwise update its content."""

    lesson = db.query(Lesson).filter(Lesson.title == title).first()

    if lesson is None:
        lesson = Lesson(title=title, content=content)
        db.add(lesson)
    else:
        lesson.content = content

    return lesson


def populate_level1(db: Session) -> None:
    """Create or update all Level 1 lessons without creating duplicates."""

    for lesson_data in LEVEL1_LESSONS:
        add_or_update_lesson(
            db,
            lesson_data["title"],
            lesson_data["content"],
        )

    db.commit()
