def cipher(s):
    return ''.join([str(219 - ord(i)) if i.isalpha() and i.islower() else i for i in s])

print(cipher("I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."))
# "I 120108102111119109'103 121118111114118101118 103115122103 I 120108102111119 12212010310212211111198 102109119118105104103122109119 100115122103 I 100122104 105118122119114109116 : 103115118 107115118109108110118109122111 107108100118105 108117 103115118 115102110122109 110114109119 ."