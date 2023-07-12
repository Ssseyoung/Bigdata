# 다음 문자열의 불필요한 문자나 숫자를 제거

from itertools import count


text_org = '**[세일]** 치와와 강아지 건식 소프트 5종 10000원 ....'
# 결과 [치와와,강아지,건식,소프트]
start = text_org.find('치')
end = text_org.find('5')
wawa = text_org[start:end]
wawa2 = wawa.strip()
wawa3 = wawa2.replace(' ',',')
print('[',wawa3,']')



# 샘플 문자
text = 'In Brazil, the; Superior Electoral* Court bars former~ president'

# 특수 문자들을 제거하고 단어를 분리해서 총 몇개가 있는지?
a = text.replace('*', ' ')
a2 = a.replace('~', ' ')
a3 = a2.split()
a3.count()