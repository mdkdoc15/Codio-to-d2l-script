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
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for record in data:
            writer.writerow(record)


def clean_data(data, project_name):
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
    points_header = f"{project_name} Points Grade" #TODO Update to variable
    username_header = "Username"
    new_data = []
    for i, student in enumerate(data):
        if i > 5:
            break
        new_data.append({})
        # Turn email to Username column
        # Username is net id, AKA, everything before at sign
        new_data[-1][username_header] = data[i][email_header][: data[i][email_header].find("@") ]
        # Update column name of the grades
        new_data[-1][points_header] = data[i][final_grade_header]
        # Add End of line info
        new_data[-1][end_of_line_header] = end_of_line_value
    return new_data

def get_d2l_filename(orig_file_path):
    '''
    Get updated file name from the path passed in

    :param orig_file_path: original path that we are parsing
    :return: file name up until the first '.' char
    '''
    updated_filename = orig_file_path[: orig_file_path.find(".")]
    return f"{updated_filename}_d2l.csv"

def main():
    file_path = "projectXX.from_codio.csv"
    d2l_file_name = get_d2l_filename(file_path)
    project_name = d2l_file_name[:-8] # Strip the _d2l.csv from the file name
    data = read_csv_file(file_path)
    d2l_data = clean_data(data, project_name)

    write_csv_file(d2l_file_name, d2l_data)


if __name__ == '__main__':
    main()
