#Process to Clean Data
Read each CSV file line by line as they are not the common CSV format and put 
them into a array.
##Delete Useless Lines
The original data has many useless rows such as null lines and the lines which 
is used to describe the table. These lines will be removed from the array. Then, 
the list is write as a CSV file to the disk.
##Re-name the Columns
Use Pandas to read the CSV files to dataframes. Then, re-name the columns in 
dataframes because some of the columns in dataframe are different with other 
files but they have the same meanings. So we re-name the columns in some dataframes 
to make them connect with other dataframes easy.
##Drop the Repeated Column
The column 'Total' could be calculated by other columns so we delete this columns.
##Fill the Null Value
All values in dataframes should not be a null value. However, some values in some 
data frames are '-'. We use 0.0 to replace them
##Re-name the Value in Column 'Month'
To make it easy to search the range of month, we use the integers instead of 
strings in the column 'Month'.
##Connect the Dataframe
The dataframes from CSV files are classified by years. We connect them to only one dataframe.
##Divide the Dataframe
Based on different methods to classify visitors, we divide the dataframe to several 
dataframes and write them to the disk as CSV format.