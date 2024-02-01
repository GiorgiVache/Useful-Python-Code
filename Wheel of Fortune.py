import random
VOWEL_COST = 250
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'

# Write the WOFPlayer class definition (part A) here
class WOFPlayer:

    def __init__(self, name):
        self.name = name
        self.prizeMoney = 0
        self.prizes = []

    def addMoney(self, amt):
        self.prizeMoney += amt

    def goBankrupt(self):
        self.prizeMoney = 0

    def addPrize(self, prize):
        self.prizes.append(prize)

    def __str__(self):
        return "{} (${})".format(self.name, self.prizeMoney)

# Write the WOFHumanPlayer class definition (part B) here
class WOFHumanPlayer(WOFPlayer):

    def getMove(self, category, obscuredPhrase, guessed):
        self.category = category
        self.obscuredPhrase = obscuredPhrase
        self.guessed = guessed
        return input("{} has ${}\n\nCategory: {}\nPhrase:  {}\nGuessed: {}\n\nGuess a letter, phrase, or type 'exit' "
                     "or 'pass':".format(self.name, self.prizeMoney, category, obscuredPhrase, guessed))

# Write the WOFComputerPlayer class definition (part C) here
class WOFComputerPlayer(WOFPlayer):

    SORTED_FREQUENCIES = "ZQXJKVBPYGFWMUCLDRHSNIOATE"

    def __init__(self, name, difficulty):
        WOFPlayer.__init__(self, name)
        self.difficulty = difficulty

    def smartCoinFlip(self):
        random_number = random.randint(1, 10)
        if random_number > self.difficulty:
            return False
        if random_number <= self.difficulty:
            return True

    def getPossibleLetters(self, guessed):
        self.guessed = guessed
        list_of_letters = []
        list_of_letters.append(letter for letter in LETTERS if letter not in self.guessed)
        if self.prizeMoney < VOWEL_COST:
            VOWELS_1 = VOWELS.split()
            list_of_letters.remove(vowel for vowel in VOWELS_1 if vowel in list_of_letters)
        return list_of_letters

    def getMove(self, category, obscuredPhrase, guessed):
        self.category = category
        self.obscurePhrase = obscuredPhrase
        self.guessed = guessed

        if self.getPossibleLetters(guessed) == []:
            return ('pass')

        if self.smartCoinFlip() == True:
            return self.SORTED_FREQUENCIES[-1]

        if self.smartCoinFlip() == False:
            return random.choice(self.SORTED_FREQUENCIES)