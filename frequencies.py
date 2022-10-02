"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    if len(items) == 0: 
        print('no items')

    else:

        for i in range(0,len(items)):

            if frequencies.get(items[i], 'None') == 'None': 
                frequencies[ items[i] ] = 1
            else:
                temp = frequencies.get(items[i])
                temp+=1
                frequencies[ items[i] ] = temp

    return frequencies

def main():
    print(frequencies(['0', 4,4,'4','d','d','e',0,'a','d','4'])) 


main()