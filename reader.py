import zbarlight
import os
import sys
import PIL

print 'Taking picture..'
try:
    f = 1
    qr_count = len(os.listdir('qr_codes'))
    os.system('sudo fswebcam -d /dev/video'+sys.argv[1]+' -q qr_codes/qr_'+str(qr_count)+'.jpg')
    print 'Picture taken..'
except:
    f = 0
    print 'Picture couldn\'t be taken..'

print

if(f):
    print 'Scanning image..'
    f = open('qr_codes/qr_'+str(qr_count)+'.jpg','rb')
    qr = PIL.Image.open(f);
    qr.load()

    codes = zbarlight.scan_codes('qrcode',qr)
    if(codes==None):
        os.remove('qr_codes/qr_'+str(qr_count)+'.jpg')
        print 'No QR code found'
    else:
        print 'QR code(s):'
        print codes
        f = open('qr_code_messages.txt','a')
        for i in range(len(codes)):
            f.write(codes[i])
            if(i!=len(codes)-1):
                f.write('^')
        f.write('~')
