#code39を貼る
import code37_c5p31098 as code37
import random
#2こめのcodeを貼る
class Drink:
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

    def calc_charge(self,ch_money,ch_id): #投入金額と入力したidからおつりを計算して表示
        self.ch_price = self.listDrink[ch_id-1].get_price()
        c1000,c500,c100,c50,c10,c5,c1 =code37.Charge(self.ch_price,ch_money) #おつりの戻り値（枚数）を変数に保存(いらない気もする)

#自販機クラスを継承したあたり機能つき自販機クラスを作成
class SlotVendingMachine(VendingMachine):
    def slot(self): #0~9の数字をランダムに２個とってきてそろってたらあたり
        x,y = random.randint(0,9),random.randint(0,9)
        print(f'スロットの結果は"{x} {y}"です')
        
        if x==y :
            print(f"おめでとうございます！{x}ゾロであたりです！")
            print("商品がおまけでもう一本もらえます！")
        else:
            print("残念！またチャレンジしてね！")

if __name__ =='__main__':
    x = SlotVendingMachine() #スロット自販機インスタンス作成
    for i in range(3): #３回登録
        id = i + 1 #iは0からなので1からにする
        name = input("商品名を入力してください")
        while True:
            try:
                price = int(input("金額を入力してください"))
                if price<=0: #一応０以下だったらエラーも追記
                    raise ValueError
                break
            except ValueError:
                print("エラーが発生しました")

        x.register_drink(id,name,price)

    x.show_drink_list() #一覧リスト表示

    buy_id = int(input("購入したい飲み物の商品IDを入力してください（1-3の間で入力）"))
    input_money = int(input("お金の投入金額を入力してください"))
    x.calc_charge(input_money,buy_id)
#---ここまで
    x.slot()
