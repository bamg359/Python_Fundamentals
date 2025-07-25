
friends = {}
books = {}
booking = {}

def createFriend():

    friend = []

    id_friend = int(input("Id Amigo: ") )
    name_friend = input("Nombre amigo:")
    friend.append(name_friend)
    phone = input("Telefono: ")
    friend.append(phone)
    friends.update({id_friend: friend})




def create_books():
    book = []
    id_book = int(input("Id libro: "))
    book_name = input("Nombre Libro: ")
    book.append(book_name)
    book_author = input("Autor: ")
    book.append(book_author)
    books.update({id_book: book})


def booking_books():
    lend_book=[]
    id_book_loan = int(input("id prestamo: "))
    id_friend = int(input("Buscar amigo por id: "))
    friend = search_friend_by_id(id_friend)
    user = friend[0] 
    lend_book.append(user) 
    id_book = int(input("Buscar libro por id: "))
    book = search_book_by_id(id_book)
    book_name = book[0]
    lend_book.append(book_name)
    loan_date= input("dia/mes/año")
    lend_book.append(loan_date)
    return_date = input("dia/mes/año")
    lend_book.append(return_date)
    booking.update({id_book_loan: lend_book})


def show_friend():
    for i,j in friends.items():
        print(i,j)


def show_books():
    for i,j in books.items():
        print(i,j)

def show_booking():
    for i,j in booking.items():
        print(i,j)



def search_friend_by_id(id_friend):
    friend = friends.get(id_friend)
    return friend 

def search_book_by_id(id_book):
    book = books.get(id_book)
    return book        


createFriend()
createFriend()
create_books()
create_books()
booking_books()
booking_books()
show_booking()



