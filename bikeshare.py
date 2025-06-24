import time
import pandas as pd
import numpy as np

# Dictionary to map city names to CSV filenames
CITY_DATA = { 
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv' 
}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "none" for no month filter
        (int) day - integer 1-7 for day of the week (1=Sunday), or 0 for no filter
    """
    print("Hello! Let's explore some US bikeshare data!")

    # Get user input for the city with validation
    city = ""
    while city not in CITY_DATA:
        city = input("Please enter a city (Chicago, New York City, Washington): ").strip().lower()
        if city not in CITY_DATA:
            print("That’s not a valid city. Try again.")

    # Ask the user how they want to filter data: by month, day, both, or none
    filter_type = ""
    while filter_type not in ['month', 'day', 'both', 'none']:
        filter_type = input("Would you like to filter by month, day, both, or none? ").strip().lower()

    # Set default values for month and day
    month = 'none'
    if filter_type in ['month', 'both']:
        valid_months = ['January', 'February', 'March', 'April', 'May', 'June']
        while True:
            month_input = input("Which month? (January to June): ").strip().title()
            if month_input in valid_months:
                month = month_input
                break
            print("Invalid month. Please try again.")

    # Ask the user for the day if necessary
    day = 0
    if filter_type in ['day', 'both']:
        while True:
            try:
                day_input = int(input("Enter a day as an integer (1=Sunday, 7=Saturday): "))
                if 1 <= day_input <= 7:
                    day = day_input
                    break
                print("Day must be between 1 and 7.")
            except ValueError:
                print("That’s not a number. Try again.")

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    
    Args:
        city (str): City name to filter the data.
        month (str): Month to filter by, or "none" for no month filter.
        day (int): Day of the week to filter by (1-7), or 0 for no filter.

    Returns:
        pd.DataFrame: The filtered DataFrame based on user input.
    """
    # Load data for the city
    df = pd.read_csv(CITY_DATA[city])

    # Convert Start Time and End Time columns to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # Extract month, day of the week, and hour from Start Time
    df['Month'] = df['Start Time'].dt.month
    df['Day Name'] = df['Start Time'].dt.day_name()
    df['Hour'] = df['Start Time'].dt.hour

    # Filter by month if applicable
    if month != 'none':
        month_lookup = {'January': 1, 'February': 2, 'March': 3,
                        'April': 4, 'May': 5, 'June': 6}
        df = df[df['Month'] == month_lookup[month]]

    # Filter by day if applicable
    if day != 0:
        day_name = ['Sunday', 'Monday', 'Tuesday', 'Wednesday',
                    'Thursday', 'Friday', 'Saturday'][day - 1]
        df = df[df['Day Name'] == day_name]
    print(f"\nData loaded successfully for {city.title()} with {len(df)} records after filtering.\n")

    return df

def time_stats(df):
    """
    Displays statistics on the most frequent times of travel.
    
    Args:
        df (pd.DataFrame): DataFrame containing bikeshare data.
    """
    print("\nCalculating The Most Frequent Times of Travel...\n")
    start = time.time()

    # Most frequent month, day of week, and start hour
    print("Most Common Month:", df['Month'].value_counts().idxmax())
    print("Most Common Day of Week:", df['Day Name'].value_counts().idxmax())
    print("Most Common Start Hour:", df['Hour'].value_counts().idxmax())

    print("\nThis took %.2f seconds." % (time.time() - start))
    print('-'*40)

def station_stats(df):
    """
    Displays statistics on the most popular stations and trip.
    
    Args:
        df (pd.DataFrame): DataFrame containing bikeshare data.
    """
    print("\nCalculating The Most Popular Stations and Trip...\n")
    start = time.time()

    # Most common start and end stations
    start_station = df['Start Station'].mode()[0]
    end_station = df['End Station'].mode()[0]

    # Most frequent combination of start and end station
    df['Trip'] = df['Start Station'] + " to " + df['End Station']
    popular_trip = df['Trip'].mode()[0]

    print("Most Common Start Station:", start_station)
    print("Most Common End Station:", end_station)
    print("Most Frequent Trip:", popular_trip)

    print("\nThis took %.2f seconds." % (time.time() - start))
    print('-'*40)

def trip_duration_stats(df):
    """
    Displays statistics on the total and average trip duration.
    
    Args:
        df (pd.DataFrame): DataFrame containing bikeshare data.
    """
    print("\nCalculating Trip Duration...\n")
    start = time.time()

    # Calculate total and average trip durations
    total_duration = df['Trip Duration'].sum()
    avg_duration = df['Trip Duration'].mean()

    print("Total Duration:", total_duration)
    print("Average Duration:", avg_duration)

    print("\nThis took %.2f seconds." % (time.time() - start))
    print('-'*40)

def user_stats(df, city):
    """
    Displays statistics on bikeshare users.
    
    Args:
        df (pd.DataFrame): DataFrame containing bikeshare data.
        city (str): The city being analyzed.
    """
    print("\nCalculating User Stats...\n")
    start = time.time()

    # Counts of user types
    print("User Types:\n", df['User Type'].value_counts())

    # Gender and Birth Year statistics (if available for the city)
    if city in ['chicago', 'new york city']:
        if 'Gender' in df.columns:
            print("\nGender Distribution:\n", df['Gender'].value_counts())
        if 'Birth Year' in df.columns:
            print("\nEarliest Birth Year:", int(df['Birth Year'].min()))
            print("Most Recent Birth Year:", int(df['Birth Year'].max()))
            print("Most Common Birth Year:", int(df['Birth Year'].mode()[0]))

    print("\nThis took %.2f seconds." % (time.time() - start))
    print('-'*40)

def display_raw_data(df):
    """
    Displays 5 lines of raw data at a time upon user request.

    Args:
        df (pd.DataFrame): DataFrame containing bikeshare data.
    """
    while True:
        show_data = input("Would you like to see raw data? Enter yes or no: ").strip().lower()
        if show_data not in ['yes', 'no']:
            print("Please enter 'yes' or 'no'.")
            continue
        break

    i = 0
    while show_data == 'yes':
        print(df.iloc[i:i+5])
        i += 5
        if i >= len(df):
            print("No more data to display.")
            break
        while True:
            show_data = input("Would you like to see 5 more lines of data? Enter yes or no: ").strip().lower()
            if show_data not in ['yes', 'no']:
                print("Please enter 'yes' or 'no'.")
            else:
                break

def main():
    """Main function that runs the bikeshare analysis."""
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        
        # Ask user if they want to see the raw data
        display_raw_data(df)

        # Ask user if they want to restart the program
        if input('\nWould you like to restart? Type yes or no: ').strip().lower() != 'yes':
            break

if __name__ == "__main__":
    main()
