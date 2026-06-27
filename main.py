#  Smart Library Management System

# Main Menu
# Login
# Signup
# Exit

# Admin Menu
# Add Book
# View All Books
# Search Book
# Update Book
# Delete Book
# View Issued Books
# View Reserved Books
# View user
# View Statistics
# View Logs
# Generate Report
# Logout

# admin Menu
# Search Book
# View All Books
# Issue Book
# Return Book
# Reserve Book
# Rate Book
# Update Profile
# Logout

# Statistics Menu
# Total Books
# Available Books
# Issued Books
# Reserved Books

import json 
import logging

logging.basicConfig(
    filename="library.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s -%(message)s"
)

def get_input(message):

    while True:
        value = input(message)

        if value.strip() == "":
            print("Field cannot be empty")
        else:
            return value


def get_number(message):

    while True:
        try:
            return int(input(message))

        except ValueError:
            print("Enter a valid number")

admin_pin = 76767576

# Main menu  
def login1():
    
    name = get_input("Enter your name:")
    password = get_number("Enter your password:")

    with open("user.json", "r") as file:
        data = json.load(file)

    for user in data:
        if user["name"] == name and user["password"] == password:
            print("Login successful")
            logging.info("User login in user menu")
            user_menu()
            return
        
    with open("admin.json", "r") as file:
        data1 = json.load(file)

    for admin in data1:
        if admin["name"] == name and admin["password"] == password:
            print("Login successful")
            logging.info("Admin login in admin menu")
            admin_menu()
            return

    print("Invalid username or password")
                
def signup():
    def user():
     
        name = get_input("Enter your name:")
        password = get_number("Enter your password:")

        new_users = {
            "name":name,
            "password":password
        }

        try:
            with open("user.json","r") as file:
                users = json.load(file)
        except(FileNotFoundError,json.JSONDecodeError):
         users = []

        users.append(new_users)
     
        with open("user.json","w") as file:
            json.dump(users,file,indent=4)


        print("user Signup sucessfulyy")
        logging.info(f"user add in admin.json file {users}")
        print("Return to main menu")

    def admin():
       name = get_input("Enter your name: ")
       password = get_number("Enter your password: ")
       pin = get_number("Enter admin pin: ")

       new_admin = {
        "name": name,
        "password": password
        }

       if pin == admin_pin:

        try:
              with open("admin.json", "r") as file:
                admins = json.load(file)

        except (FileNotFoundError, json.JSONDecodeError):
            admins = []

        admins.append(new_admin)

        with open("admin.json", "w") as file:
            json.dump(admins, file, indent=4)

        print("Admin signup successfully")
        print("Return to main menu")
        logging.info(f"Admin added in admin.json file {new_admin}")

       else:
        print("Enter valid admin pin")


    while True:
        print("======main menu======")
        print("1. signup as user" )
        print("2. Signup as admin")
        print("3. Exit")

        choice = get_number("Enter your choice:")

        if choice == 1:
           user()

        elif choice == 2:
           admin()

        elif choice == 3:
           print("Thank you!") 
           break

        else:
           print("Enter vaild number") 

# admin menu===========================================================================================================
def admin_menu():
   
    def add_book():
      
      
      title = get_input("Enter title:")
      author = get_input("Enter author name:")
      category = get_input("Enter book category:")
      Quantity = get_number("Enter book Quantity:")
      
         
      try:
          with open("book.json","r") as file:
             data = json.load(file)
       
      except(FileNotFoundError,json.JSONDecodeError):
      
         data = []

      for book in data:
         if book["title"].lower() == title.lower():
            print("Book already exists")
            return
         
      if len(data) == 0:
         new_id = 101
      else:
         new_id = data[-1]["id"]+1

      book = {
          "id":new_id,
          "title":title,
          "author":author,
          "category":category,
          "Quantity":Quantity
        }
           
      data.append(book)   

      with open("book.json","w") as file:
           json.dump(data,file,indent=4)
               
      print("Book add sucessfully")
      logging.info(f"admin add book{data}")

    def viwe_book():
       
       with open("book.json","r") as file:
          data = json.load(file)
          print(data)

    def search_book():

      find = get_input("Enter book name: ")

      with open("book.json", "r") as file:
        data = json.load(file)

        for books in data:
            if books["title"].lower() == find.lower():
                print("Book found")
                print(books)
                return

    print("Book not found")
    def update_book():
       
       def change_title():
          
         search = get_input("Enter book name:")
         
         with open("book.json","r") as file:
            data = json.load(file)

            for books in data:
               if books["title"] == search:
                  
                  change_name = get_input("Enter new book title:")

                  books["title"] = change_name

                  with open("book.json","w") as file:
                     json.dump(data,file,indent=4)

                     print("title update sucessfully")
                     logging.info(f"admin update title{books}")
          
       def change_author():
                    
         search = get_input("Enter book name:")
         
         with open("book.json","r") as file:
            data = json.load(file)

            for books in data:
               if books["title"] == search:
                  
                  change_name = get_input("Enter new author name:")

                  books["author"] = change_name

                  with open("book.json","w") as file:
                     json.dump(data,file,indent=4)

                     print("author name update sucessfully")
                     logging.info(f"admin update author name{books}")
       
       def changer_category():
                    
         search = get_input("Enter book name")
         
         with open("book.json","r") as file:
            data = json.load(file)

            for books in data:
               if books["title"] == search:
                  
                  change_name = get_input("Enter new book category:")

                  books["category"] = change_name

                  with open("book.json","w") as file:
                     json.dump(data,file,indent=4)

                     print("category update sucessfully")
                     logging.info(f"admin update book{books}")
       
       def change_Quantity():
                    
         search = get_input("Enter book name")
         
         with open("book.json","r") as file:
            data = json.load(file)

            for books in data:
               if books["title"] == search:
                  
                  change_name = get_input("Enter new book Quantity:")

                  books["Quantity"] = change_name

                  with open("book.json","w") as file:
                     json.dump(data,file,indent=4)

                     print("book Quantity update sucessfully")
                     logging.info(f"admin update book Quantity{books}")
       
       while True:
          print("======update book======")
          print("1. change title")
          print("2. change author")
          print("3. change category")
          print("4. change Quantity")
          print("5. Exit")

          choice = get_number("Enter your choice:")

          if choice == 1:
             change_title()

          elif choice == 2:
             change_author()

          elif choice == 3:
             changer_category()

          elif choice == 4:
             change_Quantity()

          elif choice == 5:
             print("Thank you")
             break
          
          else:
             print("Enter vaild number")  

    def delete_book():
       
       change = get_input("Enter book name:")

       with open("book.json","r") as file:
          data = json.load(file)

       for books in data:
          if books["title"] == change:

            
             data.remove(books)

             with open("book.json","w") as file:
                json.dump(data,file,indent=4)

             print("Books delete sucessfully")
             logging.info(f"admin delete book{books}")

    def view_issued_book(): 
       
       with open("issued_books.json","r") as file:
          data = json.load(file)
          print(data)

    def View_Reserved_Books():
       
       with open("reservations.json","r") as file:
          data = json.load(file)
          print(data)

    def view_user():
       
       with open("user.json") as file:
          data = json.load(file)

          logging.info("admin view user")
          print(data)


    def view_Statistics():
       
       def total_books():
          
          with open("book.json","r") as file:
             data = json.load(file)

             total_book = len(data)
             print("Total book in inventory:",total_book)
       
       def avabialb_books():
          
          with open("book.json","r") as file:
             data = json.load(file)

             for user in data:
                if user["Quantity"] > 0:
                   
                   print("===avabile book===") 
                   print(user)  

       def issued_book():
          
          with open("issued_books.json","r") as file:
             data = json.load(file)

             print("===issued book===")
             print(data)
       
       def resevered_book():
          
          with open("reservations.json","r") as file:
             data = json.load(file)

             print("===reseved book===")
             print(data)
       
       def total_user():
          
          with open("user.json","r") as file:
             data = json.load(file)

             total_user = len(data)
             print("===Total user===")
             print(data)
             print(total_user)
             
       while True:
          print("======STATISTICS MENU======")
          print("1. total books")
          print("2. avabialb books")
          print("3. issued books")
          print("4. resevered books")
          print("5. total user")
          print("6. Exit")

          choice = get_number("Enter your choice:")

          if choice == 1:
             total_books()

          elif choice == 2:
             avabialb_books()

          elif choice == 3:
             issued_book()

          elif choice == 4:
             resevered_book()

          elif choice == 5:
             total_user()

          elif choice == 6:
             print("Thank you")
             break

          else:
             print("Enter vaild number") 
         
    def view_logs():
       
       with open("library.log","r") as file:
          data = file.read()
          print(data)

          logging.info("admin view log")
    
    def Generate_report():
       
          with open("book.json","r") as file:
             data = json.load(file)

             total_book = len(data)

             total_quantity = 0
             for libarary in data:
                total_quantity +=  libarary["Quantity"]

             with open("user.json","r") as file:
                data1 = json.load(file)

                restirted_user = len(data1)
               
                with open("issued_books.json","r") as file:
                   data2 = json.load(file)

                   issued_book = len(data2)

             print("========== LIBRARY REPORT ==========")
             print("total books =", total_book)
             print("total quantity =", total_quantity)
             print("Total user =", restirted_user)
             print("Total issued book =", issued_book)
             print("====================================") 
                   

    while True:
        print("======Admin menu======")
        print("1. add book")
        print("2. view book")
        print("3. search book")
        print("4. update book")
        print("5. delete book")
        print("6. view issued book")
        print("7. view Reserved  book")
        print("8. view user")
        print("9. view Statistics")
        print("10. view logs")
        print("11. genrate report")
        print("12. logout")

        choice = get_number("Enter your choice:")

        if choice == 1:
            add_book()

        elif choice == 2:
            viwe_book()

        elif choice == 3:
            search_book()
    
        elif choice == 4:
            update_book()

        elif choice == 5:
            delete_book()

        elif choice == 6:
            view_issued_book()
   
        elif choice == 7:
            View_Reserved_Books()

        elif choice == 8:
            view_user()

        elif choice == 9:
         view_Statistics()

        elif choice == 10:
            view_logs()

        elif choice == 11:
            Generate_report()

        elif choice == 12:
            print("Thank you")
            break
    
        else:
         print("Enter vaild number")

# user menu =============================================================================================================

def user_menu():
   
   def search_book():

    find = get_input("Enter book name: ")

    with open("book.json", "r") as file:
        data = json.load(file)

        for books in data:
            if books["title"].lower() == find.lower():
                print("Book found")
                print(books)
                return

    print("Book not found")

   def view_book():
      
      with open("book.json","r") as file:
         data = json.load(file)

         print("All book:",data)
    
   def issue_book():

    name = get_input("Enter your name: ")
    password = get_number("Enter your password: ")

    with open("user.json", "r") as file:
        data = json.load(file)

    for user in data:

        if user["name"] == name and user["password"] == password:

            print("Welcome", name)

            book_name = get_input("Enter your book name: ")

            with open("book.json", "r") as file:
                data1 = json.load(file)

            for book in data1:

                   if book["title"].lower() == book_name.lower():

                    if book["Quantity"] > 0:

                        issue = {
                            "name": name,
                            "book": book_name
                        }

                        try:
                            with open("issued_books.json", "r") as file:
                                books = json.load(file)

                        except (FileNotFoundError, json.JSONDecodeError):
                            books = []

                        books.append(issue)

                        with open("issued_books.json", "w") as file:
                            json.dump(books, file, indent=4)

                        book["Quantity"] -= 1

                        with open("book.json", "w") as file:
                            json.dump(data1, file, indent=4)

                        print("Book issued successfully")
                        logging.info(f"user issued book {issue}")
                        return

                    else:
                        print("Book is out of stock")
                        return

            print("Book not found")
            return

    print("Invalid username or password")
   def return_book():
      
      name = get_input("Enter your name:")
      password = get_number("Enter your password:")

      with open("user.json","r") as file:
         data = json.load(file)

      for user in data:
         if user["name"] == name and user["password"] == password:
            
            books = get_input("Enter book name:")
            with open("book.json") as file:
               data1 = json.load(file)

               for book in data1:
                  if book["title"] == books:
                     book["Quantity"] += 1

                     with open("book.json","w") as file:
                        json.dump(data1,file,indent=4)
                     
                     with open("issued_books.json","r") as file:
                       data2 = json.load(file)
                       
                       for issue in data2:
                          
                          if (
                               issue["name"] == name and
                               issue["password"] == password and
                               issue["book"] == books
                              ):
                             
                             data2.remove(issue)

                             with open("issued_books.json","w") as file:
                                json.dump(data2,file,indent=4)

                     print("Book return sucessfully")
                     logging.info(f"user return book {books}")
                     return

   def Reserve_book():
      
      name = get_input("Enter your name:")
      password = get_number("Enter your password:")
      book = get_input("Enter book name:")

      with open("user.json","r") as file:
         data = json.load(file)

         for user in data:
            if user["name"] == name and user["password"] == password:

             with open("book.json","r") as file:
                data1 = json.load(file)

                for books in data1:
                   if books["title"] == book:
                      if books["Quantity"] == 0:
                         
                         Reserve = {
                            "name":name,
                            "password":password,
                            "book":book
                         }

                         try:
                           with open("reservations.json","r") as file:
                            data2 = json.load(file)

                         except(FileNotFoundError,json.JSONDecodeError):
                           
                           books1 = [] 

                           books1.append(Reserve) 

                           with open("reservations.json","w") as file:
                              json.dump(books1,file,indent=4)

                         print("Book reseverstion sucessfully")
                         logging.info(f"user resave book{Reserve}")
                         

                      else:
                         print("Book avabile")

   def view_issued_book():
      
      name = get_input("Enter your name:")
      password = get_number("Enter your password:")

      with open("user.json","r") as file:
         data = json.load(file)
         for user in data:

            if user["name"] == name and user["password"] == password:
               
               with open("issued_books.json","r") as file:
                  data1 = json.load(file)

                  for book in data1:
                     if book["name"] == name:
                        print("Your issue book",book)
                        break
                     
   def rate_book():
      
      name = get_input("Enter your name:")
      book = get_input("Enter book name:")
      rating = get_number("Enter rating 1-5:")
      feedback = get_input("Enter your feedback:")

      with open("user.json","r") as file:
         data = json.load(file)

      for user in data:
         if user["name"] == name:

            rate = {
               "name":name,
               "book":book,
               "rating":rating,
               "feedback":feedback
            }

            try:
               with open("ratings.json","r") as file:
                  data1 = json.load(file)
            
            except(FileNotFoundError,json.JSONDecodeError):
             boook = []

            boook.append(rate)

            with open("ratings.json","w") as file:
               json.dump(boook,file,indent=4)

            print("Rating add sucessfully")
            print("Thank you")

   def update_user():
      
      name = get_input("Enter your name:")
      password = get_number("Enter your password:")

      with open("user.json","r") as file:
         data = json.load(file)

         for user in data:
            if user["name"] == name and user["password"] == password:

               def update_name():
                  
                  new_name = get_input("Enter your new name:")

                  user["name"] = new_name

                  with open("user.json","w") as file:
                     json.dump(data,file,indent=4)
                     print("Named update sucessfully")
                     logging.info("user change name")

               def update_password():
                                    
                  new_password = get_number("Enter your new password:")

                  user["password"] = new_password

                  with open("user.json","w") as file:
                     json.dump(data,file,indent=4)

                     print("PAssword update sucessfully")
                     logging.info("user change password")

               while True:
                  print("======update profile======")
                  print("1. update name")
                  print("2. update password")
                  print("3. exit")

                  choice = get_number("Enter your choice:")

                  if choice == 1:
                     update_name()

                  elif choice == 2:
                     update_password()

                  elif choice == 3:
                     print("Thank you")
                     break

                  else:
                     print("Enter vaild number")
   
   while True:
        print("======user menu======")
        print("1. search book")
        print("2. view book")
        print("3. issue book")
        print("4. return book")
        print("5. Reserve  book")
        print("6. view issued book")
        print("7. rate book")
        print("8. update profile")
        print("9. logout")

        choice = get_number("Enter your choice:")

        if choice == 1:
           search_book()

        elif choice == 2:
           view_book()

        elif choice == 3:
           issue_book()

        elif choice == 4:
           return_book()

        elif choice == 5:
           Reserve_book()

        elif choice == 6:
           view_issued_book()
        
        elif choice == 7:
            rate_book()

        elif choice ==8:
           update_user()

        elif choice == 9:
            print("Thank you")
            break
        
        else:
           print("Enter vaild number!")

while True:
    print("======Library Management System======")
    print("1. Login")
    print("2. Signup")
    print("3. Exit")

    choice = get_number("Enter your choice:")

    if choice == 1:
        login1()

    elif choice == 2:
        signup()

    elif choice == 3:
        print("Thank you")
        break

    else:
        print("Enter vaild number!")