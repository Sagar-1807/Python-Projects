class library:
    def __init__(self,list,name):
        self.booklist=list
        self.libname=name
        self.lendbook={}            # {} blank dict.

    def displyBooks(self):
        print(f"Our library is free of cost: {self.libname}")
        for book in self.booklist:
            print(book)
            print("")

    def givenBooks(self,user,book):
        if book not in self.lendbook.keys():
            self.lendbook.update({book:user})
            print("Book database has been updated!!\n U can take book!")
            print("")
        else:
            print(f"{self.lendbook[book]} is already taken.")


    def addbooks(self,book):
        self.booklist.append(book)
        print(book,"has been added to list.")


    def returnbooks(self,book):
        self.booklist.remove(book)
if __name__=="__main__":
    list1=library(['ab','cd','ef','gh','jk'],'sagar Library')

    while True:
        print(f"Welcome to {list1.libname},!!"),print("")
        print("Enter 1. for display a books:")
        print("Enter 2. for lend a books:")
        print("Enter 3. for add a  books:")
        print("Enter 4. for return a books:"),print("")
        choice=int(input("Enter ur choice:"))

        if choice==1:
            list1.displyBooks()
        elif choice==2:
            book=input("Enter book name fro lend: ")
            user=input("Enter ur name: ")
            list1.givenBooks(user,book)


        elif choice==3:
            book = input("Enter book name for add: ")
            list1.addbooks(book)
        elif choice==4:
            book = input("Enter book name for return: ")
            list1.returnbooks(book)


        else:
            print("Not valid option!")
        print("Enter q for quit,c for continue:.")
        choice2 = print("------")
        while (choice2 !='q' and choice2 != 'c' ):
            choice2=input("Enter c or q:")
            if choice2 == 'q':
                exit()
            elif choice2 =='c':
                continue



















