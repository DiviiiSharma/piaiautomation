from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep

driver = webdriver.Chrome()
driver.get("https://pi.ai/talk")


# Step 1: Creating a function "first_screen" that bypasses the popup
def first_screen():
    try:
        # Find the elment => "Next butoon"
        next_button_xpath = '//*[@id="__next"]/main/div/div/button'
        next_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, next_button_xpath))
        )
        
        # Click the button => "Next button"
        next_button.click()

        # Find the element => "Next button"
        next_button_xpath = '//*[@id="__next"]/main/div/div/button'
        next_button = driver.find_element(By.XPATH, next_button_xpath)

        # Click the button => "Next button"
        next_button.click()

        # Find the element => "Talk button"
        talk_button_xpath = '//*[@id="__next"]/main/div/div/div[1]/div[1]/div[2]/button[1]'
        talk_button = WebDriverWait(driver, 7).until(
            EC.element_to_be_clickable((By.XPATH, talk_button_xpath))
        )

        # Click the button => "Talk button"
        talk_button.click()

    except:
        pass


# Step 2: Main screen
def main_screen():
    # menu button for the voices
    def select_voices_button():
        # select the voices button
        voice_button_xpath = '//*[@id="__next"]/main/div/div/div[3]/div[3]/div/div[2]'
        voice_button = WebDriverWait(driver, 8).until(EC.element_to_be_clickable((By.XPATH, voice_button_xpath)))

        # click on the button
        voice_button.click()

    # Select the prefered voice
    def select_the_voice():
        # Selecting the voice
        select_voice_button_xpath = '//*[@id="__next"]/main/div/div/div[3]/div[3]/div/div[1]/button[5]'
        select_voice = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, select_voice_button_xpath))
        )
        select_voice.click()

    select_voices_button()
    select_the_voice()

#Close the voice Selector
def close_voice_selector():
    close_voice_xpath = '//*[@id="__next"]/main/div/div/div[3]/div[3]/div/div[2]/button[2]'
    close_voice_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, close_voice_xpath))
    )
    close_voice_button.click()



#Asking questions

def ask_question(Query):

    try:
        # FInd text area to write question
        question_area_xpath = '//*[@id="__next"]/main/div/div/div[3]/div[1]/div[4]/div/div[2]/textarea'
        question_area = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, question_area_xpath))
        )

        question_area.send_keys(f"{Query} give a short answer")


        # send button
        send_button_xpath = '//*[@id="__next"]/main/div/div/div[3]/div[1]/div[4]/div/button'
        send_buton = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, send_button_xpath))
        )
        send_buton.click()
        print(f"Answering to '{Query}':")

    except Exception as e:
        print(f"Error {e} asking the question.")


# Calling the bypass function
first_screen()

# Calling the main screen function
main_screen()
close_voice_selector()

while True:
    Query = str(input("User: "))
    if Query == "EXIT":
        break
    ask_question(Query)



sleep(10)
driver.quit()

