from datetime import datetime
p1 = '10:04:00'
p2 = '11:03' # 
format = '%H:%M:%S'
time = datetime.strptime(p2, format) - datetime.strptime(p1, format)
print time
