from PIL import Image


def lutPNG2Cube(pngFile):
    LUT_3D_SIZE = 64
    img = Image.open(pngFile)
    img_array = img.load()

    fo = open(pngFile.split(".")[0]+".cube", "w")
    fo.writelines("LUT_3D_SIZE " + str(LUT_3D_SIZE) + "\n")

    totalLine = 0
    for z in range(LUT_3D_SIZE):
        startX = LUT_3D_SIZE * (int(z % 8))
        startY = LUT_3D_SIZE * (int(z / 8))
        for y in range(LUT_3D_SIZE):
            for x in range(LUT_3D_SIZE):
                if len(img_array[x + startX, y + startY])==4:
                    r, g, b, a = img_array[x + startX, y + startY]
                else:
                    r, g, b = img_array[x + startX, y + startY]
                fo.writelines(
                    str(round(float(r / 255), 9)) + " " + str(round(float(g / 255), 9)) + " " + str(round(float(b / 255), 9)) + "\n")
                totalLine = totalLine+1
    fo.close()
    print("Done, "+ pngFile+"  total line:"+str(totalLine))


lutPNG2Cube("test_lut.png")
