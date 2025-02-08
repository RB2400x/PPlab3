from re import *
octet1 = '\d'# одна цифра
octet2 = '[1-9]\d'# двузначное число
octet3 = '1[\d][\d]|2[0-4][\d]|25[0-5]'# трехзначное число
octet = f"(?:{octet1}|{octet2}|{octet3})"
pattern = f"\W?{octet}\.{octet}\.{octet}\.{octet}\W?"
with open('sample_file.txt', 'r') as file:
    string = file.read()
    result = findall(pattern, string)
if result:
    print('Найденные ip-адреса:')
    for i in range (len (result)):
        print(result[i])
else:
    print('ip-адресов не найдено')
    print(string)