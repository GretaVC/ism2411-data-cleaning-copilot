# The purpose of this file to provide a spcae for cleaning the data in sales_data_raw.csv
import pandas as pd

raw_path = "data/raw/sales_data_raw.csv"
def load_data(raw_path):                # to clarify the later use of the term load_data
    """Load raw sales data from a CSV file."""
    return pd.read_csv(raw_path)    
df_raw = load_data(raw_path)

# 1 Standardize column names (for example, lowercase and underscores) for simpiler viewing.
def clean_column_names(df_raw):
    """Standardize column names: convert to lowercase and replace spaces with underscores."""
    df_raw.columns = df_raw.columns.str.strip()  # Remove leading/trailing spaces
    df_raw.columns = df_raw.columns.str.lower().str.replace(" ", "_")
    return df_raw
df_raw = clean_column_names(df_raw)

# 2 Remove white space from  product names and categories in order to create consistency and make analsysis easier.
def remove_white_space(df_raw):
    """Remove leading and trailing white space from product names and categories."""
    df_raw = clean_column_names(df_raw)
    df_raw["prodname"] = df_raw["prodname"].str.strip()
    df_raw["category"] = df_raw["category"].str.strip()
    return df_raw
df_raw = remove_white_space(df_raw)    


# 3 Handle missing prices and quantities by dropping the missing values becuase data that is filled with averages is less reliable than removing missing numbers.
def handle_missing_values(df_raw):
    """Handle missing values by dropping missing prices or quantities."""
    clean_column_names(df_raw) # called to ensure column names are standardized
    df_raw = df_raw.dropna(subset =["price", "qty"])
    return df_raw
df_raw = handle_missing_values(df_raw)

#4 Remove rows with clearly invalid values, such as negative prices or quantities because they are inaccurate and can cause errors in analysis.
def remove_invalid_values(df_raw):
    """Remove rows with negative prices or quantities."""
    clean_column_names(df_raw)
    df_raw["price"] = pd.to_numeric(df_raw["price"], errors= "coerce")
    df_raw["qty"] = pd.to_numeric(df_raw["qty"], errors= "coerce")
    df_raw = df_raw[(df_raw["price"] >= 0) & (df_raw["qty"] >= 0)]
    return df_raw
df_raw = remove_invalid_values(df_raw)

if __name__ == "__main__":
    raw_path = "data/raw/sales_data_raw.csv"
    cleaned_path = "data/processed/sales_data_clean.csv"

    df_raw = load_data(raw_path)
    df_clean = clean_column_names(df_raw)
    df_clean = remove_white_space(df_clean)
    df_clean = remove_invalid_values(df_clean)
    df_clean = handle_missing_values(df_clean)
    df_clean.to_csv(cleaned_path, index=False)
    print("Cleaning complete. First few rows:")
    print(df_clean.head())

