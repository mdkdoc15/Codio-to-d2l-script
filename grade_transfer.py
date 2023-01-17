"""
Created by Matt Kight

Goal: Convert CSV from codio to useable D2L CSV
"""

import csv

def read_csv_file(filename):
    """
    Takes a filename denoting a CSV formatted file.
    Returns an object containing the data from the file.
    The specific representation of the object is up to you.
    The data object will be passed to the write_*_files functions.
    """

    with open(filename, newline='') as csvfile:
        return list(csv.DictReader(csvfile))


def write_csv_file(filename, data):
    """
    Takes a filename (to be writen to) and a data object
    (created by one of the read_*_file functions).
    Writes the data in the CSV format.
    """

    with open(filename, 'w', newline='') as csvfile:
        fieldnames = [field for field in data[0]]
        fieldnames.sort()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for record in data:
            writer.writerow(record)

def clean_data(data):
    """
    Takes in CSV data and converts to D2L desierable form
    :param data: CSV data
    :return: D2L readable data
    """
    # Old headers
    email_header = "email"
    final_grade_header = 'final grade'

    # New headers
    end_of_line_header = "End-of-line indicator"
    end_of_line_value = "#"
    points_header = "ProjectXX Points Grade" #TODO Update to variable
    username_header = "Username"
    new_data = []
    for i, student in enumerate(data):
        if i > 5:
            break
        new_data.append({})
        # Turn email to Username column
        # Username is net id, AKA, everything before at sign
        new_data[-1][username_header] = data[i][email_header][: (data[i][email_header].find("@") -1) ]
        # Update column name of the grades
        new_data[-1][points_header] = data[i][final_grade_header]
        # Add End of line info
        new_data[-1][end_of_line_header] = end_of_line_value

    for i, val in enumerate(new_data):
        if i > 5:
            break
        print(val)

    return new_data


def main():
    file_path = "cse-331-ss23_project00-s23_1673928366429.csv"
    data = read_csv_file(file_path)
    clean_data(data)


if __name__ == '__main__':
    main()
