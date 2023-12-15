def Vigenere_Decyription(word, key):
    Decy_word = " "

    while(len(word) > len(key)):
        key += key
        if (len(key) > len(word)):
            key = key [:-(len(key) - len(word))]

    for x in range(0, len(word)):
        word_ASCII = ord(word[x]) - 65
        key_ASCII = ord(key[x]) - 65

        number = (word_ASCII - key_ASCII) % 26
        Decy_word += chr(number+65)
        
    print (f"\n\n\nDecyripted word is {Decy_word}")
        

def Vigenere():
    word = input("\n\n\nPlease type the word you want to decyript \n\n===> ")
    key = input("\n\n\nPlease type the key word  \n\n===> ")

    Vigenere_Decyription(word.upper(), key.upper())



def Main():
    menu = "1)Vigenere \n2)Exit\n"
    User_input = "0"
    while (User_input != "2"):
        print(f"\n\n\n\n{menu}")
        User_input = input ("Please select menu number: ")

        if (User_input == "1"):
            Vigenere() 


Main()