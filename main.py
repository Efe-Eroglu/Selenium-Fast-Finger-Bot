from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class Bot:
    def __init__(self):
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()

    def run(self):
        self.driver.get("https://10fastfingers.com/typing-test/turkish")

        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"CybotCookiebotDialogBodyButtonDecline")))
        deny_button=self.driver.find_element(By.ID,"CybotCookiebotDialogBodyButtonDecline")
        deny_button.click()

        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"inputfield"))) 
        i=1

        while i<=353:
            WebDriverWait(self.driver,1).until(ec.visibility_of_element_located((By.XPATH,f"//*[@id='row1']/span[{str(i)}]")))
            text=self.driver.find_element(By.XPATH,f"//*[@id='row1']/span[{str(i)}]").text
            self.driver.find_element(By.ID,"inputfield").send_keys(text+" ")
            i+=1

    
main=Bot()
main.run()
