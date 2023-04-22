import nltk


def get_text_complexity(text: str) -> str:
    sentence_list = nltk.sent_tokenize(text=text)
    word_list = nltk.word_tokenize(text=text)
    summ_words_length = sum([len(word) for word in word_list])
    arg_sentences_length = len(word_list) / len(sentence_list)
    arg_words_length = summ_words_length / len(word_list)

    if arg_sentences_length <= 10 and arg_words_length <= 5:
        text_complexity = 'A1'
    elif arg_sentences_length <= 12 and arg_words_length <= 6:
        text_complexity = 'A2'
    elif arg_sentences_length <= 15 and arg_words_length <= 7:
        text_complexity = 'B1'
    elif arg_sentences_length <= 20 and arg_words_length <= 8:
        text_complexity = 'B2'
    elif arg_sentences_length <= 25 and arg_words_length <= 10:
        text_complexity = "C1"
    else:
        text_complexity = 'C2'

    return text_complexity


if __name__ == "__main__":
    result = get_text_complexity(text="Hello!")
    print(result)
