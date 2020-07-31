with open("fighter-links.txt", "r") as a_file:
    lol = [(line.strip()).split() for line in a_file]
    a_file.close()

lawl = ' '.join(str, lol)

with open("fighter-links-parsed2.txt", "a") as b_file:
    b_file.write(str(lawl).strip)
    b_file.close()