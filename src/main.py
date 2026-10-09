def display_welcome(): # display_welcome() - This function displays the application's welcome message.
    print("=" * 45)
    print("   PLACEMENT INTELLIGENCE PLATFORM")
    print("=" * 45)
    print("Your personal placement preparation assistant!")
    print("Track skills. Improve performance. Get placement-ready.")


def main(): #main()- This is the main entry point for our application. As the project grows, it will coordinate the different features.
    display_welcome()


if __name__ == "__main__": #if __name__ == "__main__":- This ensures that main() runs when you execute this file directly, but not simply when another Python module imports it.
    main()