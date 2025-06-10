from db.connection import get_connection

def register_user(nama,password) :
    conn = get_connection()
    cursor = conn.cursor()
    
    try :
        query = "INSERT INTO users  (nama, password ) VALUES  (%s, %s)"
        cursor.execute (query,(nama,password))
        conn.commit()
        return {"status ": "success", "message": "register erhasil"}
    except Exception as e:
        return {"status" : "error", "message": f"terjadi error: {e}"} 

    finally :
        cursor.close()
        conn.close()