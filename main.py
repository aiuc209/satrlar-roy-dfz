def satr_unicode_jami(satrlar):
    jami = 0
    for satr in satrlar:
        for harf in satr:
            jami += ord(harf)
    return jami

satrlar = ["Assalomu alaykum", "Xayr", "Dunyo"]
print(satr_unicode_jami(satrlar))
