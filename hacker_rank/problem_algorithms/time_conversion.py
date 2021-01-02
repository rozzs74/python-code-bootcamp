# Given a time in

# -hour AM/PM format, convert it to military (24-hour) time.

# Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.

# Function Description 



def timeConversion(time):
	time_lists = time.split(":")
	time_lists_length = len(time_lists)
	i = 0
	isPM = False
	isAM = False
	military_time = {"0": None, "1": None, "2": None}
	while time_lists_length > 1:
		element = time_lists[i]
		if "PM" in element:
			isPM = True
			military_time["2"] = element[0:2]
			if military_time["0"] != "12":
				military_time["0"] = int(military_time["0"]) + 12
			else:
				military_time["0"] = "12"				
		elif "AM" in element:
			isAM = True
			military_time["2"] = element[0:2]
			if military_time["0"] == "12":
				military_time["0"] = "00"
		else:
			military_time[str(i)] = element
		i = i + 1
		if i == time_lists_length:
			if isPM == True or isAM == True:
				return f"{military_time['0']}:{military_time['1']}:{military_time['2']}"

a = timeConversion("06:00:00PM")
print(a)