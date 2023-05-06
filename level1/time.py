from datetime import datetime

d = "25/5/88"
end = datetime.strptime(d, "%d/%m/%y")
start = datetime.today()
print(end)
print(start)


diff = end - start
print(diff.days)