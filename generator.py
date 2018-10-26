import csv

def get_file_header(file_path):
    header = []
    with open(file_path, 'r', newline='') as file:
        reader = csv.reader(file)
        header = list(reader)[0]
    return header

def generate_row(suffix, position_list, row):
    for index, val in enumerate(row):
        if index in position_list:
            row[index] = val + str(suffix)
    return row

def generate_file(position_list, headers, template_row, increment_count):
    '''
    generate file with name 'out.csv', which contians the auto increment data
        @position_list
            the position where we need to auto increment
        @headers
            the header of csv file
        @template_row
            the original sample row we need to process auto increment
        @increment_count
            the count we need to increment to, start index is 0
    '''
    with open('out.csv', 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(headers)
        # for loop to generate and write rows 
        index = 0
        while index < increment_count:
            bak_row = template_row.copy()
            bak_row = generate_row(index, position_list, bak_row)
            writer.writerow(bak_row)
            index = index + 1

def generate_general_csv(sample_file, increment_count):
    '''
    this method will generate the common format user file, setting as:
    1. headers contains the first two lines of csv file
    2. only auto increment the username and user id columns
        @sample_file
            the sample file contains the headers and users need to clone
        @increment_count
            the total users need to import
    '''
    # open sample file and get required info
    print("-----------> Start Generate File!")
    header01 = []
    header02 = []
    sample_row = []
    with open(sample_file) as ifile:
        reader = csv.reader(ifile)
        content = list(reader)
        header01 = content[0]
        header02 = content[1]
        sample_row = content[2]

    position_list = []
    default_increment_col = ['USERID', 'USERNAME']
    for index, val in enumerate(header01):
        if val in default_increment_col:
            print('position index: %s' % index)
            position_list.append(index)

    generate_file(position_list, [header01, header02], sample_row, increment_count)
    print("-----------> Finish Generate File!")