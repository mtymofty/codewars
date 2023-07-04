using System;
using System.Linq;

// 1. Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.
string boolToWord(bool word)
{
    return word ? "Yes" : "No";
}

// 2. Write a function that takes an array of words and smashes them together into a sentence and returns the sentence.
string Smash(string[] words)
{
    return string.Join(" ", words);
}

/* 
3. Write a function that takes an array of numbers and returns the sum of the numbers. 
The numbers can be negative or non-integer. If the array does not contain any numbers then you should return 0.
*/
double SumArray(double[] array) => array.Sum();

/*
4. Make a function that will return a greeting statement that uses an input; 
your program should return, "Hello, <name> how are you doing today?".
*/
string Greet(string name) => String.Format("Hello, {0} how are you doing today?", name);
string Greet2(string name) => $"Hello, {name} how are you doing today?";
