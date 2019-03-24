class Beaker():
    ADD_SALT = 1
    ADD_WATER = 2
    SALINE_SOLUBILITY = 26.4 # 食塩水の溶解度[%]

    def __init__(self, water, salt):
        self.water = water
        self.salt = salt
        self.melted = False
        self.mix()

    def experiment(self, param):
        if (param == Beaker.ADD_SALT):
            while self.is_melted():
                self.add_salt(1)
                self.mix()

        if (param == Beaker.ADD_WATER):
            while not self.is_melted:
                self.add_water(10)
                self.mix()

        print('食塩を1gずつ加える実験')
        self.note()
            
    def add_salt(self, salt):
        self.salt + salt

    def add_water(self, water):
        self.water + water

    def mix(self):
        # 溶解度以上に食塩が含まれる場合は溶けきらない
        self.melted = self.salt / (self.salt + self.water) * 100 < Beaker.SALINE_SOLUBILITY

    def get_salt(self):
        return self.salt

    def get_water(self):
        return self.water

    def is_melted(self):
        return self.melted

    def note(self):
        print('水: ' + self.water + 'g')
        print('食塩: ' + self.salt + 'g')
        print('濃度: ' + (self.salt / (self.water + self.salt)) * 100 + '%')
