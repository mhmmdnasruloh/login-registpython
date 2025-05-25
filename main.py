from auth.register import register_user
from auth.login import login_user 


while True :
    print ("\n1. Register\n2. login\n3. keluar")
    pilihan = input("pilihan menu :")
    
    if pilihan == "1" :
        nama = input("Nama : ")
        password =  input ("Password : ")
        register_user(nama,password)
    elif pilihan == "2" :
        nama = input ("Nama : ")
        password = input ("Password : ")
        login_user(nama,password)
    elif pilihan == "3" :
        print ("Program selesai ")
        break
    else :
        print ("pilihan tidak valid")
        
        