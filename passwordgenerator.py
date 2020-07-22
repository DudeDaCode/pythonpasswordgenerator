import random
import string

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Randomly Generated Password Of Length", length, "Is:", result_str)

length = int(input("Enter Password Length : "))

get_random_string(length)
