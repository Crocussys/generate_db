import random


def snils():
    n = random.randint(1_001_999, 999_999_999)
    str_n = str(n)
    l = len(str_n)
    if l < 9:
        str_n = "0" * (9 - l) + str_n
    summ = 0
    i = 1
    while n > 0:
        summ += (n % 10) * i
        n //= 10
        i += 1
    summ %= 101
    if summ == 100 or summ == 0:
        str_s = "00"
    elif 0 < summ < 10:
        str_s = "0" + str(summ)
    else:
        str_s = str(summ)
    str_n += str_s
    return str_n


def phone_number():
    s = str(random.randint(0, 999_99_99))
    l = len(s)
    if l < 7:
        s = "0" * (7 - l) + s
    return "+7" + str(random.randint(900, 999)) + s


def adres(array):
    line = random.choice(array)
    line = line[:len(line) - 1]
    line += f" д. {int(random.expovariate(0.1) + 1)}"
    if random.betavariate(1, 3) > 0.5:
        r_num = random.randint(1, 3)
        if r_num == 1:
            line += f"/{int(random.expovariate(0.5) + 1)} "
        elif r_num == 2:
            line += f" корп. {int(random.expovariate(0.5) + 1)}"
        elif r_num == 3:
            ABC = "АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЭЮЯ"
            line += f"{ABC[int(random.expovariate(0.5))]}"
    if random.betavariate(1, 10) > 0.5:
        line += f" стр. {int(random.expovariate(0.5) + 1)}"
    return f"{len(bytes(line, 'utf-8'))} {line}"


def name(n, s, p):
    num = random.randint(0, 316)
    if num < 209:
        line = s[random.randint(1, 571) * 2]
        man = True
    else:
        line = s[random.randint(1, 571) * 2 + 1]
        man = False
    line += n[num]
    if random.betavariate(20, 1) > 0.5:
        if man:
            line += p[random.randint(1, 540) * 2]
        else:
            line += p[random.randint(1, 540) * 2 + 1]
        line = line[:len(line) - 1]
    line = line.replace("\n", " ")
    return f"{len(bytes(line, 'utf-8'))} {line}"


def main():
    adreses = []
    with open("adreses.txt", "r", encoding="utf-8") as f:
        for line in f:
            adreses.append(line)
    names = []
    with open("names.txt", "r", encoding="utf-8") as f:
        for line in f:
            names.append(line)
    surnames = []
    with open("surnames.txt", "r", encoding="utf-8") as f:
        for line in f:
            surnames.append(line)
    patronymics = []
    with open("patronymic.txt", "r", encoding="utf-8") as f:
        for line in f:
            patronymics.append(line)
    count = 10
    file = open("db", "wb")
    file.write(f"{count}\n".encode())
    for i in range(2 ** count):
        file.write(f"1 {snils()}{phone_number()} {adres(adreses)} {name(names, surnames, patronymics)}\n".
                   encode('utf-8'))
    file.close()


if __name__ == "__main__":
    main()
