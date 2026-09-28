# src/data/level3_data.py

LEVEL3_LESSONS = [
    {
        "title": 'Lesson 1 — Repeating Work',
        "content": (
            '    # Module: Why Loops Exist\n'
            '    # Learning Objectives\n'
            '    - Understand repetition in programming.\n'
            '- Recognize when repeated work is useful.\n'
            '- Understand the general idea of a loop before learning loop syntax.\n'
            '\n'
            '    # Why This Matters\n'
            '    Programs often need to perform the same kind of action many times. A reminder program may display several messages, a game may check many turns, and a validation program may ask for an answer again. Writing every repeated instruction by hand quickly becomes difficult to maintain.\n'
            '\n'
            '    # Explanation\n'
            '    Repetition means performing an action more than once. A loop is a programming structure that lets Python repeat a block of instructions according to a rule. The rule might be a known number of repetitions, a sequence of values, or a condition. The important idea is not the syntax yet; it is the reason loops exist: they turn repeated work into a small, understandable set of instructions.\n'
            '\n'
            '    # Examples\n'
            '    Without a loop:\n'
            '```python\n'
            'print("Hello")\n'
            'print("Hello")\n'
            'print("Hello")\n'
            '```\n'
            '\n'
            'With a loop, the repeated instruction can be written once. Python can then perform it several times. This is especially useful when the number of repetitions changes later.\n'
            '\n'
            '    # Worked Example\n'
            '    Imagine a program that needs to print a status message 100 times. Copying the same `print()` line 100 times would make the program long and harder to change. A loop gives the program one description of the repeated task instead.\n'
            '\n'
            '    # Beginner-Friendly Explanation\n'
            '    Before learning loop syntax, identify the repeated part of a task. In `print("Hello")` repeated three times, the message is the same and only the repetition count changes. That repeated action is the part a loop is designed to control.\n'
            '\n'
            '    # Try It Yourself\n'
            '    Decide which of three everyday tasks require repetition and explain why.\n'
            '\n'
            '    # Guided Exercise\n'
            '    Mark these tasks as repeated or one-time: print a welcome message once; print a receipt with ten items; ask for a password until it is correct.\n'
            '\n'
            '    # Independent Exercise\n'
            '    Describe one useful computer task that would become awkward if every repetition had to be written separately.\n'
            '\n'
            '    # Hints\n'
            '    Start by identifying what stays the same and what changes. The repeated instruction is the key part.\n'
            '\n'
            '    # Common Mistakes\n'
            '    - Thinking a loop is a variable.\n'
            '- Trying to memorize syntax before understanding the purpose.\n'
            '- Assuming every task needs a loop; some tasks really happen only once.\n'
            '\n'
            '    # Short Quiz\n'
            '    1. What does repetition mean in programming?\n'
            '2. What is the main purpose of a loop?\n'
            '3. Name one situation where repetition is useful.\n'
            '\n'
            '    # Answer and Explanation\n'
            '    1. Repetition means performing an action more than once.\n'
            '2. A loop lets Python repeat a block of instructions according to a rule.\n'
            '3. Examples include counting, repeated input, and processing several values.\n'
            '\n'
            '    # Summary\n'
            '    Loops make repeated work shorter, clearer, and easier to change.\n'
            '\n'
            '    # Practice/Review\n'
            '    For three tasks you already know from Levels 1–2, identify which part could eventually be repeated by a loop.\n'
            '\n'
            '    # Optional Challenge\n'
            '    Imagine a program that must repeat a task 10,000 times. Explain why a loop is a better fit than copying the same statement 10,000 times.\n'
        ),
        "exercises": [
            {
                "instructions": 'Print the word Hello three times using three print statements. This gives you a baseline to compare with a loop later.',
                "starter_code": 'print("Hello")\nprint("Hello")\nprint("Hello")\n',
                "expected_output": 'Hello\nHello\nHello',
            },
            {
                "instructions": 'Print the numbers 1, 2, and 3 on separate lines.',
                "starter_code": '# Write three print statements.\n',
                "expected_output": '1\n2\n3',
            },
        ],
    },
    {
        "title": 'Lesson 2 — Your First while Loop',
        "content": (
            '    # Module: While Loops\n'
            '    # Learning Objectives\n'
            '    - Understand the purpose of a while loop.\n'
            '- Identify the condition, body, and changing value.\n'
            '- Explain why a simple while loop stops.\n'
            '\n'
            '    # Why This Matters\n'
            '    A `while` loop is useful when Python should keep repeating while a condition remains true. This connects directly to the `True` and `False` values and comparisons you learned in Level 2.\n'
            '\n'
            '    # Explanation\n'
            '    A `while` loop checks a condition before each repetition. If the condition is `True`, Python runs the indented loop body. After the body finishes, Python checks the condition again. A simple counting loop needs a value that changes so the condition can eventually become false.\n'
            '\n'
            '    # Examples\n'
            '    ```python\n'
            'count = 1\n'
            'while count <= 3:\n'
            '    print(count)\n'
            '    count = count + 1\n'
            '```\n'
            '\n'
            'The condition is `count <= 3`. The loop body is the two indented lines.\n'
            '\n'
            '    # Worked Example\n'
            '    `count = 1` creates the starting value. `while count <= 3:` asks whether the current value is at most 3. `print(count)` shows the current value. `count = count + 1` changes the value so the loop can move toward its stopping point.\n'
            '\n'
            '    # Beginner-Friendly Explanation\n'
            '    Execution goes like this:\n'
            '1. `count` is 1, so the condition is true.\n'
            '2. Print 1.\n'
            '3. Change `count` to 2.\n'
            '4. Repeat for 2 and 3.\n'
            '5. When `count` becomes 4, `4 <= 3` is false, so the loop stops.\n'
            '\n'
            '    # Try It Yourself\n'
            '    Write a while loop that prints 1, 2, and 3.\n'
            '\n'
            '    # Guided Exercise\n'
            '    Start with `count = 1`, use `while count <= 3`, print the count, then increase it.\n'
            '\n'
            '    # Independent Exercise\n'
            '    Change the loop so it prints 1 through 5.\n'
            '\n'
            '    # Hints\n'
            '    Check the starting value, the condition, and the line that changes the value.\n'
            '\n'
            '    # Common Mistakes\n'
            '    - Forgetting the colon after the condition.\n'
            '- Putting the loop body at the wrong indentation level.\n'
            '- Forgetting to change the value used by the condition.\n'
            '\n'
            '    # Short Quiz\n'
            '    1. What does the while condition control?\n'
            '2. Which lines repeat?\n'
            '3. What happens when the condition becomes false?\n'
            '\n'
            '    # Answer and Explanation\n'
            '    1. It controls whether another iteration should run.\n'
            '2. The indented loop body repeats.\n'
            '3. Python leaves the loop and continues with the next line after it.\n'
            '\n'
            '    # Summary\n'
            '    A while loop repeats an indented block while its condition is true.\n'
            '\n'
            '    # Practice/Review\n'
            '    Trace `count` for a loop from 1 through 4 before running it.\n'
            '\n'
            '    # Optional Challenge\n'
            '    Write a countdown from 5 to 1 using a while loop.\n'
        ),
        "exercises": [
            {
                "instructions": 'Complete the loop so it prints 1, 2, and 3.',
                "starter_code": 'count = 1\nwhile count <= 3:\n    print(count)\n    # Add the update here\n',
                "expected_output": '1\n2\n3',
            },
            {
                "instructions": 'Change the loop so it prints 1 through 5.',
                "starter_code": 'count = 1\nwhile count <= 5:\n    # Print the current count\n    count += 1\n',
                "expected_output": '1\n2\n3\n4\n5',
            },
        ],
    },
    {
        "title": 'Lesson 3 — Understanding the Loop Cycle',
        "content": (
            '    # Module: While Loops\n'
            '    # Learning Objectives\n'
            '    - Describe one iteration of a while loop.\n'
            '- Trace a loop one step at a time.\n'
            '- Predict output before running code.\n'
            '\n'
            '    # Why This Matters\n'
            '    A loop becomes easier to understand when you stop treating it as a single action and instead follow what Python does on each pass.\n'
            '\n'
            '    # Explanation\n'
            '    A simple while-loop cycle has four stages: check the condition, run the body if true, update the relevant values, and check the condition again. One complete pass through the body is called an **iteration**. Thinking in iterations helps you predict output and find bugs.\n'
            '\n'
            '    # Examples\n'
            '    For:\n'
            '```python\n'
            'number = 2\n'
            'while number <= 6:\n'
            '    print(number)\n'
            '    number += 2\n'
            '```\n'
            '\n'
            'The iterations start with 2, then 4, then 6.\n'
            '\n'
            '    # Worked Example\n'
            '    A trace can be written as:\n'
            '\n'
            '| number | condition | action |\n'
            '|---|---|---|\n'
            '| 2 | True | print 2 |\n'
            '| 4 | True | print 4 |\n'
            '| 6 | True | print 6 |\n'
            '| 8 | False | stop |\n'
            '\n'
            'The table makes the state change visible.\n'
            '\n'
            '    # Beginner-Friendly Explanation\n'
            '    For a loop that adds 2, the update happens after the print. That means the printed value is still the old value for that iteration. The next check sees the updated value.\n'
            '\n'
            '    # Try It Yourself\n'
            '    Create a trace table for a countdown from 3 to 1.\n'
            '\n'
            '    # Guided Exercise\n'
            '    Fill in the values of `number` for each iteration of a loop that starts at 0 and adds 2 until 6.\n'
            '\n'
            '    # Independent Exercise\n'
            '    Predict the exact output of a short while loop before using Run.\n'
            '\n'
            '    # Hints\n'
            '    Write the value at the start of an iteration, not the value after the update.\n'
            '\n'
            '    # Common Mistakes\n'
            '    - Skipping the condition check when tracing.\n'
            '- Updating the variable too early in your mental trace.\n'
            '- Assuming the stop value runs without checking the condition.\n'
            '\n'
            '    # Short Quiz\n'
            '    1. What is an iteration?\n'
            '2. What happens before the loop body?\n'
            '3. Why is tracing useful?\n'
            '\n'
            '    # Answer and Explanation\n'
            '    1. One iteration is one complete execution of the loop body.\n'
            '2. Python checks the loop condition.\n'
            '3. Tracing shows how values and decisions change, which helps with prediction and debugging.\n'
            '\n'
            '    # Summary\n'
            '    Tracing means following the loop one iteration at a time instead of guessing the final result.\n'
            '\n'
            '    # Practice/Review\n'
            '    Predict the outputs of two small loops and explain your prediction before running them.\n'
            '\n'
            '    # Optional Challenge\n'
            '    Trace a loop that starts at 10 and decreases by 2 until it reaches 4.\n'
        ),
        "exercises": [
            {
                "instructions": 'Predict and run the loop.',
                "starter_code": 'number = 2\nwhile number <= 6:\n    print(number)\n    number += 2\n',
                "expected_output": '2\n4\n6',
            },
            {
                "instructions": 'Predict and run the countdown.',
                "starter_code": 'number = 3\nwhile number > 0:\n    print(number)\n    number -= 1\n',
                "expected_output": '3\n2\n1',
            },
        ],
    },
    {
        "title": 'Lesson 4 — Avoiding Infinite Loops',
        "content": (
            '    # Module: While Loops\n'
            '    # Learning Objectives\n'
            '    - Understand what an infinite loop is.\n'
            '- Recognize common causes of infinite loops.\n'
            '- Inspect a loop for a reachable stopping condition.\n'
            '\n'
            '    # Why This Matters\n'
            '    A loop can be logically wrong even when Python accepts the syntax. A program that never reaches its stopping point may appear frozen, so learning to reason about loop termination is an important beginner skill.\n'
            '\n'
            '    # Explanation\n'
            '    An **infinite loop** is a loop that continues without reaching a stopping point. A common cause is forgetting to change the value used by the condition. Another is changing the value in the wrong direction.\n'
            '\n'
            '    # Examples\n'
            '    This example should be studied as a debugging example rather than run:\n'
            '```text\n'
            'count = 1\n'
            'while count <= 3:\n'
            '    print(count)\n'
            '```\n'
            '\n'
            '`count` never changes, so the condition remains true.\n'
            '\n'
            '    # Worked Example\n'
            '    A safe version adds an update:\n'
            '```python\n'
            'count = 1\n'
            'while count <= 3:\n'
            '    print(count)\n'
            '    count += 1\n'
            '```\n'
            '\n'
            'The update moves `count` from 1 to 4, making the condition false.\n'
            '\n'
            '    # Beginner-Friendly Explanation\n'
            '    Before running a while loop, ask three questions:\n'
            '1. What starts the controlling value?\n'
            '2. What changes it?\n'
            '3. What exact value or condition makes the loop stop?\n'
            '\n'
            'If you cannot answer all three, inspect the code before running it.\n'
            '\n'
            '    # Try It Yourself\n'
            '    Find the missing update in a broken loop.\n'
            '\n'
            '    # Guided Exercise\n'
            '    Add `count += 1` to a loop that counts from 1 to 3.\n'
            '\n'
            '    # Independent Exercise\n'
            '    Explain why decrementing a value can be the wrong update when the condition is `count <= 3`.\n'
            '\n'
            '    # Hints\n'
            '    Follow the variable used in the condition and see whether it moves toward the stopping point.\n'
            '\n'
            '    # Common Mistakes\n'
            '    - Forgetting the update.\n'
            '- Updating the wrong variable.\n'
            '- Moving away from the stopping condition.\n'
            '\n'
            '    # Short Quiz\n'
            '    1. What is an infinite loop?\n'
            '2. What is a common cause?\n'
            '3. What should you check before running a while loop?\n'
            '\n'
            '    # Answer and Explanation\n'
            '    1. A loop that continues without reaching a stopping point.\n'
            '2. Failing to change the controlling value, or changing it in the wrong direction.\n'
            '3. Check the starting value, update, and stopping condition.\n'
            '\n'
            '    # Summary\n'
            '    Safe loops have a clear condition and a believable path toward becoming false.\n'
            '\n'
            '    # Practice/Review\n'
            '    Inspect two broken loops without executing unsafe code. For each, name the controlling value and the missing or incorrect update.\n'
            '\n'
            '    # Optional Challenge\n'
            '    Design a loop that deliberately counts down from 10 to 1 and explain why its condition will eventually become false.\n'
        ),
        "exercises": [
            {
                "instructions": 'Repair the loop by adding the update that makes it stop.',
                "starter_code": 'count = 1\nwhile count <= 3:\n    print(count)\n    # Add the missing update\n',
                "expected_output": '1\n2\n3',
            },
            {
                "instructions": 'Repair this countdown so it prints 3, 2, 1.',
                "starter_code": 'count = 3\nwhile count > 0:\n    print(count)\n    # Add the missing update\n',
                "expected_output": '3\n2\n1',
            },
        ],
    },
    {
        "title": 'Lesson 5 — Counters',
        "content": (
            '    # Module: Counters and Accumulation\n'
            '    # Learning Objectives\n'
            '    - Understand a counter variable.\n'
            '- Start and update a counter correctly.\n'
            '- Use a counter to count repetitions or matches.\n'
            '\n'
            '    # Why This Matters\n'
            "    Programs often need to answer questions such as 'How many values passed?' or 'How many times did this happen?' A counter gives the program a place to remember that number.\n"
            '\n'
            '    # Explanation\n'
            '    A **counter** is a variable whose job is to keep track of how many times something happens. A common pattern is to start at zero and increase by one when the event being counted occurs.\n'
            '\n'
            '    # Examples\n'
            '    ```python\n'
            'count = 0\n'
            'for number in range(5):\n'
            '    count += 1\n'
            'print(count)\n'
            '```\n'
            '\n'
            'The final answer is 5 because the loop processed five values.\n'
            '\n'
            '    # Worked Example\n'
            '    To count only even values:\n'
            '```python\n'
            'count = 0\n'
            'for number in range(1, 11):\n'
            '    if number % 2 == 0:\n'
            '        count += 1\n'
            'print(count)\n'
            '```\n'
            '\n'
            'The counter increases only when the condition is true.\n'
            '\n'
            '    # Beginner-Friendly Explanation\n'
            '    The important placement is the update. If `count += 1` is inside the `if`, only matching values are counted. If it is outside the `if`, every loop iteration is counted.\n'
            '\n'
            '    # Try It Yourself\n'
            '    Count how many times a loop repeats.\n'
            '\n'
            '    # Guided Exercise\n'
            '    Use a counter starting at 0 and increase it once per iteration of `range(3)`.\n'
            '\n'
            '    # Independent Exercise\n'
            '    Count how many numbers from 1 to 20 are divisible by 3.\n'
            '\n'
            '    # Hints\n'
            '    Create the counter before the loop so the value survives across iterations.\n'
            '\n'
            '    # Common Mistakes\n'
            '    - Resetting the counter inside the loop.\n'
            '- Incrementing when the event did not happen.\n'
            '- Using a total when a count is required.\n'
            '\n'
            '    # Short Quiz\n'
            '    1. What is a counter?\n'
            '2. What value does a simple counter often start with?\n'
            '3. When should a conditional counter increase?\n'
            '\n'
            '    # Answer and Explanation\n'
            '    1. A variable that tracks how many times something happens.\n'
            '2. Zero.\n'
            '3. Only when the condition being counted is true.\n'
            '\n'
            '    # Summary\n'
            '    Counters measure quantity. Initialize them before the loop and update them at the moment the counted event occurs.\n'
            '\n'
            '    # Practice/Review\n'
            '    Count even numbers, numbers greater than 10, and three fixed repetitions. Notice how the counter pattern stays similar while the condition changes.\n'
            '\n'
            '    # Optional Challenge\n'
            '    Count how many numbers from 1 to 50 are divisible by both 3 and 5.\n'
        ),
        "exercises": [
            {
                "instructions": 'Count how many times the loop runs.',
                "starter_code": 'count = 0\nfor number in range(5):\n    count += 1\nprint(count)\n',
                "expected_output": '5',
            },
            {
                "instructions": 'Count the even values from 1 through 10.',
                "starter_code": 'count = 0\nfor number in range(1, 11):\n    if number % 2 == 0:\n        count += 1\nprint(count)\n',
                "expected_output": '5',
            },
        ],
    },
    {
        "title": 'Lesson 6 — Accumulating a Total',
        "content": (
            '    # Module: Counters and Accumulation\n'
            '    # Learning Objectives\n'
            '    - Understand an accumulator.\n'
            '- Build a running total.\n'
            '- Distinguish an accumulator from a counter.\n'
            '\n'
            '    # Why This Matters\n'
            '    A counter tells you how many items you saw. An accumulator remembers a combined result, such as a total score, total price, or sum of numbers.\n'
            '\n'
            '    # Explanation\n'
            '    An **accumulator** is a variable that builds a result over multiple iterations. For addition, it commonly starts at zero and adds the current value on each iteration.\n'
            '\n'
            '    # Examples\n'
            '    ```python\n'
            'total = 0\n'
            'for number in range(1, 6):\n'
            '    total += number\n'
            'print(total)\n'
            '```\n'
            '\n'
            'The running total becomes 1, 3, 6, 10, and 15.\n'
            '\n'
            '    # Worked Example\n'
            '    For values 4, 7, and 2:\n'
            '\n'
            '```text\n'
            'total = 0\n'
            '+ 4 → 4\n'
            '+ 7 → 11\n'
            '+ 2 → 13\n'
            '```\n'
            '\n'
            'The accumulator keeps the previous result and adds the next value.\n'
            '\n'
            '    # Beginner-Friendly Explanation\n'
            '    Counter:\n'
            '```python\n'
            'count += 1\n'
            '```\n'
            '\n'
            'Accumulator:\n'
            '```python\n'
            'total += value\n'
            '```\n'
            '\n'
            'Both patterns persist across iterations, but they answer different questions.\n'
            '\n'
            '    # Try It Yourself\n'
            '    Calculate the total of 2, 4, and 6.\n'
            '\n'
            '    # Guided Exercise\n'
            '    Start `total = 0`, loop through the values, and add each current value.\n'
            '\n'
            '    # Independent Exercise\n'
            '    Calculate the total price of 5, 8, and 12.\n'
            '\n'
            '    # Hints\n'
            '    Ask whether you are adding 1 or adding the current value. That tells you whether you are counting or accumulating.\n'
            '\n'
            '    # Common Mistakes\n'
            '    - Resetting total inside the loop.\n'
            '- Adding 1 instead of the current value.\n'
            '- Starting an addition accumulator with a non-zero value without a reason.\n'
            '\n'
            '    # Short Quiz\n'
            '    1. What does an accumulator store?\n'
            '2. How is it different from a counter?\n'
            '3. Why does addition commonly start at zero?\n'
            '\n'
            '    # Answer and Explanation\n'
            '    1. It stores a running combined result.\n'
            '2. A counter counts occurrences, while an accumulator combines values.\n'
            '3. Zero does not change the first value added.\n'
            '\n'
            '    # Summary\n'
            '    An accumulator carries a result from one iteration to the next, often building a total.\n'
            '\n'
            '    # Practice/Review\n'
            '    Trace the running totals for 3, 5, and 8. Then compare that trace with a counter processing the same three values.\n'
            '\n'
            '    # Optional Challenge\n'
            '    Use both a counter and an accumulator to find the total and number of values in a fixed set.\n'
        ),
        "exercises": [
            {
                "instructions": 'Calculate the sum of 1 through 5.',
                "starter_code": 'total = 0\nfor number in range(1, 6):\n    total += number\nprint(total)\n',
                "expected_output": '15',
            },
            {
                "instructions": 'Calculate the total price.',
                "starter_code": 'total = 0\nfor price in [5, 8, 12]:\n    total += price\nprint(total)\n',
                "expected_output": '25',
            },
        ],
    },
    {
        "title": 'Lesson 7 — Loops with input()',
        "content": (
            '    # Module: Counters and Accumulation\n'
            '    # Learning Objectives\n'
            '    - Combine input() with a loop.\n'
            '- Use type conversion inside a loop.\n'
            '- Build a total from repeated user input.\n'
            '\n'
            '    # Why This Matters\n'
            '    You already know how to read input and convert text to numbers. A loop lets you repeat that process so a program can collect several values instead of just one.\n'
            '\n'
            '    # Explanation\n'
            '    In a fixed-count input loop, one variable controls how many inputs have been collected, while another stores the current number and a third keeps the running total. Keeping these roles separate makes the code easier to reason about.\n'
            '\n'
            '    # Examples\n'
            '    ```python\n'
            'total = 0\n'
            'count = 0\n'
            'while count < 3:\n'
            '    number = int(input("Enter a number: "))\n'
            '    total += number\n'
            '    count += 1\n'
            'print("Total:", total)\n'
            '```\n'
            '\n'
            '    # Worked Example\n'
            '    Suppose the user enters 4, 7, and 2. The total becomes 4, then 11, then 13. The count becomes 1, 2, then 3. At that point, `count < 3` is false.\n'
            '\n'
            '    # Beginner-Friendly Explanation\n'
            '    This program combines earlier ideas rather than introducing a new one at each line:\n'
            '- `input()` gets text.\n'
            '- `int()` converts that text to an integer.\n'
            '- `total += number` accumulates.\n'
            '- `count += 1` counts.\n'
            '- the while condition controls repetition.\n'
            '\n'
            '    # Try It Yourself\n'
            '    Build a loop that collects two numbers and calculates their total.\n'
            '\n'
            '    # Guided Exercise\n'
            '    Start with `total = 0` and `count = 0`. Repeat while `count < 2`.\n'
            '\n'
            '    # Independent Exercise\n'
            '    Create a fixed three-number score collector and print the average after the loop.\n'
            '\n'
            '    # Hints\n'
            '    Keep `total` and `count` outside the loop so their values are remembered.\n'
            '\n'
            '    # Common Mistakes\n'
            '    - Trying to add input text without converting it.\n'
            '- Resetting total inside the loop.\n'
            '- Forgetting to increase the count.\n'
            '\n'
            '    # Short Quiz\n'
            '    1. Why use `int(input(...))`?\n'
            '2. What controls the number of inputs?\n'
            '3. Why is `total` initialized before the loop?\n'
            '\n'
            '    # Answer and Explanation\n'
            '    1. `input()` returns text, so `int()` converts it to a number.\n'
            '2. The count controls the number of inputs.\n'
            '3. The total must keep its accumulated value across iterations.\n'
            '\n'
            '    # Summary\n'
            '    Loops let earlier Level 1 tools work repeatedly, turning one input operation into a small data-collection program.\n'
            '\n'
            '    # Practice/Review\n'
            '    Trace the total and count for three sample inputs without running the program.\n'
            '\n'
            '    # Optional Challenge\n'
            '    Change the program to collect five values and report both total and average.\n'
        ),
        "exercises": [
            {
                "instructions": 'Read two integers and print their total. Test with 10 and 20.',
                "starter_code": 'total = 0\ncount = 0\nwhile count < 2:\n    number = int(input())\n    total += number\n    count += 1\nprint(total)\n',
                "expected_output": '30',
            },
            {
                "instructions": 'Calculate the total and average of the fixed values without interactive input.',
                "starter_code": 'numbers = [10, 20, 30]\ntotal = 0\ncount = 0\nfor number in numbers:\n    total += number\n    count += 1\nprint(total)\nprint(total / count)\n',
                "expected_output": '60\n20.0',
            },
        ],
    },
    {
        "title": 'Lesson 8 — Why for Loops Exist',
        "content": (
            '    # Module: For Loops\n'
            '    # Learning Objectives\n'
            '    - Understand the purpose of a for loop.\n'
            '- Recognize that a for loop processes one item at a time.\n'
            '- Identify the loop variable and loop body.\n'
            '\n'
            '    # Why This Matters\n'
            '    A for loop is a convenient way to repeat work for each item in a sequence. This is especially useful when the number of items is already known.\n'
            '\n'
            '    # Explanation\n'
            '    A `for` loop assigns one item at a time to a loop variable and runs the indented body for each item. The loop variable is not a list of all items; it represents the current item for the current iteration.\n'
            '\n'
            '    # Examples\n'
            '    ```python\n'
            'for animal in ["cat", "dog", "rabbit"]:\n'
            '    print(animal)\n'
            '```\n'
            '\n'
            'Python prints each item one at a time.\n'
            '\n'
            '    # Worked Example\n'
            '    ```python\n'
            'for letter in "cat":\n'
            '    print(letter)\n'
            '```\n'
            '\n'
            'The loop variable is `letter`, and its values are `c`, `a`, and `t`.\n'
            '\n'
            '    # Beginner-Friendly Explanation\n'
            "    Read the loop as: 'For each current item in this sequence, run the indented code.' On the first iteration the variable holds the first item, then the second, and so on.\n"
            '\n'
            '    # Try It Yourself\n'
            '    Loop through a short word and print each character.\n'
            '\n'
            '    # Guided Exercise\n'
            '    Use `for letter in "cat":` and print `letter`.\n'
            '\n'
            '    # Independent Exercise\n'
            '    Loop through a sequence of three values and print each one twice using two print statements in the loop body.\n'
            '\n'
            '    # Hints\n'
            '    Focus on the current item. The loop supplies it for you.\n'
            '\n'
            '    # Common Mistakes\n'
            '    - Putting the loop variable outside the loop body when it is needed inside.\n'
            '- Thinking the variable stores every item at once.\n'
            '- Forgetting the colon or indentation.\n'
            '\n'
            '    # Short Quiz\n'
            '    1. What does the loop variable represent?\n'
            '2. How many times does a loop over three items run?\n'
            '3. What happens after one iteration?\n'
            '\n'
            '    # Answer and Explanation\n'
            '    1. It represents the current item.\n'
            '2. Three times.\n'
            '3. Python moves to the next item and runs the body again.\n'
            '\n'
            '    # Summary\n'
            '    A for loop processes items one at a time, making repeated processing easy to read.\n'
            '\n'
            '    # Practice/Review\n'
            '    Predict the number of iterations for the words `Python`, `code`, and an empty string.\n'
            '\n'
            '    # Optional Challenge\n'
            "    Explain in plain English what 'current item' means.\n"
        ),
        "exercises": [
            {
                "instructions": 'Print each character in Python.',
                "starter_code": 'for letter in "Python":\n    print(letter)\n',
                "expected_output": 'P\ny\nt\nh\no\nn',
            },
            {
                "instructions": 'Print each item on its own line.',
                "starter_code": 'for item in ["red", "green", "blue"]:\n    print(item)\n',
                "expected_output": 'red\ngreen\nblue',
            },
        ],
    },
    {
        "title": 'Lesson 9 — Understanding the Loop Variable',
        "content": (
            '    # Module: For Loops\n'
            '    # Learning Objectives\n'
            '    - Predict how a loop variable changes.\n'
            '- Use clear loop-variable names.\n'
            '- Explain what the loop variable contains on a given iteration.\n'
            '\n'
            '    # Why This Matters\n'
            '    Understanding the loop variable prevents a common beginner mistake: thinking the variable is a permanent label for the whole sequence.\n'
            '\n'
            '    # Explanation\n'
            '    The loop variable changes automatically as the for loop moves through its sequence. In `for animal in ["cat", "dog"]`, the variable `animal` refers first to `cat` and then to `dog`.\n'
            '\n'
            '    # Examples\n'
            '    ```python\n'
            'for animal in ["cat", "dog", "rabbit"]:\n'
            '    print(animal)\n'
            '```\n'
            '\n'
            'The second iteration has `animal == "dog"`.\n'
            '\n'
            '    # Worked Example\n'
            '    Meaningful names improve readability:\n'
            '```python\n'
            'for temperature in [18, 21, 24]:\n'
            '    print(temperature)\n'
            '```\n'
            '\n'
            '`temperature` tells the reader what the current value represents.\n'
            '\n'
            '    # Beginner-Friendly Explanation\n'
            '    The loop variable name is chosen by the programmer. `item`, `number`, `name`, and `score` are ordinary variable names. Python does not treat `item` as a special keyword.\n'
            '\n'
            '    # Try It Yourself\n'
            '    Predict the second loop-variable value for a three-item sequence.\n'
            '\n'
            '    # Guided Exercise\n'
            '    Write a loop over `hello` and print the current character.\n'
            '\n'
            '    # Independent Exercise\n'
            '    Choose a descriptive variable name for a loop that processes prices.\n'
            '\n'
            '    # Hints\n'
            "    Ask: 'What is the current item right now?' That is the value stored in the loop variable.\n"
            '\n'
            '    # Common Mistakes\n'
            '    - Assuming the variable contains the whole sequence.\n'
            '- Using a misleading name that hides what the current value means.\n'
            '\n'
            '    # Short Quiz\n'
            '    1. Does the loop variable change?\n'
            '2. Does its name have to be `item`?\n'
            '3. What is in the variable during the second iteration of `[10, 20, 30]`?\n'
            '\n'
            '    # Answer and Explanation\n'
            '    1. Yes.\n'
            '2. No; use a clear descriptive name.\n'
            '3. The value is 20.\n'
            '\n'
            '    # Summary\n'
            '    A loop variable represents the current item and changes as the for loop progresses.\n'
            '\n'
            '    # Practice/Review\n'
            '    Trace the loop variable for `[4, 9, 2]` and write its value on each iteration.\n'
            '\n'
            '    # Optional Challenge\n'
            '    Rewrite a loop using a more descriptive variable name without changing its behavior.\n'
        ),
        "exercises": [
            {
                "instructions": 'Print the current animal on each iteration.',
                "starter_code": 'for animal in ["cat", "dog", "rabbit"]:\n    print(animal)\n',
                "expected_output": 'cat\ndog\nrabbit',
            },
            {
                "instructions": 'Print the second-item value by processing the sequence in order.',
                "starter_code": 'for value in [10, 20, 30]:\n    print(value)\n',
                "expected_output": '10\n20\n30',
            },
        ],
    },
    {
        "title": 'Lesson 10 — range()',
        "content": (
            '    # Module: range()\n'
            '    # Learning Objectives\n'
            '    - Understand the purpose of range().\n'
            '- Use range() with a for loop.\n'
            '- Understand that the stop value is excluded.\n'
            '\n'
            '    # Why This Matters\n'
            '    Typing every number in a sequence is tedious. `range()` gives a for loop a controlled sequence of integers without requiring you to type them all.\n'
            '\n'
            '    # Explanation\n'
            '    With one argument, `range(n)` starts at 0 and continues up to, but not including, `n`. So `range(5)` is used by a loop to visit 0, 1, 2, 3, and 4.\n'
            '\n'
            '    # Examples\n'
            '    ```python\n'
            'for number in range(5):\n'
            '    print(number)\n'
            '```\n'
            '\n'
            'Output:\n'
            '```text\n'
            '0\n'
            '1\n'
            '2\n'
            '3\n'
            '4\n'
            '```\n'
            '\n'
            '    # Worked Example\n'
            '    To print 1 through 5, write:\n'
            '```python\n'
            'for number in range(1, 6):\n'
            '    print(number)\n'
            '```\n'
            '\n'
            'The stop value 6 is not printed.\n'
            '\n'
            '    # Beginner-Friendly Explanation\n'
            "    The easiest way to avoid the 'why is 5 missing?' question is to remember: **the stop value is a boundary, not a value included in the sequence.** `range(1, 6)` reaches values before 6.\n"
            '\n'
            '    # Try It Yourself\n'
            '    Use `range(5)` to print 0 through 4.\n'
            '\n'
            '    # Guided Exercise\n'
            '    Write a loop with `range(1, 4)` and predict the output.\n'
            '\n'
            '    # Independent Exercise\n'
            '    Print numbers 1 through 10 using `range()`.\n'
            '\n'
            '    # Hints\n'
            '    Look at the stop number first, then ask what values appear before it.\n'
            '\n'
            '    # Common Mistakes\n'
            '    - Expecting the stop value to be included.\n'
            '- Forgetting that one-argument range starts at zero.\n'
            '- Using the wrong start value for a task that begins at 1.\n'
            '\n'
            '    # Short Quiz\n'
            '    1. What values appear in `range(5)`?\n'
            '2. Is 5 included?\n'
            '3. What does `range(1, 6)` print?\n'
            '\n'
            '    # Answer and Explanation\n'
            '    1. 0 through 4.\n'
            '2. No.\n'
            '3. 1 through 5.\n'
            '\n'
            '    # Summary\n'
            '    `range()` creates a predictable sequence of integers for a loop, with the stop value excluded.\n'
            '\n'
            '    # Practice/Review\n'
            '    Without running code, write the values produced by `range(3)`, `range(1, 4)`, and `range(2, 5)`.\n'
            '\n'
            '    # Optional Challenge\n'
            '    Use `range()` to print 10 through 15.\n'
        ),
        "exercises": [
            {
                "instructions": 'Print the values produced by range(5).',
                "starter_code": 'for number in range(5):\n    print(number)\n',
                "expected_output": '0\n1\n2\n3\n4',
            },
            {
                "instructions": 'Print 1 through 5.',
                "starter_code": 'for number in range(1, 6):\n    print(number)\n',
                "expected_output": '1\n2\n3\n4\n5',
            },
        ],
    },
    {
        "title": 'Lesson 11 — range() with Start, Stop, and Step',
        "content": (
            '    # Module: range()\n'
            '    # Learning Objectives\n'
            '    - Understand start, stop, and step.\n'
            '- Use a step to skip values.\n'
            '- Use a negative step for descending sequences.\n'
            '\n'
            '    # Why This Matters\n'
            '    A three-part range gives you control over where the sequence begins, where it stops, and how it changes from one value to the next.\n'
            '\n'
            '    # Explanation\n'
            '    The form is `range(start, stop, step)`. Start is the first value, stop is excluded, and step controls the amount added or subtracted between values.\n'
            '\n'
            '    # Examples\n'
            '    ```python\n'
            'for number in range(0, 10, 2):\n'
            '    print(number)\n'
            '```\n'
            '\n'
            'This prints 0, 2, 4, 6, and 8.\n'
            '\n'
            '    # Worked Example\n'
            '    A countdown uses a negative step:\n'
            '```python\n'
            'for number in range(5, 0, -1):\n'
            '    print(number)\n'
            '```\n'
            '\n'
            'Output: 5, 4, 3, 2, 1.\n'
            '\n'
            '    # Beginner-Friendly Explanation\n'
            '    For `range(2, 10, 3)`, start at 2, then add 3: 2, 5, 8. The next value would be 11, which has passed the stop boundary of 10.\n'
            '\n'
            '    # Try It Yourself\n'
            '    Print the even numbers below 10.\n'
            '\n'
            '    # Guided Exercise\n'
            '    Use `range(0, 10, 2)` and print the loop variable.\n'
            '\n'
            '    # Independent Exercise\n'
            '    Create a countdown from 10 to 2 using a step of -2.\n'
            '\n'
            '    # Hints\n'
            '    Read the three arguments as start, stop, step in that order.\n'
            '\n'
            '    # Common Mistakes\n'
            '    - Using a positive step for a countdown.\n'
            '- Forgetting the stop value is excluded.\n'
            '- Choosing a step that skips the values you wanted.\n'
            '\n'
            '    # Short Quiz\n'
            '    1. What does the step control?\n'
            '2. What does -1 do?\n'
            '3. Which values appear in `range(2, 9, 3)`?\n'
            '\n'
            '    # Answer and Explanation\n'
            '    1. It controls how much the sequence changes.\n'
            '2. It moves downward by one.\n'
            '3. 2, 5, and 8.\n'
            '\n'
            '    # Summary\n'
            '    Start, stop, and step let a for loop walk through a precise numeric pattern.\n'
            '\n'
            '    # Practice/Review\n'
            '    Predict `range(1, 10, 3)` and `range(10, 3, -2)` without running them.\n'
            '\n'
            '    # Optional Challenge\n'
            '    Print every fourth number from 4 through 20.\n'
        ),
        "exercises": [
            {
                "instructions": 'Print the even numbers below 10.',
                "starter_code": 'for number in range(0, 10, 2):\n    print(number)\n',
                "expected_output": '0\n2\n4\n6\n8',
            },
            {
                "instructions": 'Print 10, 8, 6, 4, and 2.',
                "starter_code": 'for number in range(10, 0, -2):\n    print(number)\n',
                "expected_output": '10\n8\n6\n4\n2',
            },
        ],
    },
    {
        "title": 'Lesson 12 — Choosing while or for',
        "content": (
            '    # Module: range()\n'
            '    # Learning Objectives\n'
            '    - Compare while and for loops.\n'
            '- Choose a loop based on what controls repetition.\n'
            '- Explain the choice in plain language.\n'
            '\n'
            '    # Why This Matters\n'
            '    Python gives you more than one looping tool because problems control repetition in different ways.\n'
            '\n'
            '    # Explanation\n'
            '    A `for` loop is often a natural fit when you have a sequence or a known number of repetitions. A `while` loop is often a natural fit when the program should continue while a condition remains true. This is a guideline, not an absolute rule.\n'
            '\n'
            '    # Examples\n'
            '    Known count:\n'
            '```python\n'
            'for number in range(5):\n'
            '    print(number)\n'
            '```\n'
            '\n'
            'Condition-controlled:\n'
            '```python\n'
            'answer = ""\n'
            'while answer != "yes":\n'
            '    answer = input("Ready? " )\n'
            '```\n'
            '\n'
            '    # Worked Example\n'
            "    If a task says 'repeat exactly five times', `for` with `range()` is usually clear. If it says 'keep asking until the answer is valid', `while` often communicates the condition more directly.\n"
            '\n'
            '    # Beginner-Friendly Explanation\n'
            '    The best question is: **What controls when the repetition happens?** A known set or known count often points toward `for`. A condition that changes over time often points toward `while`. Both can sometimes solve the same problem.\n'
            '\n'
            '    # Try It Yourself\n'
            '    Choose a loop type for four short situations.\n'
            '\n'
            '    # Guided Exercise\n'
            '    Use a for loop for a task that repeats exactly five times.\n'
            '\n'
            '    # Independent Exercise\n'
            '    Describe a real situation where a while loop is easier to explain than a for loop.\n'
            '\n'
            '    # Hints\n'
            '    Identify whether the problem gives you a sequence/count or a stopping condition.\n'
            '\n'
            '    # Common Mistakes\n'
            '    - Treating the guideline as a strict rule.\n'
            '- Choosing a loop because it was taught most recently.\n'
            '- Ignoring which part of the problem actually controls repetition.\n'
            '\n'
            '    # Short Quiz\n'
            '    1. When is `for` often convenient?\n'
            '2. When is `while` often convenient?\n'
            '3. Is the choice absolute?\n'
            '\n'
            '    # Answer and Explanation\n'
            '    1. When processing a known sequence or known number of repetitions.\n'
            '2. When repetition depends on a condition.\n'
            '3. No; it is a practical guideline.\n'
            '\n'
            '    # Summary\n'
            '    Choose the loop that makes the reason for repetition easiest to understand.\n'
            '\n'
            '    # Practice/Review\n'
            '    Classify these tasks: count 1–100, process each character, ask until valid, repeat until a flag changes.\n'
            '\n'
            '    # Optional Challenge\n'
            '    Rewrite a simple counting while loop using `for` and `range()`.\n'
        ),
        "exercises": [
            {
                "instructions": 'Repeat exactly five times using a for loop.',
                "starter_code": 'for number in range(5):\n    print("Practice")\n',
                "expected_output": 'Practice\nPractice\nPractice\nPractice\nPractice',
            },
            {
                "instructions": 'Use a while loop to print 1, 2, and 3.',
                "starter_code": 'count = 1\nwhile count <= 3:\n    print(count)\n    count += 1\n',
                "expected_output": '1\n2\n3',
            },
        ],
    },
    {
        "title": 'Lesson 13 — break',
        "content": (
            '    # Module: Controlling Loops\n'
            '    # Learning Objectives\n'
            '    - Understand what break does.\n'
            '- Use break to stop early.\n'
            '- Recognize when an early exit is useful.\n'
            '\n'
            '    # Why This Matters\n'
            '    Sometimes the program finds what it needs before a loop has reached its normal end. Continuing to process values would waste work or produce unwanted behavior.\n'
            '\n'
            '    # Explanation\n'
            '    `break` immediately exits the current loop. It does not merely skip one iteration. It leaves the loop and continues with the first line after the loop.\n'
            '\n'
            '    # Examples\n'
            '    ```python\n'
            'for number in range(1, 10):\n'
            '    if number == 5:\n'
            '        break\n'
            '    print(number)\n'
            '```\n'
            '\n'
            'The output is 1, 2, 3, 4.\n'
            '\n'
            '    # Worked Example\n'
            '    A search is a useful example. Once the target has been found, the loop may no longer need to continue checking later values.\n'
            '\n'
            '    # Beginner-Friendly Explanation\n'
            '    You may also see `while True` with `break`:\n'
            '```python\n'
            'while True:\n'
            '    word = input("Type quit to stop: " )\n'
            '    if word == "quit":\n'
            '        break\n'
            '```\n'
            '\n'
            '`while True` keeps the loop condition true, while `break` supplies the exit point.\n'
            '\n'
            '    # Try It Yourself\n'
            '    Stop a loop when it reaches 4.\n'
            '\n'
            '    # Guided Exercise\n'
            '    Place `break` inside an if statement that checks the target value.\n'
            '\n'
            '    # Independent Exercise\n'
            '    Write a small search that stops once it sees 7.\n'
            '\n'
            '    # Hints\n'
            '    Ask whether continuing would still be useful. If not, an early exit may be appropriate.\n'
            '\n'
            '    # Common Mistakes\n'
            '    - Putting break outside a loop.\n'
            '- Expecting break to skip only one iteration.\n'
            '- Placing break before the condition that should trigger it.\n'
            '\n'
            '    # Short Quiz\n'
            '    1. What does `break` do?\n'
            '2. Does it stop only one iteration?\n'
            '3. Why is it useful in a search?\n'
            '\n'
            '    # Answer and Explanation\n'
            '    1. It immediately exits the loop.\n'
            '2. No; it exits the entire current loop.\n'
            '3. It avoids unnecessary work after the target is found.\n'
            '\n'
            '    # Summary\n'
            '    Use `break` when the loop has reached a deliberate early-exit point.\n'
            '\n'
            '    # Practice/Review\n'
            '    Trace a loop that stops at 6 and identify which values are never processed.\n'
            '\n'
            '    # Optional Challenge\n'
            '    Use `break` in a small repeated menu that exits when the user selects the exit option.\n'
        ),
        "exercises": [
            {
                "instructions": 'Stop before printing 4.',
                "starter_code": 'for number in range(1, 8):\n    if number == 4:\n        break\n    print(number)\n',
                "expected_output": '1\n2\n3',
            },
            {
                "instructions": 'Stop after finding the first value equal to 7.',
                "starter_code": 'for number in [2, 5, 7, 9]:\n    if number == 7:\n        print("Found")\n        break\n',
                "expected_output": 'Found',
            },
        ],
    },
    {
        "title": 'Lesson 14 — continue',
        "content": (
            '    # Module: Controlling Loops\n'
            '    # Learning Objectives\n'
            '    - Understand what continue does.\n'
            '- Skip the rest of one iteration.\n'
            '- Distinguish continue from break.\n'
            '\n'
            '    # Why This Matters\n'
            '    Sometimes one value should be ignored while the rest of the data still needs to be processed. `continue` is designed for that situation.\n'
            '\n'
            '    # Explanation\n'
            '    `continue` skips the rest of the current iteration and moves to the next iteration. The loop itself does not end.\n'
            '\n'
            '    # Examples\n'
            '    ```python\n'
            'for number in range(1, 6):\n'
            '    if number == 3:\n'
            '        continue\n'
            '    print(number)\n'
            '```\n'
            '\n'
            'Output: 1, 2, 4, 5.\n'
            '\n'
            '    # Worked Example\n'
            '    If a value should be ignored but later values still matter, `continue` is often clearer than `break`. The loop continues with the next value after the skipped one.\n'
            '\n'
            '    # Beginner-Friendly Explanation\n'
            '    For `number == 3`, Python reaches `continue`, skips the print statement for that iteration, then returns to the top of the loop for 4.\n'
            '\n'
            '    # Try It Yourself\n'
            '    Skip the number 3 while printing 1 through 5.\n'
            '\n'
            '    # Guided Exercise\n'
            '    Put `continue` inside `if number == 3:` before the print statement.\n'
            '\n'
            '    # Independent Exercise\n'
            '    Skip a single unwanted value from a numeric sequence.\n'
            '\n'
            '    # Hints\n'
            '    Remember: break ends the loop; continue keeps the loop going.\n'
            '\n'
            '    # Common Mistakes\n'
            '    - Using continue when you really need to stop.\n'
            '- Placing continue after the code you intended to skip.\n'
            '- Thinking continue freezes the loop variable.\n'
            '\n'
            '    # Short Quiz\n'
            '    1. What does continue skip?\n'
            '2. Does it end the loop?\n'
            '3. Which keyword exits the loop entirely?\n'
            '\n'
            '    # Answer and Explanation\n'
            '    1. It skips the rest of the current iteration.\n'
            '2. No.\n'
            '3. `break`.\n'
            '\n'
            '    # Summary\n'
            "    `continue` skips one iteration's remaining work while `break` exits the loop.\n"
            '\n'
            '    # Practice/Review\n'
            '    Predict outputs for two loops, one with break and one with continue.\n'
            '\n'
            '    # Optional Challenge\n'
            '    Use continue to ignore zero values while processing a fixed set of numbers.\n'
        ),
        "exercises": [
            {
                "instructions": 'Print 1 through 5 but skip 3.',
                "starter_code": 'for number in range(1, 6):\n    if number == 3:\n        continue\n    print(number)\n',
                "expected_output": '1\n2\n4\n5',
            },
            {
                "instructions": 'Print all values except 0.',
                "starter_code": 'for number in [3, 0, 5, 7]:\n    if number == 0:\n        continue\n    print(number)\n',
                "expected_output": '3\n5\n7',
            },
        ],
    },
    {
        "title": 'Lesson 15 — break vs continue',
        "content": (
            '    # Module: Controlling Loops\n'
            '    # Learning Objectives\n'
            '    - Compare break and continue.\n'
            '- Predict the effect of each keyword.\n'
            '- Choose the appropriate keyword for a problem.\n'
            '\n'
            '    # Why This Matters\n'
            '    Both statements change normal loop flow, but they solve different problems. Being precise about that difference will help you debug loops later.\n'
            '\n'
            '    # Explanation\n'
            "    `break` means 'leave the loop now.' `continue` means 'skip the rest of this iteration and move to the next one.'\n"
            '\n'
            '    # Examples\n'
            '    Break example:\n'
            '```python\n'
            'for number in range(1, 6):\n'
            '    if number == 3:\n'
            '        break\n'
            '    print(number)\n'
            '```\n'
            '\n'
            'Continue example:\n'
            '```python\n'
            'for number in range(1, 6):\n'
            '    if number == 3:\n'
            '        continue\n'
            '    print(number)\n'
            '```\n'
            '\n'
            '    # Worked Example\n'
            '    The break version prints 1 and 2. The continue version prints 1, 2, 4, and 5. The difference is what happens after the special value is reached.\n'
            '\n'
            '    # Beginner-Friendly Explanation\n'
            '    Ask one question: **Do later iterations still need to happen?** If no, `break` may fit. If yes, but the current value should be skipped, `continue` may fit.\n'
            '\n'
            '    # Try It Yourself\n'
            '    Classify short scenarios as break or continue.\n'
            '\n'
            '    # Guided Exercise\n'
            '    Predict the output of one break example and one continue example.\n'
            '\n'
            '    # Independent Exercise\n'
            '    Write your own one-sentence example of when each keyword would be useful.\n'
            '\n'
            '    # Hints\n'
            '    Focus on intended behavior before choosing a keyword.\n'
            '\n'
            '    # Common Mistakes\n'
            "    - Choosing by the word's name instead of the required behavior.\n"
            '- Forgetting that continue allows later iterations.\n'
            '- Putting the statement in the wrong branch.\n'
            '\n'
            '    # Short Quiz\n'
            '    1. Which keyword exits the loop?\n'
            '2. Which keyword skips only the current iteration?\n'
            '3. What happens after continue?\n'
            '\n'
            '    # Answer and Explanation\n'
            '    1. `break`.\n'
            '2. `continue`.\n'
            '3. Python moves to the next iteration.\n'
            '\n'
            '    # Summary\n'
            '    Break ends; continue skips and keeps going.\n'
            '\n'
            '    # Practice/Review\n'
            '    Predict whether each of four example loops ends early or skips a value.\n'
            '\n'
            '    # Optional Challenge\n'
            '    Create two tiny programs that demonstrate the difference as clearly as possible.\n'
        ),
        "exercises": [
            {
                "instructions": 'Stop the loop when the value reaches 3.',
                "starter_code": 'for number in range(1, 6):\n    if number == 3:\n        break\n    print(number)\n',
                "expected_output": '1\n2',
            },
            {
                "instructions": 'Skip 3 but continue with the remaining values.',
                "starter_code": 'for number in range(1, 6):\n    if number == 3:\n        continue\n    print(number)\n',
                "expected_output": '1\n2\n4\n5',
            },
        ],
    },
    {
        "title": 'Lesson 16 — Nested Loops',
        "content": (
            '    # Module: Nested Loops\n'
            '    # Learning Objectives\n'
            '    - Understand a loop inside another loop.\n'
            '- Distinguish the outer and inner loops.\n'
            '- Trace execution order.\n'
            '\n'
            '    # Why This Matters\n'
            '    Some problems contain two levels of repetition, such as rows and columns in a grid. A nested loop gives the program a way to represent both levels.\n'
            '\n'
            '    # Explanation\n'
            '    A **nested loop** is a loop inside another loop. For each value handled by the outer loop, the inner loop runs through all of its values.\n'
            '\n'
            '    # Examples\n'
            '    ```python\n'
            'for row in range(3):\n'
            '    for column in range(2):\n'
            '        print(row, column)\n'
            '```\n'
            '\n'
            'The inner loop completes before the outer loop moves to its next value.\n'
            '\n'
            '    # Worked Example\n'
            '    For `row = 0`, the inner loop prints `0 0` and `0 1`. Then row becomes 1, and the inner loop starts again. This produces six coordinate pairs in total.\n'
            '\n'
            '    # Beginner-Friendly Explanation\n'
            '    With 3 outer iterations and 2 inner iterations, the inner body runs 3 × 2 = 6 times. Thinking about one outer value at a time makes the pattern manageable.\n'
            '\n'
            '    # Try It Yourself\n'
            '    Predict how many times the inner loop runs for 2 outer values and 4 inner values.\n'
            '\n'
            '    # Guided Exercise\n'
            '    Write a 2 by 2 coordinate loop.\n'
            '\n'
            '    # Independent Exercise\n'
            '    Print a small 3 by 3 pattern.\n'
            '\n'
            '    # Hints\n'
            '    Trace the outer loop first, then list all inner-loop values for that outer value.\n'
            '\n'
            '    # Common Mistakes\n'
            '    - Reusing the same variable name in both loops.\n'
            '- Forgetting the inner loop starts again for each outer value.\n'
            '- Trying to calculate the entire output in one mental step.\n'
            '\n'
            '    # Short Quiz\n'
            '    1. What is a nested loop?\n'
            '2. How many inner executions occur for 3 outer and 2 inner repetitions?\n'
            '3. Which loop runs completely first for one outer value?\n'
            '\n'
            '    # Answer and Explanation\n'
            '    1. A loop inside another loop.\n'
            '2. Six.\n'
            '3. The inner loop runs completely.\n'
            '\n'
            '    # Summary\n'
            '    Nested loops create multiple layers of repetition. Start small and trace one outer iteration at a time.\n'
            '\n'
            '    # Practice/Review\n'
            '    Draw a trace for a 2 by 3 nested loop.\n'
            '\n'
            '    # Optional Challenge\n'
            '    Use nested loops to print coordinate pairs for a small grid and explain the output order.\n'
        ),
        "exercises": [
            {
                "instructions": 'Print coordinates for a 2 by 2 grid.',
                "starter_code": 'for row in range(2):\n    for column in range(2):\n        print(row, column)\n',
                "expected_output": '0 0\n0 1\n1 0\n1 1',
            },
            {
                "instructions": 'Print coordinates for rows 0–1 and columns 0–2.',
                "starter_code": 'for row in range(2):\n    for column in range(3):\n        print(row, column)\n',
                "expected_output": '0 0\n0 1\n0 2\n1 0\n1 1\n1 2',
            },
        ],
    },
    {
        "title": 'Lesson 17 — Nested Loops in Practice',
        "content": (
            '    # Module: Nested Loops\n'
            '    # Learning Objectives\n'
            '    - Use nested loops for small tables.\n'
            '- Understand repeated combinations.\n'
            '- Apply the outer/inner loop pattern to a practical task.\n'
            '\n'
            '    # Why This Matters\n'
            '    Nested loops are useful whenever every item in one small group needs to be paired with every item in another group.\n'
            '\n'
            '    # Explanation\n'
            '    The outer loop chooses one value for the larger repetition level. The inner loop completes its work for every value belonging to that outer choice.\n'
            '\n'
            '    # Examples\n'
            '    ```python\n'
            'for number in range(1, 4):\n'
            '    for multiplier in range(1, 4):\n'
            '        print(number * multiplier)\n'
            '```\n'
            '\n'
            'The inner loop calculates all three products for 1, then for 2, then for 3.\n'
            '\n'
            '    # Worked Example\n'
            '    For `number = 2`, the inner loop prints 2, 4, and 6. Then the outer loop advances to 3 and the inner loop begins again.\n'
            '\n'
            '    # Beginner-Friendly Explanation\n'
            '    The same pattern can represent rows and columns, combinations of choices, or a small multiplication table. The key is that the inner loop is tied to the current outer value.\n'
            '\n'
            '    # Try It Yourself\n'
            '    Create a 3 by 3 coordinate table.\n'
            '\n'
            '    # Guided Exercise\n'
            '    Use two ranges and print the product of the current values.\n'
            '\n'
            '    # Independent Exercise\n'
            '    Build a small multiplication table from 1 through 3.\n'
            '\n'
            '    # Hints\n'
            '    First decide what the outer loop represents and what the inner loop represents.\n'
            '\n'
            '    # Common Mistakes\n'
            '    - Mixing up the roles of the outer and inner variables.\n'
            '- Forgetting to use the current outer value inside the inner loop.\n'
            '- Making the nested loops too large before understanding the small case.\n'
            '\n'
            '    # Short Quiz\n'
            '    1. Why are nested loops useful?\n'
            '2. What happens to the inner loop when the outer loop changes?\n'
            '3. What can the two loop variables represent?\n'
            '\n'
            '    # Answer and Explanation\n'
            '    1. They handle two levels of repetition.\n'
            '2. The inner loop starts its full sequence again.\n'
            '3. Examples include row/column, number/multiplier, or two small groups of choices.\n'
            '\n'
            '    # Summary\n'
            '    Nested loops are most useful when a task has two dimensions or repeated combinations.\n'
            '\n'
            '    # Practice/Review\n'
            '    Trace one row of a multiplication table before coding the whole table.\n'
            '\n'
            '    # Optional Challenge\n'
            '    Create a 1–5 multiplication table using nested loops.\n'
        ),
        "exercises": [
            {
                "instructions": 'Print the products for 1, 2, and 3 multiplied by 1, 2, and 3.',
                "starter_code": 'for number in range(1, 4):\n    for multiplier in range(1, 4):\n        print(number * multiplier)\n',
                "expected_output": '1\n2\n3\n2\n4\n6\n3\n6\n9',
            },
            {
                "instructions": 'Print all coordinate pairs for a 3 by 3 grid.',
                "starter_code": 'for row in range(3):\n    for column in range(3):\n        print(row, column)\n',
                "expected_output": '0 0\n0 1\n0 2\n1 0\n1 1\n1 2\n2 0\n2 1\n2 2',
            },
        ],
    },
    {
        "title": 'Lesson 18 — Conditions Inside Loops',
        "content": (
            '    # Module: Loops + Decisions\n'
            '    # Learning Objectives\n'
            '    - Combine loops with if statements.\n'
            '- Use a condition for each current value.\n'
            '- Reuse Level 2 decision-making inside repetition.\n'
            '\n'
            '    # Why This Matters\n'
            '    Real programs often repeat over many values while making a decision about each one. This is one of the most important combinations in Python.\n'
            '\n'
            '    # Explanation\n'
            '    A loop decides **what values to visit**. An `if` decides **what to do with the current value**. The condition is evaluated once for each iteration when the `if` is inside the loop.\n'
            '\n'
            '    # Examples\n'
            '    ```python\n'
            'for number in range(1, 11):\n'
            '    if number % 2 == 0:\n'
            '        print(number)\n'
            '```\n'
            '\n'
            'The loop visits 1 through 10; the condition selects the even values.\n'
            '\n'
            '    # Worked Example\n'
            '    You can classify every value:\n'
            '```python\n'
            'for number in range(1, 4):\n'
            '    if number % 2 == 0:\n'
            '        print("Even")\n'
            '    else:\n'
            '        print("Odd")\n'
            '```\n'
            '\n'
            '    # Beginner-Friendly Explanation\n'
            '    For each number, Python enters the `if`, gets either `True` or `False`, and chooses a branch. Then the loop moves to the next number and the decision happens again.\n'
            '\n'
            '    # Try It Yourself\n'
            '    Print only numbers greater than 5 from 1 through 10.\n'
            '\n'
            '    # Guided Exercise\n'
            '    Put an if statement inside a for loop and test one comparison.\n'
            '\n'
            '    # Independent Exercise\n'
            '    Classify numbers from 1 to 6 as even or odd.\n'
            '\n'
            '    # Hints\n'
            '    Write the loop first, then decide what should happen for one current value.\n'
            '\n'
            '    # Common Mistakes\n'
            '    - Putting the if outside the loop when the decision should happen for every value.\n'
            '- Forgetting that the current value changes each iteration.\n'
            '- Using a condition that refers to an unrelated variable.\n'
            '\n'
            '    # Short Quiz\n'
            '    1. What does the loop provide?\n'
            '2. What does the if decide?\n'
            '3. How often is the condition checked?\n'
            '\n'
            '    # Answer and Explanation\n'
            '    1. It provides one current value per iteration.\n'
            '2. It decides what happens for that current value.\n'
            '3. Once per iteration while the if is inside the loop.\n'
            '\n'
            '    # Summary\n'
            '    Loops handle repetition; conditions handle decisions about each repeated value.\n'
            '\n'
            '    # Practice/Review\n'
            '    Combine a Level 2 comparison with a Level 3 loop and explain the two responsibilities separately.\n'
            '\n'
            '    # Optional Challenge\n'
            '    Use `if` and `elif` inside a loop to classify values into three categories.\n'
        ),
        "exercises": [
            {
                "instructions": 'Print the even numbers from 1 through 10.',
                "starter_code": 'for number in range(1, 11):\n    if number % 2 == 0:\n        print(number)\n',
                "expected_output": '2\n4\n6\n8\n10',
            },
            {
                "instructions": 'Print Positive for each positive number.',
                "starter_code": 'for number in [2, 5, 8]:\n    if number > 0:\n        print("Positive")\n',
                "expected_output": 'Positive\nPositive\nPositive',
            },
        ],
    },
    {
        "title": 'Lesson 19 — Counting Matching Values',
        "content": (
            '    # Module: Loops + Decisions\n'
            '    # Learning Objectives\n'
            '    - Combine a loop, condition, and counter.\n'
            '- Count only matching values.\n'
            '- Explain the role of each variable.\n'
            '\n'
            '    # Why This Matters\n'
            '    Many useful programs ask how many items meet a rule. The loop finds the items, the condition decides whether an item matches, and the counter records how many matches have occurred.\n'
            '\n'
            '    # Explanation\n'
            '    Create the counter before the loop. For each current value, check the rule. Increase the counter only when the rule is true.\n'
            '\n'
            '    # Examples\n'
            '    ```python\n'
            'count = 0\n'
            'for number in range(1, 11):\n'
            '    if number % 2 == 0:\n'
            '        count += 1\n'
            'print(count)\n'
            '```\n'
            '\n'
            'The result is 5.\n'
            '\n'
            '    # Worked Example\n'
            '    The `number` variable is the current value. The `if` is the matching rule. `count` is the number of matches found so far. Keeping these roles separate makes debugging easier.\n'
            '\n'
            '    # Beginner-Friendly Explanation\n'
            '    For values 1 through 6, the counter changes only at 2, 4, and 6:\n'
            '\n'
            '```text\n'
            '1 → count 0\n'
            '2 → count 1\n'
            '3 → count 1\n'
            '4 → count 2\n'
            '5 → count 2\n'
            '6 → count 3\n'
            '```\n'
            '\n'
            '    # Try It Yourself\n'
            '    Count the values from 1 through 20 that are divisible by 5.\n'
            '\n'
            '    # Guided Exercise\n'
            '    Initialize `count = 0`, then increase it when the divisibility condition is true.\n'
            '\n'
            '    # Independent Exercise\n'
            '    Count how many values in `[4, 9, 12, 3, 15]` are greater than 10.\n'
            '\n'
            '    # Hints\n'
            '    The counter should change only when the condition is satisfied.\n'
            '\n'
            '    # Common Mistakes\n'
            '    - Incrementing on every iteration.\n'
            '- Resetting count inside the loop.\n'
            '- Testing the wrong property.\n'
            '\n'
            '    # Short Quiz\n'
            '    1. What does `count` represent?\n'
            '2. When does it increase?\n'
            '3. Why is it initialized before the loop?\n'
            '\n'
            '    # Answer and Explanation\n'
            '    1. The number of matches found so far.\n'
            '2. Only when the condition is true.\n'
            '3. So its previous value is preserved across all iterations.\n'
            '\n'
            '    # Summary\n'
            '    A conditional counter counts matches instead of counting every loop iteration.\n'
            '\n'
            '    # Practice/Review\n'
            '    Trace the counter for even values from 1 through 6.\n'
            '\n'
            '    # Optional Challenge\n'
            '    Count numbers that are both positive and even.\n'
        ),
        "exercises": [
            {
                "instructions": 'Count the even numbers from 1 through 10.',
                "starter_code": 'count = 0\nfor number in range(1, 11):\n    if number % 2 == 0:\n        count += 1\nprint(count)\n',
                "expected_output": '5',
            },
            {
                "instructions": 'Count the values greater than 10.',
                "starter_code": 'numbers = [4, 9, 12, 3, 15]\ncount = 0\nfor number in numbers:\n    if number > 10:\n        count += 1\nprint(count)\n',
                "expected_output": '2',
            },
        ],
    },
    {
        "title": 'Lesson 20 — Filtering with a Loop',
        "content": (
            '    # Module: Loops + Decisions\n'
            '    # Learning Objectives\n'
            '    - Use a loop to select matching values.\n'
            '- Apply conditions to realistic small data.\n'
            '- Explain why non-matching values are still checked.\n'
            '\n'
            '    # Why This Matters\n'
            '    Filtering is the process of selecting values that meet a rule. It appears in everyday programs such as selecting passing scores or finding temperatures above a threshold.\n'
            '\n'
            '    # Explanation\n'
            '    A filter usually follows the pattern: loop through each value, test the current value, and do something only when the condition is true.\n'
            '\n'
            '    # Examples\n'
            '    ```python\n'
            'for score in [55, 82, 91, 64]:\n'
            '    if score >= 70:\n'
            '        print(score)\n'
            '```\n'
            '\n'
            'Output: 82 and 91.\n'
            '\n'
            '    # Worked Example\n'
            '    For temperatures:\n'
            '```python\n'
            'for temperature in [12, 18, 31, 27]:\n'
            '    if temperature > 30:\n'
            '        print(temperature)\n'
            '```\n'
            '\n'
            'Only 31 passes the filter.\n'
            '\n'
            '    # Beginner-Friendly Explanation\n'
            '    The loop still checks values that do not match. Filtering does not remove the need to inspect them; it decides which inspected values should produce an action.\n'
            '\n'
            '    # Try It Yourself\n'
            '    Filter numbers greater than 10.\n'
            '\n'
            '    # Guided Exercise\n'
            '    Put one comparison inside the loop and print only values that pass.\n'
            '\n'
            '    # Independent Exercise\n'
            '    Filter a set of scores to show passing scores of 70 or more.\n'
            '\n'
            '    # Hints\n'
            '    Translate the English rule into a comparison before writing the Python.\n'
            '\n'
            '    # Common Mistakes\n'
            '    - Using the wrong boundary such as `>` instead of `>=`.\n'
            '- Assuming a non-match stops the loop.\n'
            '- Putting the condition outside the loop.\n'
            '\n'
            '    # Short Quiz\n'
            '    1. What does filtering mean?\n'
            '2. Are non-matching items still visited?\n'
            '3. Where does the filter rule usually appear?\n'
            '\n'
            '    # Answer and Explanation\n'
            '    1. Selecting values that meet a rule.\n'
            '2. Yes, the loop still visits them.\n'
            '3. Inside the loop, often in an if statement.\n'
            '\n'
            '    # Summary\n'
            '    Filtering combines repeated processing with a decision about each current value.\n'
            '\n'
            '    # Practice/Review\n'
            '    Create two different filters for the same fixed values and explain how the rule changes.\n'
            '\n'
            '    # Optional Challenge\n'
            '    Filter values using two conditions connected with `and`, reusing your Level 2 logic skills.\n'
        ),
        "exercises": [
            {
                "instructions": 'Print scores of 70 or higher.',
                "starter_code": 'for score in [55, 82, 91, 64]:\n    if score >= 70:\n        print(score)\n',
                "expected_output": '82\n91',
            },
            {
                "instructions": 'Print only positive numbers.',
                "starter_code": 'for number in [-3, 0, 4, -1, 8]:\n    if number > 0:\n        print(number)\n',
                "expected_output": '4\n8',
            },
        ],
    },
    {
        "title": 'Lesson 21 — Number Counter',
        "content": (
            '    # Module: Practical Loop Problems\n'
            '    # Learning Objectives\n'
            '    - Build a simple counting program.\n'
            '- Use range() to control a known count.\n'
            '- Plan a loop before writing it.\n'
            '\n'
            '    # Why This Matters\n'
            '    A small counting program is a useful way to practise the core pattern without adding new concepts.\n'
            '\n'
            '    # Explanation\n'
            '    When the start and end values are known, `for` with `range()` is often straightforward. The loop variable itself represents the current number to print.\n'
            '\n'
            '    # Examples\n'
            '    ```python\n'
            'for number in range(1, 11):\n'
            '    print(number)\n'
            '```\n'
            '\n'
            'This prints 1 through 10.\n'
            '\n'
            '    # Worked Example\n'
            '    A countdown can use a negative step:\n'
            '```python\n'
            'for number in range(10, 0, -1):\n'
            '    print(number)\n'
            '```\n'
            '\n'
            '    # Beginner-Friendly Explanation\n'
            '    Plan the task first: first value, final value, direction, step, and output. If the final value should be included, remember that the stop argument must be one step beyond it when counting upward.\n'
            '\n'
            '    # Try It Yourself\n'
            '    Count from 1 to 10.\n'
            '\n'
            '    # Guided Exercise\n'
            '    Use `range(1, 11)` and print the loop variable.\n'
            '\n'
            '    # Independent Exercise\n'
            '    Count from 20 down to 10.\n'
            '\n'
            '    # Hints\n'
            '    Choose start, stop, and step on paper before typing.\n'
            '\n'
            '    # Common Mistakes\n'
            '    - Off-by-one mistakes in range().\n'
            '- Using a positive step for a descending task.\n'
            '\n'
            '    # Short Quiz\n'
            '    1. Why is `range()` useful?\n'
            '2. Why is the stop value one greater than 10 in `range(1, 11)`?\n'
            '3. What controls direction in a countdown?\n'
            '\n'
            '    # Answer and Explanation\n'
            '    1. It supplies a numeric sequence.\n'
            '2. Because the stop is excluded.\n'
            '3. The sign of the step.\n'
            '\n'
            '    # Summary\n'
            '    Counting loops are simple but important practice for range(), loop variables, and planning.\n'
            '\n'
            '    # Practice/Review\n'
            '    Write an ascending count and a descending count, then compare their range arguments.\n'
            '\n'
            '    # Optional Challenge\n'
            '    Print every third number from 3 through 18.\n'
        ),
        "exercises": [
            {
                "instructions": 'Print 1 through 10.',
                "starter_code": 'for number in range(1, 11):\n    print(number)\n',
                "expected_output": '1\n2\n3\n4\n5\n6\n7\n8\n9\n10',
            },
            {
                "instructions": 'Print 20 down to 10.',
                "starter_code": 'for number in range(20, 9, -1):\n    print(number)\n',
                "expected_output": '20\n19\n18\n17\n16\n15\n14\n13\n12\n11\n10',
            },
        ],
    },
    {
        "title": 'Lesson 22 — Running Total',
        "content": (
            '    # Module: Practical Loop Problems\n'
            '    # Learning Objectives\n'
            '    - Build a running total.\n'
            '- Combine looping and accumulation.\n'
            '- Keep the current value separate from the total.\n'
            '\n'
            '    # Why This Matters\n'
            '    Running totals are common in shopping carts, scores, budgets, and reports. The loop processes each value while the accumulator remembers the sum so far.\n'
            '\n'
            '    # Explanation\n'
            '    Initialize the total once before the loop. During each iteration, add the current value to it. Do not replace the total with the current value, because the purpose of the accumulator is to remember all previous additions.\n'
            '\n'
            '    # Examples\n'
            '    ```python\n'
            'total = 0\n'
            'for price in [5, 8, 12]:\n'
            '    total += price\n'
            'print(total)\n'
            '```\n'
            '\n'
            'The total is 25.\n'
            '\n'
            '    # Worked Example\n'
            '    For 10, 5, and 8, the running total is 10 → 15 → 23. The current value changes every iteration; the total carries the history.\n'
            '\n'
            '    # Beginner-Friendly Explanation\n'
            '    A common bug is:\n'
            '```python\n'
            'total = price\n'
            '```\n'
            'inside the loop. That throws away the old total. `total += price` keeps the old result and adds the new value.\n'
            '\n'
            '    # Try It Yourself\n'
            '    Calculate the total of five fixed numbers.\n'
            '\n'
            '    # Guided Exercise\n'
            '    Start `total = 0` and add one current value each iteration.\n'
            '\n'
            '    # Independent Exercise\n'
            '    Calculate the total of `[12, 8, 25, 10]`.\n'
            '\n'
            '    # Hints\n'
            '    Ask whether the line should preserve the old total. If yes, use an accumulating update.\n'
            '\n'
            '    # Common Mistakes\n'
            '    - Resetting total each iteration.\n'
            '- Replacing instead of adding.\n'
            '- Starting with an inappropriate initial value.\n'
            '\n'
            '    # Short Quiz\n'
            '    1. What does a running total store?\n'
            '2. Why does it need to be outside the loop?\n'
            '3. What does `total += value` mean?\n'
            '\n'
            '    # Answer and Explanation\n'
            '    1. The sum of values processed so far.\n'
            '2. So earlier values are not forgotten.\n'
            '3. Add the current value to the existing total.\n'
            '\n'
            '    # Summary\n'
            '    A running total is an accumulator that carries the result from one iteration to the next.\n'
            '\n'
            '    # Practice/Review\n'
            '    Trace the total for `[3, 5, 7]` and write each intermediate result.\n'
            '\n'
            '    # Optional Challenge\n'
            '    Combine a running total with a counter and calculate an average.\n'
        ),
        "exercises": [
            {
                "instructions": 'Calculate the total of the numbers.',
                "starter_code": 'total = 0\nfor number in [3, 7, 10, 5]:\n    total += number\nprint(total)\n',
                "expected_output": '25',
            },
            {
                "instructions": 'Calculate the total price.',
                "starter_code": 'prices = [4, 6, 15]\ntotal = 0\nfor price in prices:\n    total += price\nprint("Total:", total)\n',
                "expected_output": 'Total: 25',
            },
        ],
    },
    {
        "title": 'Lesson 23 — Average Calculator',
        "content": (
            '    # Module: Practical Loop Problems\n'
            '    # Learning Objectives\n'
            '    - Calculate an average using a loop.\n'
            '- Understand why total and count are both needed.\n'
            '- Avoid dividing by the wrong quantity.\n'
            '\n'
            '    # Why This Matters\n'
            '    An average combines accumulation and counting. Learning to calculate it now prepares you for later data-processing tasks.\n'
            '\n'
            '    # Explanation\n'
            '    The average is `total / count`. A loop can accumulate the total and increase a counter as it processes values. The division should happen after all values have been processed.\n'
            '\n'
            '    # Examples\n'
            '    ```python\n'
            'numbers = [10, 20, 30]\n'
            'total = 0\n'
            'count = 0\n'
            'for number in numbers:\n'
            '    total += number\n'
            '    count += 1\n'
            'print(total / count)\n'
            '```\n'
            '\n'
            'Output: 20.0\n'
            '\n'
            '    # Worked Example\n'
            '    For 10, 20, and 30, the total is 60 and the count is 3, so the average is 20.0.\n'
            '\n'
            '    # Beginner-Friendly Explanation\n'
            '    The two variables have different jobs:\n'
            '- `total` stores the sum.\n'
            '- `count` stores how many values were included.\n'
            '\n'
            'Using `total / count` keeps the calculation connected to the actual number of values processed.\n'
            '\n'
            '    # Try It Yourself\n'
            '    Calculate the average of 4, 6, and 8.\n'
            '\n'
            '    # Guided Exercise\n'
            '    Build a total and count in the same loop, then divide after the loop.\n'
            '\n'
            '    # Independent Exercise\n'
            '    Calculate the average of `[70, 80, 90, 100]`.\n'
            '\n'
            '    # Hints\n'
            '    First calculate total, then count, then divide total by count.\n'
            '\n'
            '    # Common Mistakes\n'
            '    - Dividing by the wrong number.\n'
            '- Calculating before all values are processed.\n'
            '- Confusing the current value with the running total.\n'
            '\n'
            '    # Short Quiz\n'
            '    1. What is the average formula?\n'
            '2. Why do we need count?\n'
            '3. When should the average normally be calculated?\n'
            '\n'
            '    # Answer and Explanation\n'
            '    1. `average = total / count`.\n'
            '2. It tells us how many values are included.\n'
            '3. After the loop has processed the values.\n'
            '\n'
            '    # Summary\n'
            '    An average is a total divided by the number of values included in the total.\n'
            '\n'
            '    # Practice/Review\n'
            '    Trace total and count for three values and calculate the average by hand.\n'
            '\n'
            '    # Optional Challenge\n'
            '    Build an average calculator for five values, using the same accumulator and counter pattern.\n'
        ),
        "exercises": [
            {
                "instructions": 'Calculate the average of 10, 20, and 30.',
                "starter_code": 'numbers = [10, 20, 30]\ntotal = 0\ncount = 0\nfor number in numbers:\n    total += number\n    count += 1\nprint(total / count)\n',
                "expected_output": '20.0',
            },
            {
                "instructions": 'Calculate the average of four scores.',
                "starter_code": 'scores = [70, 80, 90, 100]\ntotal = 0\ncount = 0\nfor score in scores:\n    total += score\n    count += 1\nprint(total / count)\n',
                "expected_output": '85.0',
            },
        ],
    },
    {
        "title": 'Lesson 24 — Multiplication Tables',
        "content": (
            '    # Module: Practical Loop Problems\n'
            '    # Learning Objectives\n'
            '    - Use a loop for repeated arithmetic.\n'
            '- Use range() for a multiplication table.\n'
            '- Keep a fixed value separate from a changing multiplier.\n'
            '\n'
            '    # Why This Matters\n'
            '    Multiplication tables provide a compact way to practise loops, range(), variables, and arithmetic together.\n'
            '\n'
            '    # Explanation\n'
            '    Choose the table number that stays fixed. Let the loop variable represent the multiplier. Each iteration calculates a new product.\n'
            '\n'
            '    # Examples\n'
            '    ```python\n'
            'for multiplier in range(1, 6):\n'
            '    print(5 * multiplier)\n'
            '```\n'
            '\n'
            'This prints the first five results in the 5 times table.\n'
            '\n'
            '    # Worked Example\n'
            '    A clearer version labels the equation:\n'
            '```python\n'
            'for multiplier in range(1, 6):\n'
            '    print(5, "x", multiplier, "=", 5 * multiplier)\n'
            '```\n'
            '\n'
            '    # Beginner-Friendly Explanation\n'
            '    The number 5 remains fixed. `multiplier` changes from 1 to 5. The loop handles the changing part; arithmetic combines the two values.\n'
            '\n'
            '    # Try It Yourself\n'
            '    Print the first five values of the 3 times table.\n'
            '\n'
            '    # Guided Exercise\n'
            '    Use `range(1, 6)` and multiply the current multiplier by 3.\n'
            '\n'
            '    # Independent Exercise\n'
            '    Generate the 7 times table from 1 to 10.\n'
            '\n'
            '    # Hints\n'
            '    Decide which number stays fixed and which number changes.\n'
            '\n'
            '    # Common Mistakes\n'
            '    - Using the wrong range.\n'
            '- Changing the fixed table number by accident.\n'
            '- Printing the multiplier instead of the product.\n'
            '\n'
            '    # Short Quiz\n'
            '    1. Which variable changes?\n'
            '2. What stays fixed?\n'
            '3. Why is range useful?\n'
            '\n'
            '    # Answer and Explanation\n'
            '    1. The multiplier.\n'
            '2. The selected table number.\n'
            '3. It supplies the multiplier values automatically.\n'
            '\n'
            '    # Summary\n'
            '    A multiplication table is a controlled repetition of a simple arithmetic rule.\n'
            '\n'
            '    # Practice/Review\n'
            '    Write the 4 times table by hand, then compare your values with a loop output.\n'
            '\n'
            '    # Optional Challenge\n'
            '    Use nested loops to print a small 1–5 multiplication table after reviewing nested loops.\n'
        ),
        "exercises": [
            {
                "instructions": 'Print the 3 times table from 1 through 5.',
                "starter_code": 'for multiplier in range(1, 6):\n    print(3 * multiplier)\n',
                "expected_output": '3\n6\n9\n12\n15',
            },
            {
                "instructions": 'Print the 7 times table from 1 through 10.',
                "starter_code": 'for multiplier in range(1, 11):\n    print(7 * multiplier)\n',
                "expected_output": '7\n14\n21\n28\n35\n42\n49\n56\n63\n70',
            },
        ],
    },
    {
        "title": 'Lesson 25 — Input Validation Loop',
        "content": (
            '    # Module: Practical Loop Problems\n'
            '    # Learning Objectives\n'
            '    - Use a while loop for validation.\n'
            '- Reuse Level 2 comparisons and logical operators.\n'
            '- Explain why invalid input triggers another iteration.\n'
            '\n'
            '    # Why This Matters\n'
            '    You already know how to decide whether a value is valid. A while loop lets the program keep asking until the user satisfies that rule.\n'
            '\n'
            '    # Explanation\n'
            '    A validation loop keeps repeating while the input is invalid. For a required range from 1 to 10, the invalid condition is `number < 1 or number > 10`.\n'
            '\n'
            '    # Examples\n'
            '    ```python\n'
            'number = int(input("Enter 1-10: "))\n'
            'while number < 1 or number > 10:\n'
            '    print("Invalid")\n'
            '    number = int(input("Try again: "))\n'
            'print("Accepted:", number)\n'
            '```\n'
            '\n'
            '    # Worked Example\n'
            '    The loop condition describes the bad state that requires another attempt. When the number finally enters the valid range, the condition becomes false and the program continues.\n'
            '\n'
            '    # Beginner-Friendly Explanation\n'
            '    This is a direct combination of Level 2 and Level 3:\n'
            '- Level 2 supplies the validation rule.\n'
            '- Level 3 supplies repetition until the rule is satisfied.\n'
            '\n'
            '    # Try It Yourself\n'
            '    Create a validation loop for numbers from 1 to 5.\n'
            '\n'
            '    # Guided Exercise\n'
            '    Use `number < 1 or number > 5` as the invalid condition.\n'
            '\n'
            '    # Independent Exercise\n'
            '    Design a validation loop for a menu choice of 1, 2, or 3.\n'
            '\n'
            '    # Hints\n'
            '    Describe the invalid condition first; it is usually easier than writing the whole loop immediately.\n'
            '\n'
            '    # Common Mistakes\n'
            '    - Using `and` instead of `or` for an outside-range condition.\n'
            '- Forgetting to request new input inside the loop.\n'
            '- Writing the valid condition when the loop needs the invalid condition.\n'
            '\n'
            '    # Short Quiz\n'
            '    1. What should the loop condition represent?\n'
            '2. Why is `or` used for outside-range validation?\n'
            '3. What happens when the input becomes valid?\n'
            '\n'
            '    # Answer and Explanation\n'
            '    1. The invalid state that requires another attempt.\n'
            '2. A value can be too small or too large.\n'
            '3. The condition becomes false and the loop ends.\n'
            '\n'
            '    # Summary\n'
            '    Validation loops repeat a familiar decision until the value becomes acceptable.\n'
            '\n'
            '    # Practice/Review\n'
            '    Translate three Level 2 validation rules into while-loop conditions.\n'
            '\n'
            '    # Optional Challenge\n'
            '    Create a validation loop that accepts only even numbers between 2 and 20.\n'
        ),
        "exercises": [
            {
                "instructions": 'Keep asking until the number is between 1 and 5. Test with 8, 0, then 4.',
                "starter_code": 'number = int(input())\nwhile number < 1 or number > 5:\n    number = int(input())\nprint("Accepted:", number)\n',
                "expected_output": 'Accepted: 4',
            },
            {
                "instructions": 'Keep asking until the user enters a positive number. Test with -2, 0, then 7.',
                "starter_code": 'number = int(input())\nwhile number <= 0:\n    number = int(input())\nprint("Accepted:", number)\n',
                "expected_output": 'Accepted: 7',
            },
        ],
    },
    {
        "title": 'Lesson 26 — Simple Menu Loop',
        "content": (
            '    # Module: Practical Loop Problems\n'
            '    # Learning Objectives\n'
            '    - Build a repeating text menu.\n'
            '- Combine input with if/elif/else.\n'
            '- Use break as a clear exit option.\n'
            '\n'
            '    # Why This Matters\n'
            '    Many programs repeatedly show choices to the user. A menu loop provides a clear place to choose an action and then return to the menu.\n'
            '\n'
            '    # Explanation\n'
            '    A simple menu can use `while True` and `break`. The loop repeats the menu, `input()` reads the choice, and `if`/`elif` decides which action to take. The exit choice triggers `break`.\n'
            '\n'
            '    # Examples\n'
            '    ```python\n'
            'while True:\n'
            '    print("1. Say hello")\n'
            '    print("2. Show status")\n'
            '    print("3. Exit")\n'
            '\n'
            '    choice = input("Choose: " )\n'
            '\n'
            '    if choice == "1":\n'
            '        print("Hello")\n'
            '    elif choice == "2":\n'
            '        print("Ready")\n'
            '    elif choice == "3":\n'
            '        break\n'
            '    else:\n'
            '        print("Invalid choice")\n'
            '```\n'
            '\n'
            '    # Worked Example\n'
            '    The menu has one job per part: display choices, read the choice, handle each valid branch, handle invalid input, and exit when requested.\n'
            '\n'
            '    # Beginner-Friendly Explanation\n'
            '    `while True` does not tell Python when to stop. That is why `break` matters here. The program stops only when the user selects the deliberate exit branch.\n'
            '\n'
            '    # Try It Yourself\n'
            '    Create a two-option menu with an exit choice.\n'
            '\n'
            '    # Guided Exercise\n'
            '    Start with `while True`, then write one branch for each menu option and one branch for exit.\n'
            '\n'
            '    # Independent Exercise\n'
            '    Add a simple third action such as printing the current number from 1 to 3.\n'
            '\n'
            '    # Hints\n'
            '    Keep menu choices as strings because `input()` returns text.\n'
            '\n'
            '    # Common Mistakes\n'
            '    - Forgetting the exit branch.\n'
            '- Comparing an input string to an integer without conversion.\n'
            '- Putting break in the wrong branch.\n'
            '\n'
            '    # Short Quiz\n'
            '    1. Why is `while True` useful here?\n'
            '2. What actually ends the menu loop?\n'
            '3. Why are choices compared as strings?\n'
            '\n'
            '    # Answer and Explanation\n'
            '    1. It keeps the menu repeating until a deliberate exit.\n'
            '2. `break`.\n'
            '3. Because `input()` returns text.\n'
            '\n'
            '    # Summary\n'
            '    A menu loop combines repetition, decisions, input, and an explicit exit.\n'
            '\n'
            '    # Practice/Review\n'
            '    Trace one menu cycle and identify which branch runs for each possible choice.\n'
            '\n'
            '    # Optional Challenge\n'
            '    Add a fourth menu option that prints a short multiplication table.\n'
        ),
        "exercises": [
            {
                "instructions": 'Run the menu with choices 1, 2, and 3 in order; 3 exits.',
                "starter_code": 'while True:\n    choice = input()\n    if choice == "1":\n        print("Hello")\n    elif choice == "2":\n        print("Ready")\n    elif choice == "3":\n        break\n',
                "expected_output": 'Hello\nReady',
            },
            {
                "instructions": 'Build a menu that prints Start for 1, Help for 2, and exits for 3.',
                "starter_code": 'while True:\n    choice = input()\n    # Write the menu logic here\n',
                "expected_output": 'Start\nHelp',
            },
        ],
    },
    {
        "title": 'Lesson 27 — Debugging Loop Output',
        "content": (
            '    # Module: Practical Loop Problems\n'
            '    # Learning Objectives\n'
            '    - Use expected output to locate loop bugs.\n'
            '- Distinguish loop bugs from arithmetic bugs.\n'
            '- Make the smallest necessary correction.\n'
            '\n'
            '    # Why This Matters\n'
            '    Debugging becomes easier when you predict what code should do and compare that with what it actually does. Loop bugs often come from the start, stop, step, or update.\n'
            '\n'
            '    # Explanation\n'
            '    A practical debugging cycle is: state the expected output, inspect the loop control, predict the first few iterations, identify the smallest mismatch, and change only what is necessary.\n'
            '\n'
            '    # Examples\n'
            '    ```python\n'
            'for number in range(1, 6):\n'
            '    print(number + 1)\n'
            '```\n'
            '\n'
            'If the requirement is to print 1 through 5, the loop range is fine; the problem is the `+ 1`.\n'
            '\n'
            '    # Worked Example\n'
            '    Another example:\n'
            '```python\n'
            'count = 1\n'
            'while count <= 5:\n'
            '    print(count)\n'
            '    count += 2\n'
            '```\n'
            '\n'
            'This loop intentionally prints 1, 3, 5. If the requirement is every number, the update is the problem.\n'
            '\n'
            '    # Beginner-Friendly Explanation\n'
            '    Do not change three lines at once. First ask whether the error is in the start, stop, step, condition, or loop-body calculation. A focused correction is easier to verify.\n'
            '\n'
            '    # Try It Yourself\n'
            '    Predict the output of a loop before looking for its bug.\n'
            '\n'
            '    # Guided Exercise\n'
            '    Identify whether the bug is in start, stop, step, update, or body output.\n'
            '\n'
            '    # Independent Exercise\n'
            '    Fix a loop that prints the wrong sequence without changing unrelated lines.\n'
            '\n'
            '    # Hints\n'
            '    Compare expected and actual output one line at a time.\n'
            '\n'
            '    # Common Mistakes\n'
            '    - Changing many things at once.\n'
            '- Assuming every bad output means the loop itself is wrong.\n'
            '- Skipping prediction and guessing fixes.\n'
            '\n'
            '    # Short Quiz\n'
            '    1. What should you compare when debugging?\n'
            '2. Why make the smallest change?\n'
            '3. Which loop parts often cause sequence errors?\n'
            '\n'
            '    # Answer and Explanation\n'
            '    1. Expected versus actual behavior.\n'
            '2. It isolates the cause and makes the fix easier to verify.\n'
            '3. Start, stop, step, condition, update, and loop-body calculation.\n'
            '\n'
            '    # Summary\n'
            '    Good debugging is controlled reasoning: predict, compare, isolate, change, and test.\n'
            '\n'
            '    # Practice/Review\n'
            '    Take one working loop and deliberately change one control value. Predict how the output changes.\n'
            '\n'
            '    # Optional Challenge\n'
            '    Write a debugging explanation for a loop that should print even numbers but prints odd numbers.\n'
        ),
        "exercises": [
            {
                "instructions": 'Fix the arithmetic so the loop prints 1 through 5.',
                "starter_code": 'for number in range(1, 6):\n    print(number + 1)\n',
                "expected_output": '1\n2\n3\n4\n5',
            },
            {
                "instructions": 'Fix the update so every number from 1 through 5 is printed.',
                "starter_code": 'count = 1\nwhile count <= 5:\n    print(count)\n    count += 2\n',
                "expected_output": '1\n2\n3\n4\n5',
            },
        ],
    },
    {
        "title": 'Lesson 28 — Mixed Loop Challenge',
        "content": (
            '    # Module: Level 3 Review and Project Preparation\n'
            '    # Learning Objectives\n'
            '    - Combine loops with conditions, counters, and accumulators.\n'
            '- Choose a suitable loop.\n'
            '- Plan a solution before coding.\n'
            '\n'
            '    # Why This Matters\n'
            '    Real problems rarely tell you which loop keyword to use. You need to identify what repeats, what controls the repetition, and what information must be remembered between iterations.\n'
            '\n'
            '    # Explanation\n'
            '    A useful planning sequence is: what repeats, what controls the loop, what is the current value, what must be counted, what must be accumulated, and what should happen when a value matches a rule.\n'
            '\n'
            '    # Examples\n'
            '    ```python\n'
            'total = 0\n'
            'count = 0\n'
            'for number in range(1, 11):\n'
            '    if number % 2 == 0:\n'
            '        total += number\n'
            '        count += 1\n'
            'print(total)\n'
            'print(count)\n'
            '```\n'
            '\n'
            '    # Worked Example\n'
            '    This single example combines a range, loop, condition, accumulator, counter, and output. None of the pieces are new; the challenge is deciding where they belong together.\n'
            '\n'
            '    # Beginner-Friendly Explanation\n'
            '    Before coding, label each variable:\n'
            '- `number`: current value\n'
            '- `total`: accumulated sum\n'
            '- `count`: number of matching values\n'
            '\n'
            'Clear roles make mixed problems easier.\n'
            '\n'
            '    # Try It Yourself\n'
            '    Choose a loop and variables for a short problem statement.\n'
            '\n'
            '    # Guided Exercise\n'
            '    Plan a program that counts and totals only even numbers from 1 to 20.\n'
            '\n'
            '    # Independent Exercise\n'
            '    Solve a problem that filters values while maintaining both a count and total.\n'
            '\n'
            '    # Hints\n'
            '    Write the plan in plain English before the code.\n'
            '\n'
            '    # Common Mistakes\n'
            '    - Coding before deciding what each variable means.\n'
            '- Using break or continue unnecessarily.\n'
            '- Resetting totals or counters inside the loop.\n'
            '\n'
            '    # Short Quiz\n'
            '    1. What should you decide before coding?\n'
            '2. Can one loop contain both an if and a counter?\n'
            '3. Can a loop use both a counter and accumulator?\n'
            '\n'
            '    # Answer and Explanation\n'
            '    1. Decide what repeats, what controls it, and what must be remembered.\n'
            '2. Yes.\n'
            '3. Yes; this is common in practical problems.\n'
            '\n'
            '    # Summary\n'
            '    Mixed problems are solved by assigning each concept one clear responsibility and then combining them.\n'
            '\n'
            '    # Practice/Review\n'
            '    Trace the even-number total-and-count example by hand.\n'
            '\n'
            '    # Optional Challenge\n'
            '    Solve a new problem from only a plain-English description without looking at a finished code example.\n'
        ),
        "exercises": [
            {
                "instructions": 'Add the even numbers from 1 through 10.',
                "starter_code": 'total = 0\nfor number in range(1, 11):\n    if number % 2 == 0:\n        total += number\nprint(total)\n',
                "expected_output": '30',
            },
            {
                "instructions": 'Count numbers greater than 5 from 1 through 10.',
                "starter_code": 'count = 0\nfor number in range(1, 11):\n    if number > 5:\n        count += 1\nprint(count)\n',
                "expected_output": '5',
            },
        ],
    },
    {
        "title": 'Lesson 29 — Level 3 Review',
        "content": (
            '    # Module: Level 3 Review and Project Preparation\n'
            '    # Learning Objectives\n'
            '    - Recall the core loop concepts.\n'
            '- Predict and debug loop behavior.\n'
            '- Prepare for the final project.\n'
            '\n'
            '    # Why This Matters\n'
            '    Review is where individual techniques become connected. You should now be able to read a loop, predict its behavior, write a small loop, and explain the purpose of each variable.\n'
            '\n'
            '    # Explanation\n'
            '    The Level 3 toolbox includes `while`, `for`, `range()`, counters, accumulators, `break`, `continue`, nested loops, and conditions inside loops. Each tool solves a different part of repetition.\n'
            '\n'
            '    # Examples\n'
            '    Quick reference:\n'
            '```python\n'
            'for number in range(1, 6):\n'
            '    print(number)\n'
            '```\n'
            '\n'
            '```python\n'
            'total = 0\n'
            'for number in range(1, 6):\n'
            '    total += number\n'
            '```\n'
            '\n'
            '```python\n'
            'count = 0\n'
            'for number in range(1, 11):\n'
            '    if number % 2 == 0:\n'
            '        count += 1\n'
            '```\n'
            '\n'
            '    # Worked Example\n'
            '    A reliable learning routine is:\n'
            '**Understand → Predict → Run → Compare → Fix → Review**\n'
            '\n'
            'The goal is not to memorise every pattern. The goal is to understand what each line contributes.\n'
            '\n'
            '    # Beginner-Friendly Explanation\n'
            '    When a loop is confusing, reduce it to questions:\n'
            '- What value changes?\n'
            '- What condition is checked?\n'
            '- What repeats?\n'
            '- What state is remembered?\n'
            '- What event stops or skips the work?\n'
            '\n'
            '    # Try It Yourself\n'
            '    Explain each Level 3 concept in one sentence.\n'
            '\n'
            '    # Guided Exercise\n'
            '    Predict one output question and one debugging question without running them first.\n'
            '\n'
            '    # Independent Exercise\n'
            '    Fix a mixed loop and explain why your correction works.\n'
            '\n'
            '    # Hints\n'
            '    Use your own words before reading the answer.\n'
            '\n'
            '    # Common Mistakes\n'
            '    - Confusing counter with accumulator.\n'
            '- Confusing break with continue.\n'
            '- Forgetting the stop value is excluded in range().\n'
            '\n'
            '    # Short Quiz\n'
            '    1. What does `range(5)` supply?\n'
            '2. What does an accumulator do?\n'
            '3. What does break do?\n'
            '4. What does continue do?\n'
            '5. What is a nested loop?\n'
            '\n'
            '    # Answer and Explanation\n'
            '    1. 0 through 4.\n'
            '2. It builds a running result.\n'
            '3. It exits the loop.\n'
            '4. It skips the current iteration and continues.\n'
            '5. A loop inside another loop.\n'
            '\n'
            '    # Summary\n'
            '    You now have the core Level 3 loop patterns needed for practical beginner programs.\n'
            '\n'
            '    # Practice/Review\n'
            '    Create a personal checklist of loop questions to ask whenever code behaves unexpectedly.\n'
            '\n'
            '    # Optional Challenge\n'
            '    Attempt the final project from a blank editor after planning the variables and loop structure on paper.\n'
        ),
        "exercises": [
            {
                "instructions": 'Count even numbers from 1 through 20.',
                "starter_code": 'count = 0\nfor number in range(1, 21):\n    if number % 2 == 0:\n        count += 1\nprint(count)\n',
                "expected_output": '10',
            },
            {
                "instructions": 'Calculate the total from 1 through 10.',
                "starter_code": 'total = 0\nfor number in range(1, 11):\n    total += number\nprint(total)\n',
                "expected_output": '55',
            },
        ],
    },
    {
        "title": 'Lesson 30 — Number Analysis Tool',
        "content": (
            '    # Module: Level 3 Review and Project Preparation\n'
            '    # Learning Objectives\n'
            '    - Apply Level 3 skills in one practical program.\n'
            '- Break a larger problem into milestones.\n'
            '- Test a loop-based program systematically.\n'
            '\n'
            '    # Why This Matters\n'
            '    The final Level 3 project brings earlier skills together without requiring later topics such as functions, files, or classes. The aim is to build confidence with planning and repetition.\n'
            '\n'
            '    # Explanation\n'
            '    Build a Number Analysis Tool that processes a series of numbers and reports useful results. The project must accept multiple values, count entries, accumulate a total, calculate an average, count positive values, count negative values, and count values that satisfy one chosen condition such as being greater than 10.\n'
            '\n'
            '    # Examples\n'
            '    ## Project Requirements\n'
            '1. Accept several numbers.\n'
            '2. Count how many numbers were accepted.\n'
            '3. Maintain a running total.\n'
            '4. Calculate an average.\n'
            '5. Count positive numbers.\n'
            '6. Count negative numbers.\n'
            '7. Count values matching one extra condition.\n'
            '8. Print a readable final summary.\n'
            '\n'
            '    # Worked Example\n'
            '    ## Milestones\n'
            '**1 — Input loop:** collect a fixed number of numbers.\n'
            '\n'
            '**2 — Counter:** track how many entries were processed.\n'
            '\n'
            '**3 — Total:** add each number to an accumulator.\n'
            '\n'
            '**4 — Decisions:** use `if` to count positive and negative values.\n'
            '\n'
            '**5 — Average:** divide total by count after the loop.\n'
            '\n'
            '**6 — Extra condition:** count values above a threshold.\n'
            '\n'
            '**7 — Final summary:** label every result clearly.\n'
            '\n'
            '    # Beginner-Friendly Explanation\n'
            '    Do not write the complete program at once. Build one milestone, run it, check the result, and only then add the next part. For example, if Milestone 2 is wrong, there is no benefit in adding the average calculation until the count works.\n'
            '\n'
            '    # Try It Yourself\n'
            '    Write down the variables you expect to need before coding.\n'
            '\n'
            '    # Guided Exercise\n'
            '    Complete Milestones 1–3 first. Test them with 4, -2, and 7.\n'
            '\n'
            '    # Independent Exercise\n'
            '    Finish the full analysis and test it with positive, negative, and zero values.\n'
            '\n'
            '    # Hints\n'
            '    Assign one job to each variable: current number, count, total, and any condition-specific counters.\n'
            '\n'
            '    # Common Mistakes\n'
            '    - Resetting totals or counters inside the loop.\n'
            '- Dividing by zero when no values have been collected.\n'
            '- Using a threshold that does not match the stated requirement.\n'
            '- Trying to add every feature before testing the core loop.\n'
            '\n'
            '    # Short Quiz\n'
            '    1. Why build the project in milestones?\n'
            '2. Which variable stores the running total?\n'
            '3. What tracks the number of values?\n'
            '4. When should average be calculated?\n'
            '5. Why test each milestone?\n'
            '\n'
            '    # Answer and Explanation\n'
            '    1. Milestones break a large problem into smaller testable pieces.\n'
            '2. An accumulator such as `total`.\n'
            '3. A counter such as `count`.\n'
            '4. After the values have been processed.\n'
            '5. Testing early makes it easier to locate the source of a bug.\n'
            '\n'
            '    # Summary\n'
            '    The Number Analysis Tool should demonstrate that you can combine loops, decisions, counters, accumulators, and earlier input skills without needing an AI to write the solution for you.\n'
            '\n'
            '    # Practice/Review\n'
            '    ### Validation Checklist\n'
            'Test at least three values, include zero, include both positive and negative numbers, and test a case where the chosen threshold matches nothing. Check total, count, average, and all conditional counts.\n'
            '\n'
            '    # Optional Challenge\n'
            '    ### Optional Challenge\n'
            "Add a count of even numbers, a second threshold, or a repeated 'run another analysis' menu. Stay within Level 3 concepts.\n"
        ),
        "exercises": [
            {
                "instructions": 'Complete the first project milestone: read three numbers and print the count. Test with 4, -2, and 7.',
                "starter_code": 'count = 0\nwhile count < 3:\n    number = int(input())\n    count += 1\nprint("Count:", count)\n',
                "expected_output": 'Count: 3',
            },
            {
                "instructions": 'Complete the core analysis for three fixed values: count, total, and average.',
                "starter_code": 'numbers = [4, -2, 7]\ncount = 0\ntotal = 0\nfor number in numbers:\n    total += number\n    count += 1\naverage = total / count\nprint("Count:", count)\nprint("Total:", total)\nprint("Average:", average)\n',
                "expected_output": 'Count: 3\nTotal: 9\nAverage: 3.0',
            },
        ],
    },
]
