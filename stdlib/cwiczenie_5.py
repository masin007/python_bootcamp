import re

# regex = re.compile("\d+")
#
# wynik = regex.findall("dsfasdfsadfasetest;lk234jiotestjdlsf")
#
# print(wynik)
regex = re.compile("\d{2}-\d{3}")
regex_data = re.compile("d\{2} [A-Z][a-z]{2} \d{4}")


with open("kody.txt") as file:
    tekst = file.read()

    kody_pocztowe = regex.findall(tekst)
    daty = regex_data.findall(tekst)

print(kody_pocztowe)
print(daty)
