from PIL import Image


def lutPNG2Cube(pngFile):
    LUT_3D_SIZE = 64
    img = Image.open(pngFile)
    img_array = img.load()

    fo = open(pngFile.split(".")[0]+".cube", "w")
    fo.writelines("LUT_3D_SIZE " + str(LUT_3D_SIZE) + "\n")

    for z in range(LUT_3D_SIZE):
        startX = LUT_3D_SIZE * (z % 8)
        startY = LUT_3D_SIZE * (z / 8)
        for y in range(LUT_3D_SIZE):
            for x in range(LUT_3D_SIZE):
                # r, g, b, a = img_array[x + startX, +startY]
                r, g, b = img_array[x + startX, +startY]
                fo.writelines(
                    str(round(r / 255, 6)) + " " + str(round(g / 255, 6)) + " " + str(round(b / 255, 6)) + "\n")
    fo.close()


lutPNG2Cube("test_lut.png")
