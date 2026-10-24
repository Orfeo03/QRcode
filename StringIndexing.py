# indexing = accessing elements of a sequence using [] (indexing operator;
# [start : end : step]
# start → Pozicioni ku fillojmë.
# end → Pozicioni ku ndalojmë (nuk përfshihet).
# step → Sa pozicione lëvizim çdo herë.

# Indexing përdoret për të aksesuar një karakter të caktuar
# brenda një string-u duke përdorur [].
# Në Python, numërimi i pozicioneve fillon gjithmonë nga 0, dhe llogariten dhe hapesirat.


credit_number = "1234-5678-9012-3456"

# print(credit_number[10])
# print(credit_number[1:5])

#For example if we want dhe digits or the character till the ending we don't need
#to calculate the last index we can just write this command

print (credit_number[4:])

#and if you need the last characters in a String

print (credit_number[-1])

#The step
#here python takes a character ,step to another and continues like this till the end
#for doing that you have to write :: and python step = 2 → Python selects
# every third character in this case , starting at index 0.

print (credit_number[::3])