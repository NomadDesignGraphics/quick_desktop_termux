import os
import sys

os.system("git clone --depth=1 https://github.com/adi1090x/termux-desktop.git")
os.system("cd termux-desktop")
os.system("+x setup.sh")
os.system("clear")
input("Birazdan Termux desktop kurulumu başlayacak \n  ilk başta şifre girmeniz istenecek \n ardından şifreyi doğruladıktan sonra \n view-only sorusu gelecek ona \n n diyip devam edin \n işlemlere başlamak için 'Enter' basınız")
os.system("clear")
os.system("./setup.sh --install")