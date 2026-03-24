#هذا نظام متكامل لادارة المكتبه من اضافه حذف عرض كل الكتب عرض الكتب الموجودة عرض الكتب المستعاره بحث استعاره 

book={}
ID_book=0
name_book="unknow"
author_book="unknow"
status_book="unknow"
number_pages=0
#to check the input is integer 
def get_number_or_skip(prompt):
    while True:
        user_input = input(prompt).strip()
        try:
            return int(user_input)
        except ValueError:
            print("❌ please,enter number not text : ")
#functoin to  add book
def add_book():
    while True:
      ID_book=get_number_or_skip("enter the ID of book: ")
      if ID_book in book:
         print("⚠️  sorry,the ID is already exists! ")
         continue
      name_book=input("enter the name of book: ").strip()
      author_book=input("enter the author of book: ").strip()
      number_page=get_number_or_skip("enter the number of pages: ")
      status_book="available"
      book.update({ID_book:{"name_book":name_book,"author_book":author_book, "number_pages":number_page,"status_book":status_book}})
      print("\n***** Book is added successfully *****")
      #check to  add another book
      while True:
        ask=input("Do you want another book (yes or no ): ").lower()
        if ask =='yes':
          break
        elif ask=='no':
            return
        else:
           print("unavailable option ")
           print("please,enter yes or no")
           
     
# function to delete book
def delete_book():
   while True:
    length_book= len(book)
    if length_book>=1:
      print("\n" + "="*30)
      print("---delete Menu ---")
      print("1:To delete by ID ")  
      print("2:To delete by name of book ")
      choice=get_number_or_skip("enter your choice: ")
     
      if choice==1:
          ID_deletion=get_number_or_skip("enter the ID of book: ")
          if ID_deletion in book:
           book.pop(ID_deletion)
           print("***** the book is deleted successfully *****")
          else:
           print("ID not found!")
       
      elif choice==2:
        name_deletion=input("enter the name of book: ").strip().lower()
         # serche book
        matches=[]

        found=False
        for ID_book in list(book.keys()):
            if book[ID_book]["name_book"].lower()==name_deletion:
                matches.append(ID_book)
        if not matches:
            print("The name of book not found")
        elif len(matches)==1:
           book.pop(matches[0])
           print("***** the book is deleted successfully *****")
        else:
           print(f"\n!!! warning found {len(matches)} books with the same name\n ")
           print("Details of matching books: ")
           print("*"*50)

           for ID in matches:
              print(f"the details of the book has ID {ID}: ")
              print(f"the name of the book {book[ID]['name_book']}: ")
              print(f"the author of the book {book[ID]['author_book']}: ")
              print(f"the number of the pages {book[ID]['number_pages']}: ")
              print("*"*50)
           id_deletion=get_number_or_skip("enter the ID of book that you want delete: ")
           if id_deletion in matches:
              book.pop(id_deletion)
              print("***** the book is deleted successfully *****")
           else:
              print("unavailable ID! deletion cancelled.")
      else:
          print("Unavailable option!")

                
    else:
       print("sorry,the database of library is empty")
       return
    while True:
        ask = input("\nDo you want to delete another book? (yes/no): ").lower().strip()
        if ask == 'yes':
            break # يرجع لبداية الـ while الكبيرة
        elif ask == 'no':
            return # يخرج من الدالة بالكامل
        else:
            print("Please enter yes or no")
# function to serche book
def search_book():
    while True:
        length_book = len(book)
        if length_book >= 1:
            print("\n" + "="*30)
            print("--- Search Menu ---")
            print("1. Search by ID")
            print("2. Search by Name")
            print("3. Search by Author")
            choice = get_number_or_skip("Please, enter your choice: ")

            # 1. البحث بالـ ID (مباشر)
            if choice == 1:
                id_search = get_number_or_skip("Enter the ID to search")
                if id_search in book:
                     print("-" * 60)
                     print(f"ID: {id_search} | Name: {book[id_search]['name_book']} | Author: {book[id_search]['author_book']} | Status: {book[id_search]['status_book']}")
                     print("-" * 60)
                else:
                    print("❌ Sorry, ID not found.")

            # 2 & 3. البحث بالاسم أو المؤلف (نظام القائمة)
            elif choice == 2 or choice == 3:
                search_type = "name_book" if choice == 2 else "author_book"
                label = "Name" if choice == 2 else "Author"
                
                query = input(f"Enter the {label} to search: ").strip().lower()
                
                matches = []
                for b_id in book:
                    if book[b_id][search_type].lower() == query:
                        matches.append(b_id)
                
                # فحص النتائج
                if len(matches)==1:
                    print("-" * 60)
                    print(f"ID: {b_id} | Name: {book[b_id]['name_book']} | Author: {book[b_id]['author_book']} | Status: {book[b_id]['status_book']}")
                    print("-" * 60)
                elif not matches:
                    print(f"❌ No books found with this {label}.")
                else:
                    print(f"\n🔔 Found {len(matches)} books matching your search:")
                    print("-" * 60)
                    for b_id in matches:
                        print(f"ID: {b_id} | Name: {book[b_id]['name_book']} | Author: {book[b_id]['author_book']} | Status: {book[b_id]['status_book']}")
                    print("-" * 60)

            else:
                print("Unavailable option!")

        else:
            print("Sorry, the database is empty.")
            return

        # سؤال الاستمرارية اللي بيخليك جوه الـ While
        while True:
            ask = input("\nDo you want to search again? (yes/no): ").lower().strip()
            if ask == 'yes':
                break
            elif ask == 'no':
                return
            else:
                print("Please enter yes or no.")               

               
#function to borrow a book
def borrow_book():
   while True:
        length_book = len(book)
        if length_book >= 1:
            print("\n" + "="*30)
            print("--- Borrow Menu ---")
            print("1. Borrow by ID")
            print("2. Borrow by Name")
            print("3. Borrow by Author")
            choice=get_number_or_skip("enter your choice: ")
            if choice==1:
              ID_borrow=get_number_or_skip("enter the ID of book to borrow :")
              if ID_borrow in book:
                if  book[ID_borrow]["status_book"]=="Borrow":
                   print("sorry,the book is already borrowed")
                else:
                  print(f"\n✅ Success! Book with ID {ID_borrow} found:")
                  book[ID_borrow]["status_book"]="Borrow"
              else:
                print("❌ Sorry, ID not found.")
            elif choice==2 or choice==3:
               search_type = "name_book" if choice == 2 else "author_book"
               label = "Name" if choice == 2 else "Author"          
               query = input(f"Enter the {label} to Borrow : ").strip().lower ()   
               matches = []
               for b_id in book:
                  if book[b_id][search_type].lower() == query:
                    matches.append(b_id)
               if len(matches)==1 and book[b_id]["status_book"]=="available":
                  print(f"\n✅ Success! Book with ID {b_id} found:")
                  book[b_id]["status_book"]="Borrow"
               elif len(matches)==1 and book[b_id]["status_book"]=="Borrow":
                  print("sorry,the book is already borrowed")
               elif not matches:
                 print(f"❌ No books found with this {label}.")
               else:
                  print(f"\n🔔 Found {len(matches)} books matching your Borrow:")
                  print("-" * 60)
                  for b_id in matches:
                     print(f"ID: {b_id} | Name: {book[b_id]['name_book']} | Author: {book[b_id]['author_book']} | Status: {book[b_id]['status_book']}")
                     print("-" * 60)
                  id_borrow=get_number_or_skip("enter the ID of book that you want Borrow:")
                  if id_borrow in matches: 
                     if book[id_borrow]["status_book"]=="Borrow":
                        print("sorry,the book is already borrowed")
                     else:
                       print("***** the book is Borrow successfully *****")
                       book[id_borrow]["status_book"]="Borrow"
                  else:
                   print("unavailable ID! Borrow cancelled.")
            else:
             print("Unavailable option!")
        else:
            print("Sorry, the database is empty.")
            return

        # سؤال الاستمرارية اللي بيخليك جوه الـ While
        while True:
            ask = input("\nDo you want to Borrow again? (yes/no): ").lower().strip()
            if ask == 'yes':
                break
            elif ask == 'no':
                return
            else:
                print("Please enter yes or no.")               
        
#function to return book 
def return_book():
   while True:
       length_book = len(book)
       if length_book >= 1:
            print("\n" + "="*30)
            print("---Return  Menu ---")
            print("1. Return by ID")
            print("2. Return by Name")
            print("3. Return by Author")
            choice=get_number_or_skip("enter your choice: ")
            if choice==1:
               re_id=get_number_or_skip("enter the ID of book that you want return: ")
               if re_id in book:
                  if  book[re_id]["status_book"]=="available":
                    print("sorry,the book is already available")
                  else:
                   print(f"\n✅ Success! Book with ID {re_id} found:")
                   book[re_id]["status_book"]="available"
               else:
                 print("❌ Sorry, ID not found.")
            elif choice==2 or choice==3:
                search_type = "name_book" if choice == 2 else "author_book"
                label = "Name" if choice == 2 else "Author"          
                query = input(f"Enter the {label} to Return : ").strip().lower ()   
                matches = []
                for b_id in book:
                  if book[b_id][search_type].lower() == query:
                    matches.append(b_id)
                if len(matches)==1 and book[b_id]["status_book"]=="Borrow":
                  print(f"\n✅ Success! Book with ID {b_id} found:")
                  book[b_id]["status_book"]="available"
                elif len(matches)==1 and book[b_id]["status_book"]=="available":
                  print("sorry,the book is already available")
                elif not matches:
                 print(f"❌ No books found with this {label}.")
                else:
                  print(f"\n🔔 Found {len(matches)} books matching your return:")
                  print("-" * 60)
                  for b_id in matches:
                     print(f"ID: {b_id} | Name: {book[b_id]['name_book']} | Author: {book[b_id]['author_book']} | Status: {book[b_id]['status_book']}")
                     print("-" * 60)
                  id_return=get_number_or_skip("enter the ID of book that you want Return: ")
                  if id_return in matches: 
                     if book[id_return]["status_book"]=="available":
                        print("sorry,the book is already available")
                     else:
                       print("***** the book is Return successfully *****")
                       book[id_return]["status_book"]="available"
                  else:
                   print("unavailable ID! Borrow cancelled.")
            else:
             print("Unavailable option!")
       else:
            print("Sorry, the database is empty.")
            return
       while True:       # سؤال الاستمرارية اللي بيخليك جوه الـ While
            ask = input("\nDo you want to Return again? (yes/no): ").lower().strip()
            if ask == 'yes':
                break
            elif ask == 'no':
                return
            else:
                print("Please enter yes or no.")               
#function to display book           
def display_book():
   while True:
        length_book = len(book)
        if length_book >= 1:
            print("\n" + "="*30)
            print("---display Menu ---")
            print("1. display all book")
            print("2. display borrow book")
            print("3. display available book")
            choice=get_number_or_skip("enter your choice: ")
            found=False
            if choice==1:
               for b_id in book:
                     print("-" * 60)
                     print(f"ID: {b_id} | Name: {book[b_id]['name_book']} | Author: {book[b_id]['author_book']} | Status: {book[b_id]['status_book']}")
                     print("-" * 60)
            elif choice==2:
                for status in book:
                   if book[status]['status_book']=='Borrow':
                     print("-" * 60)
                     print(f"ID: {status} | Name: {book[status]['name_book']} | Author: {book[status]['author_book']} | Status: {book[status]['status_book']}")
                     print("-" * 60)
                     found=True
                if not found:
                      print("NO Borrowed Books")
            elif choice==3:
                 for status in book:
                   if book[status]['status_book']=='available':
                     print("-" * 60)
                     print(f"ID: {status} | Name: {book[status]['name_book']} | Author: {book[status]['author_book']} | Status: {book[status]['status_book']}")
                     print("-" * 60)
                     found=True
                 if not found:
                      print("NO Available Books")
            else:
               print("Unavailable option!")
        else:
            print("Sorry, the database is empty.")
            return
        while True:       # سؤال الاستمرارية اللي بيخليك جوه الـ While
            ask = input("\nDo you want to dispaly again? (yes/no): ").lower().strip()
            if ask == 'yes':
                break
            elif ask == 'no':
                return
            else:
                print("Please enter yes or no.")            
#the main function
def main_function():
      while True:
        print("Welcome to Library System ")
        print("1: add a book")
        print("2: delete a book")
        print("3: serche a book")
        print("4: borrow a book")
        print("5: return a book")
        print("6: display books")
        print("7: exit from system")
        choice=get_number_or_skip("Hello, enter your choice please: ")
        if choice==1:
           add_book()
        elif choice==2:
           delete_book()
        elif choice==3:
           search_book()
        elif choice==4:
           borrow_book()
        elif choice==5:
           return_book()
        elif choice==6:
           display_book()
        elif choice==7:
           print("💕💕 Thank you for using my system 💕💕")
           break
        else:
           print("Unavailable option!")
           
         
main_function()