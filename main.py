import webbrowser

# Pre-defined Google dorks for each category
dorks = {
    "movies": [
        "intitle:index.of? mkv {}",
        "intitle:index.of? avi {}",
        "intitle:index.of? mp4 {}",
        "intitle:index.of? mkv {} parent directory",
        "intitle:index.of? avi {} parent directory",
        "intitle:index.of? mp4 {} parent directory",
    ],
    "music": [
        "intitle:index.of? mp3 {}",
        "intitle:index.of? ogg {}",
        "intitle:index.of? flac {}",
        "intitle:index.of? mp3 {} parent directory",
        "intitle:index.of? ogg {} parent directory",
        "intitle:index.of? flac {} parent directory",
    ],
    "drive": [
        "site:drive.google.com {}",
        "intitle:index.of? {} site:drive.google.com",
        "intitle:index.of? {} parent directory site:drive.google.com",
    ],
    "courses": [
        "intitle:index.of? {} site:udemy.com",
        "intitle:index.of? {} site:coursera.org",
        "intitle:index.of? {} site:udacity.com",
        "intitle:index.of? {} site:edx.org",
    ],
    "books": [
        "intitle:index.of? pdf {}",
        "intitle:index.of? epub {}",
        "intitle:index.of? mobi {}",
        "intitle:index.of? pdf {} parent directory",
        "intitle:index.of? epub {} parent directory",
        "intitle:index.of? mobi {} parent directory",
    ],
    "softwares": [
        "intitle:index.of? exe {}",
        "intitle:index.of? dmg {}",
        "intitle:index.of? deb {}",
        "intitle:index.of? rpm {}",
        "intitle:index.of? exe {} parent directory",
        "intitle:index.of? dmg {} parent directory",
        "intitle:index.of? deb {} parent directory",
        "intitle:index.of? rpm {} parent directory",
    ],
    "pc games": [
        "intitle:index.of? iso {}",
        "intitle:index.of? rar {}",
        "intitle:index.of? zip {}",
        "intitle:index.of? iso {} parent directory",
        "intitle:index.of? rar {} parent directory",
        "intitle:index.of? zip {} parent directory",
    ],
    "android games": [
        "intitle:index.of? apk {}",
        "intitle:index.of? obb {}",
        "intitle:index.of? apk {} parent directory",
        "intitle:index.of? obb {} parent directory",
    ],
    "wikipedia": [
        "intitle:index.of? wikipedia {}",
        "intitle:index.of? wikipedia {} parent directory",
    ],
    "essay": [
        "intitle:index.of? essay {}",
        "intitle:index.of? essay {} parent directory",
    ]
}

def search_category(category):
    """Prompt the user to enter the name of the content they want to search for,
    then construct and perform a Google search using the appropriate dorks for the
    specified category.
    """
    name = input("Enter the name of the {}: ".format(category))
    dork_list = dorks[category]
    for dork in dork_list:
        query = dork.format(name)
        url = "https://www.google.com/search?q={}".format(query)
        webbrowser.open_new_tab(url)

def main():
    """Main function that prompts the user to select a category and searches for
    the specified content using Google dorks.
    """
    print("Select a category:\n1. Movies\n2. Music\n3. Google Drive files\n4. Courses\n5. Books\n6. Softwares\n7. Pc Games\n8. Android games\n9. Wikipedia\n10.Essay")
    choice = input("Enter the category number: ")
    if choice == "1":
        search_category("movies")
    elif choice == "2":
        search_category("music")
    elif choice == "3":
        search_category("drive")
    elif choice == "4":
        search_category("courses")
    elif choice == "5":
        search_category("books")
    elif choice == "6":
        search_category("softwares")
    elif choice == "7":
        search_category("pc games")
    elif choice == "8":
        search_category("android games")
    elif choice == "9":
        search_category("wikipedia")
    elif choice == "10":
        search_category("essay")
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == '__main__':
    main()
