from human_letter_factory import HumanLetterFactory


def takeAPhoto(letter):
    print(letter.getLetter())


if __name__ == '__main__':
    factory = HumanLetterFactory.get_instance()
    あ = factory.getHumanLetter("あ")
    takeAPhoto(あ)
    い = factory.getHumanLetter("い")
    takeAPhoto(い)
    は = factory.getHumanLetter("は")
    takeAPhoto(は)
    あ2 = factory.getHumanLetter("あ")
    takeAPhoto(あ2)
    い2 = factory.getHumanLetter("い")
    takeAPhoto(い2)
    よ = factory.getHumanLetter("よ")
    takeAPhoto(よ)
    り = factory.getHumanLetter("り")
    takeAPhoto(り)
    も = factory.getHumanLetter("も")
    takeAPhoto(も)
    あ3 = factory.getHumanLetter("あ")
    takeAPhoto(あ3)
    お = factory.getHumanLetter("お")
    takeAPhoto(お)
    い3 = factory.getHumanLetter("い")
    takeAPhoto(い3)
