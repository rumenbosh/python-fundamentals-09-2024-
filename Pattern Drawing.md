# Task: Python Pattern Drawing

Create twelve different patterns using Python's printing capabilities.

![0*Phr3VozbQ1KSOISM](https://github.com/user-attachments/assets/af1b03c3-7637-473c-80e2-1b36e60eae10)


### Pattern 1: Right-angled Triangle

Develop a Python script that generates a right-angled triangle pattern. The script should prompt the user to specify the number of rows. Here's a sample output for a user input of 5:

```
*
**
***
****
*****
```
num_rows = int(input())
for i in range(1, num_rows + 1):
    print('*' * i)
```

```

### Pattern 2: Square with Hollow Center
 
Craft a Python program that produces a square pattern with a hollow center. The program should take the size of the square as input from the user. Here's an example output for a user input of 5:

```
*****
*   *
*   *
*   *
*****
```
num_row = int(input())
print('*' * num_row)
for i in range(1, num_row - 1):
    print('*' + ' ' * (num_row - 2) + '*')
print('*' * num_row)
```
### Pattern 3: Diamond

Write a Python script that displays a diamond pattern based on the number of rows (height) specified by the user. For instance, if the user enters 5, the output should resemble the following:

```
  *
 ***
*****
 ***
  *
```
```
num_rows = int(input())  #If even number is the input, it will still print add stars only
stars = 1
if num_rows % 2 == 0:
    space = int((num_rows / 2) - 1)
else:
    space = int(num_rows // 2)
while True:
    print(' ' * space, stars * '*')
    if space == 0:
        break
    space -= 1
    stars += 2
while True:
    space += 1
    stars -= 2
    print(' ' * space, stars * '*')
    if stars <= 1:
        break
```
### Pattern 4: Left-angled Triangle

Design a Python code snippet to print a left-angled triangle pattern. The user should provide the number of rows. For instance, if the user inputs 4, the output should be:

```
****
***
**
*
```
num_rows = int(input())
for i in range(num_rows, 0, -1):
    print('*' * i)
```
### Pattern 5: Hollow Square

Implement a Python program that prints a square pattern with a hollow center, where the user specifies the size of the square. For example, if the user inputs 6, the output should be:

```
******
*    *
*    *
*    *
*    *
******
```
```
num_row = int(input())
print('*' * num_row)
for i in range(1, num_row - 1):
    print('*' + ' ' * (num_row - 2) + '*')
print('*' * num_row)
```
### Pattern 6: Pyramid

Create a Python script that prints a pyramid pattern based on the user-input number of rows. For example, if the user inputs 4, the output should be:

```
   *
  ***
 *****
*******
```
```
num_rows = int(input())
stars = 1
space = num_rows - 1

while True:
    print(' ' * space, stars * '*')
    if space == 0:
        break
    space -= 1
    stars += 2

```

### Pattern 7: Right-angled Triangle (Numbers)

Write a Python program that prints a right-angled triangle using numbers. The user will provide the number of rows. For example, if the user inputs 5, the output should look like this:

```
1
12
123
1234
12345
```
n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()
```

### Pattern 8: Inverted Pyramid

Develop a Python script that prints an inverted pyramid pattern based on the number of rows provided by the user. For instance, if the user inputs 5, the output should be:

```
*********
 *******
  *****
   ***
    *
```
```
num_rows = int(input())
space = 0
stars = (num_rows * 2) - 1
while True:
    print(' ' * space, stars * '*')
    if stars <= 1:
        break
    space += 1
    stars -= 2

```

### Pattern 9: Diamond (Numbers)

Write a Python program that prints a diamond shape pattern with numbers. The user provides the number of rows for the top half of the diamond. If the user inputs 4, the output should look like this:

```
   1
  121
 12321
1234321
 12321
  121
   1
```

### Pattern 10: Mirrored Right-angled Triangle

Craft a Python script to print a mirrored right-angled triangle pattern. The user provides the number of rows. For example, if the user inputs 5, the output should resemble:

```
    *
   **
  ***
 ****
*****
```
num_rows = int(input())
for i in range(1, num_rows + 1):
    print(' ' * (num_rows - i) + '*' * i)
```

### Pattern 11: Alternating Star-Dash Square

Write a Python script that prints a square pattern where stars and dashes alternate in each row. The size of the square should be provided by the user. Here's an example for user input of 5:

```
*-*-*
-*-*-
*-*-*
-*-*-
*-*-*
```

### Pattern 12: Hourglass Shape

Design a Python program to display an hourglass shape. The user should specify the number of rows. If the user inputs 4, the output should be:

```
*-*-*
-*-*-
*-*-*
-*-*-
*-*-*
```


➡ Instructions:

1. Utilize nested loops to control the row and column structure of each pattern.
2. Use the print function to output patterns. For spacing, consider using either the space character (" ") or tabs ("\t").
3. Prompt the user to enter the necessary parameters for each pattern.
