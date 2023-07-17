import csv
import os

genres = ['Horror', 'Children', 'Crime', 'Adventure', 'Thriller', 'Sci-Fi', 'Fantasy', 'War', 'Comedy', '(no genres listed)', 'Animation', 'Film-Noir', 'Action', 'IMAX', 'Mystery', 'Drama', 'Documentary', 'Musical', 'Western', 'genres', 'Romance']
   
# print(genres)  

filename = 'data/movies.csv'

if os.path.exists(filename):
    fr = open(filename, 'r', encoding='utf-8')
    data = csv.reader(fr)
    
    genres_dict = {}
    
    for i in data:
        # print(i[2])
        for g in genres:
            if i[2].find(g) != -1 :
                if genres_dict.get(g):
                    genres_dict[g] += 1
                else:
                    genres_dict[g] = 1
            
    print(genres_dict)
    