import os
from operator import attrgetter

class Book():
    def __init__(self):
        self.ID = -1
        self.name = ""
        self.author = ""
        self.price = -1.0

    def setID(self, val):
        self.ID = val

    def setName(self, text):
        self.name = text

    def setAuthor(self, text):
        self.author = text

    def setPrice(self, val):
        self.price = val

    def __repr__(self):
        return repr((self.price, self.name, self.ID, self.author))

class BookList():
    def __init__(self):
        self.List = []

    def printAll(self):
        for book in self.List:
            print(book.ID, book.name, book.author, book.price)

    def findBookName(self, text):
        for book in self.List:
            if text in book.name:
                print(book.name)

    def printByIncreasePrice(self):
        beSorted = sorted(self.List, key=attrgetter("price"))
        
        for book in beSorted:
            print(book.ID, book.name, book.author, book.price)

    def printByDecreasePrice(self):
        beSorted = sorted(self.List, key=attrgetter("price"), reverse=True)

        for book in beSorted:
            print(book.ID, book.name, book.author, book.price)

class Calculator():
    def __init__(self, bookList):
        self.bookList = bookList

        #print("輸入 0 列出所有書籍。\n輸入 1 進入查詢功能，可以用關鍵字查詢書籍（例如輸入「那些年」，可以找到「那些年我們一起追的女孩」）。\n輸入 2 可以將所有書激依造價格升冪排序，輸入 3 則是依價格降冪排序。\n輸入 4 進入結帳區，可以輸入要購買書籍的ID（例如：1,2,3），輸入方式自行設計，自動計算總價並顯示。")

        while True:
            print("請輸入欲執行的功能編號：")
            state = int(input())

            if state == 0:
                exec0()
            elif state == 1:
                exec1()
            elif state == 2:
                exec2()
            elif state == 3:
                exec3()
            elif state == 4:
                exec4()
            else:
                print("Invalid Option. ")

            print("是否結束程式？（Ｙ／Ｎ）")
            s = input()
            if(s[0] == "Y" or s[0] == "y"):
                break

    def exec0(self):
        self.bookList.printAll()

    def exec1(self):
        print("請輸入關鍵字查詢書名：")
        s = input()
        
        self.bookList.findBookName(s)

    def exec2(self):
        self.bookList.printByIncreasePrice()

    def exec3(self):
        self.bookList.printByDecreasePrice()

    def exec4(self):
        
        self.bookList.printAll()
        
        total = 0.0

        while True:
            print("請輸入要購買書的ID（例如：1, 2, 3）")
            val = input()
            
            if val < self.bookList.size():

                print(self.bookList[val].name + "已加入購物車")

                total += self.bookList[val].price
                
                print("是否加購其他書籍？（Y/N）")
                s = input()

                if(s[0] == "Y" or s[0] == 'y'):
                    break
        print("您的帳單金額總共為" + total + "元")
        print("謝謝您的惠顧")


if __name__=='__main__':

    if os.path.exists("./01-input.txt"):
        f = open("./01-input.txt", "r")
        
        bookList = BookList()
        for s in f:
            s = s.strip()

            if len(s) > 0:
                s = s.split(",")

                book = Book()
                book.setID(int(s[0]))
                book.setName(s[1])
                book.setAuthor(s[2])
                book.setPrice(float(s[3]))
                
                bookList.List.append(book)
        bookList.printAll()
            
    else:
        print("No Input File!")
