# nested loop = A loop within another loop (outer,inner)
#               outer loop
#               inner loop:

# Një Nested Loop është një cikël for brenda një cikli tjetër for.

# Outer Loop (x) – Cikli i jashtëm, përsëritet 3 herë.
# Inner Loop (y) – Cikli i brendshëm, përsëritet 10 herë për çdo përsëritje

for x in range(3):
    for y in range(0, 10):
        print(y, end=" ")  # end="" bën që Python
    print()  # print poshte empty do te beje qe te printohet ne cdo rrjesht kodi
    # të mos kalojë në rresht të ri pas çdo numri.
    # end="" – Pa hapësirë,end=" " – Me hapësirë,end="-" – Me vizë
# end=", " – Me presje,end="\n" – Rresht i ri


# for x in range(5):
#     for y in range(3):
#         print("*" , end = " ")
#         print()


# Si të ndihmon PyCharm?
# Në PyCharm:
# - Tab – E zhvendos kodin një nivel djathtas.
# - Shift + Tab – E zhvendos një nivel majtas.
# - Ctrl + Alt + L – Riformaton kodin (por nuk e rregullon domosdoshmërisht logjikën).
# - Vijat vertikale të indentation të ndihmojnë të shohësh nivelet e kodit.
