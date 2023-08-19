# If you want, change the frequencies of the tone burst.

tone = int(1050) # change 1750Hz  to 1050 Hz for test NOAA channel , if want ,can change any frequency in Hz


##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct
print('Running',os.path.basename(sys.argv[0]),'mod...')

fw =  bytearray(open(sys.argv[1],'rb').read())

if fw[0x29cc] == 0xd6 and fw[0x29cd] == 0x06 :
    print('Changing tone burst frequency to',tone,'Hz')
    fw[0x29cc:0x29cc+4] = struct.pack('<I',tone)
    
else:
    print('ERROR: Cant find function')


open(sys.argv[1],'wb').write(fw)
