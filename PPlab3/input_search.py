from re import *
def regexIP(string: str):
    octet1 = '\d'# одна цифра
    octet2 = '[1-9]\d'# двузначное число
    octet3 = '1[\d][\d]|2[0-4][\d]|25[0-5]'# трехзначное число
    octet = f"(?:{octet1}|{octet2}|{octet3})"
    pattern = f"^{octet}\.{octet}\.{octet}\.{octet}$"
    result = findall(pattern, string)
    if result:
        print("ip-адрес корректен")
        return True
    else:
        print("ip-адрес некорректен")
        return False
string = input("Введите ip-адрес ")
regexIP(string)