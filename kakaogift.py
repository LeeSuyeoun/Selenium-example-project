from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import unittest, time

class KakaogiftTestcase (unittest.TestCase) :
    
    def setUp(self) :
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30) # 30초안에 웹페이지를 load 하면 바로 넘어가거나, 30초를 기다림

    def test_kakaogift(self):
        driver = self.driver
        driver.get("https://store.kakao.com/")
        driver.maximize_window()

        manwon = driver.find_element(By.CSS_SELECTOR, '#mArticle > div > div.bunch_store.bunch_intro > app-view-short-cut > div > ul > li:nth-child(3) > a')
        self.assertEqual(manwon.text,"1+1 톡딜")
        
        manwon.click()
        themedeal = driver.find_element(By.CSS_SELECTOR,'#scrolled > div > div > strong')
        self.assertEqual(themedeal.text, "하나 사면 하나 더")
        
        body = driver.find_element(By.CSS_SELECTOR,'body')
        body.send_keys(Keys.PAGE_DOWN)

        zzim = driver.find_element(By.CSS_SELECTOR, '#scrolled > cu-infinite-scroll > div > ul > li:nth-child(1) > app-view-themedeal-product > span > fu-view-favorite-button > span > button')
        zzim.click()

        kakao = driver.find_element(By.CSS_SELECTOR, '#__next > div > div > main > div > h1 > span')
        self.assertEqual(kakao.text, "Kakao")
        
        time.sleep(5) #5초 기다림
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
	unittest.main()