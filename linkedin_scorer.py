import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException



def existProfile(url):
    with webdriver.Chrome(executable_path='chromedriver_win32/v_106/chromedriver.exe') as driver:
        try:
            driver.get(url)
            time.sleep(5)
            driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Inicia sesión')]").click()

            # En entorno de prueba se solicitan credenciales de inicio de sesión para el testeo
            n_usuario = input('ingrese su email para iniciar sesión: ')
            pw_usuario = input('Ingrese su contraseña para iniciar sesión: ')

            driver.find_element(by=By.NAME, value='session_key').send_keys(n_usuario)
            driver.find_element(by=By.NAME, value='session_password').send_keys(pw_usuario + '\n')
            time.sleep(5)
            try:
                driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Saltar')]").click()
            except NoSuchElementException:
                pass
            finally:
                driver.get(url)
                if driver.current_url == url:
                    linkedin_exist = True
                    span_contactos = driver.find_element(by=By.CLASS_NAME, value="t-bold")
                    lkn_contactos = float((span_contactos.text).replace(".", "").replace(",", ""))
                    return lkn_contactos, linkedin_exist
                else:
                    linkedin_exist = False
                    return -99, linkedin_exist
        except:
            linkedin_exist = False
            return -99, linkedin_exist

        
        