# this fuction purpose is to count the number of vowels in a string it takes in a word  as parameter
#it uses the sum build in function in python to sum each character by on for each charater in the string if the character is a vowel

def count_vowels(word):
    vowels = "aeiou"
    return sum(1 for ch in word if ch in vowels)

# this function main is to checks is the since of two varaibles are equall it takes in two parameters

def is_balanced(v1,v2):
    return v1 == v2

#here is where the main function is defined
def main():
    print("This challenge checks if both halves of a word have equal vowels. ")

    s = input("Enter the word: ").lower()
    l = len(s)
    print("The length of the word is", l)

    mid = l // 2
    first_half = s[:mid]
    second_half = s[mid:]

    v1 = count_vowels(first_half)
    v2 = count_vowels(second_half)

    print("The number of vowels in the first half is", v1)
    print("The number of vowels in the second half is", v2)

    if is_balanced(v1 ,v2):
        print("Balanced: both halves have equal vowel.")
    else:
        print("Not balanced: both halves donot have equal vowel values count")    

main()        




