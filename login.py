import os
import csv
from settings import username,account_id

def login_func():
	os.system('echo -n > shellOut.txt')
	os.system('face_recognition face_recognition/known/ face_recognition/unknown/  > shellOut.txt')

	curr_path = os.path.dirname(os.path.realpath(__file__))
	file=open("shellOut.txt","r")
	lines=file.readlines()
	file.close()
	names=[]
	possible_user=[]

	for line in lines:
		names.append(line[line.index(",")+1:line.index('\n')])
	with open("data/credentials.csv",'r') as file:
		reader = csv.reader(file, delimiter= ',')
		for row in reader:
			if(row[0] in names):
				possible_user.append(row)
	if(len(possible_user)==0):
		print ("User not found")
		op=raw_input("Try again? Y/N")
		if(op=="Y" or op=="y"):
			return (-1,-1)
		else:
			exit()
	else:
		u=raw_input("Enter username : ")
		p=raw_input("Enter password : ")
		confirmed_user=[]
		for user in possible_user:
			if(user[1]==u and user[2]==p):
				confirmed_user=user
				break
		if(len(confirmed_user)==0):
			print("User not found")
			op=raw_input("Try again? Y/N")
			if(op=="Y" or op=="y"):
				return (-1,-1)
			else:
				exit()
		else:
			return (confirmed_user[1],confirmed_user[3])

def main():
	return