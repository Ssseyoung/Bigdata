import json     # 파이썬 표준모듈
import tensorflow as tf
from keras.preprocessing.text import Tokenizer

with open('data/sarcasm.json', 'r') as f:  # 'data/sarcasm.json' 파일을 읽기 모드로 열고 f에 할당
    datas = json.load(f)  # f에서 데이터를 읽어와서 datas에 할당

# print(data)     # headline, is_sarcast, link

sentences = []
labels = []
links = []

for data in datas:  # datas 리스트의 각 요소에 대해 반복문 실행
    sentences.append(data['headline'])  # data 딕셔너리의 'headline' 키에 해당하는 값을 sentences 리스트에 추가한다.  
    labels.append(data['is_sarcastic'])  # data 딕셔너리의 'is_sarcastic' 키에 해당하는 값을 labels 리스트에 추가
    links.append(data['article_link'])  # data 딕셔너리의 'article_link' 키에 해당하는 값을 links 리스트에 추가
    
# text 문장에 총단어수
myToken = Tokenizer(oov_token='<OOV>')  # Tokenizer 객체 생성
myToken.fit_on_texts(sentences)  # 문장들을 토큰화하여 토큰 인덱스를 생성
word = myToken.word_index  # 단어와 인덱스를 매핑한 딕셔너리 반환
print('총단어수 : ', len(word))