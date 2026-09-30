#Binary filter: Black and White

file = open('./volcan.bmp','rb')
fileo = open('./volcanFILTROejemplo.bmp','wb')
metadata = file.read(54)
fileo.write(metadata)

colors = [[0xFF,0xFF,0xFF],[0xD8,0xF3,0xDC] , [0xB7, 0xE4, 0xC7] , [0x95,0xD5,0xB2] , [0x74,0xC6,0x9D] , [0x52,0xB7,0x88] , [0x40, 0x91, 0x6C] , [0x2D, 0x6A, 0x4F] , [0x1B, 0x43, 0x32] , [0x08, 0x1C, 0x15] , [0x00,0x00,0x00] ]

file.seek(54,0)
no_pix = 0
limite = (pow(2, 24)-1)
while(True):
    pixel_data = file.read(3)
    if(len(pixel_data) > 0):
        valor_int = int.from_bytes(bytes(pixel_data),byteorder='little')
        if(valor_int>=limite/1):
            fileo.write(bytes(colors[0]))
        elif(valor_int>=limite/2):
            fileo.write(bytes(colors[1]))
        elif(valor_int>=limite/3):
            fileo.write(bytes(colors[2]))
        elif(valor_int>=limite/4):
            fileo.write(bytes(colors[3]))
        elif(valor_int>=limite/5):
            fileo.write(bytes(colors[4]))
        elif(valor_int>=limite/6):
            fileo.write(bytes(colors[5]))
        elif(valor_int>=limite/7):
            fileo.write(bytes(colors[6]))
        elif(valor_int>=limite/8):
            fileo.write(bytes(colors[7]))
        elif(valor_int>=limite/9):
            fileo.write(bytes(colors[8]))
        elif(valor_int>=limite/10):
            fileo.write(bytes(colors[9]))
        else:
            fileo.write(bytes(colors[10]))
        no_pix += 1
    else:
        break
print('No Pixels: '+str(no_pix))
file.close()
fileo.close()
