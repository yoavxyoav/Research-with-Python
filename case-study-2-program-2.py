language, text = hamlets.iloc[0]


print(data)
i = 0
for pair in counted_text:
    print(pair)
    print(counted_text[pair])
    print(i)
    print
    data.loc[i] = pair, counted_text[pair]
    #data.iloc[i] = counted_text.keys()[i], counted_text.values[i]
    
    i += 1
