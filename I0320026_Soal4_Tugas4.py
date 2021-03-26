print ("===Pendaftaran Kursus Online===,\n")

min_usia = 21
u = int(input("Berapa Umur Anda : "))
if min_usia <= u :
    print("Anda cukup umur")
    u = input("Apakah anda sudah lulus ujian kualifikasi [Y/T]")
    if u == "Y":
        print("Anda dapat mendaftar di kursus")
    elif u == "T":
        print("Anda tidak dapat mendaftar di kursus")
else :
    print ("Anda belum cukup umur")