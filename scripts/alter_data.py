def alter_data(df, context):
    """
    Perform any alterations here on the Pandas DataFrame "df".

    For example, here is how you might drop the "education" column
    from indicator ENV1-3-2:

    if context['indicator_id'] == 'ENV1-3-2':
        df = df.drop(columns=['education'])
    """
    # Don't forget to return the DataFrame at the end:
    return df
