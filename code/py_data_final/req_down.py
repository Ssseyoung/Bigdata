import requests 

img_src_403 = 'https://wallpapercave.com/wp/ryvfi3g.jpg'
sample = 'https://pixabay.com/ko/images/search/%eb%b0%94%eb%8b%a4%20%ed%92%8d%ea%b2%bd%20%ec%9d%b4%eb%af%b8%ec%a7%80/'

response = requests.get(img_src_403)

save_path = 'images/'
save_file = 'bgimg2.jpg'

with open(save_path+save_file, 'wb') as f:
    f.write(response.content)