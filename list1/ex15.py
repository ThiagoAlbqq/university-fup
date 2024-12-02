time = int(input())
hrs = time // 360
mins = time % 360 // 60
segs = time % 360 % 60
print(hrs, mins, segs)