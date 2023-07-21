'''
다음 문자열의 불필요한 문자나 숫자를 제거하는 문제입니다

text_org = '**[세일]** 치와와 강아지 건식 소프트 5종 10000원 ....'
#결과와 같이 문자열 처리하시오
#결과 [치와와,강아지,건식,소프트]
'''
text_org = '**[세일]** 치와와 강아지 건식 소프트 5종 10000원 ....'
start = text_org.find('치')
end = text_org.find('5')
wawa = text_org[start:end]
wawa2 = wawa.strip()
wawa3 = wawa2.replace(' ',',')
print('[',wawa3,']')
    
    
    