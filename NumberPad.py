Number = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
    ("*", 0, "#"),
)

#or 

# Number = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     ["*", 0, "#"],
# ]

for num in Number:
    for i in num:
        print(i, end=" ")
    print()
