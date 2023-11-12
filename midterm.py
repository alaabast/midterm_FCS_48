import webbrowser
import requests
import pathlib
import operator
import os
import json
website_dict = {}
def main():
    

    print("WELCOME!")
    while True:
        print("\nChoose an option from the list :\n ")
        print("1. Open Tab \n2. Close Tab \n3. Switch Tab \n4. Display All Tabs \n5. Open Nested Tab \n6. Clear All Tabs \n7. Save Tabs \n8. Import Tabs\n9. Exit")
        x = int(input("Your choose:"))



        if x == 1: #source: https://blog.finxter.com/how-to-open-a-url-in-your-browser-from-a-python-script/#:~:text=A%20short%20way%20of%20opening,string%20as%20a%20single%20argument.
            openTab()

        elif x == 2:
            closeTab()
            
        elif x==3: #source: https://stackoverflow.com/questions/3533528/python-web-crawlers-and-getting-html-source-code
             switchTab()
               
        elif x==4:
            displayTab()
            
        elif x == 6:
            website_dict={}
            
        elif x == 7: #source: https://realpython.com/lessons/serializing-json-data/
            saveTabs()
           
        elif x == 8: #source:https://www.geeksforgeeks.org/read-a-file-line-by-line-in-python/
            importTabs

        elif x == 9:
            # Exit the program.
            break

        else:
            print("Invalid choice.")

   
    print("End of the program \nThank you...")

    
def openTab():
    title = input("Enter the title of the website:")
    link = input("Enter the link of the website: ")
    website_dict[title] = link
    webbrowser.open(link)
    
 
    
 
def closeTab():
    
    index = input("Enter the title of the website :")
    if index in website_dict:
            t=index
            webbrowser.get(website_dict[t]).close_window()
    if index not in website_dict:
        print("This tab is not availble\n Closing the last tab...")
        keys_list = list(website_dict.keys())
        t = keys_list[-1]
        webbrowser.get(website_dict[t]).close_window()
    del website_dict[t]
    print(website_dict)




def switchTab():
    
    i = input("Enter the title of the website :")
    if i in website_dict:
        website_url = website_dict[i]
        req = requests.get(website_url) #create request 
        source = req.content #grt the page source
        source = source.decode() # convert it to string 
    else:
        
        print("this tab is not availble\n ")
        l1 = list(website_dict);
        website_url = l1[-1]
        req = requests.get(website_url) #create a request
        source = req.content #get the content of the page source
        source = source.decode() #convert it to string
    print("the page source is :\n")
    print(source)
                  
 
    
 
    
def displayTab():
    print("All open tabs:")
    for name,link in website_dict.items():
        print("_ "+name+"\n")   
    



def saveTabs():
    data = {}
    y=input("Enter the path of the file:\n")
    for k, v in website_dict.items():
        website_url = website_dict[k]
        req = requests.get(website_url)  # create request
        source = req.content  # get the page source
        source = source.decode()  # convert it to string
        data[k] = [v, source]

    with open(y +"data.json", "w", encoding="utf-8") as writing:
        json.dump(data, writing)
        

    


def importTabs():
    path=input("Enter the path of your file:\n")
    with open(path, "r") as f:
        for line in f:
            words = line.split()
            name = words[0]
            link = words[1]
            website_dict[name] = link
                   
    print(website_dict)

    




main()
