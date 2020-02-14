import numpy as np
# Session1 kata module

def berlin_clock(input_string):
    # Get number of hours
    hours = int(input_string.split(':')[0])
    minutes = int(input_string.split(':')[1])
    seconds = int(input_string.split(':')[2])

    top_light = ['O\n']
    top_row = ['OOOO\n']
    second_row = ['OOOO\n']
    third_row = ['OOOOOOOOOOO\n']
    fourth_row = ['OOOO\n']

    if seconds % 2 == 0:
        top_light[0] = 'Y'

    number_lights_on_top_row = int(np.floor(hours / 5.0))
    top_row[:number_lights_on_top_row] = 'R'

    number_lights_on_second_row = hours % 5
    second_row[:number_lights_on_second_row] = 'R'

    number_lights_on_third_row = int(np.floor(minutes / 5))
    third_row[:number_lights_on_third_row] = 'Y'

    number_lights_on_fourth_row = minutes % 5
    fourth_row[:number_lights_on_fourth_row] = 'Y'

    print(top_light)
    print(top_row)
    print(second_row)

    clock = top_light
    clock = clock.append(top_row)
    clock = clock.append(second_row)
    clock = clock.append(third_row)
    clock = clock.append(fourth_row)

    return clock

if __name__ == '__main__':
    print(berlin_clock('12:56:01'))








