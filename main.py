# Họ và Tên: Nguyễn Đức Hưng
# MSSV: 202418913

"""Menu chạy các kịch bản kiểm thử phần C."""
from kichban import KichBan
def showMenu():
    print("\n===== KIỂM THỬ KỊCH BẢN PHẦN C =====")
    print(" 1. Tạo hai Employee")
    print(" 2. Tạo hai SoftwareEngineer")
    print(" 3. Tăng lương cố định")
    print(" 4. Tăng lương theo phần trăm")
    print(" 5. Tạo nhóm không có trưởng nhóm")
    print(" 6. addMember(employee)")
    print(" 7. addMember(employee, True) - đặt trưởng nhóm")
    print(" 8. Thêm lại thành viên đã tồn tại")
    print(" 9. Hiển thị danh sách (đa hình)")
    print("10. Tổng chi phí hằng tháng")
    print("11. Thử xóa trưởng nhóm")
    print("12. Đổi trưởng nhóm rồi xóa trưởng nhóm cũ")
    print("13. Tạo nhóm thứ hai và hủy khi kết thúc khối lệnh (kịch bản 13-14)")
    print("15. Nhân sự vẫn tồn tại sau khi nhóm bị hủy")
    print(" A. Chạy toàn bộ kịch bản")
    print(" 0. Thoát")
def main():
    kichBan = KichBan()
    nextStep = 1  # các kịch bản dùng chung dữ liệu nên phải chạy đúng thứ tự
    while True:
        showMenu()
        choice = input("Chọn: ").strip().upper()

        if choice.isdigit() and choice != "0" and int(choice) != nextStep:
            if nextStep > 15:
                print("Đã chạy xong tất cả kịch bản.")
            else:
                print(f"Hãy chạy kịch bản {nextStep} trước.")
            continue
        if choice == "1":
            kichBan.step1()
        elif choice == "2":
            kichBan.step2()
        elif choice == "3":
            kichBan.step3()
        elif choice == "4":
            kichBan.step4()
        elif choice == "5":
            kichBan.step5()
        elif choice == "6":
            kichBan.step6()
        elif choice == "7":
            kichBan.step7()
        elif choice == "8":
            kichBan.step8()
        elif choice == "9":
            kichBan.step9()
        elif choice == "10":
            kichBan.step10()
        elif choice == "11":
            kichBan.step11()
        elif choice == "12":
            kichBan.step12()
        elif choice == "13":
            kichBan.step13to14()
            nextStep = 14  # kịch bản 13 đã gồm kịch bản 14
        elif choice == "15":
            kichBan.step15()
        elif choice == "A":
            KichBan().runAll()  # dùng dữ liệu mới, không ảnh hưởng tiến độ chạy từng kịch bản
            continue
        elif choice == "0":
            break
        else:
            print("Lựa chọn không hợp lệ.")
            continue

        nextStep += 1


if __name__ == "__main__":
    main()
