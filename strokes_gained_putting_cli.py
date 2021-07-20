# Baseline data from the PGA tour for a tour pro for strokes gained putting.
from strokes_gained_calculations import calculate_strokes_gained_putting as sgp
import json

def get_baseline_data(input_file):
    '''Get stored baseline data if available'''
    try:
        with open(input_file) as f:
            input_data = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return input_data


def capture_putting_input ():
    '''Present a prompt to the user to capture input for Strokes Gained putting
    and return the information in dictionary'''

    user_input = {}

    user_input['distance'] = int(input("Enter the distance: "))
    user_input['putts'] = int(input("How many putts did you have: "))

    print(f"\nYou entered {user_input['putts']} putts from a distance of {user_input['distance']} feet.\n")

    return user_input

# Load the input database
file_name = 'sg_putts_baseline.json'
tour_pro_sg_putts_baseline = get_baseline_data(file_name)

if tour_pro_sg_putts_baseline:
    # capture the input from the command line prompt
    putts_input = capture_putting_input()

    strokes_gained = sgp(tour_pro_sg_putts_baseline, putts_input)

    print(f"\nThe final strokes gained value is: {strokes_gained}!")
else:
    print(f"The input file {file_name} does not exist")

#filename = 'sg_putts_baseline.json'
#with open(filename, 'w') as f:
#    json.dump(tour_pro_sg_putts_baseline, f)
