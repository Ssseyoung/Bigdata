# 영어 성적 30명
scores = [90, 80, 60, 55, 65,
          70, 89, 68, 72, 67,
          80, 77, 90, 55, 98,
          60, 89, 70, 68, 78,
          99, 83, 89, 59, 100,
          55, 58, 78, 88, 98]

# 카테고리로 나눔 A B C D F
# 막대그래프 학점별 인원수
# 파이그래프 학점별 퍼센트 (시작=90)

import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import matplotlib.pyplot as plt

font_path="C:/windows/Fonts/MALGUN.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)
plt.rcParams['axes.unicode_minus'] = False

# 각 학점 범위 정의
grade_dict = {'A': [90, 100], 'B': [80, 89], 'C': [70, 79], 'D': [60, 69], 'F': [0, 59]}
# 성적을 등급으로 매핑하는 딕셔너리 생성

# 각 학점 범위에 해당하는 학생 수
grade_counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}

# 학점별 인원수 계산
for score in scores:
    for grade, range_ in grade_dict.items():
        if score >= range_[0] and score <= range_[1]:
            grade_counts[grade] += 1
            break

# 막대그래프 출력
x = list(grade_counts.keys())
y = list(grade_counts.values())

plt.bar(x, y)
plt.xlabel('Grade')
plt.ylabel('Count')
plt.title('Number of students by grade')
plt.show()

# 학점별 퍼센트 계산
total_count = sum(grade_counts.values())
percentages = {}

for grade, count in grade_counts.items():
    percentages[grade] = round(count / total_count * 100, 2)

# 파이그래프 출력
labels = list(percentages.keys())
sizes = list(percentages.values())

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, startangle=90, autopct='%1.1f%%')
ax1.axis('equal')

plt.title('Percentage of students by grade')
plt.show()