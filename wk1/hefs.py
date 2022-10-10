def win(name):
    pl = open("players.txt", "a+")
    pl.seek(0, 0)
    for line in pl:
        pl_name = line.split()[0]
        if pl_name == name:
            newfile = open("new.txt", "w")
            for l in pl:
                pl_name = l.split()[0]
                if pl_name != name:
                    newfile.write(l)
                else:
                    newl = pl_name + " " + str(int(l.split()[0]) + 1)
