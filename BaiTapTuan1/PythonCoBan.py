from random import choice
def Bai1():
    text = input("Nhập chuỗi: ")
    words = text.split()
    new_texts = []
    for word in words:
        new_text = word.capitalize()
        new_texts.append(new_text)
    result = " ".join(new_texts)
    print(" Kết quả: ", result)
def Bai2():
    text = input("Nhập chuỗi: ")
    words = text.split()
    new_text_reversed = []
    i = len(words) - 1
    while i >= 0:
        new_text_reversed.append(words[i])
        i -= 1
    result = " ".join(new_text_reversed)
    print(" Kết quả: ", result)
def Bai3():
    text = input("Nhập chuỗi: ")
    max_char = ''
    max_count = 0
    for char in text:
        count = 0
        for char2 in text:
            if char2 == char:
                count += 1
        if count > max_count:
            max_char = char
            max_count = count
    print("Ký tự xuất hiện nhiều nhất ",max_char , "với ",max_count, "lần")
def Bai4():
    text = input("Nhập chuỗi: ")
    text_count= []
    for char in text:
        if char in text_count:
            continue
        count = 0
        for char2 in text:
            if char2 == char:
                count += 1
        text_count.append(char)
        print("Ký tự ",char, "xuất hiện ",count, "lần")
def Bai5():
    def tach_so(num):
        numbers = []
        for char in num:
            if char.isdigit():
                numbers.append(char)
        if numbers:
            return  numbers
        else:
            return  []
    text = input("Nhập chuỗi: ")
    list_number = tach_so(text)
    if list_number:
        print("Danh sách số có trong chuỗi", list_number)
    else:
        print("Không có ký tự số")
def Bai6():
    def tach_ho_ten(full_name):
        name = full_name.strip().split()
        if len(name) == 0:
            return "",""
        elif len(name) == 1:
            return "",name[0]
        else:
            ho_lot = " ".join(name[:-1])
            names = name[-1]
            return ho_lot, names
    ho_va_ten = input("Nhập chuỗi: ")
    ho_va_lot, ten = tach_ho_ten(ho_va_ten)
    print("Họ và tên lót: ", ho_va_lot)
    print("Tên: ",ten)
def Bai7():
    text = input("Nhập chuỗi: ")
    words = text.split()
    new_texts = []
    for word in words:
        new_text = word.capitalize()
        new_texts.append(new_text)
    result = " ".join(new_texts)
    print("Kết quả sau khi chuyển: ", result)
def Bai8():
    text = input("Nhập chuỗi: ")
    result = ""
    for i in range(len(text)):
        char = text[i]
        if i % 2 == 0:
            result += char.upper()
        else:
            result += char.lower()
    print("Kết quả xen kẽ: ", result)
def Bai9():
    text = input("Nhập chuỗi: ")
    is_palindrome = True
    for i in range(len(text) // 2):
        if text[i] != text[len(text) - 1 - i]:
            is_palindrome = False
            break
    result = text
    if is_palindrome:
        print(result, "là chuỗi đối xứng ")
    else:
        print(result, "không phải là chuối đối xứng")
def Bai10():
    def dem_chu_so(number):
        chu_so = [" không ", " một ", " hai ", " ba ", " bốn ", " năm ", " sáu ", " bảy ", " tám ", " chín "]
        tram = number // 100
        chuc = number % 100 // 10
        donvi = number % 10
        result = ""
        result += chu_so[tram] + " trăm "
        if chuc == 0:
            if donvi != 0:
                result += " lẻ " + chu_so[donvi]
        elif chuc == 1:
            result += " mười "
            if donvi == 5 :
                result += " lăm "
            elif donvi != 0:
                result += chu_so[donvi]
        else:
            result += chu_so[chuc] +  " mươi "
            if donvi == 1 :
                result += " mốt "
            elif donvi == 4:
                result += " tư "
            elif donvi == 5:
                result += " lăm "
            elif donvi != 0:
                result += chu_so[donvi]
        return result
    num = int(input("Nhập số có ba chữ số: "))
    if 100 <= num <= 999:
        print("Kết quả : ",dem_chu_so(num))
    else:
        print("Vui lòng nhập số có ba chữ ố")
def Menu():
    while True:
        print("\n--- MENU ---")
        print("1. Viết chương trình đổi các từ ở đầu câu sang chữ hoa và những từ không phải đầu câu sang chữ thường")
        print("2. Viết chương trình đảo ngược thứ tự các từ có trong chuỗi")
        print("3. Viết chương trình tìm kiếm ký tự xuất hiện nhiều nhất trong chuỗi")
        print("4. Viết chương trình nhập một chuỗi bất kỳ, liệt kê số lần xuất hiện của mỗi ký tự")
        print("5. Viết hàm kiểm tra xem trong chuỗi có ký tự số hay không. Nếu có, tách các số đó ra thành một mảng riêng")
        print("6. Viết hàm cắt chuỗi họ tên thành chuỗi họ lót và chuỗi tên")
        print("7. Viết chương trình chuyển ký tự đầu tiên của mỗi từ trong chuỗi thành chữ in hoa")
        print("8. Viết chương trình đổi chữ xen kẽ: một chữ hoa và một chữ thường")
        print("9. Viết chương trình nhập vào một chuỗi ký tự, kiểm tra xem chuỗi đó có đối xứng không")
        print("10. Viết chương trình nhập vào một số có 3 chữ số, xuất ra dòng chữ mô tả giá trị con số đó")
        print("0. Thoát")
        choice = input("Chọn bài (0 - 10): ")
        if choice == '1':
            Bai1()
            break
        elif choice == '2':
            Bai2()
            break
        elif choice == '3':
            Bai3()
            break
        elif choice == '4':
            Bai4()
            break
        elif choice == '5':
            Bai5()
            break
        elif choice == '6':
            Bai6()
            break
        elif choice == '7':
            Bai7()
            break
        elif choice == '8':
            Bai8()
            break
        elif choice == '9':
            Bai9()
            break
        elif choice == '10':
            Bai10()
            break
        elif choice == '0':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại.")
Menu()