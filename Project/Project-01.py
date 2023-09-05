import os.path
from time import sleep as sl
from colorama import Fore
from os import system as sy
from datetime import datetime
import schedule
from sys import stdout as std

now = datetime.now()
def list_f():
    list_file = os.listdir("Files/txt/")
    result = ""

    for l in list_file:
        result += l + "\n"

    return result

def delete(na):
    try:
        os.remove("Files/txt/" + na + ".txt")

    except:
        print("Error")
        sl(0.5)
        sy(b)

def check_day():
    day_w = now.strftime("%A")
    return day_w

day = check_day()

def read(txtn):
    try:
        with open("Files/txt/" + txtn + ".txt", "r") as file:
            data = file.read()
            print(data)
            file.close()

    except:
        print("Error 404")

def write(text, name):
    try:
        full_path = os.path.join("Files/txt/", name + ".txt")
        with open(full_path, 'a') as file:
            file.write(text + "\n")
            print("Записано!")
            file.close()

    except:
        print("Error 404")

days = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday"
}

def check_time():

    if day == days[1]:
        print(f"{Fore.RED}Today: {Fore.CYAN}" + days[1])
        print(f"""
{Fore.RED}9:00-10:00

{Fore.RED}10:10-11:00          {Fore.CYAN}МАТЕМАТИКА

{Fore.RED}11:20-12:20          {Fore.CYAN}ФИЗИКА

{Fore.RED}12:30-13:40          {Fore.CYAN}ТЕХНОЛОГИИ


        """)

    elif day == days[2]:
        print(f"{Fore.RED}Today: {Fore.CYAN}" + days[2])
        print(f"""
{Fore.RED}9:00-10:00           {Fore.CYAN}БИОЛ/ЗАХ

{Fore.RED}10:10-11:00          {Fore.CYAN}КУЛЬТУРОЛОГИЯ

{Fore.RED}11:20-12:20          {Fore.CYAN}ИНФОРМАТИКА

{Fore.RED}12:30-13:40          {Fore.CYAN}УКР. МОВА


        """)

    elif day == days[3]:
        print(f"{Fore.RED}Today: {Fore.CYAN}" + days[3])
        print(f"""
{Fore.RED}9:00-10:00           {Fore.CYAN}ГЕОГРАФИЯ

{Fore.RED}10:10-11:00          {Fore.CYAN}ФИЗ - РА

{Fore.RED}11:20-12:20          {Fore.CYAN}МАТЕМАТИКА

{Fore.RED}12:30-13:40          {Fore.CYAN}УКР. ЛИТ


        """)

    elif day == days[4]:
        print(f"{Fore.RED}Today: {Fore.CYAN}" + days[4])
        print(f"""
{Fore.RED}9:00-10:00           {Fore.CYAN}ЗАХ. УКР

{Fore.RED}10:10-11:00          {Fore.CYAN}БИОЛОГИЯ

{Fore.RED}11:20-12:20          {Fore.CYAN}ВСЕСВ. ИСТ

{Fore.RED}12:30-13:40          {Fore.CYAN}ВИХ. ГОД


        """)

    elif day == days[5]:
        print(f"{Fore.RED}Today: {Fore.CYAN}" + days[5])
        print(f"""
{Fore.RED}9:00-10:00           {Fore.CYAN}ФИЗИКА

{Fore.RED}10:10-11:00          {Fore.CYAN}ЗАР. ЛИТ

{Fore.RED}11:20-12:20          {Fore.CYAN}АНГЛ. ЯЗ

{Fore.RED}12:30-13:40          {Fore.CYAN}ХИМИЯ


        """)

    else:
        print(f"{Fore.LIGHTRED_EX}Chill")

a = "cls"
b = a

flo = list_f()

def main_menu():
    print(Fore.RESET)
    print(f'''
█▀▀ █▀█ █░░ █░░ █▀▀ █▀▀ █▀▀
█▄▄ █▄█ █▄▄ █▄▄ ██▄ █▄█ ██▄

 {Fore.LIGHTGREEN_EX}=========by ImPuLSe=========

{Fore.RED}1) {Fore.CYAN}Расписание
{Fore.RED}2) {Fore.CYAN}Заметки
{Fore.RED}3) {Fore.CYAN}выход
    ''')

while True:
    try:

        main_menu()
        inp1 = input(f"{Fore.LIGHTRED_EX}Выберите: {Fore.CYAN}")

        if inp1 == "1":
            sl(0.5)
            sy(b)
            check_day()
            day = check_day()
            check_time()
            if input("Enter: "):
                pass

        elif inp1 == "2":
            sl(0.5)
            sy(b)
            while True:
                print(f"""
Добро пожаловать!
                
{flo}
                
{Fore.RED}1. {Fore.CYAN}Записать заметку
{Fore.RED}2. {Fore.CYAN}Читать заметку
{Fore.RED}3. {Fore.CYAN}Удалить заметку
{Fore.RED}4. {Fore.CYAN}Выход
                """)

                inp2 = input("Choose: ")

                if inp2 == "1":
                    nam = input("Название заметки: ")
                    zam = input("Заметка: ")
                    write(zam,nam)
                    sl(0.5)
                    sy(b)

                if inp2 == "2":
                    nam = input("Название заметки: ")
                    read(nam)
                    input("Enter: ")
                    sl(0.5)
                    sy(b)

                elif inp2 == "3":
                    print("\n")
                    name = input("Имя записки: ")
                    delete(name)
                    sl(0.5)
                    sy(b)
                    break

                elif inp2 == "4":
                    break


        elif inp1 == "3":
            break

        else:
            print("\nОшибка 404")
            sl(1)
            sy(b)

    except:
        print("Ошибка 404")