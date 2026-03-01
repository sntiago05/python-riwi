books = {
    1: "To Kill a Mockingbird",
    2: "1984",
    3: "The Great Gatsby",
    4: "Pride and Prejudice",
    5: "Moby-Dick",
}

borrowed_books = {}  # book_id: borrow_day
has_penalty = False
user = input("Ingresa tu nombre: ")
current_day = 1


def verify_penalty():
    for book_id, borrow_day in borrowed_books.items():
        if current_day - borrow_day > 4:
            return True
    return False


def show_main_menu():
    print(
        f"""<-- Welcome {user} -->
1. Borrow Book
2. Return Book
3. Pay Fine
4. Advance Day
5. Exit"""
    )


def show_borrow_menu():
    print("\n<-- Books Available to Borrow -->")
    available = False
    for book_id, title in books.items():
        if book_id not in borrowed_books:
            print(f"{book_id}. {title}")
            available = True
    if not available:
        print("No books available to borrow.")
    print("0. Back to Main Menu\n")


def show_return_menu():
    print("\n<-- Your Borrowed Books -->")
    if borrowed_books:
        for book_id, borrow_day in borrowed_books.items():
            days_left = 4 - (current_day - borrow_day)
            status = f"{days_left} days left" if days_left > 0 else "Overdue!"
            print(f"{book_id}. {books[book_id]} - {status}")
    else:
        print("You have no borrowed books.\n")
    print("0. Back to Main Menu\n")


def borrow_book():
    if verify_penalty():
        print("Please first pay your penalty.\n")
        return
    elif len(borrowed_books) >= 3:
        print("You can only borrow 3 books")
        return

    show_borrow_menu()
    book_id = int(input("Choose a book: "))
    if book_id in books and book_id not in borrowed_books:
        borrowed_books[book_id] = current_day
        print(f"You borrowed '{books[book_id]}' successfully!\n")
    elif book_id == 0:
        return
    else:
        print("Invalid choice.\n")


def return_book():
    global has_penalty
    show_return_menu()
    if borrowed_books:
        book_id = int(input("Choose a book to return: "))
        if book_id in borrowed_books:
            print(f"'{books[book_id]}' returned successfully.\n")
            borrowed_books.pop(book_id)
        elif book_id == 0:
            return
        else:
            print("Invalid choice.\n")


def advance_day():
    global current_day, has_penalty
    current_day += 1
    print(f"\nDay advanced! Today is day {current_day}.\n")
    has_penalty = verify_penalty()
    for book_id, borrow_day in borrowed_books.items():
        if current_day - borrow_day > 4:
            print(f"You have overdue book '{books[book_id]}'. Penalty applied!\n")


while True:
    show_main_menu()
    option = int(input("Choose an Option: "))
    match option:
        case 1:
            borrow_book()
        case 2:
            return_book()
        case 3:
            if has_penalty:
                has_penalty = False
                print("Your penalty has been cleared. You can borrow books again.\n")
            else:
                print("You currently have no penalties.\n")
        case 4:
            advance_day()
        case 5:
            print("Bye!")
            break
