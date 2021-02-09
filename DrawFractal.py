import math
from Color import Color
from Complex import Complex

#The commented parts would generate the second fractal in the gallery

pmap = []

height = 535
width = 1050
plane_height = 0.00062899471 #/ 9
plane_width = 0.00123492117 #/ 9
step_x = 0.0
step_y = 0.0
init_x = 1.224153001013#(82 / 1050 * 0.00123492117 + 1.224153001013) - 0.00123492117 / (9 * 2)
init_y = -2.26605375786#(149 / 535 * 0.00062899471 - 2.26605375786) - 0.00062899471 / (9 * 2)
pmul = Complex(1, 1)
bailout = 14567898734578675667654367678854677754676786546676
maxCount = 1000
colors = []

pixelVal = Complex(0, 0)
offset = Complex(0, 0)
z = Complex(0, 0)

def initialize():
    global pmap
    global colors
    for l in range(height):
        pmap.append([])
        for w in range(width):
            pmap[l].append("")
            
    colors.append(Color(0, 7, 100))
    colors.append(Color(32, 107, 203))
    colors.append(Color(237, 255, 255))
    colors.append(Color(255, 170, 0))
    colors.append(Color(0, 2, 0))
    colors.append(Color(0, 7, 100))

    global step_x
    global step_y
    step_x = float(plane_width / width)
    step_y = float(plane_height / height)

print("Initializing...")
initialize()
print("Initialized. Generating image (this can take a long time depending on resolution)...")

y = init_y + step_y / 2
for l in range(height):
    x = init_x + step_x / 2
    for w in range(width):
        pixelVal.re = x
        pixelVal.im = y
        offset.re = pixelVal.re
        offset.im = pixelVal.im
        offset.multiply(pmul)
        z.re = pixelVal.re
        z.im = pixelVal.im
        count = 0;
        while z.norm() < bailout:
            z.pow(pixelVal)
            z.add(offset)
            count += 1
            if count >= maxCount:
                break
            
        zn = count - math.log(math.log(z.norm()) / math.log(bailout), pixelVal.norm())
        zn = 1.5 * zn#1.8 * zn
        ratio = (math.floor(zn) % 360) / 360 - 0.2#0.4

        new_color = Color.interpolate(colors, ratio, "cosine")
        pmap[l][w] += str(int(new_color.r)) + " " + str(int(new_color.g)) + " " + str(int(new_color.b)) + " "
        
        x += step_x
    y += step_y

print("Done generating image. Writing to ppm file...")

f = open("fractal.ppm", "a")
f.write("p3\n" + str(width) + " " + str(height) + "\n" + str(255) + "\n")
for l in range(height):
    for w in range(width):
        f.write(pmap[l][w])

print("Done writing to file")
        

