class Player:
    def __init__(self, id, team):
        self.__id = id
        self.__team = team

    def __repr__(self):
        return '{} ({})'.format(self.__id, self.__team)


class Pitcher(Player):

    def __init__(self, id, team, wins, losses, era):
        super().__init__(id, team)
        self.__wins = wins
        self.__losses = losses
        self.__era = era

    def __repr__(self):
        p = super().__repr__()
        q = p + ': {} W, {} L, ERA: {}'.format(self.__wins, self.__losses, self.__era)
        return q

    def __lt__(self, other):
        if self.__era < other.__era:
            return True
        else:
            return False

    def eraSorter(self):
        if self.__wins >= 5:
            return True
        else:
            return False


class Batter(Player):

    def __init__(self, id, team, hits, hrs, battingaverage):
        super().__init__(id, team)
        self.__hits = hits
        self.__hrs = hrs
        self.__battingaverage = battingaverage

    def __repr__(self):
        p = super().__repr__()
        q = p + ': {} hits, {} HRs, Average: {}'.format(self.__hits, self.__hrs, self.__battingaverage)
        return q

    def __lt__(self, other):
        if self.__battingaverage > other.__battingaverage:
            return True
        else:
            return False

    def battingSorter(self):
        if self.__hits >= 5:
            return True
        else:
            return False


def readPitchers():
    all_pitchers = []
    with open('pitchers.txt', 'r') as pit:
        for p in pit:
            data = p.split('\t')
            pObj = Pitcher(data[0], data[1], int(data[2]), int(data[3]), float(data[4]))
            all_pitchers.append(pObj)

    return all_pitchers


def readBatters():
    all_batters = []
    with open('batters.txt', 'r') as bat:
        for b in bat:
            data = b.split('\t')
            bObj = Batter(data[0], data[1], int(data[2]), int(data[3]), float(data[4]))
            all_batters.append(bObj)

    return all_batters


def main():
    newEra = []
    newBatting = []
    era = readPitchers()
    batting = readBatters()

    for i in range(len(era)):
        if era[i].eraSorter():
            newEra.append(era[i])

    for i in range(len(batting)):
        if batting[i].battingSorter():
            newBatting.append(batting[i])

    print('-' * 15, 'pitchers', '-' * 15)

    for i in range(10):
        q = sorted(newEra)
        print(q[i])

    print('-' * 15, 'batters', '-' * 15)

    for j in range(10):
        v = sorted(newBatting)
        print(v[j])


main()
