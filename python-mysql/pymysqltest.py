import pymysql
  
def mysqlconnect():
    # To connect MySQL database
    conn = pymysql.connect(
        host='localhost',
        user='root', 
        password = "mysqlroot",
        db='testdb',
        )
      
    cur = conn.cursor()
      
    # Select query
    cur.execute("select * from emp")
    output = cur.fetchall()
      
    for i in output:
        print(i[1])
      
    # To close the connection
    conn.close()
  
# Driver Code
if __name__ == "__main__" :
    mysqlconnect()