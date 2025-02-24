def secs(min, sec):
    seconds = min * 60
    return sec + seconds


print(secs(42, 42))
######


def miles(kms):
    return kms * 1/1.61


print(miles(10))
#####


def pace(km, min, sec):
    seco = min * 60
    secs = seco + sec
    return secs / miles(km)


print(pace(10, 42, 42))

x = y = 1
print(f'{str(x)}' + f'{str(y)}')
