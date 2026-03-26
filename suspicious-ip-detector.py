with open("login-logs.txt") as f:
    lines = f.readlines()

count = {}

for line in lines:
    if "FAILED" in line:
        ip = line.split()[-1]
        count[ip] = count.get(ip, 0) + 1

for ip in count:
    if count[ip] >= 3:
        print("Suspicious IP:", ip)