"""This module can be used to convert the windows filetime values stored in hexadecimal to a stndard datetime format
Usually Microsoft stores the value of filetime in 16 hex number
- example use it to parse windoes BAM values , or windowsfiletimes in outlook emails"""
import datetime
epoch_start = datetime.datetime(1601, 1, 1)
def filetime_to_datetime(hexValue:str)->datetime:
	"""Takes the string of hex stream for thw windows filetime"""
	byte_array=bytes.fromhex(hexValue)
	filetime = int.from_bytes(byte_array, byteorder='little')
	seconds_since_1601 = filetime / 10_000_000
	filetime_date = epoch_start + datetime.timedelta(seconds=seconds_since_1601)
	return filetime_date
