import os
import getpass
from tabnanny import check
import time
from datetime import datetime, date, time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

def dayOfStudy():
    if(datetime.today().isoweekday()==1):
        print("Monday")
    if(datetime.today().isoweekday()==2):
        print("Tuesday")
    if(datetime.today().isoweekday()==3):
        print("Wednesday")
    if(datetime.today().isoweekday()==4):
        print("Thursday")
    if(datetime.today().isoweekday()==5):
        print("Friday")
    if(datetime.today().isoweekday()==6):
        print("Saturday")
    if(datetime.today().isoweekday()==7):
        print("Sunday")   




def checkCredsMirea(log, passw):
    loadBar = "Trying to log in..."
    statusConnected = False
   
    driver = webdriver.Chrome("chromedriver")
    driver.get("https://login.mirea.ru/login/?next=/oauth2/v1/authorize/%3Fresponse_type%3Dcode%26client_id%3DdnOh7sdtPxfyxzbxcMRLksWlCCE3WsgTfRY6AWKh%26redirect_uri%3Dhttps%253A%252F%252Fonline-edu.mirea.ru%252Flogin%252F%26scope%3Dbasic%2Bstudent")
    driver.find_element_by_id("id_login").send_keys(log)
    driver.find_element_by_id("id_password").send_keys(passw)
    if (driver.find_element_by_xpath("//option[text()='Войти']")==True):
        print("yes")
    else:
        print("no")

    WebDriverWait(driver=driver, timeout=10).until(lambda x: x.execute_script("return document.readyState === 'complete'"))
    error_message = "Incorrect username or password."
    errors = driver.find_elements_by_class_name("flash-error")
    print(e.text)
    if any(error_message in e.text for e in errors):
        print("[!] Login failed")
    else:
        print("[+] Login successful")



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
    dayOfStudy()
    userCredL = input('Enter your MIREA login >> ')
    userCredP = getpass.getpass('Enter your MIREA password >> ')

    checkCredsLocal(userCredL,userCredP)


if __name__ == '__main__':
    task()