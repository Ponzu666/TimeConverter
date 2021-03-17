while True:
    try:
        n = int(input('Masukkan Detik : '))
    except ValueError:
        print('Invalid Input!')
        continue

    if n <= 0:
        print('Invalid Input!')
        continue
    elif n >= 359999:
        print('Invalid Input!')
    elif n == float:
        print('Invalid Input')
    else:
        break

def convert(detik): 
    detik = detik
    jam = detik // 3600
    detik %= 3600
    menit = detik // 60
    detik %= 60
      
    return "%d:%02d:%02d" % (jam, menit, detik) 

print(convert(n)) 
