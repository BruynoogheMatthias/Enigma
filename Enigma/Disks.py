def disk(word, disknr, position = 1):
    word = word.lower()
    outword = ""
    wordarray = []

    for letters in word:
        converter = {
            'a': 0,
            'b': 1,
            'c': 2,
            'd': 3,
            'e': 4,
            'f': 5,
            'g': 6,
            'h': 7,
            'i': 8,
            'j': 9,
            'k': 10,
            'l': 11,
            'm': 12,
            'n': 13,
            'o': 14,
            'p': 15,
            'q': 16,
            'r': 17,
            's': 18,
            't': 19,
            'u': 20,
            'v': 21,
            'w': 22,
            'x': 23,
            'y': 24,
            'z': 25,
            ' ': 26,
        }

        wordarray.append(converter.get(letters))

    i = 0
    while (i < len(wordarray)):
        wordarray[i] = (wordarray[i] + position + i) % 27
        i += 1

    if (disknr == 1):
        disk1(wordarray,position)
    elif disknr == 2:
        disk2(wordarray, position)
    elif disknr == 3:
        disk3(wordarray,position)
    else:
        print('disk not supported')

    i = 0
    while (i < len(wordarray)):
        wordarray[i] = (wordarray[i] - position - i) % 27
        i += 1

    i=0
    while (i < len(wordarray)):
        converter = {
            0: "a",
            1: "b",
            2: "c",
            3: "d",
            4: "e",
            5: "f",
            6: "g",
            7: "h",
            8: "i",
            9: "j",
            10: "k",
            11: "l",
            12: "m",
            13: "n",
            14: "o",
            15: "p",
            16: "q",
            17: "r",
            18: "s",
            19: "t",
            20: "u",
            21: "v",
            22: "w",
            23: "x",
            24: "y",
            25: "z",
            26: " ",
        }

        outword += converter.get(wordarray[i])

        i += 1



    return outword


def disk1(wordarray, position):




        i = 0
        while (i<len(wordarray)):
            converter = {
                1: 19,
                2: 16,
                3: 22,
                4: 10,
                5: 20,
                6: 9,
                7: 25,
                8: 15,
                9: 6,
                10: 4,
                11: 11,
                12: 24,
                13: 18,
                14: 21,
                15: 8,
                16: 2,
                17: 26,
                18: 13,
                19: 1,
                20: 5,
                21: 14,
                22: 3,
                23: 0,
                24: 12,
                25: 7,
                26: 17,
                0: 23,
            }


            wordarray[i] = converter.get(wordarray[i])
            i+=1





        return wordarray

def disk2(wordarray, position):



    i = 0
    while (i < len(wordarray)):
        converter = {
            1: 3,
            2: 21,
            3: 1,
            4: 19,
            5: 23,
            6: 18,
            7: 12,
            8: 11,
            9: 14,
            10: 22,
            11: 8,
            12: 7,
            13: 24,
            14: 9,
            15: 16,
            16: 15,
            17: 0,
            18: 6,
            19: 4,
            20: 20,
            21: 2,
            22: 10,
            23: 5,
            24: 13,
            25: 26,
            26: 25,
            0: 17,
        }

        wordarray[i] = converter.get(wordarray[i])
        i += 1

    return wordarray

def disk3(wordarray, position):



    i = 0
    while (i < len(wordarray)):
        converter = {
            1: 6,
            2: 26,
            3: 21,
            4: 16,
            5: 9,
            6: 1,
            7: 10,
            8: 0,
            9: 5,
            10: 7,
            11: 25,
            12: 20,
            13: 23,
            14: 19,
            15: 15,
            16: 4,
            17: 18,
            18: 17,
            19: 14,
            20: 12,
            21: 3,
            22: 22,
            23: 13,
            24: 24,
            25: 11,
            26: 2,
            0: 8,
        }

        wordarray[i] = converter.get(wordarray[i])
        i += 1

    return wordarray



if __name__ == '__main__':
    test = disk(disk(disk(disk(disk('ygburtpgsnp', 1),2),3),2),1)
    print(test)

