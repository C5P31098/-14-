def oturi(price,money):
    change=money-price

    print("おつりは",change,"円です。")
                

    change_1000 = change//1000      # 1000札の枚数
    change = change%1000
    change_500 = change//500         # 500円玉の枚数
    change = change%500
    change_100 = change//100        # 100玉の枚数
    change = change%100
    change_50 = change//50           # 50円玉の枚数
    change = change%50
    change_10 = change//10           # 10円玉の枚数
    change = change%10
    change_5 = change//5              # 5円玉の枚数
    change = change%5
    change_1 = change//1             # 1円玉の枚数

    print("1000円札は",change_1000,"枚です。")
    print("500円玉は",change_500,"枚です。")
    print("100円玉は",change_100,"枚です。")
    print("50円玉は",change_50,"枚です。")
    print("10円玉は",change_10,"枚です。")
    print("5円玉は",change_5,"枚です。")
    print("1円玉は",change_1,"枚です。")

if __name__ =='__main__':
    a1 = int(input("商品の値段を入力してください[円]:"))
    b1 = int(input("預かった金額を入力してください[円]:"))
    x = oturi(a1,b1)