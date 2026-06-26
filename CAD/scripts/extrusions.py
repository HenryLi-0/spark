# code for making sure some extrusions are possible
# (ideally) returns to optimal cuts for the longest lengths left

# USING DIFFERENT SIZED LENGTHS IS NOT RELIABLE! IT DOESN'T ALWAYS WORK!

def calculate(lengthCounts:list[list[int, int]], target:list[list[int, int]]):
    lengths:list[int, list] = [item for sublist in [[[length, []] for x in range(count)] for length, count in lengthCounts] for item in sublist]
    desiredCuts = []
    for pair in target:
        desiredCuts.extend([pair[0] for x in range(pair[1])])
    print("to cut: {}\n".format(desiredCuts))
    desiredCuts = sorted(desiredCuts, reverse=True)

    for cut in desiredCuts:
        best = None
        smallest = None

        for i, length in enumerate(lengths):
            if length[0] >= cut:
                remaning = length[0] - cut
                if smallest == None or remaning < smallest:
                    smallest = remaning
                    best = i
        
        if best is None:
            print("not possible")
            return [False, []]
        
        lengths[best][1].append(cut)
        lengths[best][0] -= cut

    for group in lengths:
        group[0] = round(group[0]*1000)/1000

    return [True, lengths]


# '''ALUMINUM EXTRUSION'''

# e_count = 4 # number of extrusions
# e_length = 122 # keep units consistent, cm for now

# e_target = [ # required lengths, order by LENGTH, COUNT
#     [26, 3],
#     [26, 2],
#     [6, 2],
#     [18, 6],
#     [26, 2],
#     [26, 2],
#     [6, 2],
#     [26, 2],
#     [34, 2]
# ]

# results = calculate([[e_length, e_count]], e_target)
# if results[0]:
#     for i, length in enumerate(results[1], 1):
#         print("extrusion {} (leftover {}): {}".format(i, length[0], length[1]))



'''LINEAR RODS'''

r_supply = [
    [60, 2],
    [40, 2]
]

r_target = [
    [38, 2],
    [25.6, 2],
    [14.25, 2],
    [18, 2]
]

results = calculate(r_supply, r_target)
if results[0]:
    for i, length in enumerate(results[1], 1):
        print("rod {} (leftover {}): {}".format(i, length[0], length[1]))



# supply_options = [
#     {"length": 15, "c": 2, "price": 14.99},
#     {"length": 20, "c": 2, "price": 12.99},
#     {"length": 25, "c": 2, "price": 15.99},
#     {"length": 35, "c": 2, "price": 13.99},
#     {"length": 40, "c": 2, "price": 16.99},
#     {"length": 60, "c": 2, "price": 21.99},
#     {"length": 15, "c": 1, "price": 6.99},
#     {"length": 25, "c": 1, "price": 7.99},
# ]