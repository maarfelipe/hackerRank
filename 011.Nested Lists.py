if __name__ == '__main__':
    nameScore = []
    temp = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        temp.append(score)
        nameScore.append([score, name])

    nameScore.sort()
    print(nameScore)
    temp1 = set(temp)
    print(temp1)
    temp2 = list(temp1)
    temp2.sort()
    print(temp2)

    for i in range(len(nameScore)):
        if nameScore[i][0] == temp2[1]:
            print(nameScore[i][1])
