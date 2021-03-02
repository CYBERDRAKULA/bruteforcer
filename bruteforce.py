import random
import pyautogui

lette = "abcdefghijklmnopqrstuvwxyz1234567890"
lette_list = list(lette)


password = pyautogui.password("enter a password : ")

guess_password = ""

while(guess_password != password):
    guess_password = random.choices(lette_list, k=len(password))

    print("cyber"+ str(guess_password)+ "drakula")

    if(guess_password == list(password)):
        print("your password is : "+ "".join(guess_password))
        break

