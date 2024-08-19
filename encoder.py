def encoder(message, key):
    # Initialize the new message as an empty list
    result = []
    
    # Comb through each letter in the message
    for char in message:
        found = False

        # Comb through each pair in the key
        for original, replacement in key:

            # If the function finds the swappable char
            if char == original:

                # Replace the char
                result.append(replacement)
                found = True
                break

        # If not found translate unexpected char into '?'
        if not found:
            result.append('?')
    
    # Join list into string for the coded message
    return ''.join(result)

# Example usage:
code1 = [['a', 'n'],['b', 'o'],['c', 'p'],['d', 'q'], ['e', 'r'],['f', 's'],['g', 't'],['h', 'u'], 
         ['i', 'v'],['j', 'w'],['k', 'x'],['l', 'y'], ['m', 'z'],['n', 'a'],['o', 'b'],['p', 'c'], 
         ['q', 'd'],['r', 'e'],['s', 'f'],['t', 'g'], ['u', 'h'],['v', 'i'],['w', 'j'],['x', 'k'],
         ['y', 'l'],['z', 'm'],[' ', ' ']]

code2 = [['1','!'], ['2','@'],['3','#'],['4','$'],['5','%'],
         ['6','^'], ['7','&'],['8','*'],['9','('],['0',')']]

test1 = "the quick brown fox jumped over the lazy dog"  # Expected output: gur dhvpx oebja sbk whzcrq bire gur ynml qbt
test2 = "i do not like green eggs and ham"              # Expected output: v qb abg yvxr terra rttf naq unz
test3 = "we can't stop!"                                # Expected ouput: jr pna?g fgbc?
test4 = ""                                              # Expected output: (blank)
test5 = "9876543210"                                    # Expected ouput: (*&^%$#@!)


"""
Tester functions used to verify output (ignore)

# Running the provided test cases
print(encoder(test1, code1))  
print(encoder(test2, code1)) 
x = encoder(test2, code1)
print(x)                   

y = encoder(x, code1)
print(y)                                                # Separate test case, expected output: i do not like green eggs and ham

print(encoder(test3, code1)) 
print(encoder(test4, code1)) 
print(encoder(test5, code2)) 

"""
