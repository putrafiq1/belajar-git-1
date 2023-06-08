import os 

data_barang = []
data_transaksi = []

def menu():
  os.system('cls')
  while True:
    print('='*30)
    print('MENU KASIR SEDERHANA'.center(30))
    print('='*30)
    print('1. Input Data Barang')
    print('2. Input Data Konsumen')
    print('0. Exit')
    print('='*30)
    try:
      pilihan = int(input('Pilih Menu: '))
      if pilihan == 1:
        os.system('cls')
        input_data_barang()
      elif pilihan == 2:
        pass
      elif pilihan == 0:
        os.system('cls')
        print('='*30)
        print('Terima kasir Telah Menggunakan Program'.center(30))
        print('='*30)
        return
      else:
        os.system('cls')
        print(f'Tidak Ada Menu Ke-{pilihan}'.center(30))
    except ValueError:
      os.system('cls')
      print('!! Input Harus Angka !!'.center(30))
      
      
def validasi_input(perintah,validasi):
  while True:
    user_input = input(perintah)
    if not user_input:
      print('='*30)
      print('Harus Diisi'.center(30))
      print('='*30)  
      continue
    if validasi(user_input):
      return user_input
    print('='*30)
    print('Input Salah'.center(30))
    print('='*30)
   
   
def input_data_barang():
  print('='*30)
  print('Input Data Barang'.center(30))
  print('='*30)
  nobarang = validasi_input('NOMER BARANG: ', lambda x: x.isdigit() and len(x) == 4)
  nama = validasi_input('NAMA BARANG : ',lambda x: bool(x))
  harga = validasi_input('HARGA BARANG: ', lambda x: x.isdigit() and int(x) > 0)
  stok =  validasi_input('JUMLAH STOCK:', lambda x : x.isdigit() and int(x) > 0)
  print('='*30)
  saran = validasi_input('Apakah Ingin Menambahkan Data Ini? [Y/N] ', lambda x : bool(x))
  if saran.upper() == 'Y':
    data_barang.append({
      'Nomer Barang' : int(nobarang),
      'Nama Barang' : nama.upper(),
      'Harga Barang' : int(harga),
      'Jumlah Stock': int(stok)
    })
    os.system('cls')
    print('Data Barang Berhasil Ditambahkan'.center(30))
  else:
    os.system('cls')
    print('Data Tidak Ditambahkan'.center(30))
    
menu()