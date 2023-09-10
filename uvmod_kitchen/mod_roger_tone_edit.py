# If you want, configure these four parameters to change the frequencies and lenght of the roger beep two tones.

 
tone1 = 1033 # change 1033 to any frequency in Hz
tone2 = 2070 # change 2070 to any frequency in Hz
lt1 = 40 # change lenght tone1 150 to any time in ms (max 255 ms)
lt2 = 40 # change lenght tone2 80 to any time in ms (max 255 ms)

##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct
print('Running',os.path.basename(sys.argv[0]),'mod...')

fw =  bytearray(open(sys.argv[1],'rb').read())

if fw[0xaed0:0xaed0+4] == struct.pack('<I',0x142a) and fw[0xaed4:0xaed4+4] == struct.pack('<I',0x1c3b):
    
    fw[0xaed0:0xaed0+4] = struct.pack('<I',int(tone1 * 10.32444))
    fw[0xaed4:0xaed4+4] = struct.pack('<I',int(tone2 * 10.32444))
    fw[0xae9a] = lt1
    fw[0xaeb2] = lt2
    print('Change roger beep Tono1',tone1,'Hz',lt1,'ms & Tono2',tone2,'Hz',lt2,'ms')
    
else:
    print('ERROR: Cant find function')


open(sys.argv[1],'wb').write(fw)

