import sys

def error():
    print('This is not traffic light')


color = sys.argv[1].lower() if len(sys.argv) >= 2 else None

if color is not None:
    if color == 'green':
        print('Driver can drive a car')
    elif color == 'yellow':
        print('Driver has to be ready to stop the car or to start driving')
    elif color == 'red':
        print('Driver has to stop car and wait for green light')
    else:
        error()
else:
    error()
