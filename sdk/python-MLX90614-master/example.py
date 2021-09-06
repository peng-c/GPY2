from mlx90614 import MLX90614
import time

thermometer_address = 0x5a

thermometer = MLX90614(thermometer_address)

while True:
    print('start temperature measurement!')
    print('environment:')
    print (thermometer.get_amb_temp())
    print('people:')
    print (thermometer.get_obj_temp())
    time.sleep(2)

