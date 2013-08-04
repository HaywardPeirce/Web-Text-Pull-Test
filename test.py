import urllib
 
from stripogram import html2text
 
myurl = urllib.urlopen("http://tuxworld.wordpress.com")
 
html_string = myurl.read()
 
text = html2text( html_string )
 
print text
