# coding=utf-8
import re
import codecs


class TypoCorrect:
    def __init__(self):
        pass

    text = ""
    words = {}
    dict = {}
    typoes_and_correct = {}

    @classmethod
    def read_text(cls, ifile='brain333.txt'):
        with codecs.open(ifile, "r", "1251") as f:
            cls.text = f.read().lower()
            cls.update_words()

    @classmethod
    def update_words(cls):
        temp = re.split("[!?,;.:«()» \n\t\r]+", cls.text)
        temp = [word.lower() for word in temp if word]
        cls.words.clear()
        for word in temp:
            cls.words.update({word: cls.words.get(word, 0) + 1})

    @classmethod
    def read_dict(cls, ifile='dict1.txt'):
        with codecs.open(ifile, "r", "1251") as f:
            temp = f.readlines()
            for line in temp:
                line = line.split()
                cls.dict.update({line[0]: int(line[1])})

    @classmethod
    def count_and_print(cls):
        print("Количество словофрм - {}.".format(sum(cls.words.values())))
        print("Количество различных словофрм - {}.".format(len(cls.words.keys())))
        cls.typoes_and_correct.clear()
        for word in cls.words.keys():
            if word not in cls.dict.keys():
                cls.typoes_and_correct.update({word: word})
        print("Количество словофрм, которых нет в словаре - {}.".format(len(cls.typoes_and_correct)))

    @classmethod
    def edit_text(cls):
        for typo in cls.typoes_and_correct.keys():
            cls.typoes_and_correct[typo] = cls.correct_word(typo)
        for typo in cls.typoes_and_correct:
            if cls.find_lev_dist(typo, cls.typoes_and_correct[typo]) <= 2:
                cls.text = cls.text.replace(typo, cls.typoes_and_correct[typo])
        cls.update_words()

    @classmethod
    def find_lev_dist(cls, str1, str2):
        d = [[0 for j in range(len(str2) + 1)] for i in range(len(str1) + 1)]
        for i in range(len(str1) + 1):
            d[i][0] = i
        for j in range(len(str2) + 1):
            d[0][j] = j
        for i in range(1, len(str1) + 1):
            for j in range(1, len(str2) + 1):
                if str1[i - 1] != str2[j - 1]:
                    d[i][j] = min(d[i - 1][j] + 1, d[i][j - 1] + 1,
                                  d[i - 1][j - 1] + 1)
                else:
                    d[i][j] = d[i - 1][j - 1]
        return d[len(str1)][len(str2)]

    @classmethod
    def correct_word(cls, typo):
        dist, freq = 1000, 0
        correct_word = ""
        for word in cls.dict.keys():
            cur_dist = cls.find_lev_dist(typo, word)
            cur_freq = cls.dict[word]
            if cur_dist == dist:
                if cur_freq < freq:
                    freq = cur_freq
                    correct_word = word
            if cur_dist < dist:
                freq = cur_freq
                dist = cur_dist
                correct_word = word
        return correct_word

    @classmethod
    def print_typoes(cls):
        for typo in cls.typoes_and_correct:
            if cls.find_lev_dist(typo, cls.typoes_and_correct[typo]) > 2:
                val = "не найдено"
            else:
                val = cls.typoes_and_correct[typo]
            print("{} - {} -> {}".format(typo.encode('utf-8').decode('utf-8'),
                                         val.encode('utf-8').decode('utf-8'),
                                         cls.find_lev_dist(typo, cls.typoes_and_correct[typo])))

    @classmethod
    def write_into_file(cls, ofile='output.txt'):
        with codecs.open(ofile, "w", "1251") as out:
            out.write(cls.text)


if __name__ == '__main__':
    TypoCorrect.read_text()
    TypoCorrect.read_dict()
    TypoCorrect.count_and_print()
    print("\n")
    TypoCorrect.edit_text()
    TypoCorrect.print_typoes()
    print("\n")
    TypoCorrect.count_and_print()
    TypoCorrect.write_into_file()
