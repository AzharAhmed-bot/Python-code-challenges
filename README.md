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


# 7. Correct Article
Write a program that determines the correct article("a" or "an") to precede a given word.

Example 
apple --> an apple
banana --> a banana
cat --> a cat
elephant --> an elephant

Actual test
unicorn --> a unicorn
hour --> an hour
html-page --> an html-page 
university --> a university

# 8. Biggest of the Smallest of the Biggest of the...
You are given an array arr of integers, and a string str that contains steps to extract an array out of arr.

str contains a chained combination of "the biggest" and "the smallest" inside it. An example would be "the biggest of the smallest of the biggest of the biggest". At each step in str, extract either the biggest or the smallest values from arr, and continue to the next step with the extracted values.

Example:
Given the array [1,2,3,4,5,6,7,8,9] and the string "the biggest of the smallest", you should return [3,4]. The first step in str is "the smallest", and the smallest of the array is [1,2,3,4]. You then proceed to the next step in str with this extracted array, [1,2,3,4]. The next step in str is "the biggest", and the biggest of [1,2,3,4] is [3,4].

Specifications:
If you are given an empty array, return an empty array.{-}

If you are given an empty string, return the original array.{-}

If at any step the length of the array becomes one, return the array.{-}

If at any step the length of the array is odd, then "the biggest" part takes the middle element. For example, when taking "the biggest" of [1,2,3], your extracted array should be [2,3] and when taking "the smallest" your array should be [1].{-}

The integers inside the array that you return need to be in the same order that they were in the original array. "the biggest" and "the smallest" are not referring to the start and end of the array, but to the size of the integers inside the array. When taking "the biggest" of [5,3,9,1,2,4], your code should return [5,9,4], as they are the biggest integers in the array.

There may be duplicate integers inside the array, in which case the duplicate integers that come first are prioritized. When taking "the biggest" of [4,5,4,4], your code should return [4,5], not [5,4].

More Examples:
Given the array [23,567,33,13,67,43,678,9,1,56] and the string "the smallest of the biggest", you should return [43,56] because "the biggest" is [567,67,43,678,56], and "the smallest" of that is [43,56].

Given the array [4] and the string "the biggest of the smallest", you should return [4] because the array has only one element.

The "biggest of the smallest of the smallest" of [7,8,9] is [7]: [7,8,9]->[7]->[7].


# 9 Sum the nums,sum the sums and sum the muns up to the sum



## License
This repository is licensed under the MIT License.