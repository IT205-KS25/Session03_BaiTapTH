while True:
    employee_amount = int(input("\nNhập số lượng nhân viên: "))
    for count in range(1,employee_amount+1):
        print("\nNhân viên", count)
        employee_name = input("Tên nhân viên: ")
        work_day = int(input("Số ngày đi làm: "))
        print("Thông tin nhân viên: ")
        print(f"Tên: {employee_name}")
        print(f"Số ngày đi làm: {work_day}")
        if work_day < 20:
            print("Cần cải thiện chuyên cần")
        else:
            print("Nhân viên chuyên cần tốt")            

    continue_process = input("\nTiếp tục chương trình? (y/n): ")
    if continue_process.strip() == "y":
        continue
    elif continue_process.strip() == "n":
        print("Chương trình kết thúc")
        break
    else:
        print("Lựa chọn không hợp lệ!")
