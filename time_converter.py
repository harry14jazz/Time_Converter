h, m, s = 0, 0, 0
sisa_h, sisa_m, sisa_s = 0, 0, 0
def time_converter(time):
    if 0 < time <= 35999:
        if time >= 3600:
            sisa_h = time % 3600
            if sisa_h == 0:
                h = time // 3600
                m = 0
                s = 0
            else:
                h = time //3600
                if sisa_h >= 60:
                    m = sisa_h//60
                    s = sisa_h%60
                else:
                    s = time
        else:
            h = 0
            sisa_m = time % 60
            if sisa_m == 0:
                m = time//60
                s = 0
            else:
                m = time//60
                s = sisa_m 
            
        message = f'Konversi: {h:02}:{m:02}:{s:02}'
        return message
    else:
        return 'Invalid Input!'
    
######### Main Program
try:
    while True:
        time = int(input('Masukkan detik: '))
        print(time_converter(time))
        if time_converter(time) == 'Invalid Input!':
            break
        else:
            pass
        print('')
except:
    print('Invalid Input!')

