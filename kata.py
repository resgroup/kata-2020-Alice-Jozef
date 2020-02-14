import numpy as np


# Session1 kata module

def berlin_clock(input_string):
    # Get number of hours
    hours = int(input_string.split(':')[0])
    minutes = int(input_string.split(':')[1])
    seconds = int(input_string.split(':')[2])

    top_light = ['O']
    top_row = ['O', 'O', 'O', 'O']
    second_row = ['O', 'O', 'O', 'O']
    third_row = ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
    fourth_row = ['O', 'O', 'O', 'O']

    number_lights_on_top_light = get_number_lights_on_top_light(seconds)
    update_lights_in_row(number_lights_on_top_light, top_light, 'Y')

    number_lights_on_top_row = get_number_lights_on_top_row(hours)
    update_lights_in_row(number_lights_on_top_row, top_row, 'R')

    number_lights_on_second_row = get_number_lights_on_second_row(hours)
    update_lights_in_row(number_lights_on_second_row, second_row, 'R')

    number_lights_on_third_row = get_number_lights_on_third_row(minutes)
    update_lights_in_row(number_lights_on_third_row, third_row, 'Y')

    number_lights_on_fourth_row = get_number_lights_on_fourth_row(minutes)
    update_lights_in_row(number_lights_on_fourth_row, fourth_row, 'Y')

    clock = top_light
    clock.append(top_row)
    clock.append(second_row)
    clock.append(third_row)
    clock.append(fourth_row)

    return clock


def get_number_lights_on_fourth_row(minutes):
    number_lights_on_fourth_row = minutes % 5
    return number_lights_on_fourth_row


def get_number_lights_on_third_row(minutes):
    number_lights_on_third_row = int(np.floor(minutes / 5))
    return number_lights_on_third_row


def update_lights_in_row(number_lights_on_row, row, colour):
    for i, value in enumerate(row[:number_lights_on_row]):
        row[i] = colour
    return row


def get_number_lights_on_top_light(seconds):
    number_lights_on_top_light = (seconds + 1) % 2
    return number_lights_on_top_light


def get_number_lights_on_top_row(hours):
    number_lights_on_top_row = int(np.floor(hours / 5.0))
    return number_lights_on_top_row


def get_number_lights_on_second_row(hours):
    number_lights_on_second_row = hours % 5
    return number_lights_on_second_row


if __name__ == '__main__':
    print(berlin_clock('12:56:01'))
