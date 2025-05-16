import re
password = input("Enter password to check strength")
def passCom(password):
	score = 0
	if len(password) >= 8:
		score +=1
	if re.search("[a-z]", password):
		score +=1
	if re.search("[A-Z]" , password):
		score += 1
	if re.search("!@#$%^&*", password):
		score += 1

	if score == 5:
		return "strong"
	if score >= 3:
		return "Moderate"
	else:
		return "Weak"
		
strength = passCom(password)
print(f"Your password is {strength}")
	

