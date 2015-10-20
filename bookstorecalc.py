import os
import platform
from operator import attrgetter

def clear():
    os.system("clear" if platform.system() == "Darwin" else "cls")
        

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

    #sorted with object, using key
    def __repr__(self):
        return repr((self.price, self.name, self.ID, self.author))

class BookList():
    def __init__(self):
        self.List = []

    def printAll(self):
        for book in self.List:
            print(book.ID, book.name, book.author, "$", book.price)

    def findBookName(self, text):
        flg = False

        for book in self.List:
            if text in book.name:
                if flg == False:#first time print the name
                    print("查詢結果：")
                print(book.name, book.author, "$", book.price)
                flg = True
        
        if flg == False:
            print("查無此書名")

    def printByIncreasePrice(self):
        beSorted = sorted(self.List, key=attrgetter("price"))
        
        for book in beSorted:
            print(book.name, book.author, book.price)

    def printByDecreasePrice(self):
        beSorted = sorted(self.List, key=attrgetter("price"), reverse=True)

        for book in beSorted:
            print(book.name, book.author, book.price)

class Calculator():
    def __init__(self, bookList):
        self.bookList = bookList

        while True:

            clear()

            print("輸入 0 列出所有書籍。\n輸入 1 進入查詢功能，可以用關鍵字查詢書籍。\n輸入 2 可以將所有書籍依照價格升冪排序。\n輸入 3 則是依價格降冪排序。\n輸入 4 進入結帳區，可以輸入要購買書籍的ID（例如：1,2,3）。")

            print("\n請輸入欲執行的功能編號：")
            state = input()

            try:
                state = int(state)
            except:
                print("請輸入數字")
                continue

            if state == 0:
                self.exec0()
            elif state == 1:
                self.exec1()
            elif state == 2:
                self.exec2()
            elif state == 3:
                self.exec3()
            elif state == 4:
                self.exec4()
            else:
                continue

            print("\n是否結束程式？（Ｙ／Ｎ）")
            s = input()
            if len(s) == 1:
                if s[0] == "Y" or s[0] == "y":
                    break
                elif s[0] =="N" or s[0] == "n":
                    continue
                #else:
                    #暫時想不到好的處理方法QQ

            #else:
                #暫時想不到好的處理方法QQ


    def exec0(self):
        clear()

        self.bookList.printAll()

    def exec1(self):
        clear()

        print("請輸入關鍵字查詢書名：")
        s = input()

        print("\n")
        
        self.bookList.findBookName(s)

    def exec2(self):
        clear()

        print("\n按價格由低至高：")
        self.bookList.printByIncreasePrice()

    def exec3(self):
        clear()

        print("\n按價格由高至低：")
        self.bookList.printByDecreasePrice()

    def exec4(self):
        
        total = 0.0
        bookCount = []
        for i in range(0, len(self.bookList.List)):
            bookCount.append(0)

        clear()

        self.bookList.printAll()
        print("\n請輸入要購買書的ID（例如：1, 2, 3）或是輸入-1結束購買")

        val = input()

        while True:

            try:
                val = int(val)
            except ValueError:
                clear()

                self.bookList.printAll()
                print("\n輸入錯誤")
                print("\n請輸入要購買書的ID（例如：1, 2, 3）或是輸入-1結束購買")

                val = input()
                continue

            if val == -1:
                break
            elif val>0 and val <= len(self.bookList.List):
                val -= 1 #adjust to fit array

                print("已加入購物車: "+self.bookList.List[val].name )

                total += self.bookList.List[val].price

                bookCount[val] += 1 #id為val的book 數量+1
                
                print("\n目前總金額為$"+str(total))

                #continue
                clear()

                self.bookList.printAll()
                print("\n已加入購物車: "+self.bookList.List[val].name+" x "+str(bookCount[val]))
                print("目前總金額為$"+str(total))
                print("\n請輸入要購買書的ID（例如：1, 2, 3）或是輸入-1結束購買")

                val = input()
            else:
                clear()

                self.bookList.printAll()

                print("\n輸入錯誤")
                print("\n請輸入要購買書的ID（例如：1, 2, 3）或是輸入-1結束購買")

                val = input()

        clear()

        print("您的購買清單:")
        for i in range(0, len(bookCount)):
            if bookCount[i] != 0:
                print(self.bookList.List[i].name, "$"+str(self.bookList.List[i].price)+" x", bookCount[i])
        print("\n您的帳單金額總共為$" + str(total) + "元")
        print("謝謝您的惠顧")

def LoadFile(bookList, filePath):
    if os.path.exists(filePath):
        f = open(filePath, "r")
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
    else:
        print("No Input File!")

if __name__=='__main__':
        bookList = BookList()

        LoadFile(bookList, "./01-input.txt")
        
        Calculator(bookList)
