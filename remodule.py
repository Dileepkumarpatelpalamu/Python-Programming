import re
"""---------------------Regular expression-----------------------------------------
 There are many functions
 1. search()- search() method takes the pattern and text to scan, and returns a Match object when the pattern is
    found. If the pattern is not found, search() returns None.
 synatx -----
 re.search(patern,string) this function return match object
 match object have to function 
    start() start method return starting index of matching patern
        synatx------------
        re.search(patern,string).start()
    end() end method return ending index of matching patern
        synatx------------
        re.search(patern,string).end()
 2. compile()- module-level functions for working with regular expressions as text strings, but it is usually more 
 efficient to compile the expressions your program uses frequently. The compile() function converts an expression 
 string into a Regex Object.
 synatx of compile() method--------
    re.compile(patern).search(string)
 3. findall() this method is use for find all patern in string or file or document and paragraph and return type is 
 list object
 syntax -------------
    re.findall(patern string, text string)
finditer() returns an iterator that produces Match instances instead of the strings returned
by findall().
syntax ----------------------
    re.finditer(patern,text)
Repetition
There are five ways to express repetition in a pattern. A pattern followed by the
metacharacter * is repeated zero or more times (allowing a pattern to repeat zero times
means it does not need to appear at all to match). Replace the * with + and the pattern
must appear at least once. Using ?means the pattern appears zero or one time. For a
specific number of occurrences, use {m} after the pattern, where m is replaced with the
number of times the pattern should repeat. And finally, to allow a variable but limited
number of repetitions, use {m,n} where m is the minimum number of repetitions and n is
the maximum. Leaving out n ({m,}) means the value appears at least m times, with no
maximum.
Metacharacter in re modules.
1 '.'- this matches any character except a newline. If the DOTALL flag has been specified, this matches any character
 including a newline
2 '^' (Caret.) Matches the start of the string, and in MULTILINE mode also matches immediately after each newline.
3. '$' Matches the end of the string or just before the newline at the end of the string
4. '*' match 0 or more repetitions of the preceding RE, as many repetitions as are possible. ab* will match ‘a’, 
‘ab’, or ‘a’ followed by any number of ‘b’s.
5. '+' match 1 or more repetitions of the preceding RE. ab+ will match ‘a’ followed by any non-zero number of 
‘b’s; it will not match just ‘a’.
6. '?' match followed by zero or one character example [ab?] a followed by zero or one character of b
7. '{}' 'ab{3}'- a followed by three b compulsary
"""
patterns ='ab'
text = 'abaaabbbbaaaccababab'
# for pattern in patterns:
#     print('Looking for "%s" in "%s" ->' % (pattern, text))
#     if re.search(pattern, text):
#         print('found a match!')
#         print("Start index : ",re.search(pattern,text).start())
#         print("End index : ",re.search(pattern,text).end()) 
#     else:
#         print('no match')
#example of compile method
# data=re.compile(patterns).search(text)
# print(data.start(),data.end())
# example of find all function
# match = re.findall(patterns,text)
# print(match)
# Example for finditer() method
# for match in re.finditer(patterns,text):
#     print(f"found : {text[match.start():match.end()]} Start index :{match.start()} End Index : {match.end()}")
def test_patterns(text, patterns=[]):
    for pattern in patterns:
        print ('Matching "%s"' % pattern)
    for match in re.finditer(pattern, text):
        s = match.start()
        e = match.end()
        print ('%2d : %2d = "%s"' % (s, e-1, text[s:e]))
    return
if __name__ == '__main__':
    test_patterns(text,['ab*?'])

