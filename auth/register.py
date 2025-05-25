from db.connection import get_connection

def register_user(nama,password) :
    conn = get_connection()
    cursor = conn.cursor()
    
    try :
        query = "INSERT INTO users  (nama, password ) VALUES  (%s, %s)"
        cursor.execute (query,(nama,password))
        conn.commit()
        print ("Registrasi berhasil")
    except Exception as e:
        print("Terjadi error saat registrasi:", e)

    finally :
        cursor.close()
        conn.close()