import os
import sys

def main():
  print("Github dan veri indirme başlatılıyor...")
  os.system("git clone --depth=1 https://github.com/adi1090x/termux-desktop.git")
  print("kullanım klasörü değiştiriliyor")
  os.chdir("/termux-desktop")
  os.system("chmod +x setup.sh")
  os.system("clear")
  input("Birazdan Termux desktop kurulumu başlayacak \n  ilk başta şifre girmeniz istenecek \n ardından şifreyi doğruladıktan sonra \n view-only sorusu gelecek ona \n n diyip devam edin \n işlemlere başlamak için 'Enter' basınız")
  os.system("clear")
  print("Kurulum işlemleri başlatılıyor...")
  os.system("./setup.sh --install")
