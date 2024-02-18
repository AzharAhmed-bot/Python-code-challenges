def what_is_the_time(time_in_mirror):
    # Extract hours and minutes from the mirrored time
    hours = 11 - int(time_in_mirror.split(":")[0])
    
    # Handle special cases when hours become negative or zero
    if hours == -1:
        hours = 11
    elif hours == 0:
        hours = 12
    
    # Calculate minutes by subtracting mirrored minutes from 60
    minutes = 60 - int(time_in_mirror.split(":")[1])
    
    # Adjust hours if minutes overflow 60
    if minutes == 60:
        minutes = 0
        hours += 1
    
    # Format hours and minutes to ensure leading zeros
    formatted_hours = str(hours).zfill(2)
    formatted_minutes = str(minutes).zfill(2)
    
    # Return the formatted time
    return f"{formatted_hours}:{formatted_minutes}"


print(what_is_the_time("12:01"))