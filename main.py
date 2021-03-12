import hotbin as h

a = True

while a:
    i = input("hotbin>")

    if i.split(" ")[0] == "enter":
        if i.split(" ")[1] == "bin":print(h.mkBin(i.split(" ")[2]))
        elif i.split(" ")[1] == "binstatement":print(h.mkBinStatement(i.split(" ")[2], i.split(" ")[3]))
        elif i.split(" ")[1] == "arc":print(h.mkArc(len(i.split(" ")[2])))
        elif i.split(" ")[1] == "code":print(h.mkCode(i.split(" ")[2]))