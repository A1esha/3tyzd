# 3. zadanie: kalendár
# autor: Yesipovich Aliaksei
# datum: 09.10.2020

def pocet_dni_v_mesiaci(mesiac, priestupny=False):
    if(mesiac == 'jan'):
        return 31
    if(mesiac == 'feb'):
        if(priestupny):
            return 29
        else:
            return 28
    if(mesiac == 'mar'):
        return 31
    if(mesiac == 'apr'):
        return 30
    if(mesiac == 'maj'):
        return 31
    if(mesiac == 'jun'):
        return 30
    if(mesiac == 'jul'):
        return 31
    if(mesiac == 'aug'):
        return 31
    if(mesiac == 'sep'):
        return 30
    if(mesiac == 'okt'):
        return 31
    if(mesiac == 'nov'):
        return 30
    if(mesiac == 'dec'):
        return 31
def pocet_dni_medzi(datum1, datum2):
    pos1 = datum1.find('.')
    pos2 = datum2.find('.')
    m1 = datum1[:3]
    m2 = datum2[:3]
    r1 = int(datum1[pos1+1:])
    r2 = int(datum2[pos2+1:])
    ans = 0

    s = ['jan', 'feb', 'mar', 'apr', 'maj', 'jun', 'jul', 'aug', 'sep', 'okt', 'nov', 'dec']

    if r1 == r2:
        flag = False
        for i in s:
            if i == m1:
                flag = True
            if i == m2:
                flag = False
            if flag:
                ans += pocet_dni_v_mesiaci(i, r1 % 4 == 0)
        return ans


    flag1 = False
    for i in s:
        if i == m1:
            flag1 = True
        if flag1:
            ans += pocet_dni_v_mesiaci(i, r1 % 4 == 0)
            flag1 = True


    for i in range(r1+1, r2):
        if i % 4 == 0:
            ans += 366
        else:
            ans += 365


    for i in s:
        if i != m2:
            ans += pocet_dni_v_mesiaci(i, r2 % 4 == 0)
        if i == m2:
            break

    return ans
def den_v_tyzdni(date1):
    pos1 = date1.find('.')
    pos2 = date1.find('.', 3)
    day = int(date1[:pos1])
    month = date1[pos1+1:pos2]
    year = int(date1[pos2+1:])
    month = month[:3]

    monthes = ['jan', 'feb', 'mar', 'apr', 'maj', 'jun', 'jul', 'aug', 'sep', 'okt', 'nov', 'dec']
    kol = 1
    M = 0
    for i in monthes:
        if i == month:
            M = kol
        kol += 1

    a = int((14-M)/12)
    y = int(year - a)
    m = int(M + 12 * a - 2)
    day_of_week = int(7000 + (day + y + int(y/4) - int(y/100) + int(y/400) + int((31 * m)/12)))
    day_of_week %= 7
    ans = ['ned', 'pon', 'uto', 'str', 'stv', 'pia','sob']
    return ans[day_of_week]
def kalendar(datum):
    pos = datum.find('.')
    mm = datum[:3]
    yy = int(datum[pos+1:])

    day_of_week = ['pon', 'uto', 'str', 'stv', 'pia', 'sob', 'ned']
    now = den_v_tyzdni(str(1) + "." + mm + '.' + str(yy))

    day = 0
    for i in day_of_week:
        if i == now:
            break
        day += 1

    print('pon', 'uto', 'str', 'stv', 'pia', 'sob', 'ned')

    p = pocet_dni_v_mesiaci(mm, yy % 4 == 0)

    for i in range(1, p + day + 1):
        if i <= day:
            print("   ", end=' ')
        else:
            print("{:3d}".format(i-day), end=' ')
            if i % 7 == 0:
                print()

#календарь
