import wikipedia
import pyttsx3
from botex import robot_voice_speech,open_notpad,write_and_save,create_contact_table,add_contact,search_contact,send_whatsapp_message,information,informationsearch,songs,open_system_camera,closesong,user_data,fetch_user_all_data
import subprocess
import pyautogui
import time
from datetime import datetime
import datetime
import os
def simple_chatbot():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        robot_voice_speech("Good Morning!")
    elif hour>=12 and hour<18:
        robot_voice_speech("Good Afternoon!")
    else:
        robot_voice_speech("Good Evening")
    print("Hello I'm your AI friend.")
    robot_voice_speech("Hello I'm your AI friend")

    while True:
        user_input=input("You: ")
        if user_input.lower() in ["bye","BYE","ok bye","Ok Good bye","Bye"]: 
                        hour = int(datetime.datetime.now().hour)
                        if hour>=0 and hour<12:
                            robot_voice_speech("Good Morning!")
                            print("Good Morning!")
                        elif hour>=12 and hour<18:
                            robot_voice_speech("Good Afternoon!")
                            print("Good Afternoon!")
                        else:
                            robot_voice_speech("Good Evening")
                            print("Good Evening")
                        print("Goodbye! have a great day.")
                        robot_voice_speech("AI:Goodbye! have a great day.")
                        exit()
                        
        elif user_input.lower() in ["HI","hi","hello"]:
            print("Hi,how can I help?")
            robot_voice_speech("Hi, how can I help?,I can I assist today?")
        elif user_input.lower() in ["good morning!","good afternoon!","good evening!"]:
            hour = int(datetime.datetime.now().hour)
            if hour>=0 and hour<12:
                    if user_input.lower() in ["good morning!"]:
                        print("Good Morning!How can I help you today!")
                        robot_voice_speech("Good Morning!How can I help you today!")
            elif hour>=12 and hour<18:
                    if user_input.lower() in ["good afternoon!"]:
                        print("Good Afternoon!How can I help you today!")
                        robot_voice_speech("Good Afternoon!How can I help you today!")
            elif user_input.lower() in ["good evening!"]:
                    print("Good Evening!How can I help you today!")
                    robot_voice_speech("Good Evening!How can I help you today!")

        elif user_input.lower() in ["your working"]:
            print("I am Artificial intelligence")
            robot_voice_speech("I am Artificial intelligence")
            print("AI (Artificial Intelligence) is the simulation of human intelligence processes by machines, including learning, reasoning, and self-correction. It utilizes algorithms to analyze data, make predictions, and automate tasks, enabling systems to perceive, comprehend, and act upon information. AI applications range from virtual assistants and recommendation systems to autonomous vehicles and medical diagnosis.")
            robot_voice_speech("AI (Artificial Intelligence) is the simulation of human intelligence processes by machines, including learning, reasoning, and self-correction. It utilizes algorithms to analyze data, make predictions, and automate tasks, enabling systems to perceive, comprehend, and act upon information. AI applications range from virtual assistants and recommendation systems to autonomous vehicles and medical diagnosis.")

        elif user_input.lower() in ["the time","today date"]:
                current_time=time.localtime()
                formatted_time=time.strftime(" %H:%M:%S",current_time)
                date = time.strftime("%Y-%m-%d ")
                #Print the formatted time
                if user_input.lower() in ["today date"]:
                    print("Today Date:",date)
                    robot_voice_speech(f"Today Date:{date}")
                elif user_input.lower() in ["the time"]:
                    print("Current Time:",formatted_time)
                    robot_voice_speech(formatted_time)

        elif user_input.lower() in ["notepad"]:
             noteped_text=str(input("Enter the contents->"))
             file_name=str(input("Enter the file name(.txt):"))
             open_notpad()
             write_and_save(noteped_text,file_name)
             robot_voice_speech("Your Notepad is save successfully...")

        elif user_input.lower() in ["wikipedia","wikipedia open","open to wikipedia"]:
            robot_voice_speech("Open wikipedia")
            print("Opening widipedia!....")
            voice=pyttsx3.init()
            try:
                input_data=str(input("Enter the Content-->"))
                sent=int(input("Enter the sentences-->"))
                wiki=wikipedia.summary(f"{input_data}",sentences={sent})
                print(f"search:{wiki}")
                robot_voice_speech(wiki)
            except:
                 robot_voice_speech("Not connect internet!..")
                 print("Not connect internet!..")
                 

        elif user_input.lower() in ["thank you","thanks"]:
             print("You're welcome! If you have any more questions or need further information, feel free to ask!")
             robot_voice_speech("You're welcome! If you have any more questions or need further information, feel free to ask!")
             
             
        elif user_input.lower() in ["shutdown in my Pc","shutdown",]:
            #shutdown in pc (YES/NO)
            a=str(input("Last time your PC Shutdown(YES/NO)-->"))
            if a=="NO":
                 robot_voice_speech("No shutdown in pc")
            elif a=="YES":
                 robot_voice_speech("Your PC shutdown...")
                 os.system("shutdown/s /t 1")


        elif user_input.lower() in ["open my contacts"]:
            def main():
                while True:
                    create_contact_table()
                    print("1.Add Contact \n 2.Search Contact \n 3.Exit")
                    user_choice = input("Enter the your Choice:")
                    if user_choice == '1':
                        name = input("Enter the cotact name:")
                        phone_number = input("Enter the Phone Number:")
                        add_contact(name,phone_number)
                        print("This Contact in save !...")
                        robot_voice_speech("This Contact in save !...")
                    elif user_choice == '2':
                        name = input("Enter Name to Search:")
                        phone_number = search_contact(name)
                        if phone_number:
                            print(f"Phone number for {name}:{phone_number}")
                        else:
                            print(f"No contact found with the name '{name}'.")
                    elif user_choice == '3':
                        print("Exiting....")
                        break
                    else:
                        print("Invalid choice .Please try again.")
            if __name__ == "__main__":
                 main()

        elif user_input.lower() in ["whatsapp auto message"]:
             robot_voice_speech("Whatsapp auto message on...")
             name =input("Enter the contact name:")
             message = input("Enter message:")
             timer=int(input("Enter time set to  the timer(one second:1,one minute:100,one hour:10000):"))
             send_whatsapp_message(name,message,timer)
        elif user_input.lower() in ["music time on"]:
             robot_voice_speech("Music time is on,type your favourite song name")
             fav_song=input("Enter the Song Name:")
             songs(fav_song)
             print("playing song...")
             robot_voice_speech("Playing song...")
        elif user_input.lower() in ["information bank"]:
            print("Hi sir,you tell me the information and I will save it")
            robot_voice_speech("Hi sir,you tell me the information and I will save it")
            insert_infor=input("Enter the information:")
            insert_id=input("Enter the information Key:")
            information(insert_id,insert_infor)
            print("sir,I have saved what you gave")
            robot_voice_speech("sir,I have saved what you gave")
        elif user_input.lower() in ["search information bank"]:
            print("Are you going to look at the information you gave me?")
            choice = input("Enter the (Yes/No):")
            if choice.lower() in ["YES","yes","y","Y","Yes"]:
                search_infor=input("Enter the information ID:")
                informa=informationsearch(search_infor)
                if informa:
                    print(f"Take it:{informa}")
                else:
                    print("Not found in id and information..!")
            else:
                 print("Ok sir!..")
                 robot_voice_speech("Ok sir")
        elif user_input.lower() in ["open camera"]:
            robot_voice_speech("open camera")
            open_system_camera()
            print("image save!")
            robot_voice_speech("image save!")
        
        elif user_input.lower() in ["music time off"]:
             closesong()
             print("music time is close...!")
             robot_voice_speech("music time close...!")
        elif user_input.lower() in ["user data create"]:
             user_id = int(input("Enter user_id:"))
             username = input("Enter username: ")
             email = input("Enter email: ")
             address = input("Enter address: ")
             password = input("Enter password: ")
             date_of_birth = input("Enter date of birth (YYYY-MM-DD): ")
             user_data(user_id,username, email, address, password, date_of_birth)
             robot_voice_speech("your data is succfully create..!")
             print("your data is succfully create..!")


        elif user_input.lower() in ["user data"]:
             print("User data")
             robot_voice_speech("User data")
             fetch_user_all_data()
                 
        else:
            print("I'm just a simple AI friend.You said:",user_input)
        
if __name__=="__main__":
    simple_chatbot()