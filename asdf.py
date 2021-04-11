import pandas as pd # pandas를 pd라는 이름으로 사용
import matplotlib.pyplot as plt # matplotlib.pyplot를 plt라는 이름으로  사용
from pandas import Series, DataFrame
from operator import itemgetter


# -- 파일 불러오고, 폰트 설정 -- #

df = pd.read_csv('LOL_info.csv')
plt.rc('font', family='Malgun Gothic')

# ------------------------------ #



# -- 포지션별로 리스트에 담기 -- #

total = []
df_toplane = []
df_jglane = []
df_midlane = []
df_botlane = []
df_supplane = []
cnt = 0

for i in df['포지션']:
    tmp_list = []
    
    # 이름 가져오기
    tmp = str(df.iloc[[cnt],[0]])
    tmp = tmp.replace(f'챔피언 이름\n{cnt}','')
    tmp = tmp.strip()
    tmp_list.append(tmp)
    
    # 픽률 가져오기 
    tmp = str(df.iloc[[cnt],[3]])
    tmp = tmp.replace(f'픽률(%)\n{cnt}','')
    tmp = tmp.strip()
    tmp_list.append(tmp)
    
    # 승률 가져오기
    tmp = str(df.iloc[[cnt],[4]])
    tmp = tmp.replace(f'승률(%)\n{cnt}','')
    tmp = tmp.strip()
    tmp_list.append(tmp)
    
    # 각 포지션별로 리스트에 저장
    if(i == '탑'):
        df_toplane.append(tmp_list)
    elif(i == '정글'):
        df_jglane.append(tmp_list)
    elif(i == '미드'):
        df_midlane.append(tmp_list)
    elif(i == '원딜'):
        df_botlane.append(tmp_list)
    elif(i == '서폿'):
        df_supplane.append(tmp_list)
    cnt+=1

total.append(df_toplane)
total.append(df_jglane)
total.append(df_midlane)
total.append(df_botlane)
total.append(df_supplane)

# ------------------------------ #



# ----- 포지션별 챔피언 수 ----- #

champ_amount = []

# 리스트에 각 포지션별 챔피언 수 저장
for i in range(0,5):
    champ_amount.append(len(total[i]))

# 그래프 그리기
plt.bar(range(5),champ_amount,width=0.6, color = "#3AAFDC")
plt.title('포지션별 챔피언 수',fontsize=15)
plt.xlabel('포지션')
plt.ylabel('챔피언 수(개)')
plt.xticks(range(5),['탑', '정글','미드','원딜','서폿'])
for i in range(0,5):
    plt.text(i, champ_amount[i], str(champ_amount[i]),fontsize=11,horizontalalignment='center',verticalalignment='bottom')
plt.ylim(5, 40)
plt.show()

# ------------------------------ #



# -- 라인별 챔피언 픽률그래프 -- #

# 그래프의 크기 조정
plt.figure(figsize=(15,5))

# 포지션별로 그래프를 그릴 수 있게 반복문을 돌려줌
for i in range(len(total)):
    pick = []
    pick_rate = [] # 그래프를 그릴 때 사용
    
    # pick 리스트에 챔피언의 이름과 픽률만 따로 저장
    for j in range(len(total[i])):
        tmp = []
        tmp.append(total[i][j][0])
        tmp.append(float(total[i][j][1]))
        pick.append(tmp)
    
    # 픽률이 높은 순서로 정렬하기
    pick.sort(key=itemgetter(1), reverse = True)
    
    # pick_rate에 상위 3개의 값만 저장
    for j in range(len(pick)):
        pick_rate.append(pick[j][1])
    pick_rate = pick_rate[0:3]
    
    # 그래프와 그래프 사이의 간격
    pick_rate.append(0)
    
    # 그래프 그리기
    plt.bar(range(i*4,i*4+4),pick_rate, width=1.0, color = ['#D1B2FF','#CEF279','#B2CCFF'])
    plt.title('포지션별 챔피언 픽률',fontsize=15)
    plt.xlabel('포지션(1등,2등,3등)')
    plt.ylabel('픽률(%)')
    plt.xticks(range(1, 20, 4),['탑','정글','미드','원딜','서폿'])
    for j in range(0,4):
        if (j == 3):break
        plt.text(j+i*4,pick_rate[j],str(pick[j][0])+'\n( '+str(pick[j][1])+'% )',fontsize=9,horizontalalignment='center',verticalalignment='bottom')
plt.ylim(5.5, 37.5)
plt.show()

# ------------------------------ #




# ---라인별 챔피언 승률그래프--- #

# 그래프의 크기 조정
plt.figure(figsize=(15,5))

# 포지션별로 그래프를 그릴 수 있게 반복문을 돌려줌
for i in range(len(total)):
    win = []
    win_rate = [] # 그래프를 그릴 때 사용
    
    for j in range(len(total[i])):
        tmp = []
        tmp.append(total[i][j][0])
        tmp.append(float(total[i][j][2]))
        win.append(tmp)
        
    # 승률이 높은 순서대로 정렬
    win.sort(key = lambda x: x[1], reverse = True)
    
    # win_rate에 가장 승률이 높은 값, 낮은 값을 넣어준다.
    win_rate.append(win[0][1])
    win_rate.append(win[-1][1])
    
    # 그래프와 그래프 사이의 간격
    win_rate.append(0)
    
    # 그래프 그리기
    plt.bar(range(i*3,i*3+3),win_rate, width=1.0, color = ['#FF4848','#489CFF'])
    plt.title('포지션별 챔피언 승률',fontsize=15)
    plt.xlabel('포지션(1등, 꼴등)')
    plt.ylabel('승률(%)')
    plt.xticks(range(1, 15, 3),['탑','정글','미드','원딜','서폿'])
    for j in range(0,3):
        tmp = j
        if(j==2):break
        elif(j==1): tmp = -1
        plt.text(j+i*3,win_rate[j],str(win[tmp][0])+'\n( '+str(win[tmp][1])+'% )',fontsize=9,horizontalalignment='center',verticalalignment='bottom')

plt.ylim(35.7, 55.7)
plt.show()

# ------------------------------ #