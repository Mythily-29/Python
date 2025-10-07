from models.config import dbconnect

def query_operations(query,values=None,fetch=False,commit=False):
    conn=dbconnect()
    cursor=conn.cursor()

    cursor.execute(query,values) if values else cursor.execute(query)

    fetchdata=cursor.fetchall() if fetch else None

    conn.commit() if commit else None

    cursor.close()
    conn.close()

    return fetchdata

