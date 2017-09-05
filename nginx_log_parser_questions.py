import sys

import psycopg2

conn = psycopg2.connect(database="rusbd", user="rus", password="111", host="127.0.0.1", port="5432")
cur = conn.cursor()

if sys.argv[1] == "fill":

    cur.execute("delete from nginx_log_parser");

    nginx_log_file = open("nginx.log")

    for line in nginx_log_file:

        line_list = line.split(" ")

        query_params = '{}, \'{}\', \'{}\''.format(int(line_list[8]), line_list[0], line_list[5].replace("\"",""))

        cur.execute("insert into nginx_log_parser (code, ip, method) \
            values ({}) ".format(query_params) );

    conn.commit()
    conn.close()

if sys.argv[1] == "count":
    
# Вот здесь вместо rows = cur.fetchall(), for row in rows:, str(rows[0]), str(rows[1]), str(rows[2]), написал unique_elements и не работает код
# пишет list index out of range

	cur.execute("select count (distinct ip), count (distinct method), count (distinct code) from nginx_log_parser");
	unique_elements = cur.fetchall()

	for element in unique_elements:

		print("IP: " + str(unique_elements[0]) + ", METHOD: " + str(unique_elements[1]) + ", CODE: " + str(unique_elements[2]))


conn.close()