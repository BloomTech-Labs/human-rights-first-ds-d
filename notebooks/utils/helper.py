def read(fp):
    df = (pd.read_csv(fp)
          .pipe(clean_columns)
          #.pipe(mapping)
         )
    return df

def clean_columns(df):
    #df = pd.read_csv(df)
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
    
    return df

def mapping(df):
    col_mapping_dict = {c[0]:c[1] for c in enumerate(df.columns)}
    
    return col_mapping_dict