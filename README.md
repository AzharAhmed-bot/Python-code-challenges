## Introduction 
Welcome to the code challenge repository! This repo is a collection of various coding challenges in python across different genres including Algorithms, Math problems in order to refine programming skills. 

## Guidelines 
Here are some steps you can follow when designing a solution for your challenges:
1. Understand the problem: This involves gathering information, identifying the problem's requirements, and breaking down the problem into smaller, more manageable parts.
2. Design a solution: Once the problem is understood, the next step is to design a solution. This involves selecting an appropriate algorithm, data structures, and programming language to solve the problem.The solution should be optimized for time and space complexity and be easy to maintain and modify.
3. Write code: After designing a solution, the programmer needs to write code to implement the solution. This involves translating the design into programming instructions, ensuring that the code is correct, efficient, and easy to read and understand.
4. Test the solution: The next step is to test the solution to ensure that it works as expected. This involves running the program with different inputs and checking whether it produces the desired outputs. Testing helps identify and fix bugs and ensures that the solution meets the problem requirements.
5. Refine and optimize: After testing, the programmer may need to refine and optimize the solution further to improve its performance, scalability, or maintainability. This may involve redesigning the solution, changing the algorithms, or using different data structures.
6. Document the solution: Finally, the programmer needs to document the solution, including comments in the code and creating user manuals and technical documentation. 

This steps will help you figure out the solution and can be kept  for future reference.

## Set up
- Navigate to Challenges directory
```
cd challenges
```
- Run the virtual environment
```
pipenv shell
```


## Problem questions.
# 1.Rot-13
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.
Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation". Visit this [file](https://github.com/AzharAhmed-bot/Python-code-challenges/blob/main/Challenges/rot13.py) for code
To run the code:

- Run the code:
```
python3 rot13.py
```

# 2. Clock in the mirror
Peter can see a clock in the mirror from the place he sits in the office. When he saw the clock shows 12:22. He knows that the time is 11:38. in the same manner:

05:25 --> 06:35

01:50 --> 10:10

11:58 --> 12:02

12:01 --> 11:59

Please complete the function WhatIsTheTime(timeInMirror), where timeInMirror is the mirrored time (what Peter sees) as string.

Return the real time as a string.

Consider hours to be between 1 <= hour < 13.

So there is no 00:20, instead it is 12:20.

There is no 13:20, instead it is 01:20.
Visit this [file](https://github.com/AzharAhmed-bot/Python-code-challenges/blob/main/Challenges/clockInTheMirror.py) for code.

```
python3 clockInTheMirror.py
```

# 3. The latest clock
Write a function which receives 4 digits and returns the latest time of day that can be built with those digits.

The time should be in HH:MM format.

Examples:

digits: 1, 9, 8, 3 => result: "19:38"
digits: 9, 1, 2, 5 => result: "21:59" ("19:25" is also a valid time, but 21:59 is later)

Visit this [file](https://github.com/AzharAhmed-bot/Python-code-challenges/blob/main/Challenges/latestClock.py) for code.

```
python3 latestClock.py
```

# 4. RGB TO HEX conversion 

The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

Visit this [file](https://github.com/AzharAhmed-bot/Python-code-challenges/blob/main/Challenges/rgbtohex.py) for code.

```
python3 rgbtohex.py
```
# 5. Fibonnacci Product
You are given a positive integer n greater than one.

How many ways are there to represent it as a product of some Fibonacci numbers greater than one?

(Fibonacci sequence: 1, 1, 2, 3, 5, 8...).

For example, there are two ways for n = 40:

2 * 2 * 2 * 5
5 * 8
But you can't represent n = 7 in an aforementioned way.

Note that n may be really big (up to 10^36). Good luck!

Visit this [file](https://github.com/AzharAhmed-bot/Python-code-challenges/blob/main/Challenges/FibonacciProduct.py) for code.

```
python3 FibonacciProduct.py
```
# 6. Three Details Simple fun
Dudka has n details. He must keep exactly 3 of them.

To do this, he performs the following operations until he has only 3 details left:

He numbers them.
He keeps those with either odd or even numbers and throws the others away.
Dudka wants to know how many ways there are to get exactly 3 details. Your task is to help him calculate it.

Example
For n = 6, the output should be 2.

Dudka has 6 details, numbered 1 2 3 4 5 6. 
He can keep either details with numbers 1, 3, 5, 
or with numbers 2, 4, 6. 
Both options leave him with 3 details, 
so the answer is 2.

Visit this [file](https://github.com/AzharAhmed-bot/Python-code-challenges/blob/main/Challenges/ThreeDetails.py) for code.



## License
This repository is licensed under the MIT License.