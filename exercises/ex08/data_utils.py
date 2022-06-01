"""Dictionary related utility functions."""

__author__ = "730449161"

# Define your functions below


from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a table."""
    result: list[dict[str, str]] = []
    
    # Open a handle to the data file.
    file_handle = open(filename, "r", encoding="utf8")
    
    # Prepare to read the data file as a CSV rather than just strings.
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line.
    for row in csv_reader:
        result.append(row)
    
    # Close the file when we're done, to free its resources.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transfrom a row-oriented table to a column oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(column_table: dict[str, list[str]], row_number: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the firsts N rows of data for each column."""
    result: dict[str, list[str]] = {}
    shortened_values: list[str] = []
    i: int = 0
    for item in column_table:
        shortened_values = []
        length: int = len(column_table[item])
        i = 0
        while i < row_number and i < length:
            shortened_values.append(column_table[item][i])
            i += 1
        result[item] = shortened_values

    return result


def select(column_table: dict[str, list[str]], column_names: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for column in column_names:
        result[column] = column_table[column]
    
    return result


def concat(column_table_one: dict[str, list[str]], column_table_two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for column in column_table_one:
        result[column] = column_table_one[column]
    for column in column_table_two:
        if column in result:
            result[column] += column_table_two[column]
        else:
            result[column] = column_table_two[column]
    
    return result


def count(values: list[str]) -> dict[str, int]:
    """Counts the frequencies of objects in a string list."""
    result: dict[str, int] = {}
    for item in values:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    
    return result


def column_list_extract(column_table: dict[str, list[str]], key: str) -> list[str]:
    """Extracts a list of type string from a dictionary."""
    chosen_list: list[str] = column_table[key]
    return chosen_list