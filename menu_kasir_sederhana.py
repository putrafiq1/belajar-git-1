import os 

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
        pass
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
      
def input_data_barang():
  pass
