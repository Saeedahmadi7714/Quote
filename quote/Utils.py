# Write your custom classes and functions here

# Estimating post reading time
def reading_time(content):
    """"
    https://infusion.media/content-marketing/how-to-calculate-reading-time/
    """
    words = content.split()
    words = len(words)
    read_time = words / 200
    spliced_read_time = str(read_time).split('.')

    # If time has decimal places
    if spliced_read_time[1]:

        extra_time = ((int(spliced_read_time[1]) / 1000) * .60) * 100

        # If decimal places numbers smaller than 30 seconds return read_time without change and decimal places
        if extra_time < 30:
            final_time = int(spliced_read_time[0])
            return final_time

        # If decimal places numbers bigger than 30 seconds we add a minute to reading time
        final_time = int(spliced_read_time[0]) + 1
        return final_time

    # If read_time is round without decimal places
    final_time = read_time
