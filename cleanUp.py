import pandas as pd
#open the file and read each line to a list
for i in range(2006, 2020):
    f = open('original_data/original_attributes_'+str(i)+'.csv', 'r')
    # list contains the title of useless lines
    list = ['\"Unweighted Base\"', '\" Start month of trip\"', '\"Total\"']
    docs = range(2006, 2020)
    line = f.readline()
    input = []
    # read each lines to the list
    while line:
        input.append(line)
        line = f.readline()
    # close the file
    f.close()
    output = []
    # For each line in the list, check if it is useless. If not, add it to the output list
    for item in input:
        item = item.split(',')
        if item[0] == '\"\"' and (item[1] == '\"Total\"' or item[1] == '\"TOTAL\"'):
            item[0] = '\"Month\"'
            output.append(','.join(x for x in item))
        elif not item[0] == '\"\"' and len(item) > 1 and not list.__contains__(item[0]):
            output.append(','.join(x for x in item))
    # Open another file to write the output list to CSV file.
    f = open('data/visitor_attributes_'+str(i)+'.csv', 'w')
    for item in output:
        f.write(item)
    f.close()
    # Read the new CSV file
    data = pd.read_csv('data/visitor_attributes_'+str(i)+'.csv')
    # Drop all columns which all values in column are null
    data = data.dropna(axis=1, how="all")
    # Write to a new csv file
    data.to_csv('data/visitor_attributes_'+str(i)+'.csv', index=0)