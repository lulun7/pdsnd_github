import time
import pandas as pd
import numpy as np

cities = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['all','january', 'february', 'march', 'april', 'may', 'june']
days = ['all','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


def get_filters():


    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('\nWould you like to see data for Chicago, New York City, or Washington?\n').lower()
        if city in cities:
            break
        else:
            print('\nInvalid input, please type a valid city name.')

    # get user input for month (january, february, ... , june)
    while True:
        month = input('\nPlease choose a month to filter by: January, February, March, April, May, or June.\nType "All" to apply no month filter.\n').lower()
        if month in months:
            break
        else:
            print('\nInvalid input, please enter a valid month or type "All" to apply no month filter.')

    # get user input for day of week (monday, tuesday, ... sunday)
    while True:
        day = input('\nPlease choose a day to filter by: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday.\nType "All" to apply no day filter.\n').lower()
        if day in days:
            break
        else:
            print('\nInvalid input, please enter a valid day or type "All" to apply no day filter.')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    df = pd.read_csv(cities[city])
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['Month'] = df['Start Time'].dt.month
    df['Day_of_Week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        df = df[df['Month'] == months.index(month)]

    # filter by day of week if applicable
    if day != 'all':
        df = df[df['Day_of_Week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = months[df['Month'].mode()[0]].title()
    print('\nThe most common month: {}'.format(popular_month))

    # display the most common day of week
    popular_weekday = df['Day_of_Week'].mode()[0]
    print('\nThe most common day of week: {}'.format(popular_weekday))

    # display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour
    popular_hour = df['Hour'].mode()[0]
    print('\nThe most common start hour: {}'.format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('\nThe most common start station: {}'.format(common_start_station))
    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('\nThe most common end station: {}'.format(common_end_station))
    # display most frequent combination of start station and end station trip
    df['Trip'] = 'From ' + df['Start Station'] + ' to ' + df['End Station']
    common_trip = df['Trip'].mode()[0]
    print('\nThe most common trip: {}'.format(common_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('\nThe total travel time in seconds: {}'.format(total_travel_time))

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('\nThe mean travel time in seconds: {}'.format(mean_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('\nThe counts of user types:\n{}'.format(user_types))

    if city != 'washington':
        # Display counts of gender
        gender_counts = df['Gender'].value_counts()
        print('\nThe counts of gender:\n{}'.format(gender_counts))
        # Display earliest, most recent, and most common year of birth
        earliest_birth_year = df['Birth Year'].min()
        print('\nThe earliest year of birth: {}'.format(earliest_birth_year))

        recent_birth_year = df['Birth Year'].max()
        print('\nThe most recent year of birth: {}'.format(recent_birth_year))

        common_birth_year =  df['Birth Year'].mode()[0]
        print('\nThe most common year of birth: {}'.format(common_birth_year))

    else:
        print('\nNo gender data to share.')
        print('\nNo birth year data to share.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """Displays the first 5 lines of raw data upon request by the user."""

    # Prompt the user if they want to see 5 lines of raw data
    user_input = input('\nWould you like to see the first 5 rows of raw data?\nPlease type "Yes" or "No".\n').lower()

    # Display data if the answer is 'Yes'
    if user_input == 'yes':
        i = 0
        print('\nBelow is the first 5 rows of raw data:')
        #Continue iterating these prompts and displaying the next 5 lines of raw data at each iteration
        #Stop the program when the user says 'No' or there is no more raw data to display.
        while True:
            print('\n',df.iloc[i:i+5])
            i += 5
            more_data=input('\nDo you want to see the next 5 rows?\nPlease type "Yes" or "No".\n').lower()
            if more_data != 'yes':
                break

    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        raw_data(df)

        restart = input('\nWould you like to restart? Please type "Yes" or "No".\n')
        if restart.lower() != 'yes':
            print('\nHave a nice day!')
            break


if __name__ == "__main__":
	main()
