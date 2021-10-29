MAX_PACKAGES = 16
AVG_SPEED_MPH = 18
AVG_SPEED_MPM = AVG_SPEED_MPH / 60

def truncate_to_tenth(num):
		num = int(num * 10)
		return (num / 10.0)

def reverse_array(orig):
	reverse = list()
	while(len(orig) > 0):
		reverse.append(orig.pop())
	return reverse