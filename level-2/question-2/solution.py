def solution(xs):
    # Filter positive and negative outputs into arrays
    negative_outputs = [number for number in xs if number < 0]
    positive_outputs = [number for number in xs if number > 0]

    """
        If there are negative outputs, add them to the
        positive output list to be multiplied together

        If theres an odd number of negative outputs, sort the
        list in descending to obtain the highest magnitude order,
        and remove the smallest value prior to concatenation of positive and negative lists
    """
    negative_output_length = len(negative_outputs)
    if negative_output_length:
        if negative_output_length % 2 != 0:
            _negatives = [x for x in negative_outputs]
            _negatives.remove(max(negative_outputs))
        positive_outputs += _negatives

    if len(positive_outputs):
        return str(reduce(lambda x, y: x * y, positive_outputs)) if len(positive_outputs) else "0"
    elif 0 in xs:
        return "0"
    else:
        return str(negative_outputs[0])