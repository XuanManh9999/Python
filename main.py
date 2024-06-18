from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QStackedWidget
import sys
# import MySQLdb as mdb

# Hàm để căn cửa sổ ra giữa màn hình
def center_widget(widget):
    screen = QApplication.primaryScreen()
    screen_geometry = screen.availableGeometry()
    widget_geometry = widget.frameGeometry()
    widget_geometry.moveCenter(screen_geometry.center())
    widget.move(widget_geometry.topLeft())

# Cửa sổ đăng nhập
class DangNhap(QMainWindow):
    def __init__(self):
        super(DangNhap, self).__init__()
        uic.loadUi("DangNhap.ui", self)
        center_widget(self)
        self.btnLogin.clicked.connect(self.DangNhap)

    def DangNhap(self):
        username = self.txtName.text()
        password = self.txtPass.text()
        if username == "1" and password == "1":
            widget.setFixedWidth(981)
            widget.setFixedHeight(684)
            center_widget(widget)
            widget.setCurrentIndex(1)
        else:
            QMessageBox.information(self, "Thông báo", "Sai tên đăng nhập hoặc mật khẩu")

# Cửa sổ Trang Chủ
class TrangChu(QMainWindow):
    def __init__(self):
        super(TrangChu, self).__init__()
        uic.loadUi("TrangChu.ui", self)
        center_widget(self)
        self.btnQuanLyPhim.clicked.connect(self.QuanLyPhim)
        self.btnQuanLyLichChieu.clicked.connect(self.QuanLyLichChieu)
        self.btnQuanLyVe.clicked.connect(self.QuanLyVe)
        self.btnQuanlyDichVu.clicked.connect(self.QuanLyDichVu)
        self.btnBaoCao.clicked.connect(self.BaoCaoDoanhThu)

    def QuanLyPhim(self):
        widget.setFixedWidth(1200)
        widget.setFixedHeight(721)
        center_widget(widget)
        widget.setCurrentIndex(5)

    def QuanLyLichChieu(self):
        widget.setFixedWidth(1121)
        widget.setFixedHeight(721)
        center_widget(widget)
        widget.setCurrentIndex(4)

    def QuanLyVe(self):
        widget.setFixedWidth(1191)
        center_widget(widget)
        widget.setCurrentIndex(6)

    def QuanLyDichVu(self):
        widget.setFixedWidth(1033)
        widget.setFixedHeight(673)
        center_widget(widget)
        widget.setCurrentIndex(3)

    def BaoCaoDoanhThu(self):
        widget.setFixedWidth(1200)
        center_widget(widget)
        widget.setCurrentIndex(2)

# Cửa sổ Báo Cáo Doanh Thu
class BaoCaoDoanhThu(QMainWindow):
    def __init__(self):
        super(BaoCaoDoanhThu, self).__init__()
        uic.loadUi("BaoCaoDoanhThu.ui", self)
        center_widget(self)
        self.btnThoatb.clicked.connect(self.ThoatTrangChu)

    def ThoatTrangChu(self):
        widget.setFixedWidth(981)
        widget.setFixedHeight(684)
        center_widget(widget)
        widget.setCurrentIndex(1)

# Cửa sổ Quản Lý Dịch Vụ
class QuanLyDichVu(QMainWindow):
    def __init__(self):
        super(QuanLyDichVu, self).__init__()
        uic.loadUi("QuanLyDichVu.ui", self)
        center_widget(self)
        self.btnThoatd.clicked.connect(self.ThoatTrangChu)

    def ThoatTrangChu(self):
        widget.setFixedWidth(981)
        widget.setFixedHeight(684)
        center_widget(widget)
        widget.setCurrentIndex(1)

# Cửa sổ Quản Lý Lịch Chiếu
class QuanLyLichChieu(QMainWindow):
    def __init__(self):
        super(QuanLyLichChieu, self).__init__()
        uic.loadUi("QuanLyLichChieu.ui", self)
        center_widget(self)
        self.btnThoatl.clicked.connect(self.ThoatTrangChu)

    def ThoatTrangChu(self):
        widget.setFixedWidth(981)
        widget.setFixedHeight(684)
        center_widget(widget)
        widget.setCurrentIndex(1)

# Cửa sổ Quản Lý Phim
class QuanLyPhim(QMainWindow):
    def __init__(self):
        super(QuanLyPhim, self).__init__()
        uic.loadUi("QuanLyPhim.ui", self)
        center_widget(self)
        self.btnThoat.clicked.connect(self.ThoatTrangChu)
    #

    def ThoatTrangChu(self):
        widget.setFixedWidth(981)
        widget.setFixedHeight(684)
        center_widget(widget)
        widget.setCurrentIndex(1)

# Cửa sổ Quản Lý Vé
class QuanLyVe(QMainWindow):
    def __init__(self):
        super(QuanLyVe, self).__init__()
        uic.loadUi("QuanLyVe.ui", self)
        center_widget(self)
        self.btnThoatv.clicked.connect(self.ThoatTrangChu)

    def ThoatTrangChu(self):
        widget.setFixedWidth(981)
        widget.setFixedHeight(684)
        center_widget(widget)
        widget.setCurrentIndex(1)

# Khởi tạo ứng dụng
app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()

# Khởi tạo các cửa sổ
dangnhap_f = DangNhap()
trangchu_f = TrangChu()
baocaodoanhthu_f = BaoCaoDoanhThu()
quanlydichvu_f = QuanLyDichVu()
quanlylichchieu_f = QuanLyLichChieu()
quanlyphim_f = QuanLyPhim()
quanlyve_f = QuanLyVe()

# Thêm các cửa sổ vào stacked widget
widget.addWidget(dangnhap_f)
widget.addWidget(trangchu_f)
widget.addWidget(baocaodoanhthu_f)
widget.addWidget(quanlydichvu_f)
widget.addWidget(quanlylichchieu_f)
widget.addWidget(quanlyphim_f)
widget.addWidget(quanlyve_f)

# Thiết lập cửa sổ ban đầu
widget.setCurrentIndex(0)
widget.setFixedWidth(660)
widget.setFixedHeight(550)
center_widget(widget)
widget.show()

sys.exit(app.exec())
