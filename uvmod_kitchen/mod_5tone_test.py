# Test for use test to send a selective 5-tone ZVEI2 instead of DTMF 123A1
# unfortunately the minimum tone pause is 30ms
ton1 = int(1270 * 10.32444) # tono 1 ZVEI2
ton2 = int(1060 * 10.32444) # tono 3 ZVEI2
ton3 = int(2200 * 10.32444) # tono 9 ZVEI2
ton4 = int(1160 * 10.32444) # tono 2 ZVEI2
##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct
print('Running',os.path.basename(sys.argv[0]),'mod...')

fw =  bytearray(open(sys.argv[1],'rb').read())

# if fw[0xaed0:0xaed0+4] == struct.pack('<I',0x142a) and fw[0xaed4:0xaed4+4] == struct.pack('<I',0x1c3b):
print('Changing  tones...')
fw[0xa4dc] = 0x00
fw[0xa4dd] = 0x00
fw[0xa4e0:0xa4e0+4] = struct.pack('<I',ton1)
fw[0xa4e4] = 0x00
fw[0xa4e5] = 0x00
fw[0xa4e8:0xa4e8+4] = struct.pack('<I',ton2)
fw[0xa4ec:0xa4ec+4] = struct.pack('<I',ton3)
fw[0xa4f0] = 0x00
fw[0xa4f1] = 0x00
fw[0xa4f4] = 0x00
fw[0xa4f5] = 0x00
fw[0xa4f8:0xa4f8+4] = struct.pack('<I',ton4)
    
# else:
#    print('ERROR: Cant find function')


open(sys.argv[1],'wb').write(fw)

