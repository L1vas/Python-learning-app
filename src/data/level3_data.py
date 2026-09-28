from typing import Dict, List

# Level 3 — Loops
#
# This file keeps the same lesson structure used by the existing example:
# each lesson is a dictionary with a title and a content string.
# The content is intentionally self-contained so the learner can study it
# without needing the AI tutor.

LEVEL3_LESSONS: List[Dict[str, str]] = [
    {
        "title": "Repeating Work",
        "content": """
# Level 3 — Loops
## Lesson 1: Repeating Work

**Learning objectives**
- Understand what repetition means in programming.
- Explain why duplicated code can become difficult to maintain.
- Describe what a loop does before learning loop syntax.
- Recognise everyday tasks that benefit from repetition.

## Explanation

A program often needs to do the same kind of work more than once. In ordinary life, you might write three thank-you cards, check three temperatures, or ask three people the same question.

In a program, we can repeat an instruction by writing it several times:

```python
print("Hello")
print("Hello")
print("Hello")
```

This works, but imagine needing to print the message one hundred times. Writing the same line one hundred times would be slow and easy to get wrong. A loop gives the program a way to say, in effect, **"repeat this block of work."**

A **loop** is a programming structure that repeats a block of code. An **iteration** is one pass through the repeated block.

Loops are useful when a task is repeated a known number of times, when a program needs to process several values, or when a program should continue until some condition is met.

You already know `if` statements from Level 2. An `if` lets a program make a decision. A loop lets a program repeat work. Later in this level, you will combine the two.

## Tiny example

Without a loop:

```python
print("Welcome")
print("Welcome")
print("Welcome")
```

With a loop, the same idea can be expressed more compactly. The exact loop syntax is introduced in the next lesson. For now, focus on the purpose: **one instruction can be repeated instead of copied many times**.

## Worked thinking example

Imagine a program that must display five reminders.

One approach is to write five `print()` statements.

A better approach is to use a loop and let the program perform the repetition for us.

The important design question is not "How do I type five lines?" It is "What part of this task is repeated?"

That question will become useful throughout Python programming.

## Try it yourself

Look at these tasks and decide whether repetition is useful:

1. Print a single welcome message.
2. Print the same welcome message for 20 new users.
3. Ask one person for their age.
4. Ask 10 people for their age.
5. Check one order.
6. Check every order in a list of orders.

**Think:** What is repeated? How many times? Is the number known in advance?

## Guided exercise

Write down three real-world tasks from school, work, shopping, or home where the same action happens repeatedly. For each task, write:

- What is repeated?
- Why would copying the code many times be inconvenient?
- What information would change from one repetition to the next?

## Independent exercise

For each situation, choose **repeat** or **do once**:

- Show a menu every time a user returns to it.
- Display the name of one customer.
- Check every score in a group.
- Print a single error message.
- Ask for another password attempt after an invalid password.

Explain one of your choices in a sentence.

## Predict before running

Predict what the output should contain before thinking about how a loop would be written:

```python
print("A")
print("B")
print("C")
```

Now imagine a loop whose repeated block prints one letter from `A` to `C`. What would the output be, and how many iterations would there be?

## Common mistakes

- Thinking loops are only for counting numbers. Loops can repeat many kinds of work.
- Focusing on syntax before identifying what needs to repeat.
- Assuming every repeated task should use the same type of loop. Python has more than one looping style.

## Short quiz

**1. What is a loop?**
A. A kind of variable
B. A structure that repeats code
C. A replacement for `print()`
D. A type of string

**Answer:** B.

**Why:** A loop controls repeated execution of a block of code.

**2. What is an iteration?**
A. One complete pass through a loop body
B. A syntax error
C. A variable assignment
D. A Python file

**Answer:** A.

**3. Why are loops useful?**

**Answer:** They let a program repeat work without requiring the programmer to copy the same code over and over.

## Summary

Loops solve a simple but important problem: **repetition**. Instead of manually writing the same work again and again, a loop lets Python repeat a block of code. The next lesson introduces your first real loop.

## Review practice

Describe a task that needs exactly five repetitions and another task that should continue until a condition changes.

## Optional challenge

Imagine you are building a small quiz program. List the parts that might need repetition before you learn how to write the loop.
""",
    },
    {
        "title": "Your First while Loop",
        "content": """
## Lesson 2: Your First while Loop

**Learning objectives**
- Write the basic structure of a `while` loop.
- Understand a loop condition.
- Explain the loop body and indentation.
- Trace a short `while` loop step by step.

## Explanation

A `while` loop repeats a block of code **while a condition is `True`**.

Here is a small example:

```python
count = 1

while count <= 3:
    print(count)
    count = count + 1
```

Python works through this program in order.

1. `count = 1` creates a variable named `count` and gives it the starting value `1`.
2. `while count <= 3:` asks whether the condition is true.
3. Because `1 <= 3` is true, Python runs the indented lines.
4. `print(count)` displays `1`.
5. `count = count + 1` changes `count` to `2`.
6. Python checks `count <= 3` again.
7. The same process happens for `2` and `3`.
8. When `count` becomes `4`, `4 <= 3` is false, so the loop stops.

The indented lines are called the **loop body**. They are the instructions repeated by the loop.

## Terminology

- **Condition:** A comparison or other expression that becomes `True` or `False`.
- **Loop body:** The indented code that the loop repeats.
- **Iteration:** One complete execution of the loop body.

## Tiny example

```python
number = 1

while number < 3:
    print("Go")
    number = number + 1
```

Output:

```text
Go
Go
```

The loop runs twice because the body executes when `number` is `1` and `2`. When it becomes `3`, the condition `number < 3` is false.

## Worked example: count to five

```python
count = 1

while count <= 5:
    print(count)
    count = count + 1
```

Line by line:

- `count = 1` — choose the starting value.
- `while count <= 5:` — keep repeating while the condition is true.
- `print(count)` — show the current value.
- `count = count + 1` — move the counter forward so the loop can eventually stop.

Output:

```text
1
2
3
4
5
```

## Try it yourself

Change the example so that it prints the numbers from `1` to `4`.

## Guided exercise

Start with:

```python
count = 5
```

Build a `while` loop that prints `5`, `4`, `3`, `2`, `1`.

Hint: the value needs to move **down** instead of up.

## Independent exercise

Write a `while` loop that prints the word `Python` three times.

Your loop should use a counter variable.

## Predict before running

What does this print?

```python
count = 2
while count <= 4:
    print(count)
    count = count + 1
```

Write the output before running it in the browser.

## Common mistakes

- Forgetting the colon after the condition.
- Forgetting indentation inside the loop body.
- Changing the counter in the wrong direction.
- Using `<` when you meant `<=`, or vice versa.

## Short quiz

**1. When does the loop body run?**
A. Only when the condition is true
B. Only when the condition is false
C. Exactly once
D. Only at the end of the program

**Answer:** A.

**2. What does `count = count + 1` do?**

**Answer:** It increases `count` by one. This changes the loop's state so the condition can eventually become false.

**3. What stops the loop in the example?**

**Answer:** The condition becomes false when `count` reaches `4`.

## Summary

A `while` loop repeats its indented body while its condition is true. A safe beginner pattern is to choose a starting value, test a condition, do the work, and update the value that controls the loop.

## Review practice

Write a three-line explanation of these four pieces: starting value, condition, loop body, update.

## Optional challenge

Change the example to print only odd numbers from `1` to `9`. Think carefully about how much the counter should change each time.
""",
    },
    {
        "title": "Understanding the Loop Cycle",
        "content": """
## Lesson 3: Understanding the Loop Cycle

**Learning objectives**
- Trace a `while` loop one iteration at a time.
- Understand when the condition is checked.
- Predict output without running code.
- Explain why the update changes later iterations.

## Explanation

A useful way to understand a loop is to think of it as a cycle:

1. Check the condition.
2. If it is true, run the loop body.
3. Change the program state.
4. Check the condition again.
5. Repeat until the condition is false.

Consider:

```python
count = 1
while count <= 3:
    print(count)
    count = count + 1
```

### Trace table

| `count` before check | Condition | Action | `count` after action |
|---|---|---|---|
| 1 | `1 <= 3` → True | print 1 | 2 |
| 2 | `2 <= 3` → True | print 2 | 3 |
| 3 | `3 <= 3` → True | print 3 | 4 |
| 4 | `4 <= 3` → False | stop | 4 |

This table shows something important: **the update happens inside the loop, but the condition is checked before the next iteration.**

## Tiny example

```python
number = 2
while number < 5:
    print(number)
    number = number + 1
```

The printed values are `2`, `3`, and `4`. The value `5` is not printed because the check fails before another iteration begins.

## Worked example

Consider:

```python
score = 10
while score < 14:
    print(score)
    score = score + 2
```

Trace it:

- Start at `10` → condition true → print `10` → change to `12`.
- `12 < 14` → true → print `12` → change to `14`.
- `14 < 14` → false → stop.

Output:

```text
10
12
```

## Try it yourself

Trace this without running it:

```python
number = 3
while number <= 8:
    print(number)
    number = number + 2
```

Record the value printed on each iteration.

## Guided exercise

Complete this table for:

```python
x = 1
while x < 6:
    print(x)
    x = x + 2
```

| Before check | True/False | Printed | After update |
|---|---|---|---|
| 1 | ? | ? | ? |
| ? | ? | ? | ? |
| ? | ? | ? | ? |

## Independent exercise

Predict the exact output:

```python
n = 8
while n >= 2:
    print(n)
    n = n - 3
```

## Debugging exercise

A learner says, "`while n < 5` means the program must print 5." Explain why that is incorrect.

## Common mistakes

- Looking only at the starting value and forgetting the update.
- Forgetting that the condition is checked before every iteration.
- Assuming the final value that makes the condition false is printed automatically.

## Short quiz

**1. Which step happens before every iteration?**
A. The program closes
B. The condition is checked
C. The variable is deleted
D. The output is cleared

**Answer:** B.

**2. In the example with `score`, why is 14 not printed?**

**Answer:** Because the condition is `score < 14`. Once `score` is 14, the condition is false, so the body does not run.

**3. What should you do when predicting a loop?**

**Answer:** Track the controlling values from one iteration to the next and check the condition each time.

## Summary

The loop cycle is condition → body → update → condition again. Tracing a loop by hand is one of the best ways to understand what Python is doing and to find mistakes before running the code.

## Review practice

Make a trace table for a loop that starts at `2`, adds `3` each time, and continues while the value is below `11`.

## Optional challenge

Write a loop where the printed values increase by `5` each iteration and stop before reaching `30`.
""",
    },
    {
        "title": "Avoiding Infinite Loops",
        "content": """
## Lesson 4: Avoiding Infinite Loops

**Learning objectives**
- Explain what an infinite loop is.
- Recognise common causes of infinite loops.
- Repair a loop whose controlling value never changes.
- Check a loop for a clear stopping point before running it.

## Explanation

An **infinite loop** is a loop that keeps running because its condition never becomes false.

This loop is broken:

```python
count = 1

while count <= 3:
    print(count)
```

There is no update to `count`. It remains `1` forever. Since `1 <= 3` remains true, Python keeps printing `1`.

The fix is to change the value inside the loop:

```python
count = 1

while count <= 3:
    print(count)
    count = count + 1
```

Now `count` becomes `2`, then `3`, then `4`. At `4`, the condition is false and the loop stops.

## Safe loop habit

Before running a `while` loop, ask three questions:

1. What value controls the loop?
2. Where does that value change?
3. Why will the condition eventually become false?

If you cannot answer the third question, inspect the loop carefully.

## Worked debugging example

Broken code:

```python
number = 10
while number > 0:
    print(number)
    number = number + 1
```

The program counts upward: 10, 11, 12, 13, ... The condition `number > 0` never becomes false.

A correction is:

```python
number = 10
while number > 0:
    print(number)
    number = number - 1
```

Now the value moves toward the stopping condition.

## Try it yourself

Find the problem here:

```python
x = 0
while x < 5:
    print(x)
    x = x - 1
```

The variable changes, but in the wrong direction.

## Guided debugging exercise

Repair both loops:

**A**
```python
count = 0
while count < 4:
    print(count)
```

**B**
```python
count = 4
while count > 0:
    print(count)
    count = count + 1
```

## Independent exercise

Write a loop that counts from `1` to `5` and explain why it must stop.

## Predict before running

What happens here?

```python
n = 2
while n < 10:
    print(n)
    n = n * 2
```

Does it stop? If so, when?

## Common mistakes

- Forgetting to update the controlling variable.
- Updating it, but moving it away from the stopping point.
- Assuming a loop will stop just because it "looks like" it should.

## Short quiz

**1. What is an infinite loop?**

**Answer:** A loop that does not reach a state where its condition is false.

**2. Why does the broken `count <= 3` example repeat forever?**

**Answer:** `count` stays at `1`, so the condition stays true.

**3. Can a loop have an update and still be infinite?**

**Answer:** Yes. The update can move the value in the wrong direction or otherwise keep the condition true.

## Summary

A good `while` loop has a clear path to its stopping point. Always identify the controlling value, the update, and the reason the condition will eventually become false.

## Review practice

Look at three loops you have written and explain the stopping condition for each.

## Optional challenge

Design a loop that starts at `64` and repeatedly divides by `2` until the value is `1`.
""",
    },
    {
        "title": "Counters",
        "content": """
## Lesson 5: Counters

**Learning objectives**
- Understand a counter variable.
- Start a counter at an appropriate value.
- Increase a counter inside a loop.
- Use a counter to count events rather than merely iterations.

## Explanation

A **counter** is a variable used to keep track of how many times something has happened.

A common pattern is:

```python
count = 0

while count < 5:
    print("Hello")
    count = count + 1
```

Why start at `0`? Before anything happens, the number of completed events is zero. After the first print, the counter becomes `1`. After five prints, it becomes `5` and the loop stops.

Counters are especially useful when the event being counted is not the same thing as the loop itself. For example, we might count how many test scores are above 80.

## Worked example: count even numbers

```python
count = 0
number = 1

while number <= 10:
    if number % 2 == 0:
        count = count + 1
    number = number + 1

print(count)
```

The loop examines numbers 1 to 10. The `if` condition decides whether a number is even. Only when the condition is true does the counter increase.

The final answer is `5` because there are five even numbers from 1 through 10.

## Try it yourself

Change the example so the counter records how many numbers from `1` to `10` are greater than `7`.

## Guided exercise

A survey asks five people a question. Build a loop that increases a counter whenever the person's answer is `"yes"`.

Start with:

```python
yes_count = 0
```

Then decide what the loop should do after each answer.

## Independent exercise

Ask the user for five numbers. Count how many of them are negative.

Use:
- a loop counter to control five inputs
- a second counter to count negative numbers

## Predict before running

How many times does `match_count` increase?

```python
match_count = 0
for number in range(1, 6):
    if number >= 3:
        match_count = match_count + 1
```

## Common mistakes

- Using one variable for two different jobs.
- Starting a counter at `1` when it represents "how many have happened so far".
- Increasing the counter outside the condition when only matching items should count.

## Short quiz

**1. What does a counter store?**
A. The current text message
B. A count of events or items
C. A Python module
D. A file path

**Answer:** B.

**2. Why is `0` a natural starting value for many counters?**

**Answer:** Because before anything has happened, zero events have been counted.

**3. What is the difference between a loop-control variable and an event counter?**

**Answer:** A loop-control variable helps determine when the loop continues or stops. An event counter records how many items or events meet a specific rule.

## Summary

Counters are simple variables with an important job: keeping track of quantities. You will use them again in averages, validation loops, data processing, and projects.

## Review practice

Write a small plan for counting how many numbers from `1` to `20` are divisible by `3`.

## Optional challenge

Count how many numbers from `1` to `100` end in the digit `5`.
""",
    },
    {
        "title": "Accumulating a Total",
        "content": """
## Lesson 6: Accumulating a Total

**Learning objectives**
- Understand an accumulator variable.
- Build a running total in a loop.
- Distinguish an accumulator from a counter.
- Trace how a total changes after each iteration.

## Explanation

An **accumulator** is a variable that collects a value over time. A common accumulator keeps a running total.

Example:

```python
total = 0
number = 1

while number <= 5:
    total = total + number
    number = number + 1

print(total)
```

The accumulator starts at `0` because nothing has been added yet.

The values of `total` are:

| Iteration | `number` | `total` after addition |
|---|---:|---:|
| 1 | 1 | 1 |
| 2 | 2 | 3 |
| 3 | 3 | 6 |
| 4 | 4 | 10 |
| 5 | 5 | 15 |

The final output is `15`.

A **counter** usually answers "how many?" An **accumulator** often answers "what is the combined total?" A program can need both.

## Tiny example

```python
total = 0

total = total + 4
print(total)
```

The total changes from `0` to `4`.

## Worked example: add three prices

```python
total = 0

price = 2.50
total = total + price

price = 4.00
total = total + price

price = 1.50
total = total + price

print(total)
```

The result is `8.0`. The same pattern becomes much more useful when a loop handles an unknown number of values.

## Try it yourself

Change the first example to add only the numbers `2`, `4`, and `6`.

## Guided exercise

Create an accumulator that adds the numbers from `1` to `10`.

Check your total by doing a quick calculation on paper.

## Independent exercise

Ask the user for four prices. Add them into a running total and print the final amount.

## Predict before running

What are the values of `total` after each iteration?

```python
total = 0
for number in range(2, 6):
    total = total + number
```

## Debugging exercise

Find the error:

```python
total = 0
for number in range(1, 6):
    total = number
print(total)
```

Why does this produce `5` instead of the total of all the numbers?

## Common mistakes

- Starting the accumulator with the wrong initial value.
- Replacing the total instead of adding to it.
- Forgetting that the accumulator keeps its value between iterations.

## Short quiz

**1. What is an accumulator?**

**Answer:** A variable that gradually collects a value, such as a running total.

**2. Why does `total = number` not calculate a running total?**

**Answer:** It replaces the previous total each time instead of adding the new number to it.

**3. What is the difference between `count = count + 1` and `total = total + number`?**

**Answer:** The first usually counts events by one. The second adds the current value to a running total.

## Summary

Accumulators let programs combine values one at a time. Once you understand the pattern `total = total + value`, many practical tasks become possible.

## Review practice

Write one sentence explaining why an accumulator usually needs an initial value before the loop starts.

## Optional challenge

Calculate the sum of all multiples of `3` between `1` and `30`.
""",
    },
    {
        "title": "Loops with input()",
        "content": """
## Lesson 7: Loops with input()

**Learning objectives**
- Combine loops with `input()`.
- Reuse type conversion learned in Level 1.
- Keep a count and total while processing repeated input.
- Explain how earlier Python concepts work together.

## Explanation

Loops become much more practical when the program can repeatedly interact with the user.

Example:

```python
total = 0
count = 0

while count < 3:
    number = int(input("Enter a number: "))
    total = total + number
    count = count + 1

print("Total:", total)
```

This combines several ideas you already learned:

- `input()` gets text from the user.
- `int()` converts that text into a whole number.
- `total` accumulates the values.
- `count` keeps track of how many numbers have been entered.
- the `while` loop repeats the work three times.

## Worked example

Suppose the user enters `4`, `7`, and `2`.

The total changes like this:

- Start: `0`
- After `4`: `4`
- After `7`: `11`
- After `2`: `13`

The counter changes from `0` to `1`, then `2`, then `3`.

When `count < 3` becomes false, the loop ends and the total is printed.

## Try it yourself

Change the program to ask for five numbers instead of three.

## Guided exercise

Build a program that asks for three test scores and prints the total score.

Steps:
1. Create `total = 0`.
2. Create a counter.
3. Repeat three times.
4. Convert each input to `int`.
5. Add it to the total.
6. Print the total.

## Independent exercise

Ask for the user's daily water intake for five days and calculate the total amount entered.

## Prediction exercise

Before running this program, predict the final total if the user enters `5`, `5`, and `10`:

```python
total = 0
count = 0
while count < 3:
    number = int(input("Number: "))
    total = total + number
    count = count + 1
print(total)
```

## Common mistakes

- Forgetting `int()` when numerical arithmetic is required.
- Incrementing the counter before the input and accidentally changing how many times the loop runs.
- Using a text variable where a number is needed.

## Short quiz

**1. Why is `int(input(...))` useful here?**

**Answer:** `input()` returns text, while `int()` converts the text to a whole number that can be added.

**2. Why do we need both `total` and `count`?**

**Answer:** `total` stores the combined value, while `count` tracks how many inputs have been processed.

**3. What happens after the third input in the example?**

**Answer:** The counter becomes `3`, the condition becomes false, and the loop stops.

## Summary

A loop can repeatedly collect information from a user and process it as it arrives. This combines the skills from Levels 1 and 2 into something much more useful.

## Review practice

Change the example to collect four numbers and print both the total and the number of entries.

## Optional challenge

Ask for five temperatures and count how many are below `10` while also calculating the total.
""",
    },
    {
        "title": "Your First for Loop",
        "content": """
## Lesson 8: Your First `for` Loop

**Learning objectives**
- Understand why Python provides `for` loops.
- Recognise the loop variable.
- Repeat work over a sequence of values.
- Trace each iteration of a simple `for` loop.

## Explanation

A `for` loop is another way to repeat code. It is especially convenient when you want to go through a sequence of values one item at a time.

Start with:

```python
for number in [1, 2, 3]:
    print(number)
```

Python takes the first value, `1`, and puts it in the loop variable `number`. The body runs. Then Python moves to `2`, runs the body again, then `3`.

The list `[1, 2, 3]` is the sequence being visited. You do not need to learn every detail about lists yet; at this stage, notice only that the loop gets one value at a time.

## Terminology

- **Sequence:** An ordered collection of values that can be visited one at a time.
- **Loop variable:** The variable that refers to the current value during an iteration.

## Worked example

```python
for animal in ["cat", "dog", "rabbit"]:
    print(animal)
```

Output:

```text
cat
dog
rabbit
```

On the first iteration, `animal` refers to `"cat"`.
On the second iteration, it refers to `"dog"`.
On the third iteration, it refers to `"rabbit"`.

## Try it yourself

Change the animals to three foods you like.

## Guided exercise

Write a loop that prints each item from:

```python
["red", "green", "blue"]
```

Then change the loop variable name to something that describes the current item better.

## Independent exercise

Use a `for` loop to print three short messages from a sequence of strings.

## Predict before running

What is printed?

```python
for word in ["learn", "build", "practice"]:
    print(word)
```

## Common mistakes

- Thinking the loop variable always has to be called `i`.
- Forgetting the colon after the sequence.
- Forgetting indentation inside the loop body.
- Assuming the loop variable keeps all items instead of representing the current item.

## Short quiz

**1. What does `animal` represent in the example?**

**Answer:** It represents the current item from the sequence during the current iteration.

**2. How many iterations are there in the animal example?**

**Answer:** Three, because there are three items.

**3. Does the loop variable have to be named `item`?**

**Answer:** No. Choose a meaningful name such as `animal`, `number`, or `word`.

## Summary

A `for` loop visits values one at a time. The loop variable gives you the current value for that iteration.

## Review practice

Describe the difference between the job of a `while` condition and the job of a `for` loop variable.

## Optional challenge

Print a short sentence for each of three different foods, using the current food name inside the sentence.
""",
    },
    {
        "title": "Loop Variables",
        "content": """
## Lesson 9: Loop Variables

**Learning objectives**
- Explain how a loop variable changes between iterations.
- Predict the value of a loop variable at a particular point.
- Use meaningful loop variable names.

## Explanation

In a `for` loop, the loop variable changes automatically as Python moves through the sequence.

```python
for animal in ["cat", "dog", "rabbit"]:
    print(animal)
```

You can think of `animal` as a temporary name for **the current item**.

Second iteration: `animal` is `"dog"`.
Third iteration: `animal` is `"rabbit"`.

The loop variable is not a special kind of variable. It is an ordinary variable that Python updates for each iteration.

## Worked example

```python
for temperature in [12, 15, 18]:
    print("Temperature:", temperature)
```

The same variable name makes sense because `temperature` describes each current value.

## Try it yourself

Write a loop over three names and print:

```text
Hello, <name>
```

for each one.

## Guided exercise

Given:

```python
for score in [60, 75, 90]:
    print(score)
```

Answer:

- What is `score` on the first iteration?
- What is `score` on the second iteration?
- What is `score` on the third iteration?

Then modify the program to print `Score: <value>`.

## Independent exercise

Create a sequence of four prices and print each price with a label.

## Predict before running

What is printed?

```python
for letter in ["A", "B", "C"]:
    print("Current:", letter)
```

What is the value of `letter` on the **second** iteration?

## Debugging exercise

A learner writes:

```python
for number in [10, 20, 30]:
    print(numbers)
```

What is wrong?

**Answer:** The loop variable is named `number`, but the `print()` statement tries to use `numbers`. Those are different names.

## Common mistakes

- Mixing up singular and plural variable names.
- Assuming the loop variable has the same value on every iteration.
- Choosing vague names that make the code harder to read.

## Short quiz

**1. What will `letter` contain on the second iteration?**

```python
for letter in ["x", "y", "z"]:
    print(letter)
```

**Answer:** `"y"`.

**2. Why is `score` a good loop variable name when processing scores?**

**Answer:** It clearly describes the current value.

**3. Is the loop variable updated by the `for` loop?**

**Answer:** Yes. Python assigns the next sequence item to it on each iteration.

## Summary

A loop variable represents the current item. Good loop variable names make code easier to understand and make later exercises easier to reason about.

## Review practice

Rewrite three loops using meaningful variable names instead of `x` or `i` when the meaning is obvious.

## Optional challenge

Use two different loop variables in two separate loops and explain why their names make each loop easier to read.
""",
    },
    {
        "title": "Understanding Each Iteration",
        "content": """
## Lesson 10: Understanding Each Iteration

**Learning objectives**
- Trace a `for` loop one iteration at a time.
- Distinguish the sequence from the loop body.
- Predict output before running code.

## Explanation

A `for` loop does repeated work by taking one value at a time from a sequence.

```python
for number in [2, 4, 6]:
    print(number)
```

The execution is:

1. `number` becomes `2`; print `2`.
2. `number` becomes `4`; print `4`.
3. `number` becomes `6`; print `6`.
4. There are no more values; the loop ends.

This is different from the `while` loop cycle. With `while`, you explicitly manage the condition and often update a counter yourself. With `for`, Python moves through the sequence for you.

## Worked example

```python
for name in ["Aisha", "Ben", "Carlos"]:
    print("Welcome", name)
```

The body runs three times. Each time it uses a different current name.

## Try it yourself

Change the names to three places you would like to visit.

## Guided exercise

Trace:

```python
for value in [5, 10, 15]:
    print(value + 1)
```

Write the output and identify the value of `value` on each iteration.

## Independent exercise

Create a `for` loop over four numbers and print whether each number is above `10` using an `if` statement from Level 2.

## Predict before running

```python
for number in [1, 3, 5]:
    print(number * 2)
```

What is printed?

## Common mistakes

- Thinking Python runs the whole sequence at once.
- Forgetting that the body runs once per item.
- Confusing the current loop variable with the entire sequence.

## Short quiz

**1. How many times does the body run for a sequence of four items?**

**Answer:** Four times.

**2. Does the `for` loop need to manually increment the loop variable?**

**Answer:** No. Python moves to the next sequence item automatically.

**3. What does one iteration mean here?**

**Answer:** One execution of the loop body for one sequence value.

## Summary

The key idea of a `for` loop is simple: get the next value, place it in the loop variable, run the body, and continue until there are no more values.

## Review practice

Trace one `for` loop and one `while` loop side by side. Write one sentence about how the repetition is controlled in each.

## Optional challenge

Create a loop that turns four Celsius temperatures into Fahrenheit values using the formula `C * 9 / 5 + 32`.
""",
    },
    {
        "title": "range()",
        "content": """
## Lesson 11: `range()`

**Learning objectives**
- Understand what `range()` produces for a simple loop.
- Use `range()` with one value.
- Understand that counting starts at `0`.

## Explanation

Often you want to repeat something a certain number of times without first creating a sequence by hand. Python provides `range()` for this.

Start with:

```python
range(5)
```

For a beginner, think of `range(5)` as meaning the counting values:

```text
0, 1, 2, 3, 4
```

Notice that `5` itself is not included.

Now combine it with a `for` loop:

```python
for number in range(5):
    print(number)
```

Output:

```text
0
1
2
3
4
```

## Why does counting start at 0?

Python commonly uses zero-based counting in programming. You do not need to memorise every historical reason yet. What matters now is that `range(5)` starts at `0` and stops before `5`.

## Worked example

```python
for number in range(3):
    print("Round", number)
```

Output:

```text
Round 0
Round 1
Round 2
```

## Try it yourself

Change the example to run five rounds.

## Guided exercise

Write loops for:

- `0` through `3`
- `0` through `6`

Predict the output before running them.

## Independent exercise

Write a loop that prints the message `Practice makes progress` exactly four times using `range()`.

## Predict before running

What does this print?

```python
for x in range(4):
    print(x + 10)
```

Remember that the values from `range()` are `0`, `1`, `2`, and `3`.

## Common mistakes

- Expecting `range(5)` to include `5`.
- Forgetting that `range()` starts at `0` when only one argument is supplied.
- Confusing the loop variable with the number of repetitions.

## Short quiz

**1. What values does `range(5)` produce?**

**Answer:** `0, 1, 2, 3, 4`.

**2. How many values are there in `range(5)`?**

**Answer:** Five values.

**3. Does the number `5` appear in the sequence?**

**Answer:** No. The stop value is excluded.

## Summary

`range()` is a convenient way to generate a sequence of counting values. With one argument, `range(n)` starts at `0` and stops before `n`.

## Review practice

Predict the output of `for n in range(6): print(n * 2)` before running it.

## Optional challenge

Use `range(8)` to label eight practice questions from `0` to `7`, then adjust the output so the labels shown to the user start at `1`.
""",
    },
    {
        "title": "range() with Start, Stop, and Step",
        "content": """
## Lesson 12: `range()` with Start, Stop, and Step

**Learning objectives**
- Use the start, stop, and step arguments of `range()`.
- Predict the values produced by a range.
- Count forwards and backwards.

## Explanation

`range()` can accept more information:

```python
range(start, stop, step)
```

For example:

```python
range(0, 10, 2)
```

This means:

- start at `0`
- stop before `10`
- move by `2`

The values are:

```text
0, 2, 4, 6, 8
```

The stop value is still excluded.

## Worked example: count by twos

```python
for number in range(2, 11, 2):
    print(number)
```

Output:

```text
2
4
6
8
10
```

## Worked example: count backwards

```python
for number in range(5, 0, -1):
    print(number)
```

Output:

```text
5
4
3
2
1
```

The negative step moves downward.

## Try it yourself

Predict the values in:

```python
range(1, 10, 3)
```

## Guided exercise

Write a loop using `range()` that prints:

```text
10
8
6
4
2
```

## Independent exercise

Print every third number from `3` through `18`.

## Predict before running

What is printed?

```python
for n in range(3, 12, 4):
    print(n)
```

## Common mistakes

- Choosing a positive step when you need to count backwards.
- Forgetting that the stop value is excluded.
- Choosing a step that can never reach any value before the stop.

## Short quiz

**1. What does the third argument represent?**

**Answer:** The step, or how much the value changes between iterations.

**2. What values come from `range(10, 0, -2)`?**

**Answer:** `10, 8, 6, 4, 2`.

**3. Why is `10` included in `range(2, 11, 2)`?**

**Answer:** Because the loop stops before `11`, and `10` is the final value before that stopping point.

## Summary

Three-argument `range(start, stop, step)` lets you control where counting starts, where it stops, and how quickly it moves.

## Review practice

Create three `range()` expressions: one for counting by `1`, one by `5`, and one counting backwards.

## Optional challenge

Print the numbers from `100` down to `0` in steps of `10`.
""",
    },
    {
        "title": "Choosing while or for",
        "content": """
## Lesson 13: Choosing `while` or `for`

**Learning objectives**
- Explain a practical difference between `while` and `for`.
- Choose a suitable loop for a problem.
- Understand that the choice depends on the task, not a rigid rule.

## Explanation

Both `while` and `for` repeat code, but they often fit different kinds of problems.

A `for` loop is convenient when you are going through a sequence or repeating a known number of times:

```python
for number in range(5):
    print(number)
```

A `while` loop is often useful when repetition depends on a condition:

```python
password = ""

while password != "python":
    password = input("Password: ")
```

The first example naturally says "do this for these counting values." The second naturally says "keep going until this condition changes."

This is a useful guideline, not an absolute law. Some problems can be solved in more than one way.

## Worked comparison

**Known number of attempts:**

```python
for attempt in range(3):
    print("Try again")
```

**Unknown number of attempts:**

```python
choice = ""
while choice != "quit":
    choice = input("Type quit to stop: ")
```

## Try it yourself

For each problem, choose `for` or `while` and explain why:

1. Print numbers 1 to 50.
2. Ask for a valid age until the user enters one.
3. Print each of five labels.
4. Keep asking whether to continue until the user says no.

## Guided exercise

Write a short note explaining why a `for` loop is a natural fit for processing exactly ten quiz scores.

Then explain why a `while` loop is a natural fit for password validation where the number of attempts is not known.

## Independent exercise

Choose the loop for this scenario:

"A game repeatedly asks the player whether they want another round. The game should continue until the player chooses to quit."

Then describe the condition in plain English before writing code.

## Prediction exercise

Which loop would you choose for each code goal?

- repeat exactly 7 times
- process each item in a known sequence
- continue until the user enters `stop`

## Common mistakes

- Treating `for` as "the counting loop" and `while` as "the only input loop". Both are more flexible than that.
- Choosing a loop based only on personal habit instead of the problem's control pattern.

## Short quiz

**1. Which loop is often natural for a known number of repetitions?**

**Answer:** `for`.

**2. Which loop is often natural when the stopping point depends on a condition?**

**Answer:** `while`.

**3. Is the rule absolute?**

**Answer:** No. It is a practical guideline.

## Summary

Use `for` when you naturally have values or a known repetition pattern to visit. Use `while` when the condition itself is the main reason to continue.

## Review practice

Explain your choice of loop for one known-length task and one condition-controlled task.

## Optional challenge

Solve the same small problem once with `for` and once with `while`. Compare which version is easier to read and explain why.
""",
    },
    {
        "title": "break",
        "content": """
## Lesson 14: `break`

**Learning objectives**
- Understand what `break` does.
- Exit a loop immediately when a condition is met.
- Understand `while True` as an intentional loop pattern.

## Explanation

Sometimes a loop should stop before it reaches its normal ending condition. Python provides `break` for this.

Example:

```python
while True:
    word = input("Enter a word: ")

    if word == "quit":
        break

    print("You entered:", word)
```

`while True` creates a loop whose condition is always true. That means the loop will not stop by itself. In this design, `break` provides the exit point.

When the user enters `quit`, the `if` condition becomes true and `break` immediately leaves the loop. The `print()` statement is skipped on that iteration.

## Worked example: find the first multiple of 7

```python
for number in range(1, 30):
    if number % 7 == 0:
        print("First multiple:", number)
        break
```

The loop reaches `7`, prints it, and stops. It does not continue to `14`, `21`, or `28`.

## Try it yourself

Change the example so the loop stops when it finds the first number divisible by `5`.

## Guided exercise

Build a simple loop that keeps asking for words and stops when the user enters `stop`.

Before coding, say in plain English: "Repeat until the user enters ___."

## Independent exercise

Use a `for` loop from `1` to `20` and stop at the first number that is divisible by `4`.

## Prediction exercise

What is printed?

```python
for n in range(1, 10):
    if n == 4:
        break
    print(n)
```

## Common mistakes

- Thinking `break` skips one iteration. It does more: it exits the entire loop.
- Placing `break` outside the condition that should trigger it.
- Using `while True` without a clear exit path.

## Short quiz

**1. What does `break` do?**

**Answer:** It immediately exits the loop containing it.

**2. Why can `while True` still be safe?**

**Answer:** If the loop contains a clear and reachable `break`, the program can exit intentionally.

**3. Does `break` continue to the next iteration?**

**Answer:** No. It leaves the loop.

## Summary

`break` is useful when a loop should stop as soon as a particular event occurs. Use it deliberately and make the exit condition easy to understand.

## Review practice

Write one sentence comparing a normal `while` loop's stopping condition with a `while True` loop that uses `break`.

## Optional challenge

Search through numbers from `1` to `100` and stop when you find the first number that is both greater than `30` and divisible by `9`.
""",
    },
    {
        "title": "continue",
        "content": """
## Lesson 15: `continue`

**Learning objectives**
- Understand what `continue` does.
- Distinguish `continue` from `break`.
- Skip the remainder of one iteration without ending the loop.

## Explanation

`continue` tells Python to stop the current iteration and move on to the next one.

Example:

```python
for number in range(1, 6):
    if number == 3:
        continue

    print(number)
```

The output is:

```text
1
2
4
5
```

When `number` is `3`, `continue` is reached. Python skips the remaining body for that iteration, so `print(number)` does not run for `3`. The loop then continues with `4`.

## `break` vs `continue`

- `break` → leave the loop completely.
- `continue` → skip the rest of this iteration, then keep looping.

## Worked example

```python
for score in [10, -2, 7, -5, 9]:
    if score < 0:
        continue
    print(score)
```

Negative scores are skipped. The loop still processes later values.

## Try it yourself

Modify the example so that it skips the number `5` instead of `3`.

## Guided exercise

Print the numbers from `1` to `10`, but skip even numbers.

Hint: combine the loop with the Level 2 `%` operator and an `if` condition.

## Independent exercise

Process five temperatures but skip any temperature below `0` so only non-negative values are printed.

## Prediction exercise

What is the exact output?

```python
for n in range(1, 6):
    if n == 2 or n == 4:
        continue
    print(n)
```

## Common mistakes

- Thinking `continue` ends the loop.
- Putting useful work after `continue` in a way that can never execute for matching items.
- Using `continue` when the goal is actually to stop processing everything.

## Short quiz

**1. What happens when `continue` runs?**

**Answer:** The rest of the current loop body is skipped and the next iteration begins.

**2. What is printed when the number is `3` in the earlier example?**

**Answer:** Nothing for that iteration.

**3. Which keyword ends the loop completely?**

**Answer:** `break`.

## Summary

`continue` is a filtering tool inside a loop: it says, "I do not want to do the rest of this iteration, but I still want to keep looping."

## Review practice

Write two tiny examples: one where `break` is the correct tool, and one where `continue` is the correct tool.

## Optional challenge

Process the numbers `1` to `30`, skip numbers divisible by `3`, and print the rest.
""",
    },
    {
        "title": "break vs continue",
        "content": """
## Lesson 16: `break` vs `continue`

**Learning objectives**
- Compare `break` and `continue` precisely.
- Predict how each changes program flow.
- Debug a loop where the wrong control statement is used.

## Side-by-side explanation

Consider these two programs.

### `break`

```python
for n in range(1, 6):
    if n == 3:
        break
    print(n)
```

Output:

```text
1
2
```

The loop stops completely when `n` becomes `3`.

### `continue`

```python
for n in range(1, 6):
    if n == 3:
        continue
    print(n)
```

Output:

```text
1
2
4
5
```

Only the iteration for `3` is skipped.

## Try it yourself

Predict the output for each version before running it.

## Guided exercise

Suppose a program processes orders. If an order has an invalid item count, you want to skip that order but continue processing the rest. Should you use `break` or `continue`? Explain why.

## Independent exercise

Suppose a security check discovers a critical failure and there is no reason to process further records. Should you use `break` or `continue`? Explain why.

## Debugging exercise

The programmer wants to skip negative numbers but accidentally writes:

```python
for number in [4, -2, 7, -1, 8]:
    if number < 0:
        break
    print(number)
```

Explain why the program stops at the first negative number. Change only the control statement so later positive values are still processed.

## Common mistakes

- Choosing a keyword by memorising a phrase instead of considering the desired control flow.
- Forgetting that `break` affects the whole loop.

## Short quiz

**1. Which keyword means "leave the loop"?**

**Answer:** `break`.

**2. Which keyword means "skip this iteration"?**

**Answer:** `continue`.

**3. If you want to ignore one bad record but continue processing, which is usually appropriate?**

**Answer:** `continue`.

## Summary

Ask one question when choosing between them: **Do I want the loop to continue with another iteration?** If yes, `continue` may fit. If no, `break` may fit.

## Review practice

Explain both keywords without using the words "stop" or "skip". This forces you to describe the control flow precisely.

## Optional challenge

Write a loop that prints numbers from `1` to `20`, skips `8`, and stops completely at `15`.
""",
    },
    {
        "title": "What Is a Nested Loop?",
        "content": """
## Lesson 17: What Is a Nested Loop?

**Learning objectives**
- Understand what a nested loop is.
- Distinguish the outer loop from the inner loop.
- Trace the execution order of a nested loop.

## Explanation

A **nested loop** is a loop inside another loop.

Example:

```python
for row in range(3):
    for column in range(2):
        print(row, column)
```

The outer loop chooses a row. For each row, the inner loop runs through **all** its column values.

Trace it:

```text
row = 0, column = 0
row = 0, column = 1
row = 1, column = 0
row = 1, column = 1
row = 2, column = 0
row = 2, column = 1
```

The important idea is that the inner loop completes before the outer loop moves to its next value.

## Tiny example

```python
for outer in range(2):
    for inner in range(3):
        print("work")
```

The word `work` is printed `2 * 3 = 6` times.

## Try it yourself

Predict how many times the inner body runs for:

```python
for a in range(3):
    for b in range(4):
        print(a, b)
```

## Guided exercise

Trace:

```python
for row in range(2):
    for column in range(2):
        print(row, column)
```

Write the four lines of output in order.

## Independent exercise

Use nested loops to print a 3 by 3 grid of coordinates.

## Common mistakes

- Expecting the outer loop to move to the next value before the inner loop finishes.
- Losing track of which variable belongs to which loop.
- Overusing nested loops when a simpler solution would be clearer.

## Short quiz

**1. What is a nested loop?**

**Answer:** A loop whose body contains another loop.

**2. Which loop completes all of its iterations first?**

**Answer:** The inner loop, for the current outer iteration.

**3. How many inner iterations occur when the outer loop runs 3 times and the inner loop runs 2 times for each outer value?**

**Answer:** 6.

## Summary

Nested loops create a second level of repetition. They are useful for grids, tables, and combinations, but they should be introduced carefully because the execution can become harder to trace.

## Review practice

Draw two circles labelled "outer" and "inner" and describe in words which one changes first while Python is executing the body.

## Optional challenge

Print all coordinate pairs `(x, y)` where `x` ranges from `1` to `3` and `y` ranges from `1` to `2`.
""",
    },
    {
        "title": "Nested Loops in Practice",
        "content": """
## Lesson 18: Nested Loops in Practice

**Learning objectives**
- Use nested loops for small tables and combinations.
- Trace a multiplication-table pattern.
- Recognise when nested loops are useful.

## Example: multiplication values

```python
for number in range(1, 4):
    for multiplier in range(1, 4):
        print(number * multiplier)
```

For `number = 1`, the inner loop produces `1`, `2`, `3`.
Then `number` becomes `2`, and the inner loop starts over: `2`, `4`, `6`.
Then `number = 3`: `3`, `6`, `9`.

Output:

```text
1
2
3
2
4
6
3
6
9
```

The outer loop controls one repetition level. The inner loop runs fully for every outer value.

## Worked example: coordinate labels

```python
for row in range(1, 3):
    for column in range(1, 4):
        print("row", row, "column", column)
```

This creates six coordinate pairs.

## Try it yourself

Change the ranges so the program creates a 2 by 5 grid.

## Guided exercise

Build a 3 by 3 multiplication table. Add text that makes each product easier to read.

## Independent exercise

Create every combination of one colour from:

```python
["red", "blue"]
```

and one size from:

```python
["small", "large"]
```

Use nested loops.

## Debugging exercise

Explain why this prints more values than a beginner might expect:

```python
for a in range(4):
    for b in range(4):
        print("X")
```

## Common mistakes

- Forgetting that the inner loop restarts for every outer value.
- Creating output that is technically correct but difficult to read.
- Using a nested loop when one loop would do the job.

## Short quiz

**1. In a 4 by 3 nested loop, how many inner-body executions occur?**

**Answer:** 12.

**2. When does the inner loop restart?**

**Answer:** Each time the outer loop moves to its next iteration.

**3. Why are nested loops useful for tables?**

**Answer:** One loop can represent rows or categories while the other handles the repeated values inside each row.

## Summary

Nested loops are useful for two-dimensional patterns and combinations. The key is to trace one outer iteration completely before moving to the next.

## Review practice

Write a one-sentence explanation of how a multiplication table maps naturally onto nested loops.

## Optional challenge

Use nested loops to print a small times table with row and column headings.
""",
    },
    {
        "title": "Conditions Inside Loops",
        "content": """
## Lesson 19: Conditions Inside Loops

**Learning objectives**
- Combine `for` loops with `if` statements.
- Use a loop to inspect many values.
- Understand that the loop repeats and the condition decides what happens to each value.

## Explanation

A loop and an `if` statement solve different problems:

- the loop says **"check each value"**
- the `if` says **"do this only when the value matches the rule"**

Example:

```python
for number in range(1, 11):
    if number % 2 == 0:
        print(number)
```

The loop visits numbers 1 through 10. The `if` keeps only the even numbers.

Output:

```text
2
4
6
8
10
```

## Worked example: temperatures

```python
for temperature in [5, 12, 18, 7, 20]:
    if temperature >= 15:
        print("Warm:", temperature)
```

Only temperatures that meet the condition are printed.

## Try it yourself

Change the condition so the program prints temperatures below `10`.

## Guided exercise

Use a loop to print all numbers from `1` to `20` that are greater than `15`.

Then change the condition so it prints numbers that are both greater than `5` and less than `12`.

## Independent exercise

Given five ages, print only ages that are at least `18`.

## Prediction exercise

```python
for score in [45, 72, 88, 51]:
    if score >= 60:
        print(score)
```

Predict the exact output.

## Common mistakes

- Putting the condition outside the loop when it needs to be checked for every value.
- Using `=` instead of `==` when comparing values.
- Forgetting that the `if` block is indented inside the loop.

## Short quiz

**1. What does the loop do?**

**Answer:** It visits each value.

**2. What does the `if` do?**

**Answer:** It decides what to do for the current value based on a condition.

**3. Why is this pattern useful?**

**Answer:** It lets a program process many values while applying a rule to each one.

## Summary

Loops can revisit a whole group of values, while `if` statements let you decide how to handle each current value. This combination is one of the most useful beginner patterns in Python.

## Review practice

Describe in plain English what this pattern means: `for each value → if it matches → do something`.

## Optional challenge

Print numbers from `1` to `50` that are divisible by both `3` and `5`.
""",
    },
    {
        "title": "Counting Matching Values",
        "content": """
## Lesson 20: Counting Matching Values

**Learning objectives**
- Combine a loop, condition, and counter.
- Count how many values meet a rule.
- Explain why the counter changes only when the rule matches.

## Explanation

A useful pattern is:

```python
count = 0

for number in range(1, 11):
    if number % 2 == 0:
        count = count + 1

print(count)
```

The loop checks every number. The `if` identifies even numbers. The counter increases only when a value is even.

The final answer is `5`.

Think of the three parts as three jobs:

- `number` → current value being examined
- `if` → rule for deciding whether it counts
- `count` → remembers how many have matched so far

## Worked example: passing scores

```python
passed = 0

for score in [45, 72, 88, 51, 39]:
    if score >= 50:
        passed = passed + 1

print("Passed:", passed)
```

Three scores are at least 50, so the final count is 3.

## Try it yourself

Count how many numbers from `1` to `20` are divisible by `3`.

## Guided exercise

Start with:

```python
adult_count = 0
```

Then process the ages `[12, 19, 25, 16, 30]` and count ages that are at least `18`.

## Independent exercise

Ask the user for five numbers. Count how many are positive.

## Prediction exercise

How many times does `count` increase?

```python
count = 0
for n in [3, 8, 2, 9, 4]:
    if n > 5:
        count = count + 1
```

## Debugging exercise

Find the bug:

```python
count = 0
for number in range(1, 11):
    if number % 2 == 0:
        count = 1
print(count)
```

The assignment resets the counter instead of increasing it.

## Common mistakes

- Writing `count = 1` instead of `count = count + 1`.
- Increasing the counter for every value instead of only matches.
- Using the wrong condition for what the program is supposed to count.

## Short quiz

**1. Why does the counter start at zero?**

**Answer:** No values have matched yet.

**2. When does the counter increase?**

**Answer:** Only when the `if` condition is true.

**3. What does the final value of the counter represent?**

**Answer:** The number of values that met the condition.

## Summary

The loop + condition + counter pattern is a powerful way to answer questions like "How many values are above 50?" or "How many entries are negative?"

## Review practice

Create a plan to count how many numbers from `1` to `100` are divisible by `10`.

## Optional challenge

Count values that meet two rules, such as being greater than `20` **and** even.
""",
    },
    {
        "title": "Filtering with a Loop",
        "content": """
## Lesson 21: Filtering with a Loop

**Learning objectives**
- Understand filtering as selecting values that meet a rule.
- Build practical filters with loops and `if` statements.
- Reuse Level 2 conditions in a repeated context.

## Explanation

**Filtering** means looking through values and keeping only the ones that meet a condition.

For example:

```python
scores = [45, 81, 66, 92]

for score in scores:
    if score >= 70:
        print(score)
```

The loop visits every score, while the condition decides which ones are shown.

You can filter many kinds of information:

- scores above a threshold
- temperatures below freezing
- ages that meet a rule
- positive numbers
- names that match a simple condition

Do not worry about more advanced tools such as comprehensions yet. The goal here is to understand the logic.

## Worked example: positive numbers

```python
numbers = [5, -2, 9, -1, 4]

for number in numbers:
    if number > 0:
        print(number)
```

Output:

```text
5
9
4
```

## Try it yourself

Filter this set so only temperatures above `15` are printed:

```python
[12, 19, 8, 22, 17]
```

## Guided exercise

Given:

```python
ages = [11, 18, 25, 14, 33]
```

Print only ages that are at least `18`.

## Independent exercise

Given a sequence of scores, print only scores below `50`.

## Choose the rule

Which condition matches each description?

- positive number
- number from 10 through 20
- score below 40
- age at least 18

Write the condition in Python for each.

## Common mistakes

- Printing every value instead of only matching values.
- Using the wrong comparison operator.
- Trying to use advanced collection tools before the basic loop-and-condition pattern is clear.

## Short quiz

**1. What does filtering mean?**

**Answer:** Selecting values that meet a rule.

**2. Why does the loop still need to see every value?**

**Answer:** It must inspect each value to know whether that value matches the rule.

**3. Can filtering use `and` and `or` from Level 2?**

**Answer:** Yes. Conditions inside loops can be combined just like conditions elsewhere.

## Summary

A loop lets you inspect many values, and a condition lets you select the values you care about. This pattern appears throughout real programming.

## Review practice

Take one filtering problem from your own life and describe the rule in plain English before writing Python.

## Optional challenge

Filter numbers from `1` to `50` that are either even or divisible by `5`.
""",
    },
    {
        "title": "Number Counter",
        "content": """
## Lesson 22: Practical Problem — Number Counter

**Learning objectives**
- Translate a simple task into a loop plan.
- Use counters with numeric ranges.
- Practise writing the loop before worrying about shortcuts.

## Problem

Create a program that asks for a starting number and an ending number, then prints every whole number between them when the start is less than or equal to the end.

For example, if the user enters `3` and `7`, the program should print:

```text
3
4
5
6
7
```

## Plan before code

1. Get the starting number.
2. Get the ending number.
3. Set the current number to the start.
4. Repeat while the current number has not passed the end.
5. Print the current number.
6. Move to the next number.

This is a natural `while` loop problem because the stopping condition is directly tied to the current number.

## Guided exercise

Write the program in small pieces. Start with the two `input()` calls and type conversions. Then add the starting value. Then add the loop condition. Finally add the update.

## Independent exercise

Modify the program so that it counts backwards when the starting number is greater than the ending number.

Hint: you will need to decide whether the current value should increase or decrease.

## Debugging exercise

A learner writes:

```python
current = start
while current <= end:
    print(current)
    current = current - 1
```

If `start` is 3 and `end` is 7, explain why the loop cannot reach its stopping point.

## Common mistakes

- Forgetting to convert input to integers.
- Using the wrong update direction.
- Not considering what should happen when start and end are equal.

## Short quiz

**1. What variable represents the value currently being printed?**

**Answer:** The current-number variable, such as `current`.

**2. Why does the loop need an update?**

**Answer:** So the current value changes and the condition can eventually become false.

**3. Is `3` to `7` five numbers or four?**

**Answer:** Five: 3, 4, 5, 6, 7.

## Summary

A practical loop problem starts with a plain-English plan. Identify the changing value, the stopping condition, and the update before writing the full program.

## Review practice

Describe a version of this program that prints only every second number.

## Optional challenge

Add a mode that counts upwards or downwards depending on the values the user enters.
""",
    },
    {
        "title": "Running Total",
        "content": """
## Lesson 23: Practical Problem — Running Total

**Learning objectives**
- Build a running total from repeated input.
- Combine an accumulator with a counter-controlled loop.
- Explain how each input changes the total.

## Problem

Ask the user for five numbers and calculate their total.

A simple plan:

1. Start `total` at `0`.
2. Repeat five times.
3. Read a number.
4. Add it to `total`.
5. Print the final total.

## Worked structure

```python
total = 0
count = 0

while count < 5:
    number = int(input("Enter a number: "))
    total = total + number
    count = count + 1

print("Total:", total)
```

The two changing values have different jobs:

- `count` answers "How many inputs have I processed?"
- `total` answers "What is the combined value so far?"

## Try it yourself

Change the program to accept three numbers.

## Guided exercise

Run a manual trace using inputs `2`, `4`, `6`, `8`, and `10`.

Write down `total` after each entry.

## Independent exercise

Build a five-item shopping total. The user enters each price and the program prints the combined amount.

## Prediction exercise

Predict the final output if the inputs are `10`, `-2`, `4`, `8`, `0`.

## Debugging exercise

What is wrong here?

```python
total = 0
count = 0
while count < 5:
    number = int(input("Enter a number: "))
    total = number
    count = count + 1
```

The program remembers only the most recent number instead of the running total.

## Common mistakes

- Replacing the total instead of adding to it.
- Controlling the loop with the total instead of a separate count.
- Forgetting that `input()` returns text.

## Short quiz

**1. Which variable controls the five repetitions?**

**Answer:** `count`.

**2. Which variable accumulates the numbers?**

**Answer:** `total`.

**3. What does `total = total + number` mean in plain English?**

**Answer:** Take the current total, add the new number, and store the new total.

## Summary

A running total is one of the most important loop patterns. The same idea appears in billing, statistics, scores, and many data-processing tasks.

## Review practice

Rewrite the program using a `for` loop and `range(5)` once you understand the `while` version.

## Optional challenge

Ask how many numbers the user wants to enter, then calculate the total for that many inputs.
""",
    },
    {
        "title": "Average Calculator",
        "content": """
## Lesson 24: Practical Problem — Average Calculator

**Learning objectives**
- Understand the relationship between total, count, and average.
- Build an average calculator using a loop.
- Avoid dividing by zero.

## Explanation

An average is calculated as:

```text
average = total / count
```

That means a program needs two pieces of information:

- the combined total
- the number of values

Example plan:

```python
total = 0
count = 0

while count < 4:
    score = float(input("Enter a score: "))
    total = total + score
    count = count + 1

average = total / count
print("Average:", average)
```

Notice that `count` is not the same thing as `total`.

## Worked example

Scores: `60`, `70`, `80`, `90`

Total: `300`

Count: `4`

Average: `300 / 4 = 75`

## Try it yourself

Change the calculator to collect five scores.

## Guided exercise

Build the program one part at a time. Before writing the division, make sure you can explain what `total` and `count` mean.

## Independent exercise

Create an average calculator for four daily temperatures.

## Debugging exercise

Why is this potentially unsafe?

```python
count = 0
total = 0
average = total / count
```

**Answer:** The program is trying to divide by zero.

## Prediction exercise

What average should be produced for values `10`, `20`, and `30`?

## Common mistakes

- Dividing by the wrong number.
- Forgetting to increment `count`.
- Starting `count` at `1` instead of zero when it represents processed values.
- Using integer conversion when decimal input should be allowed.

## Short quiz

**1. What formula gives the average?**

**Answer:** `total / count`.

**2. Why do we count the values?**

**Answer:** The count is the divisor in the average calculation.

**3. Why can zero count be a problem?**

**Answer:** Division by zero is invalid.

## Summary

Many small data problems are built from the same loop pieces: process a value, update a total, update a count, then use the accumulated information.

## Review practice

Describe how a running total and a count work together to produce an average.

## Optional challenge

Let the user choose how many scores to enter, then calculate the average for that number of scores.
""",
    },
    {
        "title": "Multiplication Tables",
        "content": """
## Lesson 25: Practical Problem — Multiplication Tables

**Learning objectives**
- Use `for` and `range()` together.
- Use the loop variable in a calculation.
- Practise predictable, repeated output.

## Explanation

A multiplication table is a natural `for` loop exercise because the number of repetitions is known.

```python
for multiplier in range(1, 11):
    print(7, "x", multiplier, "=", 7 * multiplier)
```

This prints the seven times table from 1 through 10.

## Worked example

The loop variable `multiplier` changes like this:

`1 → 2 → 3 → ... → 10`

Each iteration calculates a new product.

## Try it yourself

Change the program to print the six times table.

## Guided exercise

Ask the user for a number and convert it to an integer. Then use a `for` loop to print its table from 1 to 10.

## Independent exercise

Create a small table for a number from 1 to 12 instead of 1 to 10.

## Prediction exercise

What is the last line printed by:

```python
for multiplier in range(1, 5):
    print(3 * multiplier)
```

## Common mistakes

- Using `range(1, 10)` when you want to include 10.
- Printing the multiplier instead of calculating the product.
- Forgetting that the loop variable is the current value from `range()`.

## Short quiz

**1. How many iterations does `range(1, 11)` create?**

**Answer:** 10.

**2. Which variable changes each iteration in the example?**

**Answer:** `multiplier`.

**3. Why is `for` a good fit here?**

**Answer:** The table has a known set of multipliers to process.

## Summary

Known counting patterns are an excellent use of `for` and `range()`. The loop variable can directly participate in calculations.

## Review practice

Create a table for `9` and explain why the range stops at `11` rather than `10`.

## Optional challenge

Use nested loops to print the multiplication tables for `2`, `3`, and `4`.
""",
    },
    {
        "title": "Input Validation Loop",
        "content": """
## Lesson 26: Practical Problem — Input Validation Loop

**Learning objectives**
- Reuse Level 2 validation inside a loop.
- Keep asking until the input meets a requirement.
- Explain why `while` is useful when the number of attempts is unknown.

## Explanation

A validation loop is useful when the program must reject invalid input and ask again.

Suppose a user must enter a number from 1 to 10.

```python
number = int(input("Enter a number from 1 to 10: "))

while number < 1 or number > 10:
    print("That number is outside the allowed range.")
    number = int(input("Try again: "))

print("Accepted:", number)
```

The condition says:

- too small **or** too large → invalid
- otherwise → valid

This uses `or`, which you learned in Level 2.

## Execution idea

If the user enters `20`:

- `20 < 1` is false.
- `20 > 10` is true.
- false `or` true becomes true.
- the loop runs and asks again.

If the user enters `7`, both invalid checks are false, so the loop stops.

## Try it yourself

Change the valid range to `1` through `100`.

## Guided exercise

Write a loop that repeatedly asks for an age until the user enters a number from `0` through `120`.

## Independent exercise

Create a program that asks the user to choose a menu number from `1`, `2`, or `3`. Keep asking until the user enters one of those choices.

## Debugging exercise

Find the logic error:

```python
while number < 1 and number > 10:
    number = int(input("Try again: "))
```

A number cannot usually be below 1 and above 10 at the same time. The intended rule needs `or`.

## Common mistakes

- Using `and` when the invalid cases are alternatives.
- Forgetting to ask for new input inside the loop.
- Validating only after accepting the value instead of before continuing.

## Short quiz

**1. Why is `while` useful here?**

**Answer:** The number of attempts is unknown; the loop continues until the condition becomes false.

**2. Why does the invalid condition use `or`?**

**Answer:** A number is invalid when it is too small or too large.

**3. What should happen to the input variable inside the loop?**

**Answer:** It should be updated with a new attempt.

## Summary

Validation loops are one of the first genuinely useful programs you can build. They combine decisions, booleans, input, type conversion, and repetition.

## Review practice

Write an English sentence for the rule: "Keep asking while the user's input is invalid."

## Optional challenge

Add a second validation rule: the number must be even as well as being between 1 and 10.
""",
    },
    {
        "title": "Simple Menu Loop",
        "content": """
## Lesson 27: Practical Problem — Simple Menu Loop

**Learning objectives**
- Build a small menu that repeats.
- Combine `while`, input, and `if`/`elif`/`else`.
- Use `break` for a clear exit option.

## Explanation

Many command-line programs display a menu repeatedly until the user chooses to exit.

Example structure:

```python
while True:
    print("1. Say hello")
    print("2. Say goodbye")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("Hello!")
    elif choice == "2":
        print("Goodbye!")
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Unknown option.")
```

This uses concepts from Level 2 and this level together:

- `while True` keeps the menu available.
- `if` / `elif` chooses the response.
- `break` exits when the user chooses `3`.

## Try it yourself

Replace the menu actions with three simple study actions, such as viewing a tip, practising a number, or leaving the menu.

## Guided exercise

Build a two-option menu plus exit. Keep the actions simple so the loop logic is the main focus.

## Independent exercise

Create a menu for a small unit converter with options for two conversions and an exit option. The actual conversion can use arithmetic you already know.

## Debugging exercise

A program prints the exit message but keeps showing the menu. What is probably missing?

**Answer:** The `break` statement, or another mechanism that changes the loop condition, is missing.

## Prediction exercise

What happens when the user enters `4` in the example above?

## Common mistakes

- Forgetting the `break` on the exit choice.
- Putting `break` on the wrong branch.
- Making the menu action much more complicated than the loop lesson requires.

## Short quiz

**1. Why does the menu use `while True`?**

**Answer:** It keeps showing the menu until an explicit `break` exits the loop.

**2. What handles the different menu choices?**

**Answer:** `if` / `elif` / `else`.

**3. What should happen for an invalid choice?**

**Answer:** The program should provide feedback and continue rather than silently failing.

## Summary

A repeating menu is a practical way to combine the ideas you have learned so far. It is also a useful foundation for small command-line applications.

## Review practice

List the three jobs in this program: repeat, decide, exit.

## Optional challenge

Add a counter that records how many menu actions the user completes before exiting.
""",
    },
    {
        "title": "Loop Review",
        "content": """
## Lesson 28: Level 3 Review

**Learning objectives**
- Review all major loop concepts.
- Mix Level 1, Level 2, and Level 3 skills.
- Diagnose common loop mistakes.

## Core ideas to review

### Why loops exist
Loops reduce repeated code and let a program process many values or continue until a condition changes.

### `while`
A `while` loop repeats while its condition is true.

### `for`
A `for` loop visits values from a sequence one at a time.

### `range()`
`range()` creates counting values. The stop value is excluded.

### Counters
A counter tracks how many events or matching values have occurred.

### Accumulators
An accumulator collects a running value such as a total.

### `break`
Leaves a loop immediately.

### `continue`
Skips the rest of the current iteration and moves to the next one.

### Nested loops
A loop inside another loop creates another level of repetition.

### Loops + decisions
A loop can inspect many values while an `if` statement decides what to do with each one.

## Mixed prediction practice

**1.**

```python
for n in range(2, 7):
    print(n)
```

**2.**

```python
count = 0
for n in range(1, 6):
    if n % 2 == 1:
        count = count + 1
print(count)
```

**3.**

```python
n = 10
while n > 4:
    print(n)
    n = n - 2
```

Predict all output before running the code.

## Debugging practice

Find the problem in each example.

### A
```python
count = 0
while count < 3:
    print(count)
```

### B
```python
total = 0
for n in range(1, 4):
    total = n
print(total)
```

### C
```python
for n in range(1, 6):
    if n == 3:
        break
    print(n)
```

If the goal is to print `1, 2, 4, 5`, what should change?

## Choose the approach

Choose `for` or `while` and explain why:

1. Print 100 numbered labels.
2. Keep asking for a command until the user types `exit`.
3. Visit each value in a known sequence.
4. Validate a number until it is within an allowed range.

## Integrated coding review

Write a program that asks for five numbers and reports:

- the total
- how many numbers were positive
- how many were even

You already know every concept required.

## Short quiz

**1. What is the main purpose of a loop?**

**Answer:** Repetition.

**2. Which loop is often convenient for a known sequence?**

**Answer:** `for`.

**3. Which keyword exits a loop immediately?**

**Answer:** `break`.

**4. Which keyword skips one iteration?**

**Answer:** `continue`.

**5. What is the difference between a counter and an accumulator?**

**Answer:** A counter usually tracks how many events occurred; an accumulator collects a changing total or combined value.

## Summary

You can now use loops to automate repetition, count values, build totals, validate input, filter information, and create small interactive programs.

## Review practice

Without looking at the lessons, explain each term in one sentence: loop, iteration, counter, accumulator, loop variable, nested loop.

## Optional challenge

Solve one problem twice—once with `while` and once with `for`—then compare the readability of both solutions.
""",
    },
    {
        "title": "Mixed Loop Challenge",
        "content": """
## Lesson 29: Mixed Loop Challenge

**Learning objectives**
- Plan a solution before coding.
- Combine loops, conditions, counters, accumulators, and input.
- Debug a multi-step loop problem independently.

## Challenge

Build a small program that asks the user for six numbers and reports:

- the total
- the number of positive values
- the number of negative values
- the number of even values
- the number of values greater than 50

Do not copy a full solution. Build it from smaller pieces.

## Suggested plan

1. Decide how the program will repeat six times.
2. Create a `total` accumulator.
3. Create counters for each condition you need to count.
4. Read and convert one number.
5. Add it to the total.
6. Use `if` statements to update the appropriate counters.
7. After the loop, print the summary.

## Guided checkpoint 1

Before writing code, list the variables you need and explain the job of each one.

## Guided checkpoint 2

Write only the repetition and input first. Test that exactly six values are read.

## Guided checkpoint 3

Add the running total and test it with small numbers.

## Guided checkpoint 4

Add one condition and one counter.

## Independent challenge

Finish the rest without copying a complete example.

## Debugging checklist

If your program gives the wrong result, check:

- Does the loop run exactly six times?
- Is each input converted to a number?
- Does `total` accumulate instead of reset?
- Do condition counters increase only when their conditions are true?
- Are the summary values printed after the loop?

## Short quiz

**1. Which variable should change on every input?**

**Answer:** The repetition counter and the current input value.

**2. Which values should persist across iterations?**

**Answer:** The total and the condition counters.

**3. Why print the final summary after the loop?**

**Answer:** The complete results are not known until all six inputs have been processed.

## Summary

A larger loop problem becomes manageable when you break it into small responsibilities: repetition, current input, accumulated results, conditions, and final output.

## Optional challenge

Let the user choose how many numbers to analyse, but keep the same analysis rules. Make sure your loop still has a clear stopping point.
""",
    },
    {
        "title": "Level 3 Project — Number Analysis Tool",
        "content": """
# Level 3 Project — Number Analysis Tool

**Project goal**

Build a beginner-friendly program that analyses a series of numbers using the loop concepts from Level 3.

The final program should:

- accept multiple values
- keep a running total
- count how many values were entered
- identify positive and negative values
- count values meeting a condition
- calculate an average
- display a final summary

Do not use concepts that belong to later levels. The project is intentionally built from variables, input, conversion, loops, conditions, counters, accumulators, and arithmetic.

## Requirements

Your program must:

1. Ask the user how many numbers they want to enter.
2. Repeatedly ask for each number.
3. Keep a running total.
4. Keep track of how many numbers have been processed.
5. Count positive values.
6. Count negative values.
7. Count even values.
8. Calculate an average when at least one number has been entered.
9. Print a readable summary.

## Milestone 1 — Accept repeated input

Create a loop that asks for the requested number of values.

**Success check:** If the user chooses `5`, the program asks for exactly five numbers.

**Hint:** You already know how to use a counter-controlled loop.

## Milestone 2 — Maintain a count

Track how many values have been processed.

**Success check:** The final count should match the number entered by the user.

## Milestone 3 — Add a running total

Start a total at zero and add each new number to it.

**Success check:** For inputs `2`, `4`, and `6`, the total should be `12`.

## Milestone 4 — Add conditions

For each number, use `if` statements to identify:

- positive numbers
- negative numbers
- even numbers

**Success check:** A test set should produce the correct count for each category.

## Milestone 5 — Calculate an average

Use:

```text
average = total / count
```

Make sure you do not divide by zero.

## Milestone 6 — Display the final summary

Create a clear output section such as:

```text
Numbers entered: 5
Total: 42
Positive: 3
Negative: 2
Even: 4
Average: 8.4
```

The exact formatting is up to you.

## Milestone 7 — Improve the interaction

Add beginner-friendly messages so the user always knows what the program expects.

For example:

```text
How many numbers would you like to analyse?
Enter number 1:
```

Do not add features that require functions, files, classes, or libraries. Those belong to later levels.

## Common mistakes

- Resetting `total` inside the loop.
- Forgetting to increase the processed-count variable.
- Counting zero as positive or negative without deciding what your rule should be.
- Dividing by zero when no values were entered.
- Mixing up the target count with the number of matching values.

## Validation criteria

Your project is ready for review when:

- the requested number of inputs is processed exactly once each
- the total is correct
- the average is correct
- positive/negative/even counts are correct
- the output is readable
- invalid control values are handled sensibly if you choose to add validation
- the program does not rely on future-level concepts

## Test cases

Use these test cases before considering the project finished.

### Test 1
Input:

```text
3
2
4
6
```

Expected:

- count = 3
- total = 12
- positive = 3
- negative = 0
- even = 3
- average = 4

### Test 2
Input:

```text
4
-5
0
5
10
```

Decide how your program should classify zero and document that choice.

### Test 3
Use a mix of positive, negative, odd, and even values.

## Extension challenges

Only attempt these after the core project works:

1. Add a count of values greater than 50.
2. Add a smallest-value tracker using techniques you already know.
3. Add a simple validation loop for the number of inputs.
4. Let the user run another analysis after finishing one report.

## Reflection

After completing the project, answer:

- Which variable was easiest to understand?
- Which loop was easiest to write?
- Where did you make your first bug?
- How did tracing help you debug it?
- Which Level 2 idea did you reuse most often?

## Project summary

This project is your opportunity to combine the entire Level 3 toolkit. The most important skill is not memorising loop syntax. It is learning to break a larger problem into small, understandable steps and then let repetition handle the repeated work.
""",
    },
]


def add_or_update_lesson(
    lessons: List[Dict[str, str]],
    title: str,
    content: str,
) -> Dict[str, str]:
    """Create a lesson if it does not exist, otherwise update its content."""
    for lesson in lessons:
        if lesson["title"] == title:
            lesson["content"] = content
            return lesson

    new_lesson = {"title": title, "content": content}
    lessons.append(new_lesson)
    return new_lesson


def populate_level3(lessons: List[Dict[str, str]]) -> None:
    """Create or update all Level 3 lessons without creating duplicates."""
    for lesson_data in LEVEL3_LESSONS:
        add_or_update_lesson(
            lessons,
            lesson_data["title"],
            lesson_data["content"],
        )


if __name__ == "__main__":
    existing_lessons: List[Dict[str, str]] = []
    populate_level3(existing_lessons)
    print(f"Loaded {len(existing_lessons)} Level 3 lessons.")
    for lesson in existing_lessons:
        print(f"Title: {lesson['title']}")
        print(f"Content length: {len(lesson['content'])} characters")
        print()
