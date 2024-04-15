import pyttsx3
import sqlite3
import datetime
import pyautogui
import pygetwindow
import time
from datetime import datetime,timedelta
import subprocess
from tkinter import messagebox
import tkinter as tk
def robot_voice_speech(message):
    #Initialize the text-to-speech engine
    engine=pyttsx3.init()
    #Set properties (optional)
    engine.setProperty('rate',150)#Speed of speech
    engine.setProperty('volume',0.9)#Volume level (0.0 to 1.0)
    #use a robot voice
    engine.setProperty('voice',engine.getProperty('voices')[1].id)
    #Convert text to speech
    engine.say(message)
    engine.runAndWait()
if __name__=="__main__":
    user_message="I am BOT"
    robot_voice_speech(user_message)


def open_notpad():
    subprocess.Popen(['notepad.exe'])
    time.sleep(1)
def write_and_save(text,filename):
    pyautogui.typewrite(text)
    pyautogui.hotkey('ctrl','s') #Save
    time.sleep(1)
    pyautogui.typewrite(filename)
    pyautogui.press('enter')
if __name__=="__main__":
    open_notpad()

    content_to_write="Hello,this is a sample text."
    save_file_name="example.txt"
    write_and_save(content_to_write,save_file_name)
def messageshow(mess):
    messagebox.showinfo(mess)

def create_contact_table():
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS contacts (id INTEGER PRIMARY KEY,name TEXT,phone_number TEXT)''')
    conn.commit()
    conn.close()

def add_contact(name,phone_number):
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute("INSERT INTO contacts (name,phone_number) VALUES (?,?)",(name,phone_number))
    conn.commit()
    conn.close()

def search_contact(name):
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute("SELECT phone_number FROM contacts WHERE name=?",(name,))
    result = c.fetchone()
    conn.close()
    if result:
        return result[0]
    else:
        return None
def send_whatsapp_message(name,message,timer):
    #Press Windows key to open Start menu
    time.sleep(timer)
    pyautogui.press('win',interval=0.5)
    time.sleep(1)

    #Type 'whatsapp' to search for the app
    pyautogui.write('Whatsapp',interval=0.5)
    time.sleep(1)

    #Press Enter to open WhatsApp
    pyautogui.press('enter',interval=0.5)
    time.sleep(3) #Adjust this sleep time as needed for Whatsapp to open

    #Click on the search bar
    pyautogui.click(x=811,y=92)
    time.sleep(1)

    #Type the name of the contact/group to whom you want to send the message
    pyautogui.write(name,interval=0.5)
    time.sleep(1)

    #Click on the search result to open the chat
    pyautogui.click(x=915,y=341)
    time.sleep(2)

    #Write the message usig pyautogui.write()
    pyautogui.write(message,interval=0.5)


    #Press Enter to send the message
    pyautogui.press('enter',interval=0.5)

    #Close Whatsapp
    pyautogui.click(x=1536,y=975)
    pyautogui.click(x=1675,y=30)

def songs(songname):
    pyautogui.press('win',interval=0.5)
    time.sleep(1)
    pyautogui.write('YouTube',interval=0.5)
    time.sleep(1)
    pyautogui.press('enter',interval=0.5)
    time.sleep(30)
    pyautogui.click(x=743,y=72)
    pyautogui.write(songname,interval=0.5)
    time.sleep(1)
    pyautogui.click(x=1255,y=68)
    time.sleep(1)
    pyautogui.click(x=659,y=351)
    time.sleep(8)
    pyautogui.click(x=1251,y=712)
    time.sleep(6)
    pyautogui.click(x=1777,y=7)
    time.sleep(2)

def information(id,information):
    conn = sqlite3.connect('information.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS data (id TEXT NOT NULL,Information TEXT NOT NULL)''')
    c.execute("INSERT INTO data (id,Information) VALUES (?,?)",(id,information))
    conn.commit()
    conn.close()
def informationsearch(search):
    conn = sqlite3.connect('information.db')
    c = conn.cursor()
    c.execute("SELECT information FROM data WHERE id=?",(search,))
    result = c.fetchone()
    conn.close()
    if result:
        return result[0]
    else:
        return None
def open_system_camera():
        pyautogui.press('win')
        time.sleep(1)
        pyautogui.write('Camera')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(3)
        pyautogui.click(x=1361,y=535)
        time.sleep(3)
        pyautogui.click(x=1402,y=30)
        time.sleep(1)

def closesong():
    pyautogui.click(x=1181,y=1049)
    time.sleep(5)
    pyautogui.click(x=1890,y=17)

def user_data(id,username,email,address,password,date_of_birth):
    conn = sqlite3.connect("user_info.db")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS users(
                id TEXT NOT NULL,
                username TEXT NOT NULL,
                email TEXT NOT NULL,
                address TEXT NOT NULL,
                password TEXT NOT NULL,
                date_of_birth TEXT NOT NULL
    )''')
    cur.execute("INSERT INTO users (id,username,email,address,password,date_of_birth) VALUES (?,?,?,?,?,?)",(id,username,email,address,password,date_of_birth))
    conn.commit()
def fetch_user_all_data():
    conn = sqlite3.connect("user_info.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    for row in rows:
        print(row)