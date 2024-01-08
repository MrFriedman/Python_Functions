# Code to create a calender for any month of any year
# Dylan Friedman
# FRDDYL002
# 10 April 2022
import math

def day_of_week(day, month, year):
    y = int(year)
    if month == 0 or month == 1:
        dweek = (day + ((13*(month+13))/5) + (y-1) + ((y-1)/4) - ((y-1)/100) + ((y-1)/400)) % 7
        return dweek
    else:
        dweek = (day + ((13*(month+1))/5) + y + (y/4) - (y/100) + (y/400)) % 7
        return dweek

def is_leap(year):
    # Your code here
    if (int(year) % 4 == 0) and ((int(year) % 100 != 0) or (int(year) % 400 == 0)):
        return True
    else:
        return False

def month_num(month_name):
    # Your code here
    #mnum = 0
    if month_name.lower()[0:3] == 'jan': 
        mnum = 1
        return mnum
    if month_name.lower()[0:3] == 'feb': 
        mnum = 2
        return mnum
    if month_name.lower()[0:3] == 'mar': 
        mnum = 3
        return mnum
    if month_name.lower()[0:3] == 'apr': 
        mnum = 4
        return mnum
    if month_name.lower()[0:3] == 'may': 
        mnum = 5
        return mnum
    if month_name.lower()[0:3] == 'jun': 
        mnum = 6
        return mnum
    if month_name.lower()[0:3] == 'jul':
        mnum = 7
        return mnum
    if month_name.lower()[0:3] == 'aug': 
        mnum = 8
        return mnum
    if month_name.lower()[0:3] == 'sep': 
        mnum = 9
        return mnum
    if month_name.lower()[0:3] == 'oct': 
        mnum = 10
        return mnum
    if month_name.lower()[0:3] == 'nov': 
        mnum = 11
        return mnum
    if month_name.lower()[0:3] == 'dec': 
        mnum = 12
        return mnum
    
def num_days_in(month_num, year):
    # Your code here
    mnum = month_num
    ndays = 0 
    if is_leap(year):
        if mnum == 1 or mnum == 3 or mnum == 5 or mnum == 7 or mnum == 10 or mnum == 12:
            ndays = 31
            return ndays
           
        elif mnum == 2:
            ndays = 29
            return ndays
        elif mnum == 2 or mnum == 4 or mnum == 6 or mnum == 8 or mnum == 9 or mnum == 11:
            ndays = 30
            return ndays
    else:
        if mnum == 1 or mnum == 3 or mnum == 5 or mnum == 7 or mnum == 10 or mnum == 12:
            ndays = 31
            return ndays
        elif mnum == 2:
            ndays = 28
            return ndays
        elif mnum == 2 or mnum == 4 or mnum == 6 or mnum == 8 or mnum == 9 or mnum == 11:
            ndays = 30
            return ndays


def num_weeks(month_num, year):
    # Your code here
    mnum = month_num
    ndays = num_days_in(month_num, year)
   # print('d: ', ndays)
    fst = day_of_week(1, mnum, year)
   # print('f: ', math.floor(fst))
    lst = day_of_week(ndays, month_num, year) 
   # print('l: ', math.floor(lst))
    daysrem = ndays - (8-math.floor(fst))-math.floor(lst)
  #  print('drem: ', math.floor(daysrem))
    numweeks = int(math.floor(daysrem) / 7) +2
  #  print('nweeks: ', math.floor(numweeks))
    return numweeks


def week(week_num, start_day, days_in_month):
    # Your code here
    start = ((week_num-1) * 7) + start_day
    monday_val = (start - (start_day - 1)) - (start_day - 1)
    days_in_week = ""
    for i in range(7):
        day = monday_val + i
        if (day >= 1) and (day <= days_in_month):
            if day < 10:
                day = " " + str(math.floor(day))
            else:
                day = str(math.floor(day))
            days_in_week = days_in_week + day + " "
        else:
            days_in_week = days_in_week + "  "
    return days_in_week
      

def main():
    # Your code here
    month = input('Enter month:\n')
    year = input('Enter year:\n')
    start = day_of_week(1, month_num(month), year)
    is_leap(year)
    mnum = month_num(month)
    ndays = num_days_in(mnum, year)
    numweeks = num_weeks(mnum, year)
    print(month)
    print('Mo Tu We Th Fr Sa Su')
    for i in range(1, numweeks+1):
        if i>4:
            print("{0:}".format(week(i, start, num_days_in(month_num(month), year))))
        else:
            print("{0:>20}".format(week(i, start, num_days_in(month_num(month), year))))
    
if __name__=='__main__':
    main()






