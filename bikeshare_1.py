import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
days = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday','all']


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
    city = str(input("Please enter the city name: \n(Chicago or New york city or Washington)")).lower()
    while city not in CITY_DATA.keys():
        print("Invalid Input.")
        city = str(input("Please enter the city name: (chicago or new york city or washington)")).lower()

    month = str(input("To filter by month please enter the month name \n(January, February, March, "
                      "April, May, June)\nor all for not filtering by month: ")).lower()
    while month not in months:
        print("Invalid Input.")
        month = str(input("To filter by month please enter the month name \n(January, February, March, "
                          "April, May, June)\nor all for not filtering by month: ")).lower()

    day = str(input("To filter by day please enter the day name \n(Saturday, Sunday, Monday,"
                    " Tuesday, Wednesday, Thursday, Friday)\nor all for not filtering by day: ")).lower()
    while day not in days:
        print("Invalid Input.")
        day = str(input("To filter by day please enter the day name \n(Saturday, Sunday, Monday,"
                        " Tuesday, Wednesday, Thursday, Friday)\nor all for not filtering by day: ")).lower()


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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'].str.startswith(day.title())]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()
    print("The most common month is: {}".format(common_month))

    # display the most common day of week
    common_day = df['day_of_week'].mode()
    print("The most common day is: {}".format(common_day))
    # display the most common start hour
    common_hour = df['hour'].mode()
    print("The most common start hour is: {}".format(common_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start = df["Start Station"].mode()
    print("The most common start station is: {}".format(common_start))

    # display most commonly used end station
    common_end = df["End Station"].mode()
    print("The most common end station is: {}".format(common_end))

    # display most frequent combination of start station and end station trip
    frequent_start_and_end_trip = (df["Start Station"] + " , " + df["End Station"]).mode()[0]
    print("The most frequent start & end station trip is: {}".format(frequent_start_and_end_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    travel_time = df["Trip Duration"].sum()
    print("Total travel time: {}".format(travel_time))

    # display mean travel time
    traveltime_mean = df["Trip Duration"].mean()
    print(" The mean of travel time is: {}".format(traveltime_mean))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The counts of user types are: {}".format(user_types))

    # Display counts of gender
    if "Gender" in df.columns:
        gender = df['Gender'].value_counts()
        print("The counts of gender are: {}".format(gender))
    else:
        print("Unavailable")

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birth = df["Birth Year"].min()
        print("The earliest year of birth is: {}".format(earliest_birth))
        recent_birth = df['Birth Year'].max()
        print("The recent year of birth is: {}".format(recent_birth))
        common_birth = df['Birth Year'].mode()
        print("The common year of birth is: {}".format(common_birth))
    else:
        print("Unavailable")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    index = 0
    user_input = input('would you like to display 5 rows of raw data? (Yes/No)').lower()
    while user_input in ['yes'] and index + 5 < df.shape[0]:
        print(df.iloc[index:index + 5])
        index += 5
        user_input = input('would you like to display more 5 rows of raw data? ').lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
