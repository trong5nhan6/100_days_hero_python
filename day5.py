def bag_of_word(corpus):
    vocabs = []
    for sentence in corpus:
        for word in sentence.split():
            if word not in vocabs:
                vocabs.append(word)
    return vocabs

def binary_vocabs(vocabs):
    binary_vocabs = [0 for i in range(len(vocabs))]
    str = 'Tôi thích AI thích Toán'
    for word in str.split():
        for i in range(len(vocabs)):
            if word == vocabs[i]:
                binary_vocabs[i] += 1
    return binary_vocabs

corpus = ["Tôi thích môn Toán", "Tôi thích AI", "Tôi thích âm nhạc"]
vocabs = bag_of_word(corpus)
binary_vocab = binary_vocabs(vocabs)
print(vocabs)
print(binary_vocab)
