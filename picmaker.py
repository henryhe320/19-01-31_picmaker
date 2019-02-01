import math
f = open('pic.ppm', 'w')


rainbow = {}
r = 235
g = 0
b = 0
for i in range(355):
    rainbow[str(i)] = [r,g,b]
    if (i-1) // 59 == 0:
        if g == 0: g += 3
        else: g += 4
    if (i-1) // 59 == 1:
        if r == 3: r -= 3
        else: r -= 4
    if (i-1) // 59 == 2:
        if b == 0: b += 3
        else: b += 4
    if (i-1) // 59 == 3:
        if g == 3: g -= 3
        else: g -= 4
    if (i-1) // 59 == 4:
        if r == 0: r += 3
        else: r += 4
    if (i-1) // 59 == 5:
        if b == 3: b -= 3
        else: b -= 4

final = 'P3 501 501 235 \n'
for i in range(501):
    for j in range(501):
        color = rainbow[str(math.ceil(math.pow(((250-i)*(250-i) + (250-j)*(250-j)),.5)))]
        final += f'{color[0]} {color[1]} {color[2]} '

f.write(final)
f.close