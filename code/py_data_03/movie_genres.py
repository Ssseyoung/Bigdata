import os
import csv

filename = 'data/movies.csv'
genres = []
genres2 = []    # 중복 제거된 데이터

if os.path.exists(filename):
    # print('영화샘플 데이터 존재합니다')
    fr = open(filename, 'r', encoding='utf-8')
    # line = fr.read()
    # print(line)
    data = csv.reader(fr)
    # print(next(data))
    
    for i in data:
        genres.extend(i[2].split('|'))
    
    genres2 = set(genres)
    genres2 = list(genres2)
    print(genres2)
    # print(len(genres2))
    
    
    # 장르별 영화 갯수
    fr2 = open(filename, 'r', encoding='utf-8')
    data2 = csv.reader(fr2)
    
    gr_dict = {key : None for key in genres2}
    # print(gr_dict)
    # for key in gr_dict:
    #     for i in data2:
            # print(key)
   
    
    