# Họ và Tên: Nguyễn Đức Hưng
# MSSV: 202418913

"""Mô hình Nhóm dự án và Nhân sự (Lab 03-04: Overloading).
Python không hỗ trợ nạp chồng (overloading) như C++, nên:
- Nạp chồng constructor được mô phỏng bằng *args + kiểm tra số lượng tham số.
- Nạp chồng phương thức được mô phỏng bằng tham số mặc định.
- Destructor được mô phỏng bằng __del__.
Dữ liệu đầu vào được kiểm tra trong setter của property.
"""
from numbers import Real

class Employee:
    """Nhân sự thông thường. Tồn tại độc lập với dự án."""
    DEFAULT_ID = "UNKNOWN"
    DEFAULT_NAME = "Unnamed employee"
    def __init__(self, *args):
        # Employee()
        # Employee(id, fullName)
        # Employee(id, fullName, baseSalary)
        if len(args) == 0:
            id, fullName, baseSalary = self.DEFAULT_ID, self.DEFAULT_NAME, 0
        elif len(args) == 2:
            id, fullName = args
            baseSalary = 0
        elif len(args) == 3:
            id, fullName, baseSalary = args
        else:
            raise TypeError("Employee nhận 0, 2 hoặc 3 tham số")
        # Gán qua property -> setter tự kiểm tra
        self.id = id
        self.fullName = fullName
        self.baseSalary = baseSalary
        # Giống C++: chỉ gọi destructor cho đối tượng đã khởi tạo thành công
        self._constructed = True
    # ----- Property -----
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Mã nhân sự không được rỗng")
        self._id = value.strip()
    @property
    def fullName(self):
        return self._fullName
    @fullName.setter
    def fullName(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Họ tên không được rỗng")
        self._fullName = value.strip()
    @property
    def baseSalary(self):
        return self._baseSalary
    @baseSalary.setter
    def baseSalary(self, value):
        if isinstance(value, bool) or not isinstance(value, Real):
            raise TypeError("Lương cơ bản phải là số")
        if value < 0:
            raise ValueError("Lương cơ bản không được âm")
        self._baseSalary = float(value)
    # ----- Nạp chồng increaseSalary -----
    # increaseSalary(amount)              -> tăng số tiền cố định
    # increaseSalary(value, byPercentage) -> True: theo %, False: số tiền cố định
    def increaseSalary(self, value, byPercentage=False):
        if isinstance(value, bool) or not isinstance(value, Real):
            raise TypeError("Giá trị tăng phải là số")
        if value <= 0:
            raise ValueError("Giá trị tăng phải dương")
        if byPercentage:
            self.baseSalary += self.baseSalary * value / 100
        else:
            self.baseSalary += value
    # ----- Phương thức "virtual" -----
    def calculateMonthlyCost(self):
        return self.baseSalary

    def displayInfo(self):
        print(f"[Employee] {self.id} | {self.fullName} | "
              f"Lương: {self.baseSalary:,.0f} | "
              f"Chi phí/tháng: {self.calculateMonthlyCost():,.0f}")
    def __del__(self):
        if getattr(self, "_constructed", False):
            print(f"~Employee(): hủy nhân sự {self._id}")
class SoftwareEngineer(Employee):
    """Kỹ sư phần mềm: có thêm ngôn ngữ chính và phụ cấp kỹ thuật."""
    def __init__(self, *args):
        # SoftwareEngineer(id, fullName, primaryLanguage)
        # SoftwareEngineer(id, fullName, baseSalary, primaryLanguage, technicalAllowance)
        if len(args) == 3:
            id, fullName, primaryLanguage = args
            baseSalary, technicalAllowance = 0, 0
        elif len(args) == 5:
            id, fullName, baseSalary, primaryLanguage, technicalAllowance = args
        else:
            raise TypeError("SoftwareEngineer nhận 3 hoặc 5 tham số")

        # Kiểm tra thuộc tính riêng trước, để lỗi xảy ra khi đối tượng chưa "khởi tạo xong"
        self.primaryLanguage = primaryLanguage
        self.technicalAllowance = technicalAllowance
        super().__init__(id, fullName, baseSalary)
    # ----- Property -----
    @property
    def primaryLanguage(self):
        return self._primaryLanguage
    @primaryLanguage.setter
    def primaryLanguage(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Ngôn ngữ chính không được rỗng")
        self._primaryLanguage = value.strip()
    @property
    def technicalAllowance(self):
        return self._technicalAllowance
    @technicalAllowance.setter
    def technicalAllowance(self, value):
        if isinstance(value, bool) or not isinstance(value, Real):
            raise TypeError("Phụ cấp phải là số")
        if value < 0:
            raise ValueError("Phụ cấp không được âm")
        self._technicalAllowance = float(value)
    def calculateMonthlyCost(self):
        return self.baseSalary + self.technicalAllowance
    def displayInfo(self):
        print(f"[SoftwareEngineer] {self.id} | {self.fullName} | "
              f"Lương: {self.baseSalary:,.0f} | "
              f"Ngôn ngữ: {self.primaryLanguage} | "
              f"Phụ cấp: {self.technicalAllowance:,.0f} | "
              f"Chi phí/tháng: {self.calculateMonthlyCost():,.0f}")
    def __del__(self):
        if getattr(self, "_constructed", False):
            print(f"~SoftwareEngineer(): hủy kỹ sư {self._id}")
        super().__del__()
class ProjectTeam:
    """Nhóm dự án. Quan hệ kết tập (aggregation) với Employee:
    nhóm chỉ giữ liên kết, KHÔNG sở hữu đối tượng Employee."""
    def __init__(self, projectCode, projectName, leader=None):
        # ProjectTeam(projectCode, projectName)
        # ProjectTeam(projectCode, projectName, leader)
        self.projectCode = projectCode
        self.projectName = projectName
        self._leader = None
        self._members = []
        if leader is not None:
            self.addMember(leader, True)
    # ----- Property -----
    @property
    def projectCode(self):
        return self._projectCode
    @projectCode.setter
    def projectCode(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Mã dự án không được rỗng")
        self._projectCode = value.strip()
    @property
    def projectName(self):
        return self._projectName
    @projectName.setter
    def projectName(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Tên dự án không được rỗng")
        self._projectName = value.strip()
    @property
    def leader(self):
        # Chỉ đọc: đổi trưởng nhóm phải qua changeLeader() / addMember(e, True)
        return self._leader
    @property
    def members(self):
        return tuple(self._members)  # bản sao chỉ đọc
    def size(self):
        return len(self._members)
    # ----- Hỗ trợ nội bộ -----
    @staticmethod
    def _checkEmployee(employee):
        if not isinstance(employee, Employee):
            raise TypeError("Thành viên phải là Employee")
    def _find(self, employeeId):
        for member in self._members:
            if member.id == employeeId:
                return member
        return None
    # ----- Nạp chồng addMember -----
    # addMember(employee)
    # addMember(employee, makeLeader)
    def addMember(self, employee, makeLeader=False):
        self._checkEmployee(employee)
        if self.contains(employee.id):
            print(f"Từ chối: {employee.id} đã có trong nhóm {self.projectCode}")
            return False
        self._members.append(employee)
        if makeLeader:
            self._leader = employee  # trưởng nhóm cũ vẫn là thành viên
        return True
    def removeMember(self, employeeId):
        member = self._find(employeeId)
        if member is None:
            print(f"Từ chối: không tìm thấy {employeeId} trong nhóm {self.projectCode}")
            return False
        if member is self._leader:
            print(f"Từ chối: {employeeId} là trưởng nhóm, hãy đổi trưởng nhóm trước")
            return False
        self._members.remove(member)
        return True
    def changeLeader(self, employee):
        self._checkEmployee(employee)
        existing = self._find(employee.id)
        if existing is None:
            self._members.append(employee)
        elif existing is not employee:
            print(f"Từ chối: mã {employee.id} đã thuộc về nhân sự khác trong nhóm")
            return False
        self._leader = employee
        return True
    def contains(self, employeeId):
        return self._find(employeeId) is not None
    def calculateTotalMonthlyCost(self):
        return sum(m.calculateMonthlyCost() for m in self._members)
    def displayTeam(self):
        leader = self._leader.id if self._leader else "(chưa có)"
        print(f"=== Nhóm {self.projectCode} - {self.projectName} ===")
        print(f"Trưởng nhóm: {leader} | Số thành viên: {len(self._members)}")
        for member in self._members:
            member.displayInfo()  # lời gọi đa hình
    def __del__(self):
        # Chỉ hủy cấu trúc liên kết nội bộ, KHÔNG hủy các Employee
        if not hasattr(self, "_members"):
            return
        print(f"~ProjectTeam(): hủy nhóm {self._projectCode}")
        self._members = []
        self._leader = None
