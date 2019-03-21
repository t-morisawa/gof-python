from human_letter import HumanLetter


class HumanLetterFactory():
    _unique_instance = None
    _map = {}

    def __new__(cls):
        raise NotImplementedError('Cannot initialize via Constructor')

    @classmethod
    def __internal_new__(cls):
        return super().__new__(cls)

    @classmethod
    def get_instance(cls):
        if not cls._unique_instance:
            cls._unique_instance = cls.__internal_new__()

        return cls._unique_instance

    """
    人文字を取得するメソッド。
    すでに持っているものであれば、map から返す。
    map に持っていないものは生成して map への登録を行った後に返り値として返す。

    @param letter
    @return humanLetter
    """
    def getHumanLetter(self, letter):
        humanLetter = self._map.get(letter)
        if humanLetter is None:
            humanLetter = HumanLetter(letter)
            self._map[letter] = humanLetter

        return humanLetter
