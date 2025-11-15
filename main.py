class Mahsulot:
    def yetkazib_berish_narxi(self, shahar):
        raise NotImplementedError

    def chegirma_qollash(self, foydalanuvchi):
        raise NotImplementedError

    def kafolat_muddati(self):
        return None


class Elektronika(Mahsulot):
    def __init__(self, nom, narx, yetkazish, chegirma, kafolat):
        self.nom = nom
        self.narx = narx
        self.yetkazish = yetkazish
        self.chegirma = chegirma
        self.kafolat = kafolat

    def yetkazib_berish_narxi(self, shahar):
        return self.yetkazish.get(shahar, 20000)

    def chegirma_qollash(self, foydalanuvchi):
        if foydalanuvchi == "premium":
            return self.narx * (1 - self.chegirma)
        return self.narx

    def kafolat_muddati(self):
        return self.kafolat


class Kiyim(Mahsulot):
    def __init__(self, nom, narx, yetkazish, chegirma):
        self.nom = nom
        self.narx = narx
        self.yetkazish = yetkazish
        self.chegirma = chegirma

    def yetkazib_berish_narxi(self, shahar):
        return self.yetkazish.get(shahar, 15000)

    def chegirma_qollash(self, foydalanuvchi):
        if foydalanuvchi == "premium":
            return self.narx * (1 - self.chegirma)
        return self.narx


class Kitob(Mahsulot):
    def __init__(self, nom, narx, yetkazish):
        self.nom = nom
        self.narx = narx
        self.yetkazish = yetkazish

    def yetkazib_berish_narxi(self, shahar):
        return self.yetkazish.get(shahar, 10000)

    def chegirma_qollash(self, foydalanuvchi):
        if foydalanuvchi == "premium":
            return self.narx * 0.95
        return self.narx


savat = [
    Elektronika("Telefon", 3000000, {"Toshkent": 10000}, 0.1, "12 oy"),
    Kiyim("Kurtka", 500000, {"Toshkent": 8000}, 0.2),
    Kitob("Python darsi", 120000, {"Toshkent": 5000})
]

foydalanuvchi = "premium"
shahar = "Toshkent"

umumiy_yetkazish = 0
umumiy_chegirmadan_keyin = 0

for m in savat:
    umumiy_yetkazish += m.yetkazib_berish_narxi(shahar)
    umumiy_chegirmadan_keyin += m.chegirma_qollash(foydalanuvchi)

print(umumiy_yetkazish)
print(umumiy_chegirmadan_keyin)
print(savat[0].kafolat_muddati())
print(savat[1].kafolat_muddati())
