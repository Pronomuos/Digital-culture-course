# coding=utf-8
from math import log, ceil
from PIL import Image


def sort_dict(d, member, rev=True):
    return {i[0]: i[1] for i in sorted(d.items(), key=lambda x: x[member], reverse=rev)}


def find_freq(mes):
    temp = {}
    for el in mes:
        if el not in temp:
            temp.update({el: 1})
        else:
            temp[el] += 1
    return sort_dict({el[0]: (el[1] + 0.0) / len(mes) for el in temp.items()}, 1)


def enthropy(freq):
    hx = 0
    for el in freq:
        hx -= el * log(el, 2)
    return hx


def even_binary_decoding(freq, max):
    def binary(n):
        s = ''
        while n > 0:
            s = str(n % 2) + s
            n //= 2
        while len(s) < max:
            s = ('0' + s)
        return s

    new_decoding = {}
    i = 0
    for el in freq:
        new_decoding.update({el: binary(i)})
        i += 1
    return new_decoding


def shannon_fano_coding(freq: dict, cur_code: str):
    if len(freq) == 1:
        for key in freq.keys():
            return {key: cur_code}
    else:
        a, b = {}, {}
        for item in freq.items():
            if sum(a.values()) < sum(b.values()):
                a.update({item[0]: item[1]})
            else:
                b.update({item[0]: item[1]})
        a = shannon_fano_coding(a, cur_code + '0')
        b = shannon_fano_coding(b, cur_code + '1')
        a.update(b)
        return a


def huffman_coding(freq: dict):
    new_coding = {item[0]: "" for item in freq.items()}
    temp_list = [[item[1], [item[0]]] for item in freq.items()]
    while len(temp_list) > 1:
        temp_list.sort(key=lambda x: x[0], reverse=False)
        for el in temp_list[0][1]:
            new_coding[el] = '0' + new_coding[el]
        for el in temp_list[1][1]:
            new_coding[el] = '1' + new_coding[el]
        temp_list[1][0] += temp_list[0][0]
        temp_list[1][1] += temp_list[0][1]
        temp_list.pop(0)
    return new_coding


def decode(mes: list, coding: dict):
    new_message = ""
    for el in mes:
        new_message += coding[el]
    return new_message


if __name__ == '__main__':
    image = Image.open("input.jpeg")
    image = image.convert('L').resize((128, 128))
    image.save("output.jpeg")
    pix = image.load()

    print("Выделение цифровой последовательности:")
    message = [round(pix[j, image.height // 2] / 20) * 20 for j in range(image.width)]
    print(message)

    print("Нахождние частот встречаемости символов первичного "
          "алфавита, отсортированных в порядке убывания:")
    freq = find_freq(message)
    print(freq)
    print("Количество сиволов алфавита:")
    print(len(freq.keys()))
    print("Энтропия:")
    enthropy = enthropy(freq.values())
    print(enthropy)
    print("Средняя минимальная длина двоичного кода:")
    av_min_length = ceil(log(len(freq), 2))
    print(av_min_length)

    print("Получение равномерных кодов:")
    even_binary = even_binary_decoding(sort_dict(freq, 0), av_min_length)
    print(even_binary)
    print("Получение кодов Шеннона-Фано:")
    shannon_fano = shannon_fano_coding(freq, "")
    print(shannon_fano)
    print("Получение кодов Хаффмана:")
    huffman = huffman_coding(freq)
    print(huffman)

    print("Сообщение, закодированное равномерным кодом:")
    even_binary_mes = decode(message, even_binary)
    print(even_binary_mes)
    print("Количество переданной информации - {} бит.".format(
        len(even_binary_mes)))
    print("Средняя длина кодовой комбинации - {}".format(
        len(even_binary_mes) / len(message)))
    print("Сообщение, закодированное кодом Шеннона–Фано:")
    shannon_fano_mes = decode(message, shannon_fano)
    print(shannon_fano_mes)
    print("Количество переданной информации - {} бит.".format(
        len(shannon_fano_mes)))
    print("Средняя длина кодовой комбинации - {}".format(
        len(shannon_fano_mes) / len(message)))
    print("Сообщение, закодированное кодом Хаффмана:")
    huffman_mes = decode(message, huffman)
    print(huffman_mes)
    print("Количество переданной информации - {} бит.".format(
        len(huffman_mes)))
    print("Средняя длина кодовой комбинации - {}".format(
        len(huffman_mes) / len(message)))

    print("Избыточность равномерного кодирования - {}".format(
        1 - enthropy / (len(even_binary_mes) / len(message))))
    print("Избыточность кодов Шеннона-Фано - {}".format(
        1 - enthropy / (len(shannon_fano_mes) / len(message))))
    print("Избыточность кодов Хаффмана - {}".format(
        1 - enthropy / (len(huffman_mes) / len(message))))
