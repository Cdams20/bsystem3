import calendar
import csv
import tkinter as tk
from cProfile import label
from easygui import *

import eg as eg
import tkcalendar

k = open("test.csv", 'a')
f = open("test.txt", 'a')

firstname = input("What is your firstname?: ")
surname = input("What is your lastname?: ")
age = int(input("What is your age?: "))

# message to be displayed
textGender = "What is your gender?"

# window title
titleGender = "Gender"

# item choices
choicesGender = ["Male", "Female", "Other"]

# creating a button box
output = choicebox(textGender, titleGender, choicesGender)

# title for the message box
title = "Message Box"

# message
messageGender = "You selected : " + str(output)

# creating a message box
msg = msgbox(messageGender, title)

country = input("Which country do you live in?: ")
city = input("Which city do you live in?: ")
phoneNumber = int(input("What is your phone number?: "))
eMail = input("What is your E-Mail?: ")
Height = int(input("How tall are you in centimeters?: "))
Weight = int(input("How much do you weigh in kilograms?: "))
Smoke = input("Do you smoke? If yes, please specify how many cigarettes you approximately smoke per day: ")
# message to be displayed
textSmoke = "Do you smoke? If yes, how may your smoking be categorized?"

# window title
titleGender = "Gender"

# item choices
choicesGender = ["Male", "Female", "Other"]

# creating a button box
output = choicebox(textGender, titleGender, choicesGender)

# title for the message box
title = "Message Box"

# message
messageGender = "You selected : " + str(output)

# creating a message box
msg = msgbox(messageGender, title)

Diabetes = input("Do you have any sort/type of diabetes?: ")
Hypertension = input("Do you have Hypertension?: ")
CardiacDiseases = input("Do you have any cardiac diseases?: ")
other = input("Do you have any other conditions?: ")
Operation = input("Which area of your body do you wished to have changed? please specify: ")
print("We can have our online consultation in WhatsApp, Instagram, Skype, Zoom, or Facebook Messenger.")
Platform = input("In which platform, do you wish to have the consultation?")
OnlineConsultation = input("What is your account information on this platform?: ")
print("The calendar for the year 2021 is: " + calendar.calendar(2021, 2, 1, 6))
Date = int(input("Please have a look at the calendar, and choose a date for the online consultation: YYYY-MM-DD "))

f.write(f"Name: {firstname}\n")
f.write(f"Name: {surname}\n")
f.write(f"Age: {age}\n")
f.write(f"Gender: {messageGender}\n")
f.write(f"The patient reside in: {country}\n")
f.write(f"In the city of: {city}\n")
f.write(f"The patient's phone number is: {phoneNumber}\n")
f.write(f"The patient's email is: {eMail}\n")
f.write(f"The height of the patient is :{Height}\n")
f.write(f"The weight of the patient is: {Weight}\n")
f.write(f"Does the patient smoke, if yes, how much?: {Smoke}\n")
f.write(f"Does the patient has Diabetes?: {Diabetes}\n")
f.write(f"Does the Patient has Hypertension?: {Hypertension}\n")
f.write(f"Does the patient has any sort of cardiac diseases?: {CardiacDiseases}\n")
f.write(f"Does the patient has any other condition?: {other}\n")
f.write(f"Which operation or area of the body does the patient wish the get surgery on?: {Operation}\n")
f.write(f"The platform for the consultation is: {Platform}\n")
f.write(f"The patient's account information for the platform is: {OnlineConsultation}\n")
f.write(f"{Date}\n")

# if date is true
#   set date
# print("please specify your wished time, then i'll get back to you about the specific time")


root = tk()
root.title("Calendar")

cal = calendar(root, selectmode="day", year=2021, month=5, day=22)
cal.pack(pady=21)


def grab_date():
    my_label.config(text=cal.get_date())


my_button = tk.Button(root, text="Get Date", command=grab_date)
my_button.pack(pady=21)

my_label = label(root, text="")
my_label.pack(pady=21)

root.mainloop()
