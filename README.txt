Project 2 454
Project was developed by:
  Jacques Sarraffe
  Evan Hatton
  Chris Lapp

This is our project 2, which accepts an integer input n and calculates the number of strings of length n that are "weakly divisible" by 7

To run: ensure that automata-lib is installed on the machine by running the command "pip install automata-lib"
Then "python3 main.py" should be able to run the program

Most of this project was completed in group meetings, so these contributions might not be 100% accurate

Building the NFA was the most complicated part of this project, and this was done between the three of us during zoom meetings

Jacques contribution:
    Jacque extensively read the documentation of automata-lib so that our group could properly utilize the library
    Jacque also worked on ensuring that the NFA was accurate relating to the project and formatting our NFA from JFLAP
    into the code.
    Jacque also introduced us all to google colab, which make the code part of this project a lot more accessible, and helped
    debug calcRelate


Evan's contribution:
    Evan built a very useful transition calculator which IS included in the main.py, just after all the project required functions are called.
    It is not called anywhere in our program, but the function was use in the construction of makeNFA so that we could hard code in our
    NFA. This saved us hours of time translating our NFA to a format that automata-lib accepted.
    Evan also helped debug calcRelate. Our logic was correct, just the initial state had its position moved during DFA creation
    which caused alot of headaches debugging, Evan caught this error and provided a fix.

Chris's contributions:
    Chris worked on the logic in calcRelate along with providing the initial framework for the function.
    Chris also worked to develop the initial values of curr, which was the first (base case) row in our transition table
