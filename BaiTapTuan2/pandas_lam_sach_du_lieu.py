import pandas as pd
input_my_dict = {
    "ID": [101, 102, 103, 104, 105, 106],
    "Name": ['An', 'Bình', 'Cường', 'Dương', None, 'Hạnh'],
    "Age": [25, None, 30, 22, 28, 35],
    "Department": ['HR', 'IT', 'IT', 'Finance', 'HR', None],
    "Salary": [700, 800, 750, None, 710, 770]
}
input_department_dict = {
    'Department': ['HR', 'IT', 'Finance', 'Marketing'],
    'Manager': ['Trang', 'Khoa', 'Minh', 'Lan']
}
df_staff = pd.DataFrame(input_my_dict)
df_department = pd.DataFrame(input_department_dict)
print("* Toàn bộ dữ liệu của bảng")
print(df_staff)
print("")
# 1. Kiểm tra các ô dữ liệu bị thiếu trong bảng Nhân viên.
print("1. Các ô dữ liệu bị thiếu trong bảng Nhân viên")
print(df_staff.isnull())
print("")
# Xoá các dòng trong bảng Nhân viên nếu dòng đó có hơn 2 giá trị bị thiếu.
print("2. Các dòng đã bị xóa trong bảng Nhân viên ")
print(df_staff.dropna(thresh =3))
print("")
# Điền giá trị cho các ô bị thiếu:
# Name: thay bằng "Chưa rõ".
print("3.1 Name thay bằng chưa rõ")
new_name = {
    "Name": 'Chưa rõ'
}
df_new_name = df_staff.fillna(value=new_name)
print(df_new_name)
print("")
# Age: thay bằng giá trị trung bình của cột Age.
print("3.2 Thay Age bằng giá trị trung bình của cột Age")
new_age = df_staff["Age"].mean()
df_staff["Age"] = df_staff["Age"].fillna(new_age)
print(df_staff)
print("")
# Salary: thay bằng giá trị nằm trước đó của ô bị thiếu của cột Salary.
print("3.3 Salary: thay bằng giá trị nằm trước đó của ô bị thiếu của cột Salary.")
new_salary = df_staff["Salary"].ffill()
df_staff["Salary"]=df_staff["Salary"].fillna(new_salary)
print(df_staff)
print("")
# Department: thay bằng "Unknown".
print("3.4 Department: thay bằng Unknown")
new_department = {
    "Department": 'Unknown',
}
df_new_department = df_staff.fillna(value=new_department)
print(df_new_department)
print("")
# Chuyển kiểu dữ liệu của Age và Salary sang int.
print("4. Chuyển kiểu dữ liệu của Age và Salary sang int")
df_staff["Age"]=df_staff["Age"].astype(int)
df_staff["Salary"]=df_staff["Salary"].astype(int)
print(df_staff)
print("")
# Tạo cột mới Salary_after_tax: giá trị sẽ là cột Salary -10% thuế
print("5. Tạo cột mới Salary_after_tax: giá trị sẽ là cột Salary -10% thuế")
df_staff["Salary_after_tax"] = df_staff["Salary"]* 0.9
print(df_staff)
print("")
# Lọc ra các nhân viên thuộc phòng IT và có tuổi lớn hơn 25.
print("6. Lọc ra các nhân viên thuộc phòng IT và có tuổi lớn hơn 25.")
df_filter = df_staff[(df_staff["Department"] == "IT") & (df_staff["Age"] > 25)]
print(df_filter)
print("")
# Sắp xếp bảng nhân viên theo Salary_after_tax giảm dần.
print("7. Sắp xếp bảng nhân viên theo Salary_after_tax giảm dần.")
df_descending = df_staff.sort_values("Salary_after_tax", ascending=False)
print(df_descending)
print("")
# Nhóm nhân viên theo Department và tính mức lương trung bình cho từng phòng ban.
print("8. Nhóm nhân viên theo Department và tính mức lương trung bình cho từng phòng ban.")
df_group_by = df_staff.groupby(["Department"])["Salary"].mean()
print(df_group_by)
print("")
# Dùng merge() để nối bảng nhân viên với bảng quản lý phòng ban theo cột Department để biết ai là Manager của từng nhân viên.
print("9. Dùng merge() để nối bảng nhân viên với bảng quản lý phòng ban theo cột Department để biết ai là Manager của từng nhân viên")
df_merger = df_staff.merge(df_department, left_on="Department", right_on="Department")
print(df_merger)
print("")
# Tạo bảng Nhân viên Mới gồm 2 nhân viên mới và dùng concat() để thêm họ vào bảng Nhân viên
print("10. Tạo bảng Nhân viên Mới gồm 2 nhân viên mới và dùng concat() để thêm họ vào bảng Nhân viên")
my_new_staff_dict = {
    "ID": [107, 108],
    "Name": ['Pháp', 'Huy'],
    "Age": [21, 22],
    "Department": ['HR', 'IT'],
    "Salary": [1000, 900]
}
df_new_staff = pd.DataFrame(my_new_staff_dict)
df_new_staff["Salary_after_tax"] = df_new_staff["Salary"]* 0.9
df_concat_staff = pd.concat([df_staff, df_new_staff],  ignore_index = True).merge(df_department, on="Department")
print(df_concat_staff)

