def ch_title(w):
    ch = w.title()
    return ch


def ch_lit(w):  # предполагаемая внутренность title()
    fir = w[0]
    ch = fir.upper() + w[1:len(w)]
    return ch


def ch_string():
    return ' '.join(map(ch_lit,input('Enter your string ').split()))


word = input('Enter you word: ')
print(f'Correct word {ch_title(word)}')
print(f'Correct word {ch_lit(word)}')
print(f'Correct string {ch_string()}')
