
# indexing = accessing elements of a sequence using [] (indexing operator;
# [start : end : step]

credit_number = "1234-5678-9012"

last_digits = (credit_number[10:])
#but better would be like this  last_digits = (credit_number[-4:])

print(f"XXXX-XXXX-XXXX-{last_digits}")

# To reverse a String we have to use this

# step = -1 → Move backward one character at a time. because
#[::1]	Move forward by 1

print (credit_number[::-1])