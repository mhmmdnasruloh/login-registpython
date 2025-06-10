from db.connection import get_connection

def login_user(nama,password) :
    conn = get_connection()
    cursor = conn.cursor ()
    
    query = "SELECT * FROM users WHERE nama = %s AND password = %s"
    cursor.execute(query,(nama,password))
    user=cursor.fetchone()
    
    if user :
        return {"status": "succes", "message ": f"login berhasil, selamat datang {user[1]}"}
    else : 
       return {"status " : "fail", "message": "login gagal,nama atau password salah"}
        
    cursor.close ()
    conn.close ()