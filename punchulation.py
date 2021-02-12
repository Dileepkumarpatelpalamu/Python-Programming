punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
my_str = "{{}}[[]]community------ of volunteer&&&&&''''''''''' editors using a wiki-based editing system. It is one of the 15 most popular websites as ranked by Alexa, as of January 2021[3] and The Economist newspaper placed it as the 13th-most-visited place on the web.[4] Featuring no advertisements, it is hosted by the Wikimedia Foundation, an American non-profit organization funded primarily through donations."
no_punct = ""
for char in my_str:
   if char not in punctuations:
       no_punct = no_punct + char
print(no_punct)