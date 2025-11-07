def get_discount(total,discount):
    if total>=2000:
        total -= discount* (total//2000)
    return total

# print(__name__)

# 測試模組
if __name__ == "__main__":
    data = [
        {
            "total": 6000 ,
            "discount": 200
        },

        {   
            "total": 8000,
            "discount": 200
        }
]

    for d in data:
        answer = get_discount(d["total"], d["discount"])
        print(f"折扣後的金額: {answer} 元") 
