import os
import getpass
import calendar
from tabnanny import check
import time
from datetime import datetime,date
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

def weekOfStudy(day,month,year,week):
    weeks=False
    counterOfWeeks=0
    if (day >= 21 and day <= 26  and month ==2 and year == 2022 ):
        print("Odd week\n")
        weeks=True
        counterOfWeeks+=1
    if ((day >= 28 and month == 2 and year == 2022) or (day >=1 and day <= 6 and year == 2022 and month == 3 )):
        print("Even week\n")
        weeks=False
        counterOfWeeks+=1
    
    if ((week==3 and weeks==True)or(week==4 and weeks==True)or(week==5 and weeks==True)or (week==6 and weeks==True)or(week==7 and weeks==True)or(week==1 and weeks==False)or(week==2 and weeks==False)or(week==5 and weeks==False)or(week==7 and weeks==False)):
        print('No stydy for today!!\n')
    if((weeks==1 and weeks==True and counterOfWeeks==5)or(weeks==1 and weeks==True and counterOfWeeks==9)(weeks==1 and weeks==True and counterOfWeeks==13)(weeks==1 and weeks==True and counterOfWeeks==15)):
        print('Let`s study!Today`s routine is \n\t\t\t\tSubject\t\t\t\tTime\n\tАлгоритмы компонентов п-п обработки и преобраз данных 9:00-10:30 \n\t\tМодели и методы принятия технических решений 10:40-12:10 \n\t Информационный технологии цифровой экономики 14:20-15:50\n')
    if((weeks==1 and weeks==True)):
        print('Let`s study!Today`s routine is \n\t\t\t\tSubject\t\t\t\tTime\n\tАлгоритмы компонентов п-п обработки и преобраз данных 9:00-10:30 \n\t\tМодели и методы принятия технических решений 10:40-12:10 \n\t')
    if((weeks==2 and weeks==True)):
        print('Let`s study!Today`s routine is \n\t\t\t\tSubject\t\t\t\tTime\n\tМетоды и средства защиты компьютерной информации 9:00-10:30 \n\t\tМетоды и средства защиты компьютерной информации 10:40-12:10 \n\t')
    if((weeks==3 and weeks==False)):
        print('Let`s study!Today`s routine is \n\t\t\t\tSubject\t\t\t\tTime\n\tОсновы антикоррупционной деятельности 9:00-10:30 \n\t\tБЖД 10:40-12:10\n\t Методы и средства взаимодействия компонент ПО 12:40-14:10\n')
    if((weeks==4 and weeks==False)):
        print('Let`s study!Today`s routine is \n\t\t\t\tSubject\t\t\t\tTime\n\tТехнологии Кроссплатформенного программирования 9:00-10:30 \n\tРазраб.мобильных компонентов анализа безопасного ПО 10:40-12:10\n\t Разраб.мобильных компонентов анализа безопасного ПО 12:40-14:10\n')
    if((weeks==6 and weeks==False and counterOfWeeks==2)or(weeks==6 and weeks==False and counterOfWeeks==6)or(weeks==6 and weeks==False and counterOfWeeks==10)or(weeks==6 and weeks==False and counterOfWeeks==14)):
        print('Let`s study!Today`s routine is \n\t\t\t\tSubject\t\t\t\tTime\n\tАлгоритмы компонентов цифровой обработки данных 9:00-10:30  \n')
    if((weeks==6 and weeks==False )):
        print('Let`s study!Today`s routine is \n\t\t\t\tSubject\t\t\t\tTime\n\tАлгоритмы компонентов цифровой обработки данных 9:00-10:30  \n')


def dayOfStudy():
    if(datetime.today().isoweekday()==1):
        print("Today is Monday")
        weekOfStudy(datetime.today().day,datetime.today().month,datetime.today().year,datetime.today().isoweekday())
    if(datetime.today().isoweekday()==2):
        print("Today is Tuesday")
        weekOfStudy(datetime.today().day,datetime.today().month,datetime.today().year,datetime.today().isoweekday())
    if(datetime.today().isoweekday()==3):
        print("Today is Wednesday")
        weekOfStudy(datetime.today().day,datetime.today().month,datetime.today().year,datetime.today().isoweekday())
    if(datetime.today().isoweekday()==4):
        print("Today is Thursday")
        weekOfStudy(datetime.today().day,datetime.today().month,datetime.today().year,datetime.today().isoweekday())
    if(datetime.today().isoweekday()==5):
        print("Today is Friday")
        weekOfStudy(datetime.today().day,datetime.today().month,datetime.today().year,datetime.today().isoweekday())
    if(datetime.today().isoweekday()==6):
        print("Today is Saturday")
        weekOfStudy(datetime.today().day,datetime.today().month,datetime.today().year,datetime.today().isoweekday())
    if(datetime.today().isoweekday()==7):
        print("Today is Sunday")   
        weekOfStudy(datetime.today().day,datetime.today().month,datetime.today().year,datetime.today().isoweekday())

def checkCredsMirea(log, passw):
    loadBar = "Trying to log in..."
   
    driver = webdriver.Chrome("chromedriver")
    driver.get("https://login.mirea.ru/login/?next=/oauth2/v1/authorize/%3Fresponse_type%3Dcode%26client_id%3DdnOh7sdtPxfyxzbxcMRLksWlCCE3WsgTfRY6AWKh%26redirect_uri%3Dhttps%253A%252F%252Fonline-edu.mirea.ru%252Flogin%252F%26scope%3Dbasic%2Bstudent")
    driver.find_element_by_id("id_login").send_keys(log)
    driver.find_element_by_id("id_password").send_keys(passw+Keys.ENTER)


    WebDriverWait(driver=driver, timeout=1).until(lambda x: x.execute_script("return document.readyState === 'complete'"))
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
    time.sleep(2)

    if(log.find("@edu.mirea.ru")!= -1):
        print('Mail validation sucessful')
        time.sleep(2)
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
            time.sleep(2)


def task():
    os.system('clear' if os.name == 'posix' else 'cls')
    print('Welcome to AutoLogginer Lite.\nWarning!We don`t collect/sell/store your logins & passwords \nVer 0.0.1(before release)\n')
    dayOfStudy()
    userCredL = input('Enter your MIREA login >> ')
    userCredP = getpass.getpass('Enter your MIREA password >> ')

    checkCredsLocal(userCredL,userCredP)


if __name__ == '__main__':
    task()