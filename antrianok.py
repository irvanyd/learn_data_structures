import os
import queue

class myQueue:
    def __init__(self):
        self.items = queue.Queue()
    #memeriksa apakah queue dlm keadaan kosong#
    def isEmpty(self):
        return self.items.empty()
    #menambah data ke queue#
    def qPut(self, item):
        self.items.put(item)
    #mengeluarkan data dari queu#
    def qGet(self):
        if not self.items.empty():
            return self.items.get()
        else:
            return "empty"
    #menghitung panjang queue#
    def size(self):
        return self.items.qsize()
    #main menu aplikasi#
    def mainmenu(self):
        pilih = "y"
        while (pilih == "y"):
            os.system("clear")
            print("==================")
            print("Menu Aplikasi queue")
            print("==================")
            print("1. Put Objek")
            print("2. Get Object")
            print("3. Cek Empty")
            print("4. Panjang dari Queue")
            print("==================")
            pilihan=str(input(("Silahkan masukan pilihan anda: ")))
            if (pilihan=="1"):
                os.system("clear")
                obj = str(input("masukan objek yang ingin anda tambahkan: "))
                self.qPut(obj)
                print("Object "+obj+"telah ditambahkan")
                x = input("")

            elif(pilihan=="2"):
                os.system("Clear")
                temp = self.qGet()
                if temp != "empty":
                    print("Object "+temp+"Dihapus")
                else:
                    print("Queue Kosong")
                x = input("")
            elif(pilihan=="3"):
                os.system("clear")
                print(self.isEmpty())
                x = input("")
            elif(pilihan=="4"):
                os.system("clear")
                print("Panjang dari queue adalah: "+str(self.size()))
                x = input("")
            else:
                pilih="n"

if __name__ == "__main__":
    q=myQueue()
    q.mainmenu()
                    
