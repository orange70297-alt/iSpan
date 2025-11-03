# 如果不小心進入無窮迴圈 用 Ctrl + C 強制結束程式執行
answer = 25
user_input = '0'
# 終極密碼 讓使用者能夠重複猜數字，直到猜對為止
while answer != user_input:
# 告訴使用者需要輸入的數字範圍 input()
    user_input = int(input('請輸入1~100的數字: '))
    # 超出範圍要顯示「超出範圍請重新輸入」
    if user_input < 1 or user_input > 100:
        print("超出範圍請重新輸入")

    # 數字太大 要提示「請輸入更小的數字」
    elif user_input > answer:
        print("請輸入更小的數字")

    # 數字太小 要提示「請輸入更大的數字」
    elif user_input < answer:
        print("請輸入更大的數字")

print("恭喜中獎")
