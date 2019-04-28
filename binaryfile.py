import os
from time import sleep


def main():
    size = (os.path.getsize("./song.mp3"))
    size = size
    incommingfile = open("song.mp3", 'rb')
    outfile = open("control-copy", 'wb')
    chuncksize1 = size / 100
    chuncksize = int(chuncksize1)
    x= -1
   # print('copying ')
    while True:    
        chunckbuffer = incommingfile.read(chuncksize)
        if chunckbuffer:
            outfile.write(chunckbuffer)
            x +=1
            p= str(x)
            if x!=101:
                f='%'
            else:
                f=''
                pass
            sleep(0.1)
            print(16*'\b' + p + f +'  copying..', end='', flush=True)

        else:
            break
    outfile.close()
    print(16*'\b'+ 'Done  ', end='')
    sleep(2)
    print(20*'\b' +'You can now play the video!')

if __name__ == '__main__':
    main()
