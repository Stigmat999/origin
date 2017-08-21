nginx_log_file = open("nginx.log")

success_requests = 0
ip_list = []

for line in nginx_log_file:
    line_list = line.split(" ")

    if line_list[8] == "500":
        code500 = open("code500.txt", "a")
        code500.write(line)
        code500.close()

    if line_list[8] == "200" and line_list[5] == "\"GET":
        success_requests += 1

    if line_list[0] not in ip_list:
        ip_list.append(line_list[0])
        
print("Code 200 and GET = " + str(success_requests))
print("Unique IP-adress: " + str(ip_list))
