#Script Name: Time
#Author: Emon Monsur 121367643

#first enter the number of minutes you have spent watching tv
minutes = int(input("Enter minutes watching TV : "))

#save as hours
hour = minutes // 60

#save as the remaining minutes
minutes = minutes % 60

print(minutes)
print(hour)

print("there are", hour, "hours and", minutes, "min(s) watching tv")
