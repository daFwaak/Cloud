# Function to greet the user
def greet_user(name):
    print(f"Hello, {name}! Welcome to the world of Python.")

# Main program execution
if __name__ == "__main__":
    # Prompt the user for their name
    user_name = input("Please enter your name: ")
    
    # Call the greet_user function with the user's name
    greet_user(user_name)
