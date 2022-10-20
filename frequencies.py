"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    if len(items) == 0: 
        print('no items')

    else:

        for i in range(0,len(items)):
            item = str(items[i])
            if frequencies.get(item, 'None') == 'None':
                frequencies[ item ] = 1
            else:
                temp = frequencies.get(item)
                temp+=1
                frequencies[ item ] = temp

    return frequencies

def main():
    print(frequencies(['0', 4,4,'4','d','d','e',0,'a','d','4'])) 


main()