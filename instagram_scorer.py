import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def get_values(url):
    with webdriver.Chrome(executable_path='chromedriver_win32/v_106/chromedriver.exe') as driver:
        driver.get(url)
        time.sleep(10)
        try:
            private_account = driver.find_element(by=By.XPATH, value="//h2[contains( text(), 'Esta cuenta es privada')]")
            ig_privacy = True
        except NoSuchElementException:
            ig_privacy = False

        btn_posts = driver.find_element(by=By.XPATH, value="//div[contains( text(), ' publicaciones')]")
        ig_posts = float((btn_posts.text).replace(" publicaciones", "").replace(".", "").replace(",", ""))
        btn_followers = driver.find_element(by=By.XPATH, value="//div[contains( text(), ' seguidores')]")
        ig_followers = float((btn_followers.text).replace(" seguidores", "").replace(".", "").replace(",", ""))
        btn_following = driver.find_element(by=By.XPATH, value="//div[contains( text(), ' seguidos')]")
        ig_following = float((btn_following.text).replace(" seguidos", "").replace(".", "").replace(",", ""))

    ig_score, ig_status = calculate_score(ig_privacy, ig_posts, ig_followers, ig_following)
    return ig_privacy, ig_posts, ig_followers, ig_following, ig_score, ig_status


def calculate_score(ig_privacy, ig_posts, ig_followers, ig_following):
    if ig_privacy and ig_posts < 20.0:
        return -99999, False # Score y aprobación
    else:
        ig_posts -= 50
        ig_following -= 300
        ig_followers -= 500

        if not ig_privacy:
            ig_score = 1
        else:
            ig_score = 0

        ig_score += (ig_posts/100)
        ig_score += (ig_following/10000)
        ig_score += (ig_followers/100000)

        if not ig_privacy:
            if ig_score >=1.07:
                ig_status = True
            else:
                ig_status = False
        else:
            if ig_score >= 0.01:
                ig_status = True
            else:
                ig_status = False

        return ig_score, ig_status