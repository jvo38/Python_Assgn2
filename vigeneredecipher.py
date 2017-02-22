def getCodeWord():
    code = input("Please enter the code word for decoding: ") 
    return code

def runDecoding(codedWord, cryptedText):
   totalLetter = 26
   upperAscii_Start = 65 
   upperAscii_End = 90
   lowerAscii_Start = 97
   lowerAscii_End = 122
   decodedWord = ''
   j = 0
   for i in range(0, len(cryptedText), 1): # range 0 to length of cryptedText, with step of 1 (ex. 0,1,2,3,4)
       if cryptedText[i].isupper(): # checks if the letter is UPPER CASE 
           newUpper = (ord(cryptedText[i]) + totalLetter) - (ord(codedWord[j%len(codedWord)]) - lowerAscii_Start)
           if (newUpper > upperAscii_End) or (newUpper < upperAscii_Start):
               newUpper -= totalLetter
           #adds all uppercase letters into a string
           #also converts back from ascii to alpha
           decodedWord += chr(newUpper)
           j+=1 #spaces and other special characters dont count as an index for codedWord
       elif cryptedText[i].islower():
           newLower = (ord(cryptedText[i]) + totalLetter) - (ord(codedWord[j%len(codedWord)]) - lowerAscii_Start)
           if (newLower > lowerAscii_End) or (newLower < lowerAscii_Start):
               newLower -= totalLetter
           decodedWord += chr(newLower)
           j+=1
       else:
           #basically skips/add all spaces/special characters without doing anything to it.
           otherNew = cryptedText[i]
           decodedWord += otherNew
   return decodedWord

def main():
    codeWord = getCodeWord()
    ciph_message = open('message_cipher.txt', 'r') #read text file
    clear_message = open('message_cipher_clear.txt', 'w') #writes into the text file
    for l in ciph_message: #loops through every line
        l = runDecoding(codeWord, l) #decodes every line
        print(l, end = "", file = clear_message) # prints the decoded line into "rfh" text file
    ciph_message.close()
    clear_message.close()
    print("*****Decoding Complete!*****")
main()
