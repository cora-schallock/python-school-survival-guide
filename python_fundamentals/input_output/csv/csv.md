# CSV:

# Key Terms:
* csv - a file that stores data in a spreedsheet structure 
* header - the name of the columns (this is typically the first row in a csv)

## Section 0: What's a CSV file?

A csv file (short for "Comma Seperated Values") is a file that store information in a structured format of cells, that are seperated by commas.
If you have ever used a spreedshet program such as Microsoft Excel or Google Sheets, the csv is just like a spreedsheet.

A spreedsheet is oraganized by columns (cells stacked on top of each other vertically) and rows (a line of cells that go horizontally). Most CSV files have a header at the top, that you can think of as the name of the column.

| Column 1 Name    | Column 2 Name |
| ----------- | ----------- |
| Row 1, Col 1 | Row 1, Col 2 |
| Row 2, Col 1  | Row 2, Col 2 |

## Section 1: Reading from a CSV file

As you can imagine, there a lot of potential use-cases for using this kind of structured data file.

In this section, we will imagine a Zoo that is using csv files to store information about the animals they care for. Each csv has 3 named columns: `Name`, `Subspecies`, and `Height`. Here is an example csv that can be found in the `sample_csv_files` directory that is called `giraffe.csv`:

| Name    | Subspecies | Height |
| ----------- | ----------- | ----------- |
| Glenn | Angolan | 490 |
| Galaxy | Masai | 518 |
| Geoffrey | Reticulated | 450 |

We will begin by look at how to read from a csv file

In order to easily read from a CSV we will be using the csv library.

------------------------------------------------------------------------------------
#### Example #1: Reading From a CSV

We begin by defining a function called `read_csv_file` that reads in a csv file and prints out the information row by row.
```
import csv

def read_csv_file(file_path):
    with open(file_path, newline='') as csvfile:
        csv_as_dicts = csv.DictReader(csvfile)
        return list(csv_as_dicts)
```

The key line here is `csv.DictReader(csvfile)`. This is a function from the [csv library](https://docs.python.org/3/library/csv.html#csv.DictReader) and it creates a dictionary for each row. In this dictionary, the keys are the column names and the values are the corresponding entries in that specific column and row.

To test out this function, let's call it with the sample csv `giraffe.csv`:

```
read_csv_file("sample_csv_files/giraffe.csv")
```

This will print out each line as a dictionary:
```
[{'Name': 'Glenn', 'Subspecies': 'Angolan', 'Height': '490'},
 {'Name': 'Galaxy', 'Subspecies': 'Masai ', 'Height': '518'},
 {'Name': 'Geoffrey', 'Subspecies': 'Reticulated', 'Height': '450'}]
```

------------------------------------------------------------------------------------

## Section 2: Reading in Multiple CSV Files

One common use case with csv files, is to read in mulptiple csv file to combine the data so it can be processed.

Say if you want to locate all the csv files in a folder you can use the [path library](https://docs.python.org/3/library/pathlib.html#pathlib.Path.rglob). To use the path library, you first specify the path and second specify the kind of file you are looking for (in this case, csv).

------------------------------------------------------------------------------------
#### Example #1: Reading From a CSV

We will define a new function called `read_all_csv_files` that located each csv file in a directory and calls the `read_csv_file` from the previous example.
```
def read_all_csv_files(directory=""):
    csv_dict_list = []
    for each_csv_file in Path(directory).glob("*.csv"):
        current_csv_dict = read_csv_file(each_csv_file)
        csv_dict_list.extend(current_csv_dict)
    return csv_dict_list
```

The key section here is `Path(directory).glob("*.csv")` in the for loop. Let's break this down:
* The first part `Path(directory)` creates a path object that points to a directory via it's path.
* The second part `.glob("*.csv")` locates all csv files in the directory pointed at by the path object. The name/ syntax here may seem a bit unusal but the word [glob](https://docs.python.org/3/library/glob.html) refers to a computer program that matches paterns and the `"*.csv"` says I want you to find any file name (the `*` is called a wildcard and can be thought of a fill-in-the-blank) that ends the extension `.csv`

*Key Idea*: If you pass in "" as the directory (i.e. Path("")) it by default looks in the current working directory (a.k.a the cwd). If you read through python documnetation this is typically shortened to just Path()

------------------------------------------------------------------------------------



## References:
* [Python's CSV Documentation](https://docs.python.org/3/library/csv.html)
