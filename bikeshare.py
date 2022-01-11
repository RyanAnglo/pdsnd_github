import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities = ['chicago', 'new york city', 'washington']
months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec', 'all']
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello User! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    print('Would you like to see data for Chicago, New York City, or Washington?')
    while True:
        city = input('Selection..: ').lower()
        if city in cities:
            print ('Great, let\'s look at {}!'.format(city.title()))
            break
        else:
            print ('I\'m sorry, please select the state \'Chicago\', \'New York City\' or \'Washington\'')

    print('We will now filter the data by month, day, or not at all!')
    # TO DO: get user input for month (all, january, february, ... , june)
    print('Which month? - please use the first 3 letters of the month in question. Enter \'all\' for no filter')
    while True:
        month = input ('Month: ').lower()
        if month in months:
            print('You selected {}'.format(month.title()))
            break
        else:
            print('Not recognized. Please select a month or \'all\' - use first 3 letters of the month.')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print('Which day? - please use full name of the day in question. Enter \'all\' for no filter')
    while True:
        day = input ('Day: ').lower()
        if day in days:
            print('You selected {}'.format(day.title()))
            break
        else:
            print('Not recognized. Please select a day or \'all\' - use full name of the day, i.e monday')

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

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract fields from the Start Time column to create an field column
    df['month'] =df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour #not sure if i need this line#

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('Most common month - Jan=1...Dec=12:', common_month)

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most common day:',common_day)

    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('Most common start Hour - 24hr clock:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most common start station:',common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most common end station:',common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    common_start_end_station = (df['Start Station'] + ' to ' + df['End Station']).mode()[0]
    print('Most common start-end station combo: ',common_start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time_s :", total_travel_time)
    print("Total travel time_h :", ((total_travel_time/60)/60))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean travel time_s :", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print(user_type_count)

    # TO DO: Display counts of gender

    try:
        gender_count = df['Gender'].value_counts()
        print(gender_count)

    except:
        print('No gender data')


    # TO DO: Display earliest, most recent, and most common year of birth

    try:
        birth_year = df['Birth Year']
        mode_age = df['Birth Year'].mode()[0]
        youngest_age = df['Birth Year'].max()
        oldest_age = df['Birth Year'].min()

        print('Most common Year of Birth: ', mode_age)
        print('Youngest Year of Birth: ', youngest_age)
        print('Oldest Year of Birth: ', oldest_age)

    except:
        print('No age data')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    print(df)
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while True:
        print(df.iloc[start_loc: start_loc+5])
        start_loc += 5
        view_data = input('Do you wish to continue?: ').lower()
        if view_data != 'yes':
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input ('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
