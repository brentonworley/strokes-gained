def calculate_strokes_gained(reference_value, user_putts):
    '''Return the strokes gained based on reference and user input'''
    return round((reference_value - user_putts), 2)

def calculate_strokes_gained_putting(reference_data, user_input):
    '''Return the strokes gained value from a dictionary of user input
    {distance, putts} and a list of reference strokes gained data.'''

    strokes_gained = user_input
    # get the reference distance from the first entry in the baseline data
    position = 0
    not_matched = True

    # loop through the reference data to find the right value of average putts
    while not_matched:
        # set up the reference data
        baseline_data = reference_data[position]
        reference_distance = baseline_data['distance']
        reference_putts = baseline_data['putts']
        min_reference_distance = reference_data[0]['distance']
        max_reference_distance = reference_data[-1]['distance']

        # first check that the input is within the putt_range
        if user_input['distance'] < min_reference_distance:
            # use the lowest value of the reference putts
            reference_putts = reference_data[0]['putts']
            not_matched = False
        elif user_input['distance'] > max_reference_distance:
            # use the highest value of the reference putts
            reference_putts = reference_data[-1]['putts']
            not_matched = False
        # if we get an exact match
        elif user_input['distance'] == reference_distance:
            reference_putts = reference_data[position]['putts']
            not_matched = False
        # if the putt distance sits between baseline values
        elif user_input['distance'] < reference_distance and user_input['distance'] > last_distance:
            distance_range = reference_distance - last_distance
            putt_range = reference_putts - last_putts
            proportion = (user_input['distance'] - last_distance)/distance_range

            #update the reference_putts
            reference_putts = round(last_putts + (putt_range * proportion), 2)
            not_matched = False

        # keep track of the last distance if you don't get an exact match
        last_distance = reference_distance
        last_putts = reference_putts
        position += 1

    print(f"Your input of distance of {user_input['distance']} feet equates to a tour averge of {reference_putts} putts")

    gained = calculate_strokes_gained(reference_putts, user_input['putts'])
    strokes_gained['strokes-gained'] = gained

    return strokes_gained
