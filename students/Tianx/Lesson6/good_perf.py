"""
good performing, nicely written module

"""
import cProfile
import datetime
import csv


def analyze(filename):
    """analyze file"""
    start = datetime.datetime.now()
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        year_count = {
            "2013": 0,
            "2014": 0,
            "2015": 0,
            "2016": 0,
            "2017": 0,
            "2018": 0
        }
        found = 0
        for row in reader:
            year = row[5][-4:]
            if year in year_count:
                year_count[year] += 1
            if "ao" in row[6]:
                found += 1

        print(year_count)
        print(f"'ao' was found {found} times")
        end = datetime.datetime.now()

    return (start, end, year_count, found)


def main():
    """main function"""
    filename = "data/exercise.csv"
    analyze(filename)


if __name__ == "__main__":
    pr = cProfile.Profile()
    pr.enable()
    main()
    pr.disable()
    pr.print_stats()
