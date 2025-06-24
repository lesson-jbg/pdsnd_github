# BikeShare Data Exploration

### Date created
June 24, 2025

### Project Title
Explore US Bikeshare Data

### Description
This project analyzes bikeshare data from three major U.S. cities: Chicago, New York City, and Washington. The goal is to give users the ability to filter data by city, month, and day of the week, and then compute and display various descriptive statistics about bikeshare usage.

The project is implemented in Python and is intended for educational purposes as part of Udacity’s Data Science program. It uses input from the user to determine which data to load and what statistics to calculate.

### Features
- Interactive command-line prompts to filter data by:
  - City (Chicago, New York City, Washington)
  - Month (January to June or all)
  - Day of the week
- Calculates and displays:
  - Most frequent times of travel
  - Most popular start and end stations
  - Most common trip combinations
  - Total and average trip duration
  - User demographics (e.g., user type, gender, birth year if available)
- Option to display raw data in 5-row increments upon user request

### Files used
- `bikeshare.py`: The main Python script for running the bikeshare analysis.
- `chicago.csv`: Bikeshare data for the city of Chicago.
- `new_york_city.csv`: Bikeshare data for New York City.
- `washington.csv`: Bikeshare data for the city of Washington.
- `.gitignore`: Used to exclude large data files from version control.

### How to Run
You can run the program using any Python 3 environment:




```bash
python bikeshare.py
```

### Future Improvements

- Add support for filtering by specific date ranges
- Create a GUI version of the application for non-technical users
- Visualize key statistics using charts and graphs
- Export results to CSV or PDF format for reporting



