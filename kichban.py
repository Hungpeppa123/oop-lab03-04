# Họ và Tên: Nguyễn Đức Hưng
# MSSV: 202418913

"""Kiểm thử theo kịch bản phần C.
Mỗi kịch bản là một phương thức của KichBan. Các kịch bản dùng chung dữ liệu
(lưu trong self.e1, self.e2, self.team1...) nên phải chạy theo thứ tự.
"""
from models import Employee, SoftwareEngineer, ProjectTeam
class KichBan:
    def __init__(self):
        self.e1 = self.e2 = self.se1 = self.se2 = self.team1 = None
    def step1(self):
        print("\n--- Kịch bản 1: Tạo hai Employee bằng hai constructor khác nhau ---")
        self.e1 = Employee()
        self.e2 = Employee("E02", "Tran Thi B", 12_000_000)
        self.e1.displayInfo()
        self.e2.displayInfo()
    def step2(self):
        print("\n--- Kịch bản 2: Tạo hai SoftwareEngineer bằng hai constructor khác nhau ---")
        self.se1 = SoftwareEngineer("S01", "Le Van C", "Python")
        self.se2 = SoftwareEngineer("S02", "Pham Thi D", 20_000_000, "C++", 3_000_000)
        self.se1.displayInfo()
        self.se2.displayInfo()
    def step3(self):
        print("\n--- Kịch bản 3: Tăng lương E02 bằng số tiền cố định (+1.000.000) ---")
        self.e2.increaseSalary(1_000_000)
        self.e2.displayInfo()
    def step4(self):
        print("\n--- Kịch bản 4: Tăng lương S02 theo phần trăm (+10%) ---")
        self.se2.increaseSalary(10, True)
        self.se2.displayInfo()
    def step5(self):
        print("\n--- Kịch bản 5: Tạo nhóm dự án không có trưởng nhóm ---")
        self.team1 = ProjectTeam("P01", "Web Portal")
        self.team1.displayTeam()
    def step6(self):
        print("\n--- Kịch bản 6: Thêm nhân sự bằng addMember(employee) ---")
        print("Thêm E02:", self.team1.addMember(self.e2))
    def step7(self):
        print("\n--- Kịch bản 7: Thêm kỹ sư bằng addMember(employee, True) làm trưởng nhóm ---")
        print("Thêm S02 làm trưởng nhóm:", self.team1.addMember(self.se2, True))
        print("Thêm S01:", self.team1.addMember(self.se1))
    def step8(self):
        print("\n--- Kịch bản 8: Thử thêm lại một thành viên đã tồn tại ---")
        print("Thêm lại E02:", self.team1.addMember(self.e2))
    def step9(self):
        print("\n--- Kịch bản 9: Hiển thị danh sách bằng lời gọi đa hình ---")
        self.team1.displayTeam()
    def step10(self):
        print("\n--- Kịch bản 10: Tính tổng chi phí nhân sự hằng tháng ---")
        print(f"Tổng: {self.team1.calculateTotalMonthlyCost():,.0f}")
    def step11(self):
        print("\n--- Kịch bản 11: Thử xóa trưởng nhóm hiện tại (phải bị từ chối) ---")
        print("Xóa S02 (trưởng nhóm):", self.team1.removeMember("S02"))
    def step12(self):
        print("\n--- Kịch bản 12: Đổi trưởng nhóm rồi xóa người từng là trưởng nhóm ---")
        print("Đổi trưởng nhóm sang E02:", self.team1.changeLeader(self.e2))
        print("Xóa S02:", self.team1.removeMember("S02"))
        self.team1.displayTeam()
    def step13to14(self):
        print("\n--- Kịch bản 13: Tạo nhóm thứ hai, thêm nhân sự đã có ở nhóm 1 ---")
        # Khối lệnh cục bộ: team2 chỉ tồn tại trong hàm này
        def localBlock():
            team2 = ProjectTeam("P02", "Mobile App")
            print("Thêm E02 (đã ở nhóm P01):", team2.addMember(self.e2))
            print("Thêm UNKNOWN làm trưởng nhóm:", team2.addMember(self.e1, True))
            team2.displayTeam()
            print("E02 đồng thời thuộc P01:", self.team1.contains("E02"))
            print("\n--- Kịch bản 14: Kết thúc khối lệnh cục bộ -> hủy nhóm thứ hai ---")
        localBlock()
    def step15(self):
        print("\n--- Kịch bản 15: Nhân sự của nhóm thứ hai vẫn tồn tại sau khi nhóm bị hủy ---")
        self.e2.displayInfo()
        self.e1.displayInfo()
        print("E02 vẫn trong nhóm P01:", self.team1.contains("E02"))
    def runAll(self):
        self.step1()
        self.step2()
        self.step3()
        self.step4()
        self.step5()
        self.step6()
        self.step7()
        self.step8()
        self.step9()
        self.step10()
        self.step11()
        self.step12()
        self.step13to14()
        self.step15()

