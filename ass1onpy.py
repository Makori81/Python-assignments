def main():
    # Prompt the user to enter a list of names
    names_input = input("Enter a list of names, separated by commas: ")

    # Split the input into a list of names and remove any surrounding spaces
    names_list = [name.strip() for name in names_input.split(",")]

    # Count the total number of names entered
    total_names = len(names_list)

    # Remove duplicates by converting the list to a set, then convert back to a list
    unique_names = list(set(names_list))

    # Sort the names in alphabetical order
    sorted_names = sorted(unique_names)

    # Display the final sorted list and the total number of names
    print("Final sorted list of names:", sorted_names)
    print("Total number of names entered:", total_names)

# Call the main function to run the program
if __name__ == "__main__":
    main()
