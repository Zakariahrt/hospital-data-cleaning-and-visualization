import pandas as pd

def display():
   print('is working')

def  load_csv(patth,delimiter=',', encoding='utf-8'):
    df = pd.read_csv(patth,delimiter=delimiter, encoding=encoding)
    return df

def handle_duplicates(df, duplicates_file_path):
    duplicated_df = df[df.duplicated()]
    df_cleaned = df.drop_duplicates()
    
    if not duplicated_df.empty:
        save_csv(duplicated_df, duplicates_file_path)
        print(f"Removed {len(duplicated_df)} duplicate rows. Duplicates saved to {duplicates_file_path}.")
    else:
        print("No duplicate rows found.")
    
    return df_cleaned

def missing_value(df):
  missing_value=df.isnull().sum()
  return missing_value

def fillna_with_prefix(df):
    """
    Fill missing values in the 'GENDER' column using the 'PREFIX' column.
    'Mrs.', 'Ms.' -> 'female'
    'Mr.' -> 'male'
    """
    prefix_to_gender = {
        'Mrs.': 'F',
        'Ms.': 'F',
        'Mr.': 'M'
    }
    
    df['GENDER'] = df.apply(
        lambda row: prefix_to_gender[row['PREFIX']] if pd.isnull(row['GENDER']) else row['GENDER'],
        axis=1
    )
    
    return df

def clean_dates(df, date_columns):
    for column, date_format in date_columns.items():
        if column in df.columns:
            df[column] = df[column].astype(str).str.replace('|', '-')
            
            df[column] = pd.to_datetime(df[column], format=date_format, errors='coerce')
    
    return df

def  replace_missing_value(df,column,value):
  df[column].fillna(value,inplace=True)
  return df

def  drop_column(df,column):
  df.drop(column,axis=1,inplace=True)
  return df

def save_csv(df,path):
  df.to_csv(path,index=False)

def display_info(df):
    print("DataFrame Info:")
    print(df.info())

def display_head(df):
    print("DataFrame Head:")
    print(df.head())

def display_description(df):
    print("DataFrame Description:")
    print(df.describe())

