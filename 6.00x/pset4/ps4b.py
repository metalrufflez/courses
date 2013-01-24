from ps4a import *
import time

#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    returns: string or None
    """
    scoreMax = 0
    bestWord = None

    for word in wordList:
        if not isValidWord(word,hand,wordList):
            continue
        wordScore = getWordScore(word,len(word))
        if wordScore > scoreMax:
            scoreMax = wordScore
            bestWord = word
                
    return bestWord

#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    """
    handLen = calculateHandlen(hand)
    totalScore = 0

    while handLen > 0:
        print 'Current Hand:',
        displayHand(hand)
        word=compChooseWord(hand,wordList)
        if word == None:
            print "Total Score: %d." % totalScore
            return totalScore

        wordScore = getWordScore(word,calculateHandlen(hand))
        totalScore += wordScore
        print '"%s" earned %d points. Total: %d points.\n' % ( word, wordScore, totalScore )
        hand = updateHand(hand,word)
        handLen = calculateHandlen(hand)

    print 'Total Score: %d.' % totalScore
    return totalScore
    
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """

    hand = {}
    while True:
        print
        choice = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        print
        if choice not in 'nre':
            print "Invalid Command."
            continue
        
        if choice == 'e':
            break

        if choice == 'r':
            if len(hand) == 0:
                print "You have not played a hand yet. Please play a new hand first!"
                continue

        user = None
        while user == None:
            user = raw_input("Enter u for to play or c for the computer: ")
            print

            if user not in 'uc':
                print "Invalid Command."
                print
                user = None
                continue
        
        if choice == 'n':
            hand = dealHand(HAND_SIZE) 

        if user == 'u':
            playHand(hand.copy(),wordList,HAND_SIZE)
        else:
            compPlayHand(hand.copy(),wordList)
        
def playGame2(wordList):
    while True:
        print
        choice = raw_input("Enter n to deal a new hand or e to end game: ")
        print
        if choice not in 'ne':
            print "Invalid Command."
            continue
        elif choice == 'e':
            break

        hand = dealHand(HAND_SIZE) 
        
        print 'HUMANITY TURN\n'
        userScore = playHand(hand,wordList,HAND_SIZE)
        print '\nSKYNET TURN\n'
        computerScore = compPlayHand(hand,wordList)

        print '\n-----------------'
        print "Skynet scored %d" % computerScore
        print "Humans scored %d" % userScore
        print '-----------------\n'

        if computerScore > userScore:
            print "Skynet won by %d points." % (computerScore - userScore)
            print "Humanity is DOOMED"
        elif userScore > computerScore:
            print "Humans won by %d points." % (userScore - computerScore)
            print "Hooray! We defeated those stupid machines!"
        else:
            print "It's remarkably a tie!"
            print "It's like the green ending in Mass Effect 3!"
        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame2(wordList)
