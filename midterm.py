import webbrowser
import urllib.request
import requests


def main():
    website_dict = {}

    print("WELCOME!")
    while True:
        print("\nChoose an option from the list :\n ")
        print("1. Open Tab \n2. Close Tab \n3. Switch Tab \n4. Display All Tabs \n5. Open Nested Tab \n6. Clear All Tabs \n7. Save Tabs \n8. Import Tabs\n9. Exit")
        x = int(input("Your choose:"))

        if x == 1:
            title = input("Enter the title of the website:")
            link = input("Enter the link of the website: ")
            website_dict[title] = link

            openNewTab(link)


        if x == 2:
            index = input("Enter the title of the website :")
            if index in website_dict:
                linkk=website_dict[index]
            else:
                print("this tab is not availble\n Closing the last tab...")
                l = list(website_dict);
                linkk = l[-1]
            webbrowser.get(linkk).close()
            
            
        if x==3:
            i = input("Enter the title of the website :")
            if i in website_dict:
                website_url = website_dict[i]
            else:
                print("this tab is not availble\n ")
                l1 = list(website_dict);
                website_url = l1[-1]
            neww="view-source:" + website_url
            webbrowser.open_new_tab(neww)

           
            
            
                
                
                
            
           

def openNewTab(link):
    webbrowser.open(link)

main()
