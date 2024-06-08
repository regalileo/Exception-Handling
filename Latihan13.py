#Regal Nugraha
#TI23C - 20230040175

def konversi(string):
    try:
        intgr = int(string)
        print(f"{string} berhasil di konversi ke integer")
    
    except ValueError:
        print("{string} tidak dapat di konversi ke integer")
konversi("123")
konversi("abc")

def akseselemen(daftar_list, indeks):
    try:
        elemen = daftar_list[indeks]
        print(f"Elemen di indeks {indeks} adalah {elemen}")
    except IndexError:
        print("Kesalahan: Indeks di luar jangkauan")
list_sy = [1, 2, 3]
akseselemen(list_sy, 1) 
akseselemen(list_sy, 5)  