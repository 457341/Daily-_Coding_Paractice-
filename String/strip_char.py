# Write a Python program to strip a set of characters from a string

# Original String:                                                                                              
# The quick brown fox jumps over the lazy dog.                                                                  
# After stripping a,e,i,o,u                                                                                     
# Th qck brwn fx jmps vr th lzy dg
def strip_char(string):
    string = list(string)
    # print("original: ",string,end='')
    for i in range(len(string)):
        print(i)
        if string[i] == 'a' or string[i] == 'e' or string[i] == 'i' or  string[i] == 'o' or  string[i] == 'o':
            string[i] = ''
    string = ''.join(string)
    print("After stripping: ",string)

string = "The quick brown fox jumps over the lazy dog."
strip_char(string)


