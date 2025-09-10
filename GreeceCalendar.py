

year = input("digite o ano: ")
year = int(year)

def isLeap(year):
    if year % 4 == 0 and year % 400 == 0:
        return True
    
    return False

print(isLeap(year))