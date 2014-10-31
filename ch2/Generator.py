
"""
alphabet_cycle: generate the infinite sequence a1, b1... z1, a2, b2... z2...
"""

def infinite_alphabet_number():
    alphabet=[ chr(i) for i in range(ord('a'),ord('z')+1)]
    #alphabet='a'
    number=0
    while True:
        number=number+1
        for c in alphabet:
            yield c+str(number)


if __name__=="__main__":
    for i in infinite_alphabet_number():
        print(i)
    
