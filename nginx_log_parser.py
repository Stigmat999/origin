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

	cur.execute("select count (distinct ip), count (distinct method), count (distinct code) from nginx_log_parser");
	rows = cur.fetchall()

	for row in rows:

		print("IP: " + str(row[0]) + ", METHOD: " + str(row[1]) + ", CODE: " + str(row[2]))


conn.close()