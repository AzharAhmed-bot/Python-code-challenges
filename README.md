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

Example <br>
apple --> an apple<br>
banana --> a banana<br>
cat --> a cat<br>
elephant --> an elephant<br>

Actual test<br>
unicorn --> a unicorn<br>
hour --> an hour<br>
html-page --> an html-page <br>
university --> a university<br>

Vist this [file](https://github.com/AzharAhmed-bot/Python-code-challenges/blob/main/Challenges/correctArticle.py) for the code.🙌

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

More Examples:<br>
Given the array [23,567,33,13,67,43,678,9,1,56] and the string "the smallest of the biggest", you should return [43,56] because "the biggest" is [567,67,43,678,56], and "the smallest" of that is [43,56].

Given the array [4] and the string "the biggest of the smallest", you should return [4] because the array has only one element.

The "biggest of the smallest of the smallest" of [7,8,9] is [7]: [7,8,9]->[7]->[7].<br>

Visit this [file](https://github.com/AzharAhmed-bot/Python-code-challenges/blob/main/Challenges/biggestOfSmallest.js) for the code



# 9 Sum the nums,sum the sums and sum the muns up to the sum
Let's define two functions:

```bash
S(N) — sum of all positive numbers not more than N
S(N) = 1 + 2 + 3 + ... + N
```

```bash
Z(N) — sum of all S(i), where 1 <= i <= N
Z(N) = S(1) + S(2) + S(3) + ... + S(N)
```
You will be given an integer N as input; your task is to return the value of S(Z(N)).

For example, let N = 3:
```bash
Z(3n) = 1n + 3n + 6n = 10n
S(Z(3n)) = S(10n) = 55n
The input range is 1 <= N <= 10^9 and there are 80 ( 40 in LC ) test cases, of which most are random.
```

Visit this [file](https://github.com/AzharAhmed-bot/Python-code-challenges/blob/main/Challenges/sumofsums.js) for the code.📈

# 10 Max and Min values in array
- Description:
In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

- Examples
```bash
Input: "1 2 3 4 5"   =>  Output: "5 1"
Input: "1 2 -3 4 5"  =>  Output: "5 -3"
Input: "1 9 3 4 -5"  =>  Output: "9 -5"
```
- Notes
    - All numbers are valid Int32, no need to validate them.
    - There will always be at least one number in the input string.
    - Output string must be two numbers separated by a single space, and highest number is first.


## 11 SECRET AGENT

Hello, fellow Warrior!<br>
Or, should I say, Secret Agent?<br>
This is your chance to prove that you are true spy material, and not just some amateur with a tuxedo!<br>
The first step on your way to the double 0 is also the most important: Learn how to craft and decode a secret password to communicate safely with other agents.



In the first, you will create a function that takes a string as argument and returns a jumbled string, with the following rules and restrictions:

- The input string MUST be a 9 characters long word (made only of lowercase letters from "a" to "z" of the English alphabet). If the argument doesn't meet this requirement (or no argument at all is passed to the function), it must return "BANG!" (there are no second chances in the spy world!)
- The string must be divided into 3 equal parts of 3 characters each:
    - The first and third letter will be converted to the corresponding number, according to the English alphabet (ex. a = 1, b = 2, c = 3 ... z = 26, etc.)
    - The fourth, fifth, and sixth letter will be reversed.
    - The seventh, eighth, and ninth letter will be substituted with the letter that follows them in the English alphabet (z will be substituted with a).
- Finally, the returned string must be in the following order: Part 2, Part 3, and Part 1
Examples:


```bash
encrypt("jamesbond"); // should return: "bsepoe10a13"
encrypt("I'll kill you, 007!"); // should return "BANG!"
```

In the second part of the Kata, you will create another function that takes a jumbled password and acts as follows:

- It decrypts the password argument, reversing the rules and following the same restrictions set in part 1 of the kata.
- It compares the decrypted string to an array of secret passcodes (you can't see the passcodes, but you can test if yours is present in the array). Watch out: Not all of the secret passcodes are valid strings!
- It must return:
    - "Nice to meet you, fellow Agent!" if the passcode is both valid and contained in the array, or;
    - "BANG!" if the passcode is not in the array, or if the string is not valid.

Example:
```bash
decrypt("bsepoe10a13"); //should return: "Nice to meet you, fellow Agent!"
decrypt("How are you still alive, 007??"); //should return "BANG!"
```

Visit this [file](https://github.com/AzharAhmed-bot/Python-code-challenges/blob/main/Challenges/secretAgent.js) for the code🥐

## 12 Move Ten
Move every letter in the provided string forward 10 letters through the alphabet.<br>
If it goes past 'z', start again at 'a'.<br>

Input will be a string with length > 0.<br>

Visit this [file](https://github.com/AzharAhmed-bot/Python-code-challenges/blob/main/Challenges/java/src/App.java) for the code🥓

## 13 No zeros for heroes
Description:
Numbers ending with zeros are boring.

They might be fun in your world, but not here.

Get rid of them. Only the ending ones.
```bash
1450   -> 145
960000 -> 96
1050   -> 105
-1050  -> -105
0      -> 0
```
Note: Zero should be left as it is.
## 14 Wordify an Integer
Description:
Turn a given number (an integer > 0, < 1000) into the equivalent English words. For the purposes of this kata, no hyphen is needed in numbers 21-99.
Examples:
```bash
1   --> "one"
12  --> "twelve"
17  --> "seventeen"
56  --> "fifty six"
90  --> "ninety"
326 --> "three hundred twenty six"
```
Based on "Speech module" mission from Checkio.

## 15 Sum of sums
Write a function that takes an array/list of numbers and returns a number such that

Explanation total([1,2,3,4,5]) => 48
```bash
1+2=3--\ 3+5 =>     8 \
2+3=5--/ \            ==  8+12=>20\     
          ==>5+7=> 12 / \           20+28 => 48
3+4=7--\ /            == 12+16=>28/
4+5=9--/ 7+9 =>     16  /
```
```bash
if total([1,2,3]) => 8 then

first+second => 3 \
                   then 3+5 => 8
second+third => 5 /
```

Examples<br>
```bash
total([-1,-1,-1]) => -4
total([1,2,3,4])  => 20
```
Note: each array/list will have at least an element and all elements will be valid numbers.
## 16 Real length of String
Description:<br>
In languages that use UTF-16 encoding for strings (JavaScript, JVM languages like Java, .NET languages like C#...), if the code point of a character is larger than 0xFFFF, it will be treated as two code units.

For example:
```bash
The code point of the emoji 🙉 (U+1F649, Hear-No-Evil Monkey) is 0x1F649.

'🙉'.length; // 2
```
Write a function that returns the real length of a string.
```bash
"abcd"   --> 4
"🙉"     --> 1
"😸🦌🚀" --> 3
```

## 17 Mirror Mirror on the wall
You get a list of integers, and you have to write a function mirror that returns the "mirror" (or symmetric) version of this list: i.e. the middle element is the greatest, then the next greatest on both sides, then the next greatest, and so on...<br>

More info<br>
The list will always consist of integers in range -1000..1000 and will vary in size between 0 and 10000. Your function should not mutate the input array, and this will be tested (where applicable). Notice that the returned list will always be of odd size, since there will always be a definitive middle element.

```bash
Examples
[]  -->  []
[1]  -->  [1]
[2, 1]  -->  [1, 2, 1]
[1, 3, 2]  -->  [1, 2, 3, 2, 1]
[-8, 42, 18, 0, -16]  -->  [-16, -8, 0, 18, 42, 18, 0, -8, -16]
[-3, 15, 8, -1, 7, -1] --> [-3, -1, -1, 7, 8, 15, 8, 7, -1, -1, -3]
[-5, 10, 8, 10, 2, -3, 10] --> [-5, -3, 2, 8, 10, 10, 10, 10, 10, 8, 2, -3, -5]
```

## 18 Biggest Square In a circle
Description:
Determine the area of the largest square that can fit inside a circle with radius r.

## Special score for words
Description:<br>
We define a special score for a word (ssw) as follows. We multiply the corresponding ASCII decimal code for each letter of the word by its respective frequency of this letter in the word, collect these addens and sum them up.

For example, for the word investigation, we have the respective ASCII codes and frequencies for each letter:
```bash
Letter    ASCII decimal code        Letter Frequency (in "investigation")
 i             105                            3
 n             110                            2
 t             116                            2
 a              97                            1
 e             101                            1
 g             103                            1
 o             111                            1
 s             115                            1
 v             118                            1
```
So the ssw for this word will be:<br>
```bash
ssw = 105 * 3 + 110 * 2 + 116 * 2 + 97 * 1 + 101 * 1 + 103 * 1 + 111 * 1 + 115 * 1 + 118 * 1 = 1412
```
Task <br>
Complete the function that receives two arguments,

number of letters, num_let <br>
maximum special score max_ssw for the word <br>
You were also provided with a list of 2000 words of the Oxford Dictionary Of English (U.K. English), named WORD_LIST for python, $word_list for ruby, wordList for JavaScript.<br>

The function should output a word from the database of 2000 words that has the highest possible ssw of the given number of letters but smaller or equal to the given max_ssw. <br>

If we have more than one word with the same number of letters, num_let, and the same special score, ssw, choose the largest word in lexicographical order. <br>

If there are no words in the database that satisfies the given num_let and max_ssw, return None in Python, nil in Ruby, null in JavaScript. <br>

Example<br>
Let's see some cases:
```bash
num_let = 8
max_ssw = 888
# There are three words with 8 letters and with ssw == 888
#   "question", "security" and "southern"
# The list of these words sorted with its respective ssw is 
#   [(888, "question"), (888, "security"), (888, "southern")],
# "southern" should be chosen

num_let = 9
max_ssw = 500
# The word of 9 letters with minimum ssw is "candidate" with ssw = 925
# There are no 9 letter words with less than or equal to 500 ssw
# Should return None in Python, nil in Ruby, null in JavaScript
We may have the case when the all the words of certain number of letters are below max_ssw.

num_let = 7
max_ssw = 1412
# Should return "support"
```
"support" is the word of 7 letters with highest ssw (797)

## 19 Pete, The baker
Description:<br>
Pete likes to bake some cakes. He has some recipes and ingredients. Unfortunately he is not good in maths. Can you help him to find out, how many cakes he could bake considering his recipes?<br>

Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object) and returns the maximum number of cakes Pete can bake (integer). For simplicity there are no units for the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). Ingredients that are not present in the objects, can be considered as 0.<br>

Examples:
```bash
# must return 2
cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})
# must return 0
cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000})
```

# 20. Data Mining
Your task is to build a model1 which can predict y-coordinate.
You can pass tests if predicted y-coordinates are inside error margin.


You will receive train set which should be used to build a model.
After you build a model tests will call function predict and pass x to it.
Error is going to be calculated with RMSE.

# 21. Numerical palindrome
Description:
A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward. Examples of numerical <br>
palindromes are: 2332, 110011, 54322345 <br>

For a given number num, write a function which returns an array of all the numerical palindromes contained within each number. The array should be sorted in ascending order and any duplicates should be removed.<br>

In this kata, single digit numbers and numbers which start or end with zeros (such as 010 and 00) are NOT considered valid numerical palindromes. <br>

If num contains no valid palindromes, return "No palindromes found". Otherwise, return "Not valid" if the input is not an integer or is less than 0.<br>
```bash
Examples
1221      -->  [22, 1221]
34322122  -->  [22, 212, 343, 22122]
1001331   -->  [33, 1001, 1331]
1294      -->  "No palindromes found"
"1221"    -->  "Not valid"
```
# 22. Linear Regression of Y on X
The function that you have to write accepts two list/array, x
y, representing the coordinates of the points to regress (so that, for example, the first point has coordinates(x[0],y[0]))


Your function should return a tuple (in Python) or an array (any other language) of two elements: a (intercept) and b (slope) in this order.

```bash
regressionLine([25,30,35,40,45,50], [78,70,65,58,48,42]) == (114.381, -1.4457)

regressionLine([56,42,72,36,63,47,55,49,38,42,68,60], [147,125,160,118,149,128,150,145,115,140,152,155]) == (80.7777, 1.138)
```

# 23. Matrix multiplication
Write a function that accepts two square (NxN) matrices (two dimensional arrays), and returns the product of the two. Only square matrices will be given.<br>

How to multiply two square matrices:<br>

We are given two matrices, A and B, of size 2x2 (note: tests are not limited to 2x2). Matrix C, the solution, will be equal to the product of A and B. To fill in cell [0][0] of matrix C, you need to compute: A[0][0] * B[0][0] + A[0][1] * B[1][0].

More general: To fill in cell [n][m] of matrix C, you need to first multiply the elements in the nth row of matrix A by the elements in the mth column of matrix B, then take the sum of all those products. This will give you the value for cell [m][n] in matrix C.

## License
This repository is licensed under the MIT License.