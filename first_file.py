#################################################СОРТИРОВКА СЛОВ ТЕКСТА ПО УБЫВАНИЮ ЧАСТОТЫ:
punctuation_list = ['.', ',', ';', ':', '...', '!', '?', '-', '"', '(', ')']
text_example = "A beginning is the time for taking the most delicate care that the balances are correct. This every sister of the Bene Gesserit knows. To begin your study of the life of Muad'Dib, then take care that you first place him in his time: born in the 57th year of the Padishah Emperor, Shaddam IV. And take the most special care that you locate Muad'Dib in his place: the planet Arrakis. Do not be deceived by the fact that he was born on Caladan and lived his first fifteen years there. Arrakis, the planet known as Dune, is forever his place."

def get_most_frequent_word(text):
    s=text
    for e in punctuation_list:
        s=s.replace(e,'')
    s=s.lower()
    s=s.split()
    counter=dict()
    for e in s:
        n=s.count(e)
        if e not in counter:
            counter[e]=n
    result=list(counter.items())
    result.sort(key=lambda x:x[1],reverse=True)
    return result
    
print(get_most_frequent_word(text_example))


