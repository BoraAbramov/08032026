
# 1 create tuple with 3 of your favorite movies
movie = ("westworld", "moon knight", "reacher")

# 2 create tuple with all countries in Europe (ask ChatGPT)
europe_countries = (
    "Albania",
    "Andorra",
    "Austria",
    "Belarus",
    "Belgium",
    "Bosnia and Herzegovina",
    "Bulgaria",
    "Croatia",
    "Cyprus",
    "Czech Republic",
    "Denmark",
    "Estonia",
    "Finland",
    "France",
    "Germany",
    "Greece",
    "Hungary",
    "Iceland",
    "Ireland",
    "Italy",
    "Kosovo",
    "Latvia",
    "Liechtenstein",
    "Lithuania",
    "Luxembourg",
    "Malta",
    "Moldova",
    "Monaco",
    "Montenegro",
    "Netherlands",
    "North Macedonia",
    "Norway",
    "Poland",
    "Portugal",
    "Romania",
    "San Marino",
    "Serbia",
    "Slovakia",
    "Slovenia",
    "Spain",
    "Sweden",
    "Switzerland",
    "Ukraine",
    "United Kingdom",
    "Vatican City"
)

print(len(europe_countries`))

# 3 create tuple with all the days of feb (1, 2 ... 28)
feb_days = (
    1, 2, 3, 4, 5, 6, 7,
    8, 9, 10, 11, 12, 13, 14,
    15, 16, 17, 18, 19, 20, 21,
    22, 23, 24, 25, 26, 27, 28
)

# 4 create tuple with all the days of dec (1, 2 .. 31)
dec_days = (
    1, 2, 3, 4, 5, 6, 7,
    8, 9, 10, 11, 12, 13, 14,
    15, 16, 17, 18, 19, 20, 21,
    22, 23, 24, 25, 26, 27, 28,
    29, 30, 31
)

# 5 create tuple of all the month in the year
months = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)

# 6 create tuple of all USA presidents till today (ask ChatGPT), use len to find out how many are they
usa_presidents = (
    "George Washington", "John Adams", "Thomas Jefferson", "James Madison",
    "James Monroe", "John Quincy Adams", "Andrew Jackson", "Martin Van Buren",
    "William Henry Harrison", "John Tyler", "James K. Polk", "Zachary Taylor",
    "Millard Fillmore", "Franklin Pierce", "James Buchanan", "Abraham Lincoln",
    "Andrew Johnson", "Ulysses S. Grant", "Rutherford B. Hayes", "James A. Garfield",
    "Chester A. Arthur", "Grover Cleveland", "Benjamin Harrison", "William McKinley",
    "Theodore Roosevelt", "William Howard Taft", "Woodrow Wilson", "Warren G. Harding",
    "Calvin Coolidge", "Herbert Hoover", "Franklin D. Roosevelt", "Harry S. Truman",
    "Dwight D. Eisenhower", "John F. Kennedy", "Lyndon B. Johnson", "Richard Nixon",
    "Gerald Ford", "Jimmy Carter", "Ronald Reagan", "George H. W. Bush",
    "Bill Clinton", "George W. Bush", "Barack Obama", "Donald Trump",
    "Joe Biden"
)

print(len(usa_presidents))

# 7 use mean to find the avg of this tuple = (8, 11, -3, 12)
import statistics

numbers = (8, 11, -3, 12)
total = sum(numbers)
count = len(numbers)
average = total / count
print(f"without import statistics {average}")

print(f"use statistics {statistics.mean(numbers)}")

