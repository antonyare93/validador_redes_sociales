import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def get_values(url):
    with webdriver.Chrome(executable_path='D:/Proyectos/Python/validador_redes_sociales/chromedriver_win32/v_106/chromedriver.exe') as driver:
        driver.get(url)
        time.sleep(10)
        try:
            private_account = driver.find_element(by=By.XPATH, value="//h2[contains( text(), 'Esta cuenta es privada')]")
            ig_privacy = True
        except NoSuchElementException:
            ig_privacy = False

        btn_posts = driver.find_element(by=By.XPATH, value="//div[contains( text(), ' publicaciones')]")
        ig_posts = int((btn_posts.text).replace(" publicaciones", ""))
        btn_followers = driver.find_element(by=By.XPATH, value="//div[contains( text(), ' seguidores')]")
        ig_followers = int((btn_followers.text).replace(" seguidores", ""))
        btn_following = driver.find_element(by=By.XPATH, value="//div[contains( text(), ' seguidos')]")
        ig_following = int((btn_following.text).replace(" seguidos", ""))

    ig_score, ig_status = calculate_score(ig_privacy, ig_posts, ig_followers, ig_following)
    return ig_privacy, ig_posts, ig_followers, ig_following, ig_score, ig_status


def calculate_score(ig_privacy, ig_posts, ig_followers, ig_following):
    if ig_privacy and ig_posts < 20:
        return -99999, False # Score y aprobación
    else:
        nada = None