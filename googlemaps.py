from selenium import webdriver 
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.google.com/maps/@42.7577489,-84.4022948,8.5z") 
sleep(2) 

def searchplace():
	Place=driver.find_element_by_class_name("tactile-searchbox-input")
	Place.send_keys("Lansing")
	Submit=driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button")
	Submit.click()
searchplace()

def directions():
	sleep(10)	
	directions=driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[1]/button/span/img")
	directions.click()
directions()

def find():
    sleep(6)
    find=driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/input")
    find.send_keys("Detroit")
    sleep(2)
    search=driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]")
    search.click()
find()

def miles():
    sleep(5)
    Totalmiles=driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[1]/div/div[1]/div[1]/div[2]/div")
    print("Total Miles:",Totalmiles.text)

miles()


	               
               
               
               
               
               
               
               
               
               
               
               
               
               
                   
