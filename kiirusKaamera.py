def is_speed(speed, speed_limit):
    speed_diff = speed - speed_limit
    if speed_limit == 0:
        return 'Sisestati vale piirkond'
    elif speed > speed_limit and speed_diff > 5:
        return 'Kiiruse yletamine ' + str(speed_diff) + ' km/h. Maaratakse trahv'
    elif speed > speed_limit:
        return  'Kiiruse yletamine ' + str(speed_diff) + ' km/h. Saab hoiatuse'
    else:
        return 'Hasti soidetud'

def calculate(area, speed):
    speed_limit = 0
    if area == 'linn':
        speed_limit = 50
    elif area == 'maantee':
        speed_limit = 90
    elif area == 'kiirtee':
        speed_limit = 120
    else:
        speed_limit = 0
    print(is_speed(speed, speed_limit))

# siit algab pohiprogrammi taitmine
area = input('Mis piirkonnas soidab (linn, maantee, kiirtee): ').lower()
speed = float(input('Mis kiirusega soidab (km/h): '))

calculate(area, speed)

