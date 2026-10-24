# credit_card → Është një variabël që ruan një string.
# for x in credit_card: → Kalon nëpër çdo karakter të string-ut, një nga një.
# x → Merr karakterin aktual.
# print(x) → Printon karakterin në një rresht të ri.

# credit_card = "1234-5678-3443-4343"
#
# for x in credit_card:
#     print(x)
#

#We have two useful keywords as well

for x in range (1,21):
    if x == 13:
        continue #to skip over an iteration ,you can use the continue keyword
    else:
        print(x)

#por nese ky kod do te kishte vetem break ne vend te continue do te shkonte
#deri te 12 dhe do te ndalonte ,