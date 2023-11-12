# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 07:57:37 2023

@author: Lenovo
"""
import webbrowser
       
def main():
    website_dict = {}
    print("WELCOME!")
    while True:
        print("\nChoose a option from the list :\n ")
        print("1. Open Tab \n2. Close Tab \n3. Switch Tab \n4. Display All Tabs \n5. Open Nested Tab \n6. Clear All Tabs \n7. Save Tabs \n8. Import Tabs\n9. Exit")
        x = int(input("Your choose:"))
        if x == 1:
            title=input("Enter the title of the website")                
            link = input("Enter the link of the website: ")
            website_dict[title] =link
            openNewTab(link)
        if x==2:
            index=input("Enter the title of the website :")
        



def openNewTab(link):      
    webbrowser.open(link) #the source: https://blog.finxter.com/how-to-open-a-url-in-your-browser-from-a-python-script/
    
    
    
    
    
main()