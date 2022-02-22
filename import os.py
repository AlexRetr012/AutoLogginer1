import os
import getpass
import calendar
from tabnanny import check
import time
from datetime import datetime,date
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

def penetrationToWebinars(http):
    print(http)


def setForATimer(pair):
    for p in pair:
        if p == 1:
            time_l=time.localtime()
            if (time.strftime('%H:%M:%S',time_l) >= "10:30:00"):  
                print('First pair is gone!\n')
        if p == 2:
            time_l=time.localtime()
            if (time.strftime('%H:%M:%S',time_l) >= "12:10:00"):
                print('Second pair is gone!\n')
        if p == 3:
            time_l=time.localtime() 
            if (time.strftime('%H:%M:%S',time_l) >= "14:10:00"):
                print('Third pair is gone!\n')
        if p == 4:
            time_l=time.localtime()
            if (time.strftime('%H:%M:%S',time_l) >= "15:50:00"):
                print('Fourth pair is gone!\n')
        if p == 5:
            time_l=time.localtime()
            if (time.strftime('%H:%M:%S',time_l) >= "17:50:00"):
                print('Fifth pair is gone!\n')
        if p == 6:
            time_l=time.localtime()
            if (time.strftime('%H:%M:%S',time_l) >= "19:30:00"):
                print('Sixth pair is gone!\n')
    print("Now time >> " + time.strftime('%H:%M:%S',time_l))
        
def weekOfStudy(day,month,year,week):
    weeks=False
    counterOfWeeks=0
    if (day >= 21 and day <= 26  and month ==2 and year == 2022 ):
        print("Odd week\n")
        weeks=True
        counterOfWeeks+=1
    if ((day >= 28 and month == 2 and year == 2022) or (day >=1 and day <= 6 and year == 2022 and month == 3)):
        print("Even week\n")
        weeks=False
        counterOfWeeks+=1
    
    if ((week==3 and weeks==True)or(week==4 and weeks==True)or(week==5 and weeks==True)or (week==6 and weeks==True)or(week==7 and weeks==True)or(week==1 and weeks==False)or(week==2 and weeks==False)or(week==5 and weeks==False)or(week==7 and weeks==False)):
        print('No stydy for today!!\n')
    if((week==1 and weeks==True and counterOfWeeks==5)or(week==1 and weeks==True and counterOfWeeks==9)or(week==1 and weeks==True and counterOfWeeks==13)or(week==1 and weeks==True and counterOfWeeks==15)):
        print('Let`s study!Today`s routine is \n\t\t\t\tSubject\t\t\t\tTime\n\tАлгоритмы компонентов п-п обработки и преобраз данных 9:00-10:30 \n\t\tМодели и методы принятия технических решений 10:40-12:10 \n\t Информационный технологии цифровой экономики 14:20-15:50\n')
        lessons = [1,2,4]
        less_http = ["https://online-edu.mirea.ru/course/view.php?id=8785","https://online-edu.mirea.ru/course/view.php?id=8794","https://online-edu.mirea.ru/course/view.php?id=8880"]
    if((week==1 and weeks==True)):
        print('Let`s study!Today`s routine is \n\t\t\t\tSubject\t\t\t\tTime\n\tАлгоритмы компонентов п-п обработки и преобраз данных 9:00-10:30 \n\t\tМодели и методы принятия технических решений 10:40-12:10 \n\t')
        lessons = [1,2]
        less_http = ["https://online-edu.mirea.ru/course/view.php?id=8785","https://online-edu.mirea.ru/course/view.php?id=8794"]
    if((week==2 and weeks==True)):
        print('Let`s study!Today`s routine is \n\t\t\t\tSubject\t\t\t\tTime\n\tМетоды и средства защиты компьютерной информации 9:00-10:30 \n\tМетоды и средства защиты компьютерной информации 10:40-12:10 \n\t')
        lessons = [1,2]
        less_http = ["https://online-edu.mirea.ru/course/view.php?id=8791","https://online-edu.mirea.ru/course/view.php?id=8791"]
    if((week==3 and weeks==False)):
        print('Let`s study!Today`s routine is \n\t\t\t\tSubject\t\t\t\tTime\n\tОсновы антикоррупционной деятельности 9:00-10:30 \n\t\tБЖД 10:40-12:10\n\t Методы и средства взаимодействия компонент ПО 12:40-14:10\n')
        lessons=[1,2,3]
        less_http = ["https://online-edu.mirea.ru/course/view.php?id=7948","https://online-edu.mirea.ru/course/view.php?id=563","https://online-edu.mirea.ru/course/view.php?id=8790"]
    if((week==4 and weeks==False)):
        print('Let`s study!Today`s routine is \n\t\t\t\tSubject\t\t\t\tTime\n\tТехнологии Кроссплатформенного программирования 9:00-10:30 \n\tРазраб.мобильных компонентов анализа безопасного ПО 10:40-12:10\n\t Разраб.мобильных компонентов анализа безопасного ПО 12:40-14:10\n')
        lessons = [1,2,3]
        less_http = ["https://online-edu.mirea.ru/course/view.php?id=8804","https://online-edu.mirea.ru/course/view.php?id=8800","https://online-edu.mirea.ru/course/view.php?id=8800"]
    if((week==6 and weeks==False and counterOfWeeks==2)or(week==6 and weeks==False and counterOfWeeks==6)or(week==6 and weeks==False and counterOfWeeks==10)or(week==6 and weeks==False and counterOfWeeks==14)):
        print('Let`s study!Today`s routine is \n\t\t\t\tSubject\t\t\t\tTime\n\tКомпьютерная криминалистика 9:00-10:30 \n\tКомпьютерная криминалистика 10:40-12:10\n\tАлгоритмы компонентов цифровой обработки данных 12:40-14:10  \n')
        lessons = [1,2,3]
        less_http = ["https://online-edu.mirea.ru/course/view.php?id=7824","https://online-edu.mirea.ru/course/view.php?id=7824","https://online-edu.mirea.ru/course/view.php?id=8786"]
    if((week==6 and weeks==False )):
        print('Let`s study!Today`s routine is \n\t\t\t\tSubject\t\t\t\tTime\n\tАлгоритмы компонентов цифровой обработки данных 12:40-14:10  \n')
        lessons = [3]
        less_http = ["https://online-edu.mirea.ru/course/view.php?id=8786"]
    setForATimer(lessons)
    penetrationToWebinars(less_http)

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
    os.system('cls||clear')

    WebDriverWait(driver=driver, timeout=10).until(lambda x: x.execute_script("return document.readyState === 'complete'"))
    error_message = "Указан неверный логин/пароль"
    errors = driver.find_elements_by_class_name("errorlist nonfield")
    print(errors)
    os.system('cls||clear')
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