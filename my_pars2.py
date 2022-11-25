file_out = open("patronymic.txt", "w", encoding="utf-8")
with open("123.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.replace(", ", "\n")
        line = line.replace(" и ", "\n")
        file_out.write(line[line.find("(") + 1:line.find(")")] + "\n")
file_out.close()
