import webbrowser

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
                webbrowser.get(website_dict[index]).close()
            else:
                print("this tab is not availble\n Closing the last tab...")
                l = list(website_dict);
                last_link = l[-1]
                webbrowser.get(last_link).close()
       if x==3:
           

def openNewTab(link):
    webbrowser.open(link)

main()
