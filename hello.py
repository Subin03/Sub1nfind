from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from random import *




# Hi 
i = randint(5, 30)  # 1부터 100 사이의 임의의 정수
 
f = random()   # 0부터 1 사이의 임의의 float
 
f = uniform(1.0, 36.5)   # 1부터 36.5 사이의 임의의 float
 
i = randrange(1, 101, 2) # 1부터 100 사이의 임의의 짝수
 
i = randrange(10)  # 0부터 9 사이의 임의의 정수

from random import randint

#random_wait_min = 10
#random_wait_max = 25

random_next_min = 30
random_next_max = 70


from selenium.webdriver.common.by import By

ID = '000000000' #인스타그램 ID
PW = '000000000' #인스타그램 PW

#화면 띄우기
browser = webdriver.Chrome('/Users/samuelgalaxys/desktop/chromedriver')
browser.get("https://instagram.com")

#로딩하는 시간 기다리기
time.sleep(2)

#Login ID 속성값 찾고 입력하기
login_id = browser.find_element_by_name('username')
login_id.send_keys(ID)

#Login PW 속성값 찾기 입력하기
login_pw = browser.find_element_by_name('password')
login_pw.send_keys(PW)
login_pw.send_keys(Keys.RETURN)

time.sleep(5)


# 정보 저장 팝업 닫기
popup = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
popup.send_keys(Keys.ENTER)

time.sleep(5)



# 알림 설정 팝업 닫기
time.sleep(3)
try :
    popup = browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
except :
    try : 
        popup = browser.find_element_by_xpath('html/body/div[3]/div/div/div/div[3]/button[2]')
    except : 
        try :
            popup = browser.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
        except : 
            try :
                popup = browser.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
            except : 
                try :
                    popup = browser.find_element_by_xpath('/html/body/div[7]/div/div/div/div[3]/button[2]')
                except :
                    popup = browser.find_element_by_xpath('/html/body/div[8]/div/div/div/div[3]/button[2]')
popup.send_keys(Keys.ENTER)




# 태그 검색 하기
search = browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
search.send_keys('#Mars')

#time.sleep(2)





tag = ['nasa', 'moontomars', 'spacex', 'like4like', 'jupiter', 'saturn', 'earth', 'spaceexploration' ]



# 최상위 검색 결과로 진입하기 Enter 두번으로 수행 
search.send_keys(Keys.RETURN) #최상위 검색결과로 Focus 이동
search.send_keys(Keys.RETURN) #검색결과 새로운 창으로 이동

browser.get("https://www.instagram.com/explore/tags/f2f/")
#링크로 대체


 


# 첫번쨰 게시물 선택하기

feed = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a')
feed.send_keys(Keys.ENTER)

for a in range(700):
    # 좋아요 누르기
    time.sleep(randint(random_next_min,random_next_max))
    like_list = browser.find_elements_by_xpath('//article//section/span/button')  
    like_list[0].click() #list 중 0번째 버튼을 선택
    time.sleep(randint(random_next_min,random_next_max))


    try :
      comment_list = ['Whoa, its wonderful!', 'Wonderful!', 'Nice Space Photo. i love it!', 'Space exploration is a very important task for mankind ever!', 
                'Human beings are a species of curiosity.', 'We choose go to the moon by this decade.', 'Perseverance the Rover.', 'Follow and watch Mars images during live updates.',
                'The new era is coming!', 'Follow me and get to know a lot about Mars.' ,'Just Follow me and get to know a lot about the universe.' ,'Nice pic! check my page maybe you like it.' ]


     #comment_flag = False
      comment_flag = True



      comment_content = comment_list[randint(0,len(comment_list)-1)]


      
      browser.find_element_by_xpath('/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea').click()
      browser.find_element_by_xpath('/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea').send_keys(comment_content)
      browser.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[1]/div[2]/div/article[1]/div/div[3]/div/div/section[3]/div/form/button').click()


      time.sleep(randint(random_next_min,random_next_max))

      #팔로우하기
      browser.find_element_by_xpath('/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[2]/button').click()

      time.sleep(randint(random_next_min,random_next_max))

 

#팔로우취소방지
      popup = browser.find_element_by_xpath('/html/body/div[7]/div/div/div/div[3]/button[2]')
      popup.send_keys(Keys.ENTER)


      browser.find_element(By.XPATH,"//button[@class='wpO6b  ']//*[@aria-label='다음']" ).click()

    except :
      pass


 #/html/body/div[7]/div/div/div/div[2]/button[2]

    time.sleep(3)
    try :
        popup = browser.find_element_by_xpath('/html/body/div[7]/div/div/div/div[2]/button[2]').click()
    except :
        try : 
          popup = browser.find_element_by_xpath('/html/body/div[7]/div/div/div/div[2]/button[2]').click()
        except : 
         try :
            popup = browser.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()
         except : 
            try :
                popup = browser.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]').click()
            except : 
                try :
                    popup = browser.find_element_by_xpath('/html/body/div[7]/div/div/div/div[3]/button[2]').click()
                except :
                    pass
#    popup.send_keys(Keys.ENTER)





    # 다음 피드로 이동하기 
    
    browser.find_element(By.XPATH,"//button[@class='wpO6b  ']//*[@aria-label='다음']" ).click()

  #  nextFeed[0].click()
 

 
