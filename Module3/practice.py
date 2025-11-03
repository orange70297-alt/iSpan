# 終極密碼 讓使用者能夠重複猜數字，直到猜對為止
ans = 25
while True:
# 告訴使用者需要輸入的數字範圍 input()
    try:
        user_input = int(input ("請輸入數字1~100: "))
    except Exception as e:
        print("請輸入數字")
        continue
# 超出範圍要顯示「超出範圍請重新輸入」
    if user_input <1 or user_input >100:
        print("超出範圍請重新輸入")
# 數字太大 要提示「請輸入更小的數字」
    elif user_input > ans:
        print("請輸入更小的數字")
# 數字太小 要提示「請輸入更大的數字」
    elif user_input < ans:
        print("請輸入更大的數字")
# 使用者猜對要回傳「恭喜中獎」
    elif user_input == ans:
        print("恭喜中獎")
        break
    




    

















