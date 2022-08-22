t=int(input())
for i in range(0,t):
    date=input().split(" ")
    data=int(date[0])
    month=date[1]
    if month=="Mar":
        if data>=21:
            print("Aries")
        if data<=20:
            print("Pisces")
    if month == "Apr":
        if data >= 21:
            print("Taurus")
        if data <= 20:
            print("Aries")
    if month == "May":
        if data >= 21:
            print("Gemini")
        if data <= 20:
            print("Taurus")
    if month == "Jun":
        if data >= 22:
            print("Cancer")
        if data <= 21:
            print("Gemini")
    if month == "Jul":
        if data >= 23:
            print("Leo")
        if data <= 22:
            print("Cancer")
    if month == "Aug":
        if data >= 23:
            print("Virgo")
        if data <= 22:
            print("Leo")
    if month == "Sep":
        if data >= 22:
            print("Libra")
        if data <= 21:
            print("Virgo")
    if month == "Oct":
        if data >= 23:
            print("Scorpio")
        if data <= 22:
            print("Libra")
    if month == "Nov":
        if data >= 23:
            print("Sagittarius")
        if data <= 22:
            print("Scorpio")
    if month == "Dec":
        if data >= 22:
            print("Capricorn")
        if data <= 21:
            print("Sagittarius")
    if month == "Jan":
        if data >= 21:
            print("Aquarius")
        if data <= 20:
            print("Capricorn")
    if month == "Feb":
        if data >= 20:
            print("Pisces")
        if data <= 19:
            print("Aquarius")
