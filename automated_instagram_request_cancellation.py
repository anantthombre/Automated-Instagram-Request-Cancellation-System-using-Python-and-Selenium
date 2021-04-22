from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.instagram.com/accounts/login/?next=/accounts/access_tool/current_follow_requests")
driver.implicitly_wait(10)
driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys("") #Enter Username 
driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys("") #Enter Password
driver.implicitly_wait(10)
driver.find_element_by_css_selector('button[type=submit]').click() #login In Button
driver.implicitly_wait(10)
driver.find_element(By.XPATH,'//*[@id="react-root"]/section/main/div/div/div/div/button').click() #Not Now Button
driver.implicitly_wait(10)
driver.find_element(By.XPATH,'//*[@id="react-root"]/section/main/div/article/main/button').click() #View More Button
i=0
c=1
insta_user = []
try:
    while WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type=button]'))).is_displayed() == True and c<500:
        try:
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type=button]'))).click() #View More Button
            count = 0
            while(count<10):
                if driver.find_element(By.XPATH,'//*[@id="react-root"]/section/main/div/article/main/section/div['+str(c)+']').is_displayed() == True:
                    insta_user.append(driver.find_element(By.XPATH,'//*[@id="react-root"]/section/main/div/article/main/section/div['+str(c)+']').text)
                count += 1
                c += 1
            print(i)
            i = i+1
            print(insta_user) 
            # insta_list = driver.find_element(By.XPATH,'//*[@id="react-root"]/section/main/div/article/main/section/div')
            # print(insta_list)       
        except Exception as p:
            print("Error Occured inside whie loop", p)

except Exception as e:
    print("Error occured", e)

for i in insta_user:
    try:
        driver.get("https://www.instagram.com/"+i) #User profile page
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH,'//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div/button').click() #Requested Button
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div/div[3]/button[1]').click() #Unfollow Button
        driver.implicitly_wait(10)       
    except Exception as u:
        print("Error occured in for loop", u)
        
    
print("Total"+str(len(insta_user))+"Unfollowed!!!")
print("Project Done!!!😉")

# Give comments after the code completion.

# print(view_more.is_displayed())
# while driver.find_element(By.XPATH,'//*[@id="react-root"]/section/main/div/article/main/button').is_displayed() == True:
# driver.find_element(By.XPATH,'//*[@id="react-root"]/section/main/div/article/main/button').click()
# driver.implicitly_wait(5)



