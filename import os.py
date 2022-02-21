import os
import getpass
from tabnanny import check
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

def checkCredsMirea(log, passw):
    loadBar = "Trying to log in..."
    statusConnected = False
   
    driver = webdriver.Chrome("chromedriver")
    driver.get("https://online-edu.mirea.ru/")
    driver.find_element_by_id("login_username").send_keys(log)
    driver.find_element_by_id("login_password").send_keys(passw)
    driver.find_element_by_class_name("btn btn-primary btn-block").click()





def checkCredsLocal(log, passw):
    os.system('cls||clear')
    print('Wait. Checking your credentials...\n')
    time.sleep(3)

    if(log.find("@edu.mirea.ru")!= -1):
        print('Mail validation sucessful')
        time.sleep(3)
        os.system('cls||clear')
        checkCredsMirea(log,passw)
    else:
        print('Login is incorrect')
        answer=input('Want to try once again? (Y/n) >> ')
        if (answer =="Y" or answer == "y" or answer == "д" or answer == "Д"):
            os.system('cls||clear')
            task()
        else:
            os.system('cls||clear')
            print("Goodbye!")
            time.sleep(3)


def task():
    os.system('clear' if os.name == 'posix' else 'cls')
    print('Welcome to AutoLogginer Lite.\nWarning!We don`t collect/sell/store your logins & passwords \nVer 0.0.1(before release)\n')

    userCredL = input('Enter your MIREA login >> ')
    userCredP = getpass.getpass('Enter your MIREA password >> ')

    checkCredsLocal(userCredL,userCredP)


if __name__ == '__main__':
    task()