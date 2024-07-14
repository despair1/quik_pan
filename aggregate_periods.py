print("hello")

def get_mins(df, column_name, start, num, size):
    print("hello there!!!")
    n = df[column_name].idxmin()
    print(n)
    idx_array = []
    end = start + num*size
    if end> len(df): end = len(df)
    for i in range(start, end, size):
        idx_array.append(df[i:i+size][column_name].idxmin())
    #for i in idx_array:
        #print(i)
        #print(df[i:i+1])
    print(df.loc[idx_array])
    return idx_array