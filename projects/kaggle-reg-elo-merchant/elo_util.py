
        #################################################
        ### THIS FILE WAS AUTOGENERATED! DO NOT EDIT! ###
        #################################################
        # file to edit: dev_nb/elo_data_eng_nn0.ipynb

def join_df(left, right, left_on, right_on=None, suffix='_y'):
    if right_on is None: right_on = left_on
    return left.merge(right, how='left', left_on=left_on, right_on=right_on,
                      suffixes=("", suffix))

def aggregate(df, by, agg_params, prefix=None):
    df = df.groupby(by).agg(agg_params)
    df.columns = [prefix + '_'.join(col).strip() for col in df.columns.values]
    df.reset_index(inplace=True)
    return df