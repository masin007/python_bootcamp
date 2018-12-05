# import sys
# try:
#     print(sys.argv[1])
# except IndexError:
#     print("Zapomniales podac nzawe pliku")
#
#
#
# with open(sys.argv[1]) as f: #context manager
#
#     slownik = {}
#     for linia in f:
#         linia = linia.split(";")
#         user = linia[0]
#         action = linia[1]
#         time = linia[2]
#         time = int(time)
#
#         if action == "LOGIN":
#             slownik.get[user] =  - time
#         if action == "LOGOUT":
#             slownik.get[user] =  time
#
#     print(slownik)

#rozwiazanie 1
# file_name = "dane/logs.txt"
#
# user_last_login = {}
# user_total_time = {}
#
# with open(file_name) as f:
#     for line in f:
#         user, action, time_str = line.split(";")
#         time = int(time_str)
#         if action == "LOGIN":
#             user_last_login[user] = time
#         elif action =="LOGOUT":
#             # logout - login
#             time_temp = time - user_last_login[user]
#             user_total_time[user] = user_total_time.get(user, 0) + time_temp
#
# print("Czas przebywania w systemie")
# for user, time in sorted(user_total_time.items(), key=lambda x: x[1]):
#     print(f"- {user}: {time} s")

#rozwiazanie 3

file_name = "dane/logs.txt"

out = {}
with open(file_name) as f:
    for line in f:
        user, action, time_str = line.split(";")
        time = int(time_str)
        if action =="LOGIN":
            out[user] = out.get(user, 0) - time
        if action =="LOGOUT":
            out[user] = out.get(user, 0) + time

print("Czas przebywania w systemie")
for user, time in sorted(out.items(), key=lambda x: x[1]):
    print(f"- {user}: {time} s")


