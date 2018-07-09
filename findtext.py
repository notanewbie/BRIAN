from difflib import SequenceMatcher
def scour(find, tlist):
    x = 0
    def ke(z):
        return SequenceMatcher(None, z, find).ratio() * -1
    try:
        while tlist[x]:
            SequenceMatcher(None, tlist[x], find).ratio()
            #print comp[x] + " compared to " + find;
            x = x + 1
    except IndexError:
        tlist.sort(key=ke)
        return tlist
