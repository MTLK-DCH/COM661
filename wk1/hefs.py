def win(name):
    pl = open("players.txt", "a+")
    pl.seek(0, 0)
    for line in pl:
        pl_name = line.split()[0]
        if pl_name == name:
            pl.seek
