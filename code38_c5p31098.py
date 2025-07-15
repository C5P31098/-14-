class Drink():
    def __init__(self,id,name,price):
        self.id = id
        self.name = name
        self.price = price

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

class VendingMachine:
    def __init__(self):
        self.listDrink = []

    def register_drink(self,id1,name1,price1): #飲み物登録メソッド。呼び出されたらid名前金額をlistDrinkにインスタンスごとに追加するぞ
        In = Drink(id1,name1,price1) #In（飲み物インスタンス）をリストlistDrinkに追加
        self.listDrink.append(In)

    def show_drink_list(self): #飲み物一覧表示メソッド
        print("【飲み物の一覧リスト】")
        for In in self.listDrink:
            print(f"商品ID{In.get_id()} {In.get_name()} : {In.get_price()}円")


if __name__ =='__main__':
    x = VendingMachine() #自販機インスタンス作成
    for i in range(3): #３回登録
        id = i + 1 #iは0からなので1からにする
        name = input("商品名を入力してください")
        price = int(input("金額を入力してください"))
        x.register_drink(id,name,price)

    x.show_drink_list()