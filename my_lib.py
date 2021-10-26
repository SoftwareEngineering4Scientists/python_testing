
def list_avg(vals):
    if vals == None:
        return None
    if vals == []:
        return None
    if not isinstance(vals, list):
        raise TypeError("Not the correct data type input")
    
    total = 0.0
    
    for val in vals:
        total += val
    
    avg = total/len(vals)
    return avg