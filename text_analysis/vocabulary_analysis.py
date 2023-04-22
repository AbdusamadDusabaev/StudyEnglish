from collections import defaultdict
import nltk
import re


LEMMATIZER = nltk.stem.WordNetLemmatizer()

part_of_speech_code_dict = {
    "NN": "Noun",
    "VBN": "Participle",
    "VB": "Verb",
    "JJ": "Adjective",
    "RB": "Adverb",
    "IN": "Preposition",
    "PRP": "Pronoun",
    "CC": "Conjunction",
    "CD": "Numeral",
    "VP": "Particle",
}

part_of_speech_lemmatizer_code_dict = {
    "Verb": "v",
    "Noun": "n",
    "Adjective": "a",
    "Adverb": "r",
}


def get_text_vocabulary_analysis(text: str, word_per_minute: int = 100) -> dict:
    text_vocabulary_analysis_default_dict = defaultdict(lambda: {"amount": 0})
    word_list = get_word_list(text=text)
    word_set = set(word_list)
    amount_words = len(word_list)
    reading_time = f"{round(amount_words / word_per_minute)} min"
    get_amount_each_word(word_list=word_list, vocabulary_analysis_dict=text_vocabulary_analysis_default_dict)
    get_percentage_each_word(word_list=word_list, vocabulary_analysis_dict=text_vocabulary_analysis_default_dict)
    get_vocabulary_analysis_each_word(word_set=word_set, vocabulary_analysis_dict=text_vocabulary_analysis_default_dict)
    text_vocabulary_analysis = {
        "amount_words": amount_words,
        "reading_time": reading_time,
        "text_vocabulary_analysis_dict": dict(text_vocabulary_analysis_default_dict),
    }
    return text_vocabulary_analysis


def get_word_list(text: str) -> list:
    clear_text = re.sub(pattern=r"\W", repl=" ", string=text)
    word_list = list()
    for word in clear_text.split(" "):
        if word.isalpha() and len(word) > 1:
            word_list.append(word.lower())
    return word_list


def get_amount_each_word(word_list: list, vocabulary_analysis_dict: defaultdict) -> None:
    for word in word_list:
        vocabulary_analysis_dict[word]["amount"] += 1


def get_percentage_each_word(word_list: list, vocabulary_analysis_dict: defaultdict) -> None:
    amount_all_words = len(word_list)
    for key in vocabulary_analysis_dict.keys():
        word_percentage = round(vocabulary_analysis_dict[key]["amount"] / amount_all_words * 100, 2)
        vocabulary_analysis_dict[key]["percentage"] = word_percentage


def get_vocabulary_analysis_each_word(word_set: set, vocabulary_analysis_dict: defaultdict) -> None:
    for word in word_set:
        word_vocabulary_analysis_dict = get_word_vocabulary_analysis(word=word)
        word_part_of_speech = word_vocabulary_analysis_dict["word_part_of_speech"]
        word_root = word_vocabulary_analysis_dict["word_root"]
        vocabulary_analysis_dict[word]["word_part_of_speech"] = word_part_of_speech
        vocabulary_analysis_dict[word]["word_root"] = word_root


def get_word_vocabulary_analysis(word: str) -> dict:
    word_part_of_speech = get_word_part_of_speech(word=word)
    word_root = get_word_root(word=word, word_part_of_speech=word_part_of_speech)
    word_vocabulary_analysis_dict = {
        "word_part_of_speech": word_part_of_speech,
        "word_root": word_root,
    }
    return word_vocabulary_analysis_dict


def get_word_part_of_speech(word: str) -> str:
    part_of_speech_code_by_nltk = nltk.pos_tag(tokens=[word])[0][1]
    for part_of_speech_code in part_of_speech_code_dict.keys():
        if part_of_speech_code in part_of_speech_code_by_nltk:
            word_part_of_speech = part_of_speech_code_dict[part_of_speech_code]
            return word_part_of_speech


def get_word_root(word: str, word_part_of_speech: str) -> str:
    part_of_speech_lemmatizer_code = part_of_speech_lemmatizer_code_dict.get(word_part_of_speech, "-")
    if part_of_speech_lemmatizer_code != "-":
        word_root = LEMMATIZER.lemmatize(word=word, pos=part_of_speech_lemmatizer_code)
        return word_root
    word_root = "-"
    return word_root


if __name__ == "__main__":
    result = get_text_vocabulary_analysis(text="Hello! My name is Bulldog. What's up ?")
    print(result)
