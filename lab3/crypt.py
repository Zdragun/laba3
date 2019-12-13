import string


class Crypt(object):
    alphabet = string.ascii_lowercase

    def __init__(self, n):
        self.n = n

    def crypt(self, text):
        crypted_list = []
        for letter in text:
            if letter == " ":
                crypted_list.append(" ")
            elif letter == "!":
                crypted_list.append("!")
            elif letter == ".":
                crypted_list.append(".")
            elif letter == ",":
                crypted_list.append(",")
            elif letter == "?":
                crypted_list.append("?")
            elif letter == ":":
                crypted_list.append(":")
            else:
                crypted_list.append(self.alphabet[self.alphabet.index(letter.lower()) + self.n])
        return ''.join(map(str, crypted_list))

    def encrypt(self, text):
        crypted_list = []
        for letter in text:
            if letter == " ":
                crypted_list.append(" ")
            elif letter == "!":
                crypted_list.append("!")
            elif letter == ".":
                crypted_list.append(".")
            elif letter == ",":
                crypted_list.append(",")
            elif letter == "?":
                crypted_list.append("?")
            elif letter == ":":
                crypted_list.append(":")
            else:
                crypted_list.append(self.alphabet[self.alphabet.index(
                    letter.lower()) - self.n])
        return ''.join(map(str, crypted_list))
