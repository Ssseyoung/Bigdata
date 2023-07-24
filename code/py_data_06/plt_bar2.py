# 막대 그래프

import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

font_path="C:/windows/Fonts/MALGUN.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

x = ['서울', '인천', '경기', '대구', '광주']
y = [500, 320, 490, 200, 340]

#plt.plot : 라인그래프
plt.title('시도별 스타벅스 매장갯수')
plt.xlabel('지역', fontsize=15, labelpad=7)
plt.ylabel('star_store', fontsize=15, labelpad=7)
plt.bar(x, y)
plt.show()