# CSV:

# Key Terms:

## Section 1: Reading from a CSV file

A csv file (short for "Comma Seperated Values") is a file that store information in a structured format of cells, that are seperated by commas.
If you have ever used a spreedshet program such as Microsoft Excel or Google Sheets, the csv is just like a spreedsheet.

TODO: add Image

A spreedsheet is oraganized by columns (cells stacked on top of each other vertically) and rows (a line of cells that go horizontally). Most CSV files have a header at the top, that you can think of as the name of the column.

TODO: add Image

In order to easily read from a CSV we will be using the csv library.

------------------------------------------------------------------------------------
#### Example #1: Reading From a CSV

We begin by defining a function called `read_csv_file` that reads in a csv file and prints out the information row by row.
```
import csv

def read_csv_file(file_path):
    with open(file_path, newline='') as csvfile:
        csv_rows_as_dict = csv.DictReader(csvfile)
        for each_row in csv_rows_as_dicts:
            print(row)

```

The key line here is `csv.DictReader(csvfile)`. This is a function from the [csv library](https://docs.python.org/3/library/csv.html#csv.DictReader) and it creates a dictionary for each row. In this dictionary, the keys are the column names and the values are the corresponding entries in that specific column and row.

To test out this function, let's call it with the sample csv `giraffe.csv`:

```
read_csv_file("sample_csv_files/giraffe.csv")
```

This will print out each line as a dictionary:
```
{'Name': 'Glenn', 'Subspecies': 'Angolan', 'Height': '490'}
{'Name': 'Galaxy', 'Subspecies': 'Masai ', 'Height': '518'}
{'Name': 'Geoffrey', 'Subspecies': 'Reticulated', 'Height': '450'}
```

------------------------------------------------------------------------------------

## References:
* [Python's CSV Documentation](https://docs.python.org/3/library/csv.html)
