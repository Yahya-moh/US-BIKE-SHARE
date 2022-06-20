# import moddules which will be used.#
import pandas as pd
import numpy as np
import time
# create a dictionary for cities that analyse its data.#
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
# create a list of days by which data will be filtered.#
day_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday']
# create a list of months by which the filteration will done.#
month_list = ['january', 'february', 'march', 'april', 'may', 'june']
# make a list of cities among them the user will choose.#
city_list = ['chicago', 'new york', 'washington']
# 
def load_data(city,month,day):
    """
    load data for the choosen city and filter it as the user decide.
    arg:
    str(city) : the name of the city that the user choose.
    str(month) or None: name of the month that user choose or None if user is not in need to filter by month.
    str(day) or None : name of the day that user choose or None if user is not in need to filter by day.

    return pandas Dataframe for the choosen city with or without filter as user's plan.
    """
    # load data file of choosen city as pandas Dataframe.
    df =pd.read_csv(CITY_DATA[city])
    # remove column with Nan value .
    df.dropna(axis=0,inplace= True)
    df['Trip'] = df['Start Station']+df['End Station']
    # change column of start time to datetime type.
    df['Start Time']= pd.to_datetime(df['Start Time'])
    # add a column of months name that extracted from start time column.
    df['months']=df['Start Time'].dt.month_name()
    # add a column of days name that extracted from start time column.
    df['days']=df['Start Time'].dt.day_name()
    # add a column of hours as extracted from start time column.
    df['hours']=df['Start Time'].dt.hour
    # change data type birth year column into integer to do statistics(N.B. washington file doesn't have a birth year column).     
    if city!= "washington":
        df['Birth Year']=df['Birth Year'].astype(int)
    # prepare data of choosen city  filtered by choosen month.
    if day == "" and  month != "":
        df= df.loc[df['months'] == month.title()]
        # display data of popular times of travel filtered by month. 
        most_common_day_of_week = df['days'].mode()
        most_common_hour_of_day = df['hours'].mode()
        print("the most common day of week is: {}\n,the most common hour of day is:{}".format(most_common_day_of_week,most_common_hour_of_day))
  #prepare data of choosen city filtered by choosen day. 
  if month == ""and day != "":
    df = df.loc[df['days'] == day.title()]
    # display data of popular times of travel filtered by day.
    most_common_month = df['months'].mode()
    most_common_hour_of_day = df['hours'].mode()
    print("the most common month is: {}\n,the most common hour of day is:{}".format(most_common_month, most_common_hour_of_day))
  #prepare data of choosen city not filtered.
  if month == "" and day == "":
    # display data of popular times of travel not filtered .      
    most_common_month = df['months'].mode()
    most_common_day_of_week = df['days'].mode()
    most_common_hour_of_day = df['hours'].mode()
    print("the most common month is: {}\n,the most common day of week is: {}\n,the most common hour of day is:{}".format(most_common_month, most_common_day_of_week, most_common_hour_of_day))
  #prepare data of choosen city filtered by choosen month an day.        
  if month != "" and day != "":
    df= df.loc[df['months'] == month.title()]
    df= df.loc[df['days'] == day.title()]
    # display data of popular times of travel filtered by month and day.        
    most_common_hour_of_day = df['hours'].mode()
    # verify the user reply to show more data or not.    
    print("the most common hour of day is:{}".format( most_common_hour_of_day))
  inquire =input('Do you want to see the next statistics?(y or n)\n').lower()
  while inquire != "n":
        if inquire != 'y':
            print('This is invalid input',inquire)
        if inquire == "y":
            print("please, wait loading the next statistics","."*40)
            break      
  if inquire == "n": 
     exit()
  # display statistics ofpopular stations and trip.        
  most_common_trip_from_start_to_end = df['Trip'].mode()
  most_common_start_station = df['Start Station'].mode()
  most_common_end_station = df['End Station'].mode()
  print("most common trip from start to end station is: {}\n,most common start station is: {}\n,most common end stationis{}".format(most_common_trip_from_start_to_end,most_common_start_station,most_common_end_station))
  # verify the user reply to show more data or not. 
  inquire =input('Do you want to see the next statistics?(y or n)\n').lower()
  while inquire != "n":
        if inquire != 'y':
            print('This is invalid input',inquire)
        if inquire == "y":
            print("please, wait loading the next statistics","."*40)
            break      
  if inquire == "n": 
     exit()
  # display statistics of trip duration.        
  total_trip_duration = df['Trip Duration'].count()
  average_trip_duration = df['Trip Duration'].mean()      
  print("total trip duration is: {}\n,average trip duration is: {}\n".format(total_trip_duration,average_trip_duration))
  # verify the user reply to show more data or not.     
  inquire =input('Do you want to see the next statistics?(y or n)\n').lower()
  while inquire != "n":
    if inquire != 'y':
        print('This is invalid input',inquire)
    if inquire == "y":
        print("please, wait loading the next statistics","."*40)
        break      
  if inquire == "n": 
     exit()
  #display statistics of user type only for washington if it is choose of user.        
  while city =='washington':
    counts_of_each_user_type = df['User Type'].value_counts()
    print("the counts of each user type are: {}\n".format(  counts_of_each_user_type))
    break
  # display statistics of user type,birth year and gender only for chicago and new york.   
  if city in ['chicago', 'new york']:
    counts_of_each_user_type = df['User Type'].value_counts()
    counts_of_each_gender = df['Gender'].value_counts()
    earliest_year_of_birth = df['Birth Year'].max()
    most_common_year_of_birth = df['Birth Year'].mode()
    most_recent_year_of_birth = df['Birth Year'].min()
    print("counts of each user type are: {}\n,counts of each gender are: {}\n,earliest year of birth is: {}\n, most recent year of  birth is: {}\n,most recent year of birth is: {}".format(counts_of_each_user_type,counts_of_each_gender,earliest_year_of_birth,most_recent_year_of_birth,most_common_year_of_birth))
"""
create a function to collect the user inputs and verify it.
ask user to choose city from city_list.
ask user to choose filter or not, and type that filter by day or month or both.
at the end you have (city,month,day)_function.
"""
def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    city = input("Would you like to see data for Chicago, New York, or Washington?\n").lower()
    while city not in city_list:
        invalid_statment = input('this is invalid input.Do you want to restart?(y or n)\n').lower()
        if invalid_statment == "y":
            city= input("Would you like to see data for Chicago, New York, or Washington?\n").lower()
        if invalid_statment == "n":
           exit()
    filter_selection = input("Would you like to filter the data by month, day, both or not at all?\n").lower()
    while filter_selection not in ['month', 'day', 'both', 'not at all']:
        invalid_statment = input('this is invalid input.Do you want to restart?(y or n)\n').lower()
        if invalid_statment == "y":
            filter_selection = input("Would you like to filter the data by month, day, both or not at all?\n").lower()
        if invalid_statment == "n":
            exit()
    if filter_selection in ['month', 'day', 'both', 'not at all']:
        while filter_selection == "both":
            month = input ("Which month - January, February, March, April, May, or June?\n").lower()
            if month in month_list:
               day = input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n").lower()
               while day not in day_list:
                    invalid_statment = input('this is invalid input.Do you want to restart?(y or n)\n').lower()
                    if invalid_statment == "y":
                        day = input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n").lower()
                    if invalid_statment == "n":
                        exit()
               print("please,wait loading data","."*40)
               load_data(city,month,day)
               break 
            while month not in month_list:
                invalid_statment = input('this is invalid input.Do you want to restart?(y or n)\n').lower()
                if invalid_statment == "y":
                    month = input ("Which month - January, February, March, April, May, or June?\n").lower()
                    if month in month_list:
                         day = input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n").lower()
                         while day not in day_list:
                            invalid_statment = input('this is invalid input.Do you want to restart?(y or n)\n').lower()
                            if invalid_statment == "y":
                                day = input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday\n").lower()
                            if invalid_statment == "n":
                                 exit()   
                         print("please,wait loading data","."*40)
                         load_data(city,month,day)
                if invalid_statment == "n":
                     exit()                      
                                
        if filter_selection == 'day':
            day = input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n").lower()
            while day not in day_list:
                invalid_statment = input('this is invalid input.Do you want to restart?(y or n)\n').lower()
                if invalid_statment == "y":
                    day = input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n").lower()
                if invalid_statment =="n":
                    break
            print("please,wait loading data","."*40)
            month = ""
            load_data(city,month,day)
        if filter_selection == 'month':
            month = input ("Which month - January, February, March, April, May, or June?\n").lower()
            while month not in month_list:
                invalid_statment = input('this is invalid input.Do you want to restart?(y or n)\n').lower()
                if invalid_statment == "y":
                    month = input ("Which month - January, February, March, April, May, or June?\n").lower()
                if invalid_statment == "n":
                    break
            day = ""
            print("please,wait loading data","."*40)
            load_data(city,month,day)
        if filter_selection == 'not at all':
            month = ""
            day = ""
            print("please,wait loading data","."*40)
            load_data(city,month,day)
    return
# this main function to start and obtain get_filters() function.
def main():
    while True:
     get_filters()
     restart = input("\nWould you like to restart? Enter y or n. \n")
     if restart.lower() != "y":
        break
# this the start call for main function.
main()
    

    