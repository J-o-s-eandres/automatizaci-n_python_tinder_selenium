from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# path = '/Documentos/Driver_Google/chromedriver'
path = 'C:\Driver_Google_II/chromedriver'
service= Service(executable_path=path)

mensaje_ligar =" Hello como estas?"
numero_likes= 10 
options = Options() 
options.add_experimental_option("debuggerAddress", "localhost:9222")
web = 'https://tinder.com/'
driver = webdriver.Chrome(service=service, options=options)
driver.get(web)

time.sleep(20)

for i in range(numero_likes):
    try:
        time.sleep(3)
        like_button = driver.find_element(by=xpath, value='//button//span[text()="Like"]')
        driver.execute_script("arguments[0].click();", like_button)
        # like_button.click()
        time.sleep(2)

        match_window= driver.find_element(by=xpath, value= '//textarea[@placeholder="Say something nice!"]')
        # //textarea[@placeholder="Say something noce!"]
        match_window.send_keys(mensaje_ligar)
        time.sleep(2)


        send_message_button = driver.find_element(by=xpath, value='//button/span[text()="Send"]')
        send_message_button.click()
        time.sleep(2)


        close_its_match_window = driver.find_element(by=xpath, value= '//button[@tittle="Back to Tinder"]')
        close_its_match_window.click()
        time.sleep(2)
    except:
        try:
            box = driver.find_element(by=xpath, value="//button/span[text()='Maybe Later'] | //button/span[text()='Not interested'] | //button/span[text()='No Thanks']" )
            box.click()
            # //button/span[text()='Maybe Later'] | //button/span[text()='Not interested'] | //button/span[text()='No Thanks']
        except:
            pass