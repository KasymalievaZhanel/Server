import string
from typing import List, Dict, Optional
from collections import Counter

import ast

TABULA_RECTA = string.ascii_lowercase
NUMBER_OF_DECRYPTIONS = 26


class Cipher:
    slov: Dict[int, List[str]] = {}
    etalon: Dict[str, float] = {}

    def encrypt_caesar(self, text: str, s: int) -> str:
        res = ""
        for char in text:
            if char.lower() not in TABULA_RECTA:
                res += char
            else:
                if char.isupper():
                    res += chr((ord(char) + s - ord('A')) % len(TABULA_RECTA)
                               + ord('A'))
                else:
                    res += chr((ord(char) + s - ord('a')) % len(TABULA_RECTA) +
                               ord('a'))
        return res

    def encrypt_vigenere(self, key: str, text: str) -> str:
        res = ''
        result: List[str] = []
        space = 0
        for index, ch in enumerate(text):
            if ch.lower() not in TABULA_RECTA:
                space += 1
                result.append(ch)
            else:
                mj = TABULA_RECTA.index(ch.lower())
                kj = TABULA_RECTA.index(key[(index - space) % len(key)])
                cj = (mj + kj) % len(TABULA_RECTA)
                if ch.isupper():
                    result.append(TABULA_RECTA[cj].upper())
                else:
                    result.append(TABULA_RECTA[cj])
        return res.join(result)

    def decrypt_caesar(self, text: str, s: int) -> str:
        s = -s
        return self.encrypt_caesar(text, s)


    def dict_of_letter_frequency(self, s: str) -> Dict[str, float]:
        counter = Counter(s)
        length = len(s)
        dict_of_letters = {}
        for symbol in TABULA_RECTA:
            if symbol.isalpha() and length > 0:
                dict_of_letters[symbol] = round(counter[symbol] / length, 5)
        return dict_of_letters

    def hack(self, textc: str, tslov: Dict[str,
             float]) -> Dict[int, Optional[List[str]]]:
        pt = ''
        for i in range(NUMBER_OF_DECRYPTIONS):
            pt = self.decrypt_caesar(textc, i)
            if len(self.slov) == 0:
                self.slov.setdefault(i, []).append(pt)
            elif len(self.slov) > 0:
                 self.slov[i] = pt
        summa: Dict[int, List[float]] = {}
        for key, value in self.slov.items():
            txt_r = str(value).lower()
            perevod = self.dict_of_letter_frequency(txt_r)
            summa.setdefault(key, []).append(self.
                                             sum_of_squares(tslov, perevod))
        min_key = min(summa, key=lambda x: summa[x])
        all_pop = self.slov.get(min_key)
        return all_pop

    def sum_of_squares(self, frequency_text: Dict[str, float],
                       frequency_cipher: Dict[str, float]) -> float:
        sumh: float = 0.0
        for key in frequency_cipher:
            if key in frequency_text:
                sumh += (frequency_text[key] - frequency_cipher[key])**2
        return sumh

    def decrypt_vigenere(self, key: str, text: str) -> str:
        res = ''
        result: List[str] = []
        space = 0
        for index, ch in enumerate(text):
            if ch.lower() not in TABULA_RECTA:
                space += 1
                result.append(ch)
            else:
                cj = TABULA_RECTA.index(ch.lower())
                kj = TABULA_RECTA.index(key[(index - space) % len(key)])
                mj = (cj - kj) % len(TABULA_RECTA)
                if ch.isupper():
                    result.append(TABULA_RECTA[mj].upper())
                else:
                    result.append(TABULA_RECTA[mj])
        return res.join(result)


def main(text):
    with open('train.txt', 'r') as file:
        txt: string = file.read()
    dct: Dict[str, float] = ast.literal_eval(txt)
    a = Cipher()
    result = a.hack(text, dct)
    return (result)
