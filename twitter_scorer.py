from distutils.log import error
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException



def existProfile(url):
    with webdriver.Chrome(executable_path='chromedriver_win32/v_106/chromedriver.exe') as driver:
        try:
            driver.get(url)
            time.sleep(5)
            div_tweets = driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Tweets')]")
            tw_posts = float(div_tweets.text.replace(" Tweets", "").replace(",", "").replace(".", ""))
            div_following = driver.find_element(by=By.PARTIAL_LINK_TEXT, value="Siguiendo")
            tw_following = float(div_following.text.replace(" Siguiendo", "").replace(",", "").replace(".", ""))
            div_followers = driver.find_element(by=By.PARTIAL_LINK_TEXT, value="Seguidores")
            tw_followers = float(div_followers.text.replace(" Seguidores", "").replace(",", "").replace(".", ""))

            tw_score, tw_status = calculate_score(tw_posts, tw_following, tw_followers)
            return tw_posts, tw_following, tw_followers, tw_score, tw_status
        except:
            raise error('Error al procesar la página de Twitter')


def calculate_score(tw_posts, tw_following, tw_followers):
    tw_posts -= 1000
    tw_followers -= 300
    tw_following -= 700

    tw_score = tw_posts/100000
    tw_score += tw_followers/1000
    tw_score += tw_following/10000

    if tw_score > 0.2:
        return tw_score, True
    else:
        return tw_score, False