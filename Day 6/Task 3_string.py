# ===============================
# TASK 3: STRING PROBLEMS
# ===============================

def string_tasks():

    text = input("Enter a string: ")

    # 1. Reverse String
    print("Reversed:", text[::-1])


    # 2. Check Palindrome
    if text == text[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")


    # 3. Count Characters
    count = {}
    for ch in text:
        count[ch] = count.get(ch, 0) + 1
    print("Character Count:", count)


    # 4. Count Vowels and Consonants
    vowels = "aeiou"
    v = 0
    c = 0

    for ch in text.lower():
        if ch.isalpha():
            if ch in vowels:
                v += 1
            else:
                c += 1

    print("Vowels:", v)
    print("Consonants:", c)