import secrets

def dicenumber():
    diceout = ""
    for i in range(5):  # 5 dice rolls
        rolloutput = str(secrets.randbelow(6))    # add result of dice roll to variable
        while rolloutput == "0": # dice cannot roll zero
            rolloutput = str(secrets.randbelow(6))
        diceout += rolloutput
    return diceout

def diceware(x):
    wordlist = open('diceware.wordlist.asc', 'r') # http://world.std.com/~reinhold/diceware.wordlist.asc
    for line in wordlist:
        if line.startswith(x):
            wordlist.close()
            return line

for i in range(5): print(diceware(dicenumber())),    # increase number for longer passphrases
