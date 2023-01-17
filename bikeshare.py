import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    while True:
        city = str(input("\nCity to filter by: Chicago, New York City, or Washington?\n")).lower()
        if city not in ( 'chicago', 'new york city', 'washington'):
            print("Please enter a valid city name")
            continue
        else:
            break


    # TO DO: get user input for month (all, january, february, ... , june)
    
    while True:
        month = str(input("\nMonth to filter by: January, February, March, April, May, June or type 'all' if you don't like to filter by month.\n")).title()
        if month not in ('January', 'February', 'March', 'April', 'May', 'June', 'All'):
            print("Please enter a valid month")
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    while True:
        day = str(input("\nDay to filter by: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or type 'all' if you don't like to filter by day.\n")).title()
        if day not in ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'All'):
            print("Please enter a valid day")
            continue
        else:
            break


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
        
     # convert the Start Time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
        
     # create new columns for month and day
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    
    # filter by month
    
    if month != 'All':
        valid_months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = valid_months.index(month) + 1
        df = df[df['month'] == month]

    # filter by day
    if day != 'All':
        df = df[df['day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    MC_month = df['month'].mode()[0]
    print('Most Common Month:', MC_month)



    # TO DO: display the most common day of week
    MC_day = df['day'].mode()[0]
    print('Most Common day of week:', MC_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    MC_hour = df['hour'].mode()[0]
    print('Most Common Hour of day:', MC_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    StartStation = df['Start Station'].value_counts().idxmax()
    print('Most Common start station:', StartStation)

    # TO DO: display most commonly used end station
    EndStation = df['End Station'].value_counts().idxmax()
    print('\nMost Common end station:', EndStation)


    # TO DO: display most frequent combination of start station and end station trip
    combination = df['Start Station'] + ' to ' + df['End Station']
    most_common_combination = combination.mode()[0]
    print('Most common trip from start to end is:', most_common_combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_mins, total_secs = divmod(df['Trip Duration'].sum(), 60)
    total_hrs, total_mins = divmod(total_mins, 60)
    print ('The total travel time is: ',total_hrs,' hrs, ', total_mins,' mins, and ', total_secs,' secs.')
    total_time = sum(df['Trip Duration'])
    print('The total travel time in Days:', total_time/86400, ' Days.')


    # TO DO: display mean travel time
    mean_mins, mean_secs = divmod(df['Trip Duration'].mean(), 60)
    mean_hrs, mean_mins = divmod(mean_mins, 60)
    print ('The mean travel time is: ',mean_hrs,' hrs, ', mean_mins,' mins, and ', mean_secs,' secs.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_count = df['User Type'].value_counts()
    print('Counts of each user type:\n', user_types_count)

    # TO DO: Display counts of gender
    try:
      gender_types_count = df['Gender'].value_counts()
      print('\nCounts of each gender:\n', gender_types_count)
    except KeyError:
      print("\nCounts of each gender: No available data for this month.")


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
      EarliestYear = df['Birth Year'].min()
      print('\nEarliest Year:', EarliestYear)
    except KeyError:
      print("\nEarliest Year: No available data for this month.")
    
    try:
      MostRecentYear = df['Birth Year'].max()
      print('\nMost Recent Year:', MostRecentYear)
    except KeyError:
      print("\nMost Recent Year: No available data for this month.")

    try:
      MC_Year = df['Birth Year'].value_counts().idxmax()
      print('\nMost Common Year:', MC_Year)
    except KeyError:
      print("\nMost Common Year: No available data for this month.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def Raw_data(df):
    i=0
    choice=str(input('\nDo you want to see the raw data? Enter yes or no.\n')).lower()
    while choice=='yes':
        try:
            number_of_rows=int(input('Enter the number of rows to view\n'))
            number_of_rows=i+number_of_rows
            print(df[i:number_of_rows])
            choice=str(input('Do you want more rows to be viewed? Enter yes or no.\n')).lower()
            i=number_of_rows

        except ValueError:
            print('Invalid integer value.')

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        Raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
