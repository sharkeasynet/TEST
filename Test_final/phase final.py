def la_nam_nhuan(nam):
    """Kiểm tra năm nhuận"""
    return (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0)

def kiem_tra_ngay(d, m, y):
    """Kiểm tra tính hợp lệ của ngày/tháng/năm"""
    if y < 1900 or m < 1 or m > 12 or d < 1:
        return False

    if m in [1, 3, 5, 7, 8, 10, 12]:
        max_day = 31
    elif m in [4, 6, 9, 11]:
        max_day = 30
    elif m == 2:
        if la_nam_nhuan(y):
            max_day = 29
        else:
            max_day = 28
    else:
        return False

    return d <= max_day

date_str = input("Nhập ngày theo định dạng dd/mm/yyyy: ")

try:
    d, m, y = map(int, date_str.split("/"))
    if kiem_tra_ngay(d, m, y):
        print(f"Ngày {date_str} hợp lệ")
    else:
        print(f"Ngày {date_str} không hợp lệ")
except:
    print("Định dạng nhập sai! Hãy nhập theo dạng dd/mm/yyyy")
