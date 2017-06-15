def hangman(secretWord):
    print 'Welcome to the game Hangman!'
    print 'I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.'
    
    bullets = 8
    lettersGuessed = []
    print '-------------'
    
    while bullets > 0:
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print 'Congratulations, you won!'
            break
    
        print 'You have ' + str(bullets) + ' guesses left.'
        print 'Available Letters: ' + str(getAvailableLetters(lettersGuessed))
        letter1 = raw_input('Please guess a letter: ')
        
        letter = letter1.lower()
               
        if letter in secretWord:
            if letter in lettersGuessed:
                lettersGuessed += letter
                print "Oops! You've already guessed that letter: " + str(getGuessedWord(secretWord, lettersGuessed))
            else:
                lettersGuessed += letter
                print 'Good guess: ' + str(getGuessedWord(secretWord, lettersGuessed))
        else:
            if letter in lettersGuessed:
                lettersGuessed += letter
                print "Oops! You've already guessed that letter: " + str(getGuessedWord(secretWord, lettersGuessed))
            else:
                lettersGuessed += letter
                print 'Oops! That letter is not in my word: ' + str(getGuessedWord(secretWord, lettersGuessed))
                bullets -= 1
        print '-------------'
            
    if bullets == 0:
        print 'Sorry, you ran out of guesses. The word was ' + str(secretWord) + '.' 

def isWordGuessed(secretWord, lettersGuessed):
    
    def recrCheck(secretWord, lettersGuessed):
        if len(lettersGuessed) == 0:
            return False
        else:
            if lettersGuessed[0] in secretWord:
                del lettersGuessed[0]
                return True + recrCheck(secretWord, lettersGuessed)
            else:
                del lettersGuessed[0]
                return False + recrCheck(secretWord, lettersGuessed)
    
    if len(secretWord) == 0:
        return False
    else:
        if recrCheck(secretWord, lettersGuessed) == len(secretWord):
            return True
        else:
            return False

def getGuessedWord(secretWord, lettersGuessed):
    newSecretWord = secretWord
    newLettersGuessed = lettersGuessed
    out = []
    res = ''
    
    for char in newSecretWord:
        out += ['_ ',]
    
    def find(secretWord, lettersGuessed,out):
        if len(lettersGuessed) == 0:
            counter = 0
        else:
            counter = 0
            for char in secretWord:
                if char == lettersGuessed[0]:
                    out[counter] = lettersGuessed[0] + ' '
                    counter += 1
                else:
                    counter += 1
            del lettersGuessed[0]
            return find(secretWord, lettersGuessed, out)
    
    find(newSecretWord, newLettersGuessed,out)
    
    
    def printa(out,res):
        for i in range(0,len(out)):
            res += str(out[i])
        
        return res
        
    return printa(out,res)

def getAvailableLetters(lettersGuessed):
    
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    for i in range(0,len(lettersGuessed)):
        for j in range(0,len(alphabet)):
            if lettersGuessed[i] == alphabet[j]:
                del alphabet[j]
                break
            else:
                continue
                
    res = ''
    for i in range(0,len(alphabet)):
        res += alphabet[i]
    
    return res