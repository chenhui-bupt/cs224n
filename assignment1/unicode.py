with open('utils/datasets/stanfordSentimentTreebank/dictionary2.txt', 'w') as f2:
    with open('utils/datasets/stanfordSentimentTreebank/dictionary.txt', 'r') as f1:
        for line in f1:
            f2.write(line.encode('utf-8').decode('latin1'))
