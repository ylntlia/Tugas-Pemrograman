import texttable as tt
import getpass

def menu():
    print("==========================================")
    print("\n\t----pilihan---")
    print("\t1. penilaian mahasiswa")
    print("\t2. pembayaran mahasiswa")

    pilih=input("\n\tsilakan pilih : ")
    if pilih == "1":
        nilai_mahasiswa()
    elif pilih == "2":
        pembayaran()
    else:
        exit
    tanya()

def tanya():
    tanya = input("\nKembali ke menu (y\n)?")
    if tanya == "y":
        menu()
    elif tanya == "t":
        exit
    else:
        print ("\n\tSalah input................!!!")

def nilai_mahasiswa():
    nama = []
    nim = []
    nilai_tugas = []
    nilai_uts = []
    nilai_uas = []
    nilai_akhir = []

    x = [[]]

    jawab = "y"

    tab = tt.Texttable()

    while (jawab == 'y'):
        print("\n======================================")
        nama.append(input("\n\tMasukkan Nama: "))
        nim.append(input("\tMasukkan Nim: "))
        tugas = int(input("\tNilai Tugas: "))
        tugas = float(tugas)
        nilai_tugas.append(tugas)
        uts = int(input("\tNilai UTS: "))
        uts = float(uts)
        nilai_uts.append(uts)
        uas = int(input("\tNilai UAS: "))
        uas = float(uas)
        nilai_uas.append(uas)
        hasil = (tugas+uts+uas)/3
        nilai_akhir.append(hasil)
        jawab = input("\n\tTambah data [y/n]? ")

    for i in nama:
        idx = nama.index(i)
        x.append([idx+1,nama[idx],nim[idx],nilai_tugas[idx],nilai_uts[idx],nilai_uas[idx],nilai_akhir[idx]])
    tab.add_rows(x)
    tab.set_cols_align(['l','l','l','r','r','r','r'])
    tab.header(['No','Nama','Nim','Nilai Tugas','Nilai UTS','Nilai UAS','Nilai Akhir'])
    print(tab.draw())

def pembayaran():
    print("\n===========================================")
    nama = input("\n\tmasukan nama = ")
    nim = input("\tMasukan nim = ")
    semester=input("\tmasukan semester saat ini = ")
    print("\n\t---pilihan pembayaran---")
    print("\t1. pembayaran spp")
    print("\t2. pembayaran uts")
    print("\t3. pembayaran uas")
    print("\t4. pembayaran spp & uts")
    print("\t5. pembayaran spp & uas")
    pilih = input("\n\tsilahkan pilih : ")
    if pilih == "1":
        spp()
    elif pilih == "2":
        uts()
    elif pilih == "3":
        uas()
    elif pilih == "4":
        spp_uts()
    elif pilih == "5":
        spp_uas()
    else:
        exit
        tanya()
def spp():
    bulan=int(input("\n\tjumlah bulan yang di bayar = "))
    bulan = float(bulan)
    total = 350000*bulan
    print("=====================================================")
    print("\ttotal bayar spp Rp.350000 *", bulan," = Rp.",total)

def uts():
    matkul = int(input("\n\tjumlah mata kuliah = "))
    matkul = float(matkul)
    byr_uts = 25000*matkul
    print("=====================================================")
    print("\ttotal bayar uts Rp.25000 *",matkul," = Rp.",byr_uts)

def uas():
    matkul =int(input("\n\tjumlah mata kuliah = "))
    matkul = float(matkul)
    byr_uas = 50000*matkul
    print("=====================================================")
    print("\ttotal bayar uas Rp.50000 *",matkul," = Rp.",byr_uas)

def spp_uts():
    bulan=int(input("\n\tjumlah bulan yang di bayar = "))
    matkul =int(input("\n\tjumlah mata kuliah = "))
    matkul = float(matkul)
    bulan = float(bulan)
    total_spp = 350000*bulan
    byr_uts = 25000*matkul
    total = total_spp + byr_uts + 5000
    print("\n\ttotal bayar spp Rp.350000 *",bulan," = Rp.",total_spp)
    print("\ttotal bayar uts Rp.25000 *",matkul," = Rp.",byr_uts)
    print("\tbiaya tambahan server sebesar Rp.5000")
    print("======================================================")
    print("\ttotal yang harus di bayar" ,total)

def spp_uas():
    bulan=int(input("\n\tjumlah bulan yang di bayar = "))
    matkul =int(input("\n\tjumlah mata kuliah = "))
    matkul = float(matkul)
    bulan = float(bulan)
    total_spp = 350000*bulan
    byr_uas = 50000*matkul
    total = total_spp + byr_uas + 5000
    print("\n\ttotal bayar spp Rp.350000 *",bulan," = Rp.",total_spp)
    print("\ttotal bayar uas Rp.50000 *",matkul," = Rp.",byr_uas)
    print("\tbiaya tambahan server sebesar Rp.5000")
    print("======================================================")
    print("\ttotal yang harus di bayar Rp.",total)

username = input("\nUsername : ")
password = getpass.getpass()
print("==========================================================")

if username == "yulianti" and password == "ylntlia21":
    menu()

else:
    print("maaf passwor atau username mu salah................!!!")




    
                   
