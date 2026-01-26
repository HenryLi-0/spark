# code for making sure some extrusions are possible
# (ideally) returns to optimal cuts for the longest lengths left



def calculate(length:int, count:int, target:list[int, int]):
    lengths:list[int, list] = [[length, []] for x in range(count)]
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

    return [True, lengths]



# e_count = 4 # number of extrusions
# e_length = 122 # keep units consistent, cm for now

# Z_HEIGHT = 18
# e_target = [ # required lengths, order by LENGTH, COUNT
#     [26, 3],
#     [26, 2],
#     [6, 2],
#     [Z_HEIGHT, 4],
#     [26, 2],
#     [26, 2],
#     [6, 2],
#     [26, 1],
#     [26, 2],
#     [34, 2]
# ]

# results = calculate(e_length, e_count, e_target)
# if results[0]:
#     for i, length in enumerate(results[1], 1):
#         print("extrusion {} (leftover {}): {}".format(i, length[0], length[1]))

r_count = 2
r_length = 100

r_Z_HEIGHT = 35
r_target = [
    [38, 2],
    [25.6, 2],
    [15.1, 2],
    [18, 2]
]

results = calculate(r_length, r_count, r_target)
if results[0]:
    for i, length in enumerate(results[1], 1):
        print("rod {} (leftover {}): {}".format(i, length[0], length[1]))