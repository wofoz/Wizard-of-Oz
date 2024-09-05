import random 
import time 
import os
import colorama
from time import sleep
from tqdm import tqdm
from bs4 import BeautifulSoup as htmlparser
import requests
from interface import logo


interface_choise = ["0 -- Phone lookup", "1 -- Credits", "2 -- Exit" ]


def main_menu():
   while True:
      os.system('cls')
      print(logo)
      print()
      print(*interface_choise, sep= "\n")
      print()
      user_mainmenu_choise = int(input(">>"))
      if user_mainmenu_choise == 0:
         doxx_needed_info()
      elif  user_mainmenu_choise == 1:
         print("Creator -- cawa")
         print("Some parts of code could be taken from https://github.com/lilmond/phone_lookup ")
         main_menu()
      elif user_mainmenu_choise == 2:  
         exit
      else:
         print("Wrong input, try again")
         time.sleep(2)
         main_menu()
      try:
             phone_number = input("Phone number: ").strip().replace("-", "").replace(" ", "").replace("+", "")
      except KeyboardInterrupt:
            return

      try:
            infos = lookup(phone_number)
      except AttributeError:
            print("Error: Invalid phone number\n")
            continue

      [print(f"{info}: {infos[info]}") for info in infos]
      print("\n")





def doxx_needed_info():

   try:
      number_input = input("Phone number of target>>").strip().replace("-", "").replace(" ", "").replace("+", "").replace("(", "").replace(")", "")
   except KeyboardInterrupt:
         return
   
   try:
      infos = lookup(number_input)
      [print(f"{info}: {infos[info]}") for info in infos]
      print("\n")

   except AttributeError:
      print("Error: Invalid phone number\n")
      doxx_needed_info


   
   


def lookup(number_input):
   os.system('cls')
   http = requests.get(f"https://free-lookup.net/{number_input}")
   html = htmlparser(http.text, "html.parser")
   infos = html.findChild("ul", {"class": "report-summary__list"}).findAll("div")
   return {k.text.strip(): infos[i+1].text.strip() if infos[i+1].text.strip() else "No information" for i, k in enumerate(infos) if not i % 2}
   

if __name__ == "__main__":
    main_menu()
