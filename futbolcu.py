with open("futbolcular.txt","r",encoding="utf-8") as file:
    for x in file:
        if "Fenerbahçe" in x:
            with open("fb.txt","a",encoding="utf-8") as file2:
                file2.write(x.replace(",Fenerbahçe","Galatasaray"))
        elif "Galatasaray" in x:
            with open("gs.txt","a",encoding="utf-8") as file3:
                file3.write(x.replace(",Galatasaray","Fenerbahce"))
        else:
            with open("bjk.txt","a",encoding="utf-8") as file4:
                file4.write(x.replace(",Beşiktaş","Fenerbahçe"))
