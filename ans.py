import cubed

a = input("1辺の長さを入力してください：")
try:
    a = int(a)
    cubed.cubed(a)
except (ValueError, TypeError):
    print("数値を入力してください。")


