import secrets

def dicenumber():
    diceout = ""
    for i in range(5):    # 5 dice rolls as each wordlist number is identified by 5 numbers
        rolloutput = str(secrets.randbelow(6))    # add result of dice roll to variable
        while rolloutput == "0": # dice cannot roll zero
            rolloutput = str(secrets.randbelow(6))
        diceout += rolloutput
    return diceout

def diceware(x):
    wordlist = open('diceware.wordlist.asc', 'r')
    for line in wordlist:
        if line.startswith(x):
            wordlist.close()
            line = line.strip(x)    # remove wordlist numbering
            return line.strip()    # remove tabs and newlines

passphrase = []
for i in range(6): passphrase.append(diceware(dicenumber()))    # increase range number for longer passphrases
print('-'.join(passphrase))    # prints final passphrase
