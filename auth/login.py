from db.connection import get_connection

def login_user(nama,password) :
    conn = get_connection()
    cursor = conn.cursor ()
    
    query = "SELCET * FROM users WHERE nama = %s AND password = %s"
    cursor.execute(query,(nama,password))
    user=cursor.fetchone()
    
    if user :
        print ("Login berhasil selamat datang ", user [1])
        
    else : 
        print ("Login gagal. Nama atau password mungkin salah ")
        
    cursor.close ()
    conn.close ()