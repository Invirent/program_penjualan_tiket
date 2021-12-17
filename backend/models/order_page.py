def check_condition(form_input, json_data):
    flight = []
    for json in json_data:
        if json['flight_type'] == form_input['trip_type'] and json['destination_from'] == form_input['destination_from'] and json['destination_to'] == form_input['destination_to']:
            if json['seat_class'] == form_input['seat_class']:
                if json['departure_date'] == form_input['departure_date']:
                    if form_input['trip_type'] == 'One Way':
                        flight.append(json)
                    elif form_input['trip_type'] == 'Round Trip':
                        if json['return_date'] == form_input['return_date']:
                            flight.append(json)
    
    if len(flight) == 0:
        return False
    else:
        return flight
