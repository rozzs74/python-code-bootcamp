# Given a time in

# -hour AM/PM format, convert it to military (24-hour) time.

# Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.

# Function Description 



def timeConversion(time):
	time_lists = time.split(":")
	print(f"Time lists {time_lists}")
	time_lists_length = len(time_lists)
	print(f"time lists length {time_lists_length}")
	i = 0
	while time_lists_length > 1:
		print(time_lists[i])
		i = i + 1
		if i == time_lists_length:
			break;
	return 1

a = timeConversion("07:05:35PM")