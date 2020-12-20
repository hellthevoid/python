
# import requests
# import bs4 #beautifulsoup is for parsing html
# import webbrowser

# path='http://nostarch.com'

# webbrowser.open(path) #open a page

# res=requests.get('https://automatetheboringstuff.com/files/rj.txt')#get a file
# res.raise_for_status()#did the download work?

#  playFile = open('RomeoAndJuliet.txt', 'wb') #binary code is necessary#write the txt form website into a new txt on pc

#  for chunk in res.iter_content(100000):
#         playFile.write(chunk)

#  playFile.close()


# ######

# res=requests.get('http://nostarch.com')
# res.raise_for_status()

# soup_obj=bs4.BeautifulSoup(res.text)

###################

import bs4
import os
import send2trash
import re

#os.chdir("C:\\Users\\sonyx\\Desktop\\Lena")

exampleFile = open("Bestellungen verwalten - Amazon (2).htm")
soup = bs4.BeautifulSoup(exampleFile.read())


adress_list=[]

for adress in soup.find_all("td", class_="data-display-field"):
    adress_list.append(adress)

#print(adress_list)
# del adress_list[0:2]

# adress_list=adress_list[::5]

new_adress_list=[]
adress_text=[]
# for adress in adress_list:
#     for content in adress.contents:
#         try:
#             adress_text+=content.strip()+"\n"
#         except Exception:
#             pass
#     new_adress_list.append(adress_text)
   
# adress_list=new_adress_list[:]

# umlaute_dict = {
#     '\xc3\xa4': 'ae',  # U+00E4	   \xc3\xa4
#     '\xc3\xb6': 'oe',  # U+00F6	   \xc3\xb6
#     '\xc3\xbc': 'ue',  # U+00FC	   \xc3\xbc
#     '\xc3\x84': 'Ae',  # U+00C4	   \xc3\x84
#     '\xc3\x96': 'Oe',  # U+00D6	   \xc3\x96
#     '\xc3\x9c': 'Ue',  # U+00DC	   \xc3\x9c
#     '\xc3\x9f': 'ss',  # U+00DF	   \xc3\x9f
# }


# def replace_german_umlaute(unicode_string):

#     utf8_string = unicode_string.encode('utf-8')

#     try:
#         for k in umlaute_dict.keys():
#             utf8_string = utf8_string.replace(k, umlaute_dict[k])
#     except Exception:
#         pass
#     return utf8_string.decode()

# import htmlentitydefs
# def unescape(text):
#     def fixup(m):
#         text = m.group(0)
#         if text[:2] == "&#":
#             # character reference
#             try:
#                 if text[:3] == "&#x":
#                     return unichr(int(text[3:-1], 16))
#                 else:
#                     return unichr(int(text[2:-1]))
#             except ValueError:
#                 pass
#         else:
#             # named entity
#             try:
#                 text = unichr(htmlentitydefs.name2codepoint[text[1:-1]])
#             except KeyError:
#                 pass
#         return text # leave as is
#     return re.sub("&#?\w+;", fixup, text)


import re
print(adress_list)
for adress in adress_list:
    adress=unescape(adress)
    pattern=re.compile(r"([a-zA-Z0-9) (.]+)<br/>")
    
    matches=pattern.finditer(str(adress))

    for match in matches:
        adress_text+=match.group(1)+"\n"
        print(match.group(1))
    new_adress_list.append(adress_text)


adress_list=new_adress_list[:]


################### WORD
from docx import Document

curr_table=0

#delete old etiketten file
if os.path.isfile(".\\etiketten.docx"):
   send2trash.send2trash("etiketten.docx")

#load word document
document = Document("template.docx") #word doc not dynamic - template

#set to correct table
def set_current_table(document,curr_table):
    table_obj=document.tables[curr_table]
    return table_obj

def fill_table_in_word(table_obj, adress_list,current_adress_index):
    word_columns=[0,2,4]
    count_of_adresses=len(adress_list)  # count non-duplicate adresses
    for word_row in range(9):
        for word_column in word_columns:
            if current_adress_index==count_of_adresses:
                return current_adress_index
            current_table_cell=table_obj.cell(word_row,word_column)
            current_table_cell.text=adress_list[current_adress_index]
            current_adress_index+=1
    return current_adress_index

#set to first table

table_obj=set_current_table(document,curr_table)
current_adress_index=0
count_of_adresses=len(adress_list)



#go through all deliveries
while current_adress_index<count_of_adresses:
    current_adress_index=fill_table_in_word(table_obj, adress_list,current_adress_index) #enter values for a whole table, return the newst excel row

    curr_table+=1
    table_obj=set_current_table(document,curr_table) #go to next table because prior table is full

#save document
document.save("etiketten.docx")

print('SUCCESSFULL (most likely)')
print("Das macht dann 12.000 Mark")

msg=input("Press Enter")


# "<class 'list'>"
# len(elems)

# type(elems[0])
# "<class 'bs4.element.Tag'>"
# elems[0].getText()
# 'Al Sweigart'
# str(elems[0])
# '<span id="author">Al Sweigart</span>'
# elems[0].attrs
# {'id': 'author'}


# td class="data-display-field" valign="top" align="left">
# 	Jessica Zecevic<br>Feldbergstr. 39a<br>61440&nbsp;Oberursel (Taunus)&nbsp;Hessen<br>Deutschland<br>
#     </td><