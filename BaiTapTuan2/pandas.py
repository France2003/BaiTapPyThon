import pandas as pd
my_data = {
    "Tên" : ['Pháp', 'Huy', 'Nhân', 'Hóa', 'Đạt', 'Quyền', 'Nhi', 'Diện', 'Anh', 'Bảo'],
    "Tuổi": [21, 22, 23, 24, 25, 26, 27, 21, 20, 19],
    "Giới tính": ['Nam', 'Nam', 'Nam', 'Nam', 'Nam', 'Nam', 'Nữ', 'Nữ', 'Nam', 'Nam'],
    "Điểm tổng kết": [8.5, 4.0, 8.2, 3.4, 8.0, 4.5, 3.2, 2.8, 5.5, 7.0]
}
df_students = pd.DataFrame(my_data)
# Toàn bộ dữ liệu của bảng
print("* Toàn bộ dữ liệu của bảng")
print(df_students)
print("")
# 3 dòng đầu tiên
print("* 3 dòng đầu tiên")
print(df_students.head(3))
print("")
# Theo index=2 và cột Name
index_name = df_students.loc[2, "Tên"]
print("* Theo index=2 và cột Tên: ",index_name)
print("")
# Theo index=10 và cột Age
if 10 in df_students.index:
    print("* Theo index=10 và cột Tuổi: ", df_students.loc[10, "Tuổi"])
else:
    print("* Theo index=10 không tồn tại")
print("")
# Các cột Name và Score
print("* Các cột Tên và Điểm tổng kết")
print(df_students[["Tên","Điểm tổng kết"]])
print("")
# Thêm một cột tên Pass với giá trị True nếu giá trị cột Score >= 5, ngược lại là False.
print("* Thêm cột Pass")
df_students["Pass"] = df_students['Điểm tổng kết'] >= 5
print(df_students)
print("")
# Sắp xếp danh sách sinh viên theo điểm Score giảm dần.
print("* Danh sách sinh viên theo điểm tổng kết giảm dần")
df_descending = df_students.sort_values("Điểm tổng kết", ascending=False)
print(df_descending)



