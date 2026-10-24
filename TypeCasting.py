

# Typecasting = the process of converting a variable from one data type to another
#           str(),int(),float().bool()

name = "Miguel"
age = 25
gpa = 3.2
is_student = True

type(name)

#With this we can show what type is the variable

#print(type(name))
#print(type(age))

#Now if we want to convert something

#We reassign the gpa and convert to integer

gpa =int(gpa)
print(gpa)


#We ressign the age and convert to float
age=float(age)
print(age)



age = str(age)

print(type(age))


#We will take our name variable and typecast to booleon
#We can check this for example so if someone write his name or not cause if it leave it with "" this will be false

name = bool(name)

print (name)