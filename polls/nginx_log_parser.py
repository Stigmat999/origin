def nginx_log_parser():

    import sys

    import psycopg2

    conn = psycopg2.connect(database="rusbd", user="rus", password="111", host="127.0.0.1", port="5432")
    cur = conn.cursor()

    cur.execute("delete from nginx_log_parser");

    nginx_log_file = open("/home/rus/nginx.log")

    list_for_views = []

    for line in nginx_log_file:

        line_list = line.split(" ")

        list_for_views.append(line_list)

        query_params = '{}, \'{}\', \'{}\''.format(int(line_list[8]), line_list[0], line_list[5].replace("\"",""))

        cur.execute("insert into nginx_log_parser (code, ip, method) \
            values ({}) ".format(query_params) );

    return list_for_views

    conn.commit()
    conn.close()

