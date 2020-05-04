from datetime import datetime

def date_fix(date):
    day = date[0:3]
    d = datetime.strptime(date, "%a, %b %d, %Y")
    converted = datetime.strftime(d, "%m%d%Y")
    
    return day, converted
