alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
"k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
"u", "v", "w", "x", "y", "z", " "]

def get_data():
    word = input("What you want encryp? ")
    word = word.lower()
    num = int(input("Enter a number between 1 - 26: "))
    if num > 26 or num == 0:
    # while num > 26 or num == 0:
        num = int(input("Enter CORRECT number between 1 - 26: "))
    data = (word, num)
    return(data)

def encrypt(word, num):
    new_word = ""
    for x in word:
        y = alphabet.index(x)
        y = y + num
        if y > 26:
            y = y - 27
        new_char = alphabet[y]
        new_word = new_word + new_char
    print(new_word)
    print("---")

def decrypt(word, num):
    new_word = ""
    for x in word:
        y = alphabet.index(x)
        y = y - num
        if y < 0:
            y = y + 27
        new_char = alphabet[y]
        new_word = new_word + new_char
    print(new_word)
    print("---")

def main():
    again = True
    while again == True:
        print("1. - Encrypt")
        print("2. - Decrypt")
        print("3. - Quit")
        selection = int(input("Enter your selection: "))
        if selection == 1:
            (word, num) = get_data()
            encrypt(word, num)
        elif selection == 2:
            (word, num) = get_data()
            decrypt(word, num)
        elif selection == 3:
            again = False
        else:
            print("Incorrect selection")

main()