import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

font_path="C:/windows/Fonts/MALGUN.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

x = ['서울', '인천', '경기', '대구', '광주']
star_store = [500, 320, 490, 200, 340]
z = [3200, 2000, 3100, 1300, 2200]

fig = plt.figure()  # 전체 그래프의 크기 설정
sub_plt1 = fig.add_subplot(2, 2, 1)  # 2x2 형태로 서브플롯 생성
sub_plt2 = fig.add_subplot(2, 2, 2)
sub_plt3 = fig.add_subplot(2, 2, 3)
sub_plt4 = fig.add_subplot(2, 2, 4)

# 1번 서브플롯 : 일차원 라인 그래프
sub_plt1.plot(x, star_store, color='b')
sub_plt1.set_title('스타벅스 매장갯수')

# 2번 서브플롯 : 포물선 라인 그래프
sub_plt2.plot(x, z, color='r')
sub_plt2.set_title('포물선 라인 그래프')


# 3번 서브플롯 : 스타벅스 매장갯수 막대 그래프
sub_plt3.bar(x, star_store, color='g')
sub_plt3.set_title('스타벅스 매장갯수 막대 그래프')


# 4번 서브플롯 : 스타벅스 월별 매출액(대략) 막대 그래프
sub_plt4.bar(x, z, color='y')
sub_plt4.set_title('스타벅스 월별 매출액(대략) 막대 그래프')

plt.show()