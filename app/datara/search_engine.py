def search_data(df, query):
    query = query.lower()
    matches = []
    for _, row in df.iterrows():
        for val in row:
            if query in str(val).lower():
                matches.append(row.to_dict())
                break
    return matches
