language, text = hamlets.iloc[0]

counted_text = count_words_fast(text)

data = pd.DataFrame({
    "word": list(counted_text.keys()),
    "count": list(counted_text.values())
})

data["length"] = data["word"].apply(len)

data.loc[data["count"] > 10,  "frequency"] = "frequent"
data.loc[data["count"] <= 10, "frequency"] = "infrequent"
data.loc[data["count"] == 1,  "frequency"] = "unique"

# Enter your code here.

def sum_frequency(frequency):
    data.groupby(frequency).sum()

count_frequencies = data.groupby("frequency").count()

def return_sum_words(i):
    return data.groupby("frequency")["length"].sum()[i] 
    
num_words = [  count_frequencies.loc["frequent"][0], count_frequencies.loc["infrequent"][0] ,count_frequencies.loc["unique"][0]  ]

word_sum = list(return_sum_words(i) for i in range(3))

mean_word_length = list(np.array(word_sum) / np.array(num_words))


sub_data = pd.DataFrame({
    "language": "English",
    "frequency": ["frequent", "infrequent", "unique"],
    "mean_word_length": mean_word_length,
    "num_words": num_words
    
})

#this line is just reordering the columns
sub_data = sub_data[["language", "frequency", "mean_word_length", "num_words"]]
