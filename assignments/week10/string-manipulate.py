"""

Build a Text Analysis Tool that performs the following operations on user input text:
Core Features:

1. Character Analysis:
    - Count total characters (with and without spaces)
    - Count vowels and consonants separately
    - Find most frequent character

2. Word Analysis:
    - Count total words
    - Find longest and shortest words
    - Count words starting with vowels vs consonants

3. String Transformations:
    - Convert to title case, upper case, lower case
    - Create acronym from first letter of each word
    - Reverse the entire string and each word individually
    
Example Result

Enter text: The Quick Brown Fox Jumps Over The Lazy Dog

=== TEXT ANALYSIS REPORT ===
Character Analysis:
- Total characters: 43 (with spaces), 35 (without spaces)
- Vowels: 12 (e, u, i, o, o, u, o, e, e, a, o)
- Consonants: 23
- Most frequent: 'o' (appears 4 times)

Word Analysis:
- Total words: 9
- Longest word: "Quick" (5 letters)
- Shortest word: "The" (3 letters)
- Words starting with vowels: 1 ("Over")
- Words starting with consonants: 8

Transformations:
- Title Case: The Quick Brown Fox Jumps Over The Lazy Dog
- Upper Case: THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG
- Lower Case: the quick brown fox jumps over the lazy dog
- Acronym: TQBFJOTLD
- Reversed Text: goD yzaL ehT revO spmuJ xoF nworB kciuQ ehT
- Words Reversed: ehT kciuQ nworB xoF spmuJ revO ehT yzaL goD

USE: len(), split(), count(), upper(), lower(), title(), slicing operations

"""

string = "The Quick Brown Fox jumps Over The laz" 

print("=== TEXT ANALYSIS REPORT ===")
print("Character Analysis:")
print("- Total Character: %d (with spaces), %d (without spaces)" %)
(len(string), len(string)-string.count(" ")))

strLower = string.lower() 
vowels = string.cont("a")+ strLower.count("e") + strLower.count
("i") + strLower.count("o")+ strLower.count("u")
vowelsStr =""
for char in strLower:
    if char in ['a','e''i','o','u']:
        vowelsStr += char+ ","

print("- Vowels: %d (%5)" % (vowels, vowelsStr))
print("- Consonants: %d" % (len(string)-string.count(" ")-vowels))

word = string.split()
print("Word Analysis:")
print("- Total wrods:" , len(word))

