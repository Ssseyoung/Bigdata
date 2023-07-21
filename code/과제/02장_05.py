'''
다음 html 코드에서 <option>안에 텍스트만 추출하여 출력하시오
'''

html = '''
<label for="dog-names">Choose a dog name:</label>
<select name="dog-names" id="dog-names">
<option value="rigatoni">Rigatoni</option>
<option value="dave">Dave</option>
<option value="pumpernickel">Pumpernickel</option>
<option value="reeses">Reeses</option>
</select>
'''

from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'html.parser')

option = [option.text for option in soup.select('option')]

print(option)