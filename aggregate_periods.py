#print("hello")
from count_up import count_up
from prev_less import prev_less
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
    print(df.loc[idx_array, ["<LOW>", "<CLOSE>"]])
    #more_then_prev(df,idx_array)
    # count_up(idx_array, column_name, df)
    prev_less(idx_array, df)
    return idx_array

def more_then_prev(df, indexes):
    more_inx = [df.iloc[indexes[i], 1:3] for i in range(1, len(indexes) )]
    for i in more_inx:
        print(i)