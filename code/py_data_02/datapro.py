text = '<div><h2>오늘의 요리를 소개합니다</h2></div>'

# [시작위치 : 끝나는 위치+1]
print(text[0:10])   
print(text[9:15])
print(text[9:])
print(text[:15])

print(text.index('오'))
start = text.index('오')
print(text[start:])

# '오늘의 요리를 소개'를 찾아서 출력하기
start = text.index('오')  
end = text.index('합') 
print(text[start:end]) 

print(text.find('요리')) 

start = text.find('요리')  
end = text.find('합니다')  
print(text[start:end])  

rst = text.find('요리')  
if rst == -1: 
    print('단어 위치를 찾지 못함')