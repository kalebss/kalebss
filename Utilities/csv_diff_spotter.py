import pandas as pd


def read_csv(file_name):
    """Read CSV file and return a dataframe."""
    return pd.read_csv(file_name)


def find_diff(df1, df2):
    """Find the difference between two dataframes and return the result."""
    return pd.concat([df1, df2]).drop_duplicates(keep=False)


def main():
    # Load the two CSV files into dataframes
    df1 = read_csv("/Users/kalebsaldana/Downloads/models.csv")
    df2 = read_csv("/Users/kalebsaldana/Downloads/models_2.csv")

    # Find differences between the dataframes
    diff1 = find_diff(df1, df2)
    diff2 = find_diff(df2, df1)

    # Print the results
    print("Rows in file1.csv that are not in file2.csv:")
    print(diff1)
    print("\nRows in file2.csv that are not in file1.csv:")
    print(diff2)


if __name__ == "__main__":
    main()
