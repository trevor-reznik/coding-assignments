def get_height_category(gender, height):
    if gender != "male" and gender!= "female":
        return "unknown average"
    else:
        if height <= 70 and gender == "male":
            return "below average"
        elif height <64 and gender == "female":
            return "below average"
    return "above average"
