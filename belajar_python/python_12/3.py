def luas_persegi(sisi):
    luas = sisi * sisi
    return luas

# pemanggilan fungsi
print ("Luas persegi: %d" % luas_persegi(6))


# rumus: sisi x sisi x sisi
def volume_persegi(sisi):
    volume = luas_persegi(sisi) * sisi
    return volume

# pemanggilan fungsi
print ("Volume persegi: %d" % volume_persegi(6))