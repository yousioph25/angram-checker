# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


# def find_anagram(word, anagram):
    # [assignment] Add your code here
first_string = input("Provide the first string: ")
second_string = input("Provide the second string: ") 

if sorted(first_string) == sorted(second_string):
    print("True")
else:
    print("False") 

#return True

