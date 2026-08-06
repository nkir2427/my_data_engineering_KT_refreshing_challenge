# Python Knowledge Refresh – Numbers and Arithmetic Operators

## Overview

This lesson introduces Python's numeric data types and arithmetic operators. Through simple examples, I explored how Python performs mathematical calculations, follows operator precedence, and evaluates arithmetic expressions. I also applied these concepts to solve a simple real-world problem involving travel distance and travel time.

---

## Learning Objectives

After completing this exercise, I was able to:

- Perform basic arithmetic operations.
- Understand different arithmetic operators in Python.
- Use variables in mathematical expressions.
- Apply operator precedence (PEMDAS/BODMAS).
- Perform calculations using real-world examples.

---

## Topics Covered

- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`*`)
- Division (`/`)
- Modulus (`%`)
- Exponent (`**`)
- Operator precedence
- Floating-point numbers
- Variables in calculations

---

## Examples

### Basic Arithmetic

```python
print(12 + 4)
print(3 - 1)
print(3 / 4)
print(4 * 5)
```

**Output**

```
16
2
0.75
20
```

---

### Modulus Operator

```python
11 % 5
```

**Output**

```
1
```

The modulus operator returns the remainder after division.

---

### Exponent Operator

```python
3 ** 2
2 ** 4
```

**Output**

```
9
16
```

The exponent operator raises a number to a given power.

---

### Real-World Example – Travel Distance
Problem: You are driving from Newyork to Baltimore and then going to Pittsburgh. You want to know how much total travel distance you will be travelling.

```python
newyork_baltimore_distance = 75
baltimore_pittsburgh_distance = 117

total_distance = (
    newyork_baltimore_distance +
    baltimore_pittsburgh_distance
)

print(total_distance)
```

**Output**

```
192
```

---

### Travel Time Calculation  
 Car speed is 65 mph and now we have to calculate hours we need to travel this distance

```python
car_velocity = 65

time = total_distance / car_velocity

print(time)
```

**Output**

```
2.953846153846154
```

This calculates the travel time assuming a constant speed of **65 miles per hour**.

---

### Operator Precedence

```python
10 + 2 * 3
```

Output

```
16
```

```python
(10 + 2) * 3
```

Output

```
36
```

Parentheses change the order in which expressions are evaluated.

---

### Floating-Point Precision

```python
6 - 5.7
```

Output

```
0.2999999999999998
```

Python stores decimal numbers using **floating-point representation**, which can produce very small rounding differences. This behavior is normal in most programming languages.

---

## Screenshot

The following screenshot shows the interactive Python IDLE session used during this lesson.

![Python Numbers Practice](Images/Numbers.jpg)

---

## Key Takeaways

- Python supports integer and floating-point arithmetic.
- Arithmetic operators follow standard mathematical precedence.
- Parentheses can be used to control evaluation order.
- Variables make calculations more readable and reusable.
- Floating-point arithmetic may introduce tiny precision errors due to binary representation.
