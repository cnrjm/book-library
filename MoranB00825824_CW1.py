book_list = []
book_count = 0
book_data = open("bookData", 'r')

for row in book_data:
    if not row.startswith('#'):
        row = row.rstrip('\n').split(',')
        book_list.append(row)
        book_count += 1


def option1():
    for each_book in book_list:
        print('Author, Title, Format, Publisher, Cost, Stock, Genre \n', each_book, '\n')

    total_value = 0
    total_books = 0
    for book in book_list:
        total_value += float(book[4]) * float(book[5])
        total_books += 1

    print("The total number of book titles is ", total_books)
    print("The total value of all books in stock is ", "£", format(total_value, ',.2f'))

    menu()


def option2():
    avg_price = 0
    for book in book_list:
        if float(book[5]) > 0:
            avg_price += float(book[4]) / float(book_count)

    print("The average price of books in stock is ", "£", format(avg_price, ',.2f'))

    menu()


def option3():
    fiction = 0
    biography = 0
    science = 0
    religion = 0

    for book in book_list:
        if book[6].strip() == "fiction":
            fiction += 1
        if book[6].strip() == "biography":
            biography += 1
        if book[6].strip() == "science":
            science += 1
        if book[6].strip() == "religion":
            religion += 1

    print("fiction: ", fiction, '\n' "biography: ", biography, '\n' "science: ", science, '\n' "religion: ", religion)

    menu()


def option4():
    old_avg_price = 0
    for book in book_list:
        if float(book[5]) > 0:
            old_avg_price += float(book[4]) / float(book_count)

    old_total_books = 0
    for book in book_list:
        old_total_books += 1

    author = input("Who is the author of the book? ")
    title = input("What is the title of the book? ")
    format = input("What is the format of the book? ")
    publisher = input("Who is the publisher of the book? ")
    cost = input("How much does the book cost? ")
    stock = input("How much stock do we have of the book? ")
    genre = input("What genre is the book? ")

    new_book = author, title, format, publisher, cost, stock, genre
    book_list.append(new_book)

    for each_book in book_list:
        print('Author, Title, Format, Publisher, Cost, Stock, Genre \n', each_book, '\n')

    new_avg_price = 0
    for book in book_list:
        if float(book[5]) > 0:
            new_avg_price += float(book[4]) / float(book_count)

    new_total_books = 0
    for book in book_list:
        new_total_books += 1

    x = new_avg_price - old_avg_price
    float(x)

    y = new_total_books - old_total_books
    float(y)

    print("The average price of books in stock has changed by: £", x)
    print("The change in total book titles is: ", y)

    menu()


def option5():
    book_title = input("Enter the book title you are trying to search for: ")
    for book in book_list:
        if book_title in book[1]:
            print("The amount of stock for that book is:", book[5])

    adjusted_stock = input("How much would you like to increase or decrease the stock by (Please use -x for decrease)? ")

    for book in book_list:
        if book_title in book[1]:
            new_stock = int(book[5]) + int(adjusted_stock)
            print("The amount of stock for that book is now: ", new_stock)

    for book in book_list:
        if book_title in book[1] and new_stock <= 0:
            print("This book is now out of stock")

    menu()


def option6():
    titlel = []
    for book in book_list:
        #print(book[1])
        x = (book[1])
        titlel.append(x)
    print(sorted(titlel))

    menu()

def menu():
    option = input("1. List of book titles, plus summary report" '\n' "2. Average price of books in stock" '\n' "3. Number of books in each genre" '\n' "4. Add new book and show updated summary report" '\n' "5. Check if book title is available and change stock level" '\n' "6. Return book list in alphabetical order by title" '\n' "8. Exit" '\n' "Please select an option: ")

    if option == "1":
        option1()
    elif option == "2":
        option2()
    elif option == "3":
        option3()
    elif option == "4":
        option4()
    elif option == "5":
        option5()
    elif option == "6":
        option6()
    elif option == "8":
        quit()

menu()