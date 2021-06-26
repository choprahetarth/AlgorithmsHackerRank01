thisPoint = [[1116, 525], [578, 348], [142, 643], [618, 88], [1006, 58], [519, 188], [573, 203], [1234, 159], [164, 253], [684, 34], [236, 182], [1122, 115], [494, 675], [774, 22]]
for h in range(len(thisPoint)):
    distance = ((((thisPoint[0][0]-thisPoint[h][0])**2)+(((thisPoint[0][1]-thisPoint[h][1])**2)))**(1/2))
    print(distance)


