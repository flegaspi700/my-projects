print(10>1)
print(10<1)
print(10==1)
print(10!=1)
print(10>=1)
print(10<=1)
print(10 is 1)
print(10 is not 1)

print("cat" == "Cat")

print(1>2 and 2>3)
print(1>2 or 2>3)
print(not 1>2)

# if elif else
def hint_username(username):
    if len(username) < 3:
        return "Username must be 3 characters or more"
    elif len(username) > 20:
        return "Username must be 20 characters or less"
    else:
        return "Username is valid"

print(hint_username("pe"))

#
def is_even(number):
    if number % 2 == 0:
        return True
    return False

print(is_even(3))

#Calculate block size
def calculate_block_size(file_size):
    block_size = 4096
    full_blocks = file_size // block_size
    remaining_bytes = block_size % file_size

    if remaining_bytes > 0:
        return remaining_bytes * 2
    else:
        return block_size
    
print(calculate_block_size(1))    # Should be 4096
print(calculate_block_size(4096)) # Should be 4096
print(calculate_block_size(4097)) # Should be 8192
print(calculate_block_size(6000)) # Should be 8192

