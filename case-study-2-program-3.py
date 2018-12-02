language, text = hamlets.iloc[0]

counted_text = count_words_fast(text)

data = pd.DataFrame({
    "word": list(counted_text.keys()),
    "count": list(counted_text.values())
})

# Enter your code here.

def freq(num_of_appearences):
    if num_of_appearences == 1:
        return "unique"
    elif num_of_appearences <= 10:
        return "infrequent"
    else:
        return "frequent"

new_data = pd.DataFrame({
    "length": list(len(x) for x in counted_text),
    "frequency": list(freq(x) for x in data["count"])
})

data = pd.concat([data, new_data], axis=1)
