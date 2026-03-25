def Character_counting(s):
    vowels="aeiouAEIOU"
    vowel_count=0
    consonants_count=0
    digits_count=0
    spaces_count=0
    special_character_count=0

    for ch in s:
        if ch in vowels:
            vowel_count+=1
        elif ch.isalpha():
            consonants_count+=1
        elif ch.isdigit():
            digits_count+=1
        elif ch == " ":
            spaces_count+=1
        elif not ch.isalnum():
            special_character_count+=1   

    return vowel_count,consonants_count,digits_count,spaces_count,special_character_count


def reverse_words(s):   
    temp=""
    new=""

    for ch in s:
        if ch!=" ":
            temp+=ch
        else:
            rev=""
            for c in temp:
                rev=c+rev
            new+=rev
            new+=" "
            temp=""

    rev=""
    for h in temp:
        rev=h+rev

    new+=rev
    return new


def remove_functions(s):

    vowels="aeiouAEIOU"
    spaces=" "
    spaces_removed=""
    vowels_removed=""

    for ch in s:
        if ch not in spaces:
            spaces_removed+=ch

    for ch in s:
        if ch not in vowels:
            vowels_removed+=ch

    return spaces_removed,vowels_removed


def count_words(s):

    if s == "":
        word_count=0
    else:
        word_count=1

    for ch in s:
        if ch == " ":
            word_count+=1

    return word_count


def main():

    s=input("Enter the string: ")

    vowel_count,consonants_count,digits_count,spaces_count,special_character_count = Character_counting(s)
    new = reverse_words(s)
    spaces_removed,vowels_removed = remove_functions(s)
    word_count = count_words(s)

    while True:

        print("\n-----------------------------------")
        print("COUNTING CHARACTERS IN STRING --> 1")
        print("REVERSE WORDS IN STRING ------> 2")
        print("REMOVE CHARACTERS ------------> 3")
        print("COUNT WORDS ------------------> 4")
        print("EXIT --------------------------> 5")
        print("-----------------------------------")

        choice=int(input("Enter your choice (1-5): "))


        if choice == 1:

            print("\nCount vowels -- 1")
            print("Count Consonants -- 2")
            print("Count Digits -- 3")
            print("Count Spaces -- 4")
            print("Count Special Characters -- 5")
            print("Exit -- 6")

            x=int(input("Choose (1-6): "))

            if x == 1:
                print("Vowels :",vowel_count)

            elif x == 2:
                print("Consonants :",consonants_count)

            elif x == 3:
                print("Digits :",digits_count)

            elif x == 4:
                print("Spaces :",spaces_count)

            elif x == 5:
                print("Special Characters :",special_character_count)

            elif x == 6:
                continue

        elif choice == 2:

            print("Reversed words :",new)


        elif choice == 3:

            print("\nREMOVE OPTIONS")
            print("REMOVE SPACES ---> 1")
            print("REMOVE VOWELS ---> 2")
            print("EXIT -----------> 3")

            a=int(input("Enter option (1-3): "))

            if a == 1:
                print("Spaces removed :",spaces_removed)

            elif a == 2:
                print("Vowels removed :",vowels_removed)

            elif a == 3:
                continue

        elif choice == 4:

            print("Number of words :",word_count)


        elif choice == 5:

            print("Exiting program...")
            break


main()
