import mysql.connector


conn = mysql.connector.connect(host='localhost',
                           user='root',
                           password='Rocky0925!!!',
                           database='movies')
cursor = conn.cursor()
print(f"Database connection opened.")

#---Query 1: selecting all fields for table :studio ---

print("---Displaying Studio RECORDS---\n----")


query_1="SELECT * FROM studio;"

cursor.execute(query_1)

#fetch results
results1=cursor.fetchall()

#print results with associated descriptions

for row in results1:
    print(row)
    print("-" * 25+"\n")


#---Query 2: Selecting all fields for the table : genre ---
print("---Displaying Studio Records----")
query_2="SELECT * FROM genre;"
cursor.execute(query_2)
results2=cursor.fetchall()

for row in results2:
    print(row)

    print("-" * 25+"\n")



 # --- Query 3: Select movie names for movies with runtime less than two hours ---
print("--- DISPLAYING Short Film RECORDS ---")
 # Assuming runtime is stored in minutes
query_3 = "SELECT film_name,film_runtime  FROM film WHERE film_runtime < 120;"
cursor.execute(query_3)
results3 = cursor.fetchall()

for row in results3:
    print(f"Film: {row[0]}, Runtime: {row[1]} minutes")
print("-" * 40 + "\n")


#----Query 4 : get list of film names and directors grouped by associated director----
print("DISPLAYING Director RECORDS in Order")

query_4 = "SELECT film_director,GROUP_CONCAT(film_name, ' ||') FROM film GROUP BY film_director;"
cursor.execute(query_4)
results4 = cursor.fetchall()
for row in results4:
    print(row)
    print("-" * 25+"\n")


