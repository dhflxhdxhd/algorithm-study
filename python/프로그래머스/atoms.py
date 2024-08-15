
mask = 0
day = 0

for i in range(len(atoms))
    if atoms[i][0] >= 81 or atoms[i][1] >= 36:
        if day == 0:
            mask += 1
        else:
            day += 1

        if atoms[i][0] >= 151 and atoms[i][1] >= 76:
            day = 0

    if day == 2:
        day = 0

atoms = [[80, 35], [70, 38], [100, 41], [75,30], [160,80], [77, 29], [181, 68], [151, 76]]	