def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Clear List")
    print("5. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        match choice:
            case "1":
                item = input("Enter item name: ")
                shopping_list.append(item)
                print(f"'{item}' has been added to the list.")
                print(shopping_list)
            case "2":
                item = input("Enter item name to remove: ")
                if item in shopping_list:
                    shopping_list.remove(item)
                    print(f"'{item}' has been removed from the list.")
                else:
                    print(f"'{item}' not found in the list.")
            case "3":
                print("Shopping List:")
                print(shopping_list)
            case "4":
                shopping_list.clear()
                print("Shopping list cleared.")
            case "5":
                print("Goodbye!")
                break
            case _:
                print("Invalid choice.")

if __name__ == "__main__":
    main()