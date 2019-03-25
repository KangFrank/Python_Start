R = 10000
R2 = R * R
count = 0
for x in range(-R, R+1):
    for y in range(-R, R+1):
        if x * x + y * y <= R2:
            count += 1
print(count / R2)