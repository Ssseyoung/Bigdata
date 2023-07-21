'''
샘플 문자열에서
text = 'In Brazil, the; Superior Electoral* Court bars former~ president'

# 특수문자들은 제거하고 단어를 분리해서 총 몇개가 있는지 출력하시오
'''

text = 'In Brazil, the; Superior Electoral* Court bars former~ president'
    
text2 = text.replace('*', ' ')
text3 = text2.replace('~', ' ')
text4 = text3.split()
print(len(text4))
