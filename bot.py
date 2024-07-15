from selenium import webdriver
from bs4 import BeautifulSoup
import pyautogui
import pyperclip
import time

options=webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
driver=webdriver.Chrome(options=options)

driver.get("https://www.proprofs.com/quiz-school/story.php?title=advanced-python-test_11e4")

data=BeautifulSoup(driver.page_source,"html.parser")
question_index=0

time.sleep(5)
for question in data.find_all('li', class_='ques_marg'):
    if question_index==1:
        q=question.find("h3",class_="question-text")
        a=question.find_all("div",class_="opt_text")
        ques="🎮 *Question* \n\n"+q.string
        pyperclip.copy(ques)
        time.sleep(1)
        pyautogui.hotkey("ctrl","v")
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
        pyautogui.hotkey("shift","tab")
        time.sleep(1)
        pyautogui.press("space")
        pyautogui.press("down")
        pyautogui.press("down")
        pyautogui.press("down")
        pyautogui.press("space")
        pyautogui.press("down")
        pyautogui.press("down")
        pyautogui.press("down")
        pyautogui.press("down")
        pyautogui.press("down")
        pyautogui.press("space")
        time.sleep(1)
        ans="✅"+" *Answers*"
        pyperclip.copy(ans)
        time.sleep(1)
        pyautogui.hotkey("ctrl","v")
        pyautogui.press("tab")
        pyautogui.press("tab")

        for answer in a:
            pyperclip.copy(answer.p.string)
            time.sleep(1)
            pyautogui.hotkey("ctrl","v")
            time.sleep(1)
            pyautogui.press("tab")
            pyautogui.press("tab")
            print(answer.p.string)
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        time.sleep(1)
        pyautogui.press("enter")
        print("-"*20)
    question_index+=1
