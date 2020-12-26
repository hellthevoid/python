import re

string='''<td align="left" class="data-display-field" valign="top">Jessica Zecevic<br/>Feldbergstr. 39a<br/>61440 Oberursel (Taunus) Hessen<br/>Deutschland<br/></td>'''

pattern=re.compile(r"([a-zA-Z0-9 )(.]+)<br/>")

matches=pattern.finditer(string)

for match in matches:
    print(match.group(1))