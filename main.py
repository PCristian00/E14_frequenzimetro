def contatore(stringa):
    mappa = {}
    for c in stringa:
        c = c.lower()
        if c in mappa:
            mappa[c] += 1
        else:
            mappa[c] = 1
    return mappa


print(contatore(input("Inserire testo: ")))
