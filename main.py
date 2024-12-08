from data import data_pengguna
def cek_saldo(nomor_rekening):
    if nomor_rekening in data_pengguna:
        print('Saldo Anda:', data_pengguna[nomor_rekening]['saldo'])
    else:
        print("Nomor rekening tidak dapat di temukan")

def tarik_tunai(nomor_rekening, jumlah):
    if nomor_rekening in data_pengguna:
        if data_pengguna[nomor_rekening]['saldo'] >= jumlah:
            data_pengguna[nomor_rekening]['saldo'] -= jumlah
            print('Penarikan berhasil. saldo anda sekarang:', data_pengguna[nomor_rekening]['saldo'])
        else:
            print('Saldo tidak mencukupi')

    else: 
        print('Nomor rekening tidak di temukan')


def transfer(nomor_rekening_pengirim, nomor_rekening_tujuan ,jumlah):
    if nomor_rekening_pengirim in data_pengguna and nomor_rekening_tujuan in data_pengguna:
        if data_pengguna[nomor_rekening_pengirim]['saldo'] >= jumlah:
            data_pengguna[nomor_rekening_pengirim]['saldo'] -= jumlah
            data_pengguna[nomor_rekening_tujuan]['saldo'] += jumlah
            print('Transfer Berhasil')

        else: 
            print('Saldo tidak mencukupi')
    else:
        print('Nomor rekening tidak di temukan')

while True: 
    print("\n|======================================================|")
    print("|         Selamat datang di ATM sederhana              |")
    print("|======================================================|\n")
    nomor_rekening = input('Masukan Nomor Rekening: ')
    pin = int(input("Masukan PIN : "))
    if nomor_rekening in data_pengguna and data_pengguna[nomor_rekening]['pin'] == pin:
        while True:
            print("|==============================================|")
            print("|        Selamat Datang di ATM Sederhana       |")
            print("|==============================================|")
            print("|                 1). Cek Saldo                |")
            print("|                 2). Transfer Uang            |")
            print("|                 3). Tarik Tunai              |")
            print("|                 4). Keluar                   |")
            print("|==============================================|")
            pilihan = input('Pilih Menu (1/2/3/4):')

            if pilihan == "1":
                cek_saldo(nomor_rekening)
            elif pilihan == "2":
                nomor_rekening_tujuan = input('Masukan nomor rekening tujuan:')
                jumlah = int(input('Masukan jumlah yang ingin di transfer:'))
                transfer(nomor_rekening, nomor_rekening_tujuan, jumlah)
            elif pilihan == '3':
                jumlah = int(input("Masukan jumlah yang ingin ditarik: "))
                tarik_tunai(nomor_rekening, jumlah)
            elif pilihan == '4':
                print("Terima kasih telah menggunakan ATM Kami !")
                break
            else:
                print("Pilihan tidak valid")

        else: 
             print("Nomor rekening atau pin salah")