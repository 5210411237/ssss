class Perpustakaan :
    def __init__(self, kode, judul, subjek, lokasi, info) :
        self.kode = kode
        self.judul = judul      
        self.subjek = subjek
        self.lokasi = lokasi
        self.info = info

class Buku(Perpustakaan) :
    def __init__(self, kode, judul, subjek, lokasi, info, isbn, pengarang, jmlhal, ukuran):
        super().__init__(kode, judul, subjek, lokasi, info)
        self.isbn = isbn
        self.pengarang = pengarang
        self.jmlhal = jmlhal        
        self.ukuran = ukuran      


    def Tampil(self) :
        print(f"Judul : {self.judul} <{self.kode}>")
        print(f"Pengarang : {self.pengarang}")
        print(f"Jumlah Halaman : {self.jmlhal}")
        print(f"Kategori : {self.subjek}\n")

class Majalah(Perpustakaan) :
    def __init__(self, kode, judul, subjek, lokasi, info, volume, issue):
        super().__init__(kode, judul, subjek, lokasi, info)
        self.volume = volume
        self.issue = issue

    def Tampil(self) :  #Overriding
        print(f"Judul : {self.judul} <{self.kode}>")
        print(f"Volume : {self.volume}")
        print(f"Issue : {self.issue}")
        print(f"Kategori : {self.subjek}\n")

class DVD(Perpustakaan) :
    def __init__(self, kode, judul, subjek, lokasi, info, aktor, genre):
        super().__init__(kode, judul, subjek, lokasi, info)
        self.aktor = aktor
        self.genre = genre      

    def Tampil(self) :  #Overriding
        print(f"Judul : {self.judul} <{self.kode}>")
        print(f"Aktor : {self.aktor}")
        print(f"Genre : {self.genre}")
        print(f"Kategori : {self.subjek}\n") 

#objek Buku
buku1=Buku("123", "Pemrograman Python", "Buku Cetak", "Rak 1", "Dipinjam", "945-884-98-05", "Yogi Syarif", 20, "25x15")
buku2=Buku("134", "Kultur Jaringan", "Buku panduan ", "Rak 1", "Ada", "978-602-453-239-0", "Dwi Hapsono", 112, "15x23")
buku3=Buku("156","english daily", "Buku Ajar", "Rak 1", "Ada", "978-602-475-963-6", "Marhananto", 175, "15x20")
buku4=Buku("178","HTML & CSS", "Buku Referensi", "Rak 1", "Dipinjam", "978-623-02-3810-9", "Novita", 86, "17x25")

#objek Majalah
majalah1 =Majalah("234","Ekonomi dan keuangan", "Majalah Cetak", "Rak 2", "Ada", "VII", "Ekonomi")
majalah2=Majalah("256", "Kuliner Nusantara", "Majalah Cetak", "Rak 2", "Dipinjam", "IV", "Makanan")
majalah3=Majalah("278", "Naruto Shipudden", "Majalah Manga", "Rak 2", "Ada", "IX", "Anime")
majalah4=Majalah("265", "liga Inggris", "Majalah sport", "Rak 2", "Dipinjam", "I", "Olahraga")

#objek DVD
dvd1 = DVD("312", "Naruto", "softcopy", "Rak 3", "Ada", "Mikasa", "Anime")
dvd2 = DVD("323", "Doraemon", "softcopy", "Rak 3", "Ada", "Gojo", "Kartun")
dvd3 = DVD("334", "Fast and Fourius", "softcopy", "Rak 3", "Ada", "Bryan", "Film Aksi")   
dvd4 = DVD("398", "Police story", "softcopy", "Rak 3", "Ada", "Jackie Chan", "Fulm Aksi")

while True :
    print("=======================\n    SEARCH ITEM \n=======================")
    print("1. BUKU ")  
    print("2. MAJALAH")
    print("3. DVD")
    print("0. selesai")
    menu = input("Pilihan Menu : ") 

    if menu == '1' :
        print("\nMENU BUKU\n===============\n1. Tampil Buku")
        print("2. Cari Buku")   
        pilihan = input("Pilihan : ")  
        buku = [buku1, buku2, buku3, buku4]

        if pilihan == '1' :
            print("\n==============================================")
            for buku in buku :
                buku.Tampil()

        elif pilihan == '2' :
            kode = input("Masukan Kode Buku\t: ")
            for x in buku :
                if kode == x.kode :
                    print("\n==============================================")
                    print(f"Judul : {x.judul}")
                    print(f"Letak : {x.lokasi}")    
                    print(f"Status : {x.info}\n")
                    print("==============================================")

    elif menu == '2' :
        print("\nMENU MAJALAH\n===============\n1. Tampil Data Majalah")
        print("2. Cari Majalah")        
        pilihan = input("Pilihan : ") 
        majalah = [majalah1, majalah2, majalah3, majalah4] 

        if pilihan == '1' :
            print("\n==============================================")
            for majalah in majalah :
                majalah.Tampil()

        elif pilihan == '2' :
            kode = input("Masukan Kode Majalah\t: ")
            for x in majalah :
                if kode == x.kode :
                    print("\n==============================================")
                    print(f"Judul : {x.judul}")
                    print(f"Letak : {x.lokasi}")
                    print(f"Status : {x.info}\n")
                    print("==============================================")

    elif menu == '3' :
        print("\nMENU DVD\n===============\n1. Tampil Data DVD")
        print("2. Cari DVD")
        pilihan = input("Pilihan : ")  
        dvd = [dvd1, dvd2, dvd3, dvd4]  

        if pilihan == '1' :
            print("\n==============================================")
            for dvd in dvd :
                dvd.Tampil()

        elif pilihan == '2' :
            kode = input("Masukan Kode DVD\t: ")
            for x in dvd :
                if kode == x.kode :
                    print("\n==============================================")
                    print(f"Judul : {x.judul}")
                    print(f"Letak : {x.lokasi}")
                    print(f"Status : {x.info}\n")
                    print("==============================================")

    elif menu == '0' :
        print("TERIMA KASIH :)\n")
        break

    else : 
        print("\nPilihan Tidak Ada Menu\n")
    input("\nEnter Untuk Melanjutkan......") 