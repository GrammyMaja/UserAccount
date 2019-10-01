users = {} # dictionary to store user data

class Usser(object):

	def __init__(self, name, key):
		self.name = name
		self.key = key
		self.friends = []
		self.is_online = False

	def login(self):
		# getting user info
		my_username = input("Enter username: ")
		my_password = input("Enter password: ")

		# validating user credentials
		self.validate(my_username, my_password)

	def  validate(self, user, passs):
		if user==self.name and passs == self.key:
			print("Welcome "+user)
			self.is_online = True
		else:
			print("Invalid username or password")



	def view_friends(self):
		for friend in friends:
			print(friend)


def register_users():
	this_username = input("Enter username: ")
	this_password = input("Enter password: ") 

	this_user = Usser(this_username,this_password)

	# record this usere to the user dictionar
	users[this_username] = this_user
	print(f"{this_user.name} Welcome to DevC Book...")
options = """
1. Register
2. Login
3. View Friends
4. see all users.....
5. Exit

"""
import os # Dont copy
# Main loop
while True:
	command   = input(f"{options}Select an option: ")
	os.system('cls') # Dont copy

	if command is '5':
		print("Goodbye")
		break
	elif command is '1':
		register_users()
	elif command is '2':
		name = input('username')
		users[name].login()

	elif command is '4':
		for user in users: print(user) 
	else:
		print("Invalid option!")
