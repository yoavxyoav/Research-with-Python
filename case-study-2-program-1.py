import pandas as pd
hamlets = pd.DataFrame(columns=("language", "text"))
book_dir = "Books"
title_num = 1
for language in book_titles:
    for author in book_titles[language]:
        for title in book_titles[language][author]:
            print(author)
            if title == "Hamlet":
                inputfile = data_filepath+"Books/"+language+"/"+author+"/"+title+".txt"
                print(inputfile)
                text = read_book(inputfile)
                hamlets.loc[title_num] = language, text
                title_num += 1

print(hamlets)
                
