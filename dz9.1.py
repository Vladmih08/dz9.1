def popular_words (text: str, words: str)->str:
    text = text.lower()
    text = text.split()
    kolvo_raz = []
    for slovo in words:
        kolvo = 0
        for a in text:
            if a == slovo:
                kolvo += 1
        kolvo_raz.append(kolvo)
    otvet = {}
    index = 0
    for slovo in words:
        otvet[slovo] = kolvo_raz[index]
        index += 1
    return otvet
assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')
