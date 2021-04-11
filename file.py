from bs4 import BeautifulSoup
import urllib.request as req
import csv

# 챔피언 목록도 크롤링해서 가져오고 싶었으나 능력부족으로 직접 타이핑 ㅠㅠ
champion = {'가렌':'garen','갈리오':'galio','갱플랭크':'gangplank','그라가스':'gragas','그레이브즈':'graves'
,'나르':'gnar','나미':'nami','나서스':'nasus','노틸러스':'nautilus','녹턴':'nocturne','누누와 윌럼프':'nunu','니달리':'nidalee','니코':'neeko'
,'다리우스':'darius','다이애나':'diana','드레이븐':'draven'
,'라이즈':'ryze','라칸':'rakan','람머스':'rammus','럭스':'lux','럼블':'rumble','레넥톤':'renekton','레오나':'leona','렉사이':'reksai','렐':'rell','렝가':'rengar','루시안':'lucian','룰루':'lulu','르블랑':'leblanc','리 신':'leesin','리븐':'riven','리산드라':'lissandra','릴리아':'lillia'
,'마스터 이':'masteryi','마오카이':'maokai','말자하':'malzahar','말파이트':'malphite','모데카이저':'mordekaiser','모르가나':'morgana','문도 박사':'drmundo','미스 포츈':'missfortune'
,'바드':'bard','바루스':'varus','바이':'vi','베이가':'veigar','베인':'vayne','벨코즈':'velkoz','볼리베어':'volibear','브라움':'braum','브랜드':'brand','블라디미르':'vladimir','블리츠크랭크':'blitzcrank','비에고':'viego','빅토르':'viktor','뽀삐':'poppy'
,'사미라':'samira','사이온':'sion','사일러스':'sylas','샤코':'shaco','세나':'senna','세라핀':'seraphine','세주아니':'sejuani','세트':'sett','소나':'sona','소라카':'soraka','쉔':'shen','쉬바나':'shyvana','스웨인':'swain','스카너':'skarner','시비르':'sivir','신 짜오':'xinzhao','신드라':'syndra','신지드':'singed','쓰레쉬':'thresh'
,'아리':'ahri','아무무':'amumu','아우렐리온 솔':'aurelionsol','아이번':'ivern','아지르':'azir','아칼리':'akali','아트록스':'aatrox','아펠리오스':'aphelios','알리스타':'alistar','애니':'annie','애니비아':'anivia','애쉬':'ashe','야스오':'yasuo','에코':'ekko','엘리스':'elise','오공':'wukong','오른':'ornn'
,'오리아나':'orianna','올라프':'olaf','요네':'yone','요릭':'yorick','우디르':'udyr','우르곳':'urgot','워윅':'warwick','유미':'yuumi','이렐리아':'irelia','이블린':'evelynn','이즈리얼':'ezreal','일라오이':'illaoi'
,'자르반 4세':'jarvaniv','자야':'xayah','자이라':'zyra','자크':'zac','잔나':'janna','잭스':'jax','제드':'zed','제라스':'xerath','제이스':'jayce','조이':'zoe'
,'진':'jhin','질리언':'zilean','징크스':'jinx'
,'초가스':'chogath'
,'카르마':'karma','카밀':'camille','카사딘':'kassadin','카서스':'karthus','카시오페아':'cassiopeia','카이사':'kaisa','카직스':'khazix','카타리나':'katarina','칼리스타':'kalista','케넨':'kennen','케이틀린':'caitlyn','케인':'kayn','케일':'kayle','코그모':'kogmaw','코르키':'corki','퀸':'quinn','클레드':'kled','키아나':'qiyana','킨드레드':'kindred'
,'타릭':'taric','탈론':'talon','탈리야':'taliyah','탐 켄치':'tahmkench','트런들':'trundle','트리스타나':'tristana','트린다미어':'tryndamere','트위스티드 페이트':'twistedfate','트위치':'twitch','티모':'teemo'
,'파이크':'pyke','판테온':'pantheon','피들스틱':'fiddlesticks','피오라':'fiora','피즈':'fizz'
,'하이머딩거':'heimerdinger','헤카림':'hecarim'
}

position = {'Top':'탑','Jungle':'정글','Middle':'미드','Bottom':'원딜','Support':'서폿'}

# csv에 들어갈 리스트
totalList = [['챔피언 이름','챔피언 영어 이름','포지션','픽률(%)','승률(%)'],]

# url
first_URL = 'https://www.op.gg/champion/'
last_URL = '/statistics/'



for key in champion:
    res = req.urlopen(first_URL+champion[key]+last_URL)
    soup = BeautifulSoup(res, 'html.parser')
    
    # 챔피언의 승률과, 픽률 가져오기
    pick = soup.find_all('div', {'class':'champion-stats-trend-rate'})

    # 승률 값 정리하기
    win_rate = str(pick[1])
    win_rate = win_rate.replace('<div class=\"champion-stats-trend-rate\">\n\t\t\t', '')
    win_rate = win_rate.replace('%\n\t\t</div>', '')
    
    # 픽률 값 정리하기
    pick_rate = str(pick[0])
    pick_rate = pick_rate.replace('<div class=\"champion-stats-trend-rate\">\n\t\t\t', '')
    pick_rate = pick_rate.replace('%\n\t\t</div>', '')
    
    # 챔피언의 포지션 가져오고, 정리하기
    pos = soup.find_all(class_='champion-stats-header__position__role')
    pos = str(pos[0])
    pos = pos.replace('<span class="champion-stats-header__position__role">', '')
    pos = pos.replace('</span>', '')
    if(pos == 'Top'): pos = position['Top']
    elif(pos == 'Jungle'): pos = position['Jungle']
    elif(pos == 'Middle'): pos = position['Middle']
    elif(pos == 'Bottom'): pos = position['Bottom']
    elif(pos == 'Support'): pos = position['Support']

    # 행 만들기(챔피언 이름, 영어 이름, 포지션, 승률, 픽률)
    tmp = []
    tmp.append(key)
    tmp.append(champion[key])
    tmp.append(pos)
    tmp.append(win_rate)
    tmp.append(pick_rate)
    
    # 행 추가하기
    totalList.append(tmp)
    print(tmp)

# csv파일로 저장
f = open(f'LOL_info.csv', 'w', encoding='utf-8', newline='')
csvWriter = csv.writer(f)
for i in totalList:
    csvWriter.writerow(i)
f.close()

print('완료!')

# 참고한 사이트
# 크롤링 : https://www.youtube.com/watch?v=DBK9-QdX6Yw / https://www.youtube.com/watch?v=hVjojow0oqc
# 크롤링한 데이터를 csv파일에 저장하기 : https://www.youtube.com/watch?v=ASFa0Rh4OMw