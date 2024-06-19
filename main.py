from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QStackedWidget, QTableWidgetItem
import sys
from database import Database

import pdb;   # Add this line at the start of the method where you suspect the issue


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
        widget.setFixedWidth(981)

        center_widget(self)
        self.btnQuanLyPhim.clicked.connect(self.QuanLyPhim)
        self.btnQuanLyLichChieu.clicked.connect(self.QuanLyLichChieu)
        self.btnQuanLyVe.clicked.connect(self.QuanLyVe)
        self.btnQuanlyDichVu.clicked.connect(self.QuanLyDichVu)
        self.btnBaoCao.clicked.connect(self.BaoCaoDoanhThu)

    def QuanLyPhim(self):
        widget.setFixedWidth(1215)
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
        self.db = Database()
        self.tableWidget = self.findChild(QtWidgets.QTableWidget, 'tableWidget')
        self.load_data()
        self.tableWidget.itemSelectionChanged.connect(self.select_row)
        self.btnThemd.clicked.connect(self.add_dich_vu)
        self.btnSuad.clicked.connect(self.update_selected_dich_vu)
        self.btnXoad.clicked.connect(self.delete_dich_vu)
        self.btnThoatd.clicked.connect(self.ThoatTrangChu)

    def load_data(self):
        try:
            dich_vu_list = self.db.read_dich_vu()
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(dich_vu_list):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Lỗi khi tải dữ liệu dịch vụ: {str(e)}")

    def select_row(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row < 0:
            return

        try:
            id = self.tableWidget.item(selected_row, 0).text()
            ten_dich_vu = self.tableWidget.item(selected_row, 1).text()
            gia_dich_vu = self.tableWidget.item(selected_row, 2).text()
            phi_dich_vu = self.tableWidget.item(selected_row, 3).text()
            da_ban = self.tableWidget.item(selected_row, 4).text()

            self.txtIDichVu.setText(id)
            self.txtITenDichVu.setText(ten_dich_vu)
            self.txtGiadichvu.setText(gia_dich_vu)
            self.txtPhidichvu.setText(phi_dich_vu)
            self.txtDaBan.setText(da_ban)
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Lỗi khi chọn hàng: {str(e)}")

    def add_dich_vu(self):
        ten_dich_vu = self.txtITenDichVu.text()
        gia_dich_vu = self.txtGiadichvu.text()
        phi_dich_vu = self.txtPhidichvu.text()
        da_ban = self.txtDaBan.text()
        if ten_dich_vu == "" or gia_dich_vu == "" or phi_dich_vu == "":
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đủ thông tin để thêm dịch vụ.")
            return

        try:
            gia_dich_vu = float(gia_dich_vu)
            phi_dich_vu = float(phi_dich_vu)
            da_ban = int(da_ban)
        except ValueError:
            QMessageBox.warning(self, "Lỗi", "Giá dịch vụ và phí dịch vụ phải là số.")
            return

        try:
            self.db.insert_dich_vu(ten_dich_vu, gia_dich_vu, phi_dich_vu, da_ban)
            QMessageBox.information(self, "Thông báo", "Đã thêm dịch vụ thành công.")
            self.load_data()
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Lỗi khi thêm dịch vụ: {str(e)}")

    def update_selected_dich_vu(self):
        try:
            id = int(self.txtIDichVu.text())
            ten_dich_vu = self.txtITenDichVu.text()
            gia_dich_vu = float(self.txtGiadichvu.text())
            phi_dich_vu = float(self.txtPhidichvu.text())
            da_ban = int(self.txtDaBan.text())

            if ten_dich_vu == "" or gia_dich_vu == "" or phi_dich_vu == "" or da_ban == "":
                QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đủ thông tin để cập nhật dịch vụ.")
                return

            self.db.update_dich_vu(id, ten_dich_vu, gia_dich_vu, phi_dich_vu, da_ban)
            QMessageBox.information(self, "Thông báo", "Đã cập nhật dịch vụ thành công.")
            self.load_data()
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Lỗi khi cập nhật dịch vụ: {str(e)}")

    def delete_dich_vu(self):
        try:
            id = int(self.txtIDichVu.text())
            self.db.delete_dich_vu(id)
            QMessageBox.information(self, "Thông báo", "Đã xóa dịch vụ thành công.")
            self.load_data()
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Lỗi khi xóa dịch vụ: {str(e)}")

    def ThoatTrangChu(self):
        widget.setCurrentIndex(1)

# Cửa sổ Quản Lý Lịch Chiếu
class QuanLyLichChieu(QMainWindow):
    def __init__(self):
        super(QuanLyLichChieu, self).__init__()
        uic.loadUi("QuanLyLichChieu.ui", self)
        center_widget(self)
        self.btnThoatl.clicked.connect(self.ThoatTrangChu)
        self.db = Database()
        self.tableWidget = self.findChild(QtWidgets.QTableWidget, 'tableWidget')
        self.btnTheml.clicked.connect(self.add_lich_chieu)
        self.btnSual.clicked.connect(self.update_selected_lich_chieu)
        self.btnXoal.clicked.connect(self.delete_lich_chieu)
        self.load_data()
        self.tableWidget.itemSelectionChanged.connect(self.select_row)

    def load_data(self):
        try:
            lich_chieu_list = self.db.read_lich_chieu()
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(lich_chieu_list):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            #loading cbPhim
            phim_list = self.db.read_phim()
            self.cbPhim.clear()
            for phim in phim_list:
                self.cbPhim.addItem(phim[1])
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Lỗi khi tải dữ liệu lịch chiếu: {str(e)}")

    def select_row(self):
       #khi select row thi se hien thi thong tin len cac o nhap
       # voi cbPhim thi lay id roi tim thang do trong danh sach phim
        selected_row = self.tableWidget.currentRow()
        if selected_row < 0:
            return
        try:
            id = self.tableWidget.item(selected_row, 0).text()
            phong_chieu = self.tableWidget.item(selected_row, 2).text()
            dia_diem_chieu = self.tableWidget.item(selected_row, 3).text()
            thoi_gian_chieu = self.tableWidget.item(selected_row, 1).text()
            so_luong_cho_ngoi = self.tableWidget.item(selected_row, 3).text()
            id_phim = self.tableWidget.item(selected_row, 4).text()
            self.txtIDLichchieu.setText(id)
            self.txtPhongchieu.setText(phong_chieu)
            self.txtDiadiemchieu.setText(dia_diem_chieu)
            self.txtThoigianchieu.setText(thoi_gian_chieu)
            self.txtSoluong.setText(so_luong_cho_ngoi)
            #check id_phim
            if id_phim:
                name_phim = self.db.select_phim_by_id(int(id_phim))
                if name_phim:
                    self.cbPhim.setCurrentText(name_phim[0])
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Lỗi khi chọn hàng: {str(e)}")

    # them lich chieu
    def add_lich_chieu(self):
        phong_chieu = self.txtPhongchieu.text()
        dia_diem_chieu = self.txtDiadiemchieu.text()
        thoi_gian_chieu = self.txtThoigianchieu.text()
        so_luong_cho_ngoi = self.txtSoluong.text()
        id_phim = self.db.select_id_by_name(self.cbPhim.currentText())
        if not all([phong_chieu, dia_diem_chieu, thoi_gian_chieu, so_luong_cho_ngoi, id_phim[0]]):
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đủ thông tin để thêm lịch chiếu.")
            return
        try:
            self.db.insert_lich_chieu(thoi_gian_chieu, phong_chieu, dia_diem_chieu, so_luong_cho_ngoi, id_phim[0])
            QMessageBox.information(self, "Thông báo", "Đã thêm lịch chiếu thành công.")
            self.load_data()
            #clear all input
            self.txtPhongchieu.clear()
            self.txtDiadiemchieu.clear()
            self.txtThoigianchieu.clear()
            self.txtSoluong.clear()

        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Lỗi khi thêm lịch chiếu: {str(e)}")
    def update_selected_lich_chieu(self):
        id = int(self.txtIDLichchieu.text())
        phong_chieu = self.txtPhongchieu.text()
        dia_diem_chieu = self.txtDiadiemchieu.text()
        thoi_gian_chieu = self.txtThoigianchieu.text()
        so_luong_cho_ngoi = self.txtSoluong.text()
        id_phim = self.db.select_id_by_name(self.cbPhim.currentText())
        if not all([phong_chieu, dia_diem_chieu, thoi_gian_chieu, so_luong_cho_ngoi, id_phim]):
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đủ thông tin để cập nhật lịch chiếu.")
            return
        try:
            self.db.update_lich_chieu(id, thoi_gian_chieu, phong_chieu, dia_diem_chieu, so_luong_cho_ngoi, id_phim)
            QMessageBox.information(self, "Thông báo", "Đã cập nhật lịch chiếu thành công.")
            self.load_data()
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Lỗi khi cập nhật lịch chiếu: {str(e)}")

    def delete_lich_chieu(self):
        id = int(self.txtIDLichchieu.text())
        try:
            self.db.delete_lich_chieu(id)
            QMessageBox.information(self, "Thông báo", "Đã xóa lịch chiếu thành công.")
            self.load_data()
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Lỗi khi xóa lịch chiếu: {str(e)}")



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
        self.db = Database()
        self.tableWidget = self.findChild(QtWidgets.QTableWidget, 'tableWidget')  # Tìm tableWidget trong UI

        # Kết nối sự kiện khi chọn một dòng trong tableWidget
        self.tableWidget.itemSelectionChanged.connect(self.select_row)

        self.btnThem.clicked.connect(self.add_phim)
        self.btnSua.clicked.connect(self.update_selected_phim)
        self.btnXoa.clicked.connect(self.delete_phim)
        self.btnThoat.clicked.connect(self.thoat_quan_ly_phim)
        self.load_data()

    def load_data(self):
        print("Vao load_data")
        try:
            phim_list = self.db.read_phim()
            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(phim_list):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Lỗi khi tải dữ liệu phim: {str(e)}")

    def select_row(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row < 0:  # Nếu không có hàng nào được chọn
            return

        try:
            id = self.tableWidget.item(selected_row, 0).text()
            ten_phim = self.tableWidget.item(selected_row, 1).text()
            the_loai = self.tableWidget.item(selected_row, 2).text()
            danh_gia_phim = self.tableWidget.item(selected_row, 3).text()
            mo_ta = self.tableWidget.item(selected_row, 4).text()
            ngay_phat_hanh = self.tableWidget.item(selected_row, 5).text()
            do_tuoi = self.tableWidget.item(selected_row, 6).text()
            dao_dien = self.tableWidget.item(selected_row, 7).text()
            dien_vien = self.tableWidget.item(selected_row, 8).text()
            thoi_luong = self.tableWidget.item(selected_row, 9).text()

            self.txtIDPhim.setText(id)
            self.txtTenphim.setText(ten_phim)
            self.txtTheloai.setText(the_loai)
            self.txtDanhgia.setText(danh_gia_phim)
            self.txtMota.setText(mo_ta)
            self.dateNgayPhatHanh.setDate(QtCore.QDate.fromString(ngay_phat_hanh, "yyyy-MM-dd"))
            self.txtTuoi.setText(do_tuoi)
            self.txtDaodien.setText(dao_dien)
            self.txtDienvien.setText(dien_vien)
            self.txtThoiluong.setText(thoi_luong)
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Lỗi khi chọn hàng: {str(e)}")

    def add_phim(self):
        ten_phim = self.txtTenphim.text()
        the_loai = self.txtTheloai.text()
        danh_gia_phim = self.txtDanhgia.text()
        mo_ta = self.txtMota.text()
        ngay_phat_hanh = self.dateNgayPhatHanh.date().toString("yyyy-MM-dd")
        do_tuoi = self.txtTuoi.text()
        dao_dien = self.txtDaodien.text()
        dien_vien = self.txtDienvien.text()
        thoi_luong = self.txtThoiluong.text()

        # Kiểm tra các trường có rỗng không
        if ten_phim == "" or the_loai == "" or danh_gia_phim == "" or mo_ta == "" or ngay_phat_hanh == "" or do_tuoi == "" or dao_dien == "" or dien_vien == "" or thoi_luong == "":
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đủ thông tin để thêm phim.")
            return

        # Chuyển đổi danh_gia_phim và thoi_luong sang định dạng số nếu cần
        try:
            danh_gia_phim = float(danh_gia_phim)
            thoi_luong = int(thoi_luong)
        except ValueError:
            QMessageBox.warning(self, "Lỗi", "Đánh giá phim và thời lượng phải là số.")
            return

        try:
            self.db.insert_phim(ten_phim, the_loai, danh_gia_phim, mo_ta, ngay_phat_hanh, do_tuoi, dao_dien, dien_vien, thoi_luong)
            QMessageBox.information(self, "Thông báo", "Đã thêm phim thành công.")
            #clear all input
            self.txtTenphim.clear()
            self.txtTheloai.clear()
            self.txtDanhgia.clear()
            self.txtMota.clear()
            self.txtTuoi.clear()
            self.txtDaodien.clear()

            self.load_data()
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Lỗi khi thêm phim: {str(e)}")

    def update_selected_phim(self):
        try:
            id = int(self.txtIDPhim.text())
            ten_phim = self.txtTenphim.text()
            the_loai = self.txtTheloai.text()
            danh_gia_phim = float(self.txtDanhgia.text())
            mo_ta = self.txtMota.text()
            ngay_phat_hanh = self.dateNgayPhatHanh.date().toString("yyyy-MM-dd")
            do_tuoi = self.txtTuoi.text()
            dao_dien = self.txtDaodien.text()
            dien_vien = self.txtDienvien.text()
            thoi_luong = int(self.txtThoiluong.text())

            self.db.update_phim(id, ten_phim, the_loai, danh_gia_phim, mo_ta, ngay_phat_hanh, do_tuoi, dao_dien, dien_vien, thoi_luong)
            QMessageBox.information(self, "Thông báo", "Đã cập nhật thông tin phim thành công.")
            self.load_data()
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Lỗi khi cập nhật phim: {str(e)}")

    def delete_phim(self):
        try:
            id = int(self.txtIDPhim.text())
            self.db.delete_phim(id)
            QMessageBox.information(self, "Thông báo", "Đã xóa phim thành công.")
            self.load_data()
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Lỗi khi xóa phim: {str(e)}")

    def thoat_quan_ly_phim(self):
        widget.setCurrentIndex(1)

# Cửa sổ Quản Lý Vé
class QuanLyVe(QMainWindow):
    def __init__(self):
        super(QuanLyVe, self).__init__()
        uic.loadUi("QuanLyVe.ui", self)
        center_widget(self)
        self.db = Database()
        self.tableWidget = self.findChild(QtWidgets.QTableWidget, 'tableWidget')
        self.load_data()

        # Connect signals to slots
        self.tableWidget.itemSelectionChanged.connect(self.select_row)
        self.btnThemv.clicked.connect(self.add_ve)
        self.btnSuav.clicked.connect(self.update_selected_ve)
        self.btnXoav.clicked.connect(self.delete_ve)
        self.btnThoatv.clicked.connect(self.thoat_quan_ly_ve)

    def load_data(self):
        self.load_phim_list()
        self.load_lich_chieu_list()
        ve_list = self.db.read_ve()
        self.display_ve_list(ve_list)

    def load_phim_list(self):
        phim_list = self.db.read_phim()
        self.cbPhim.clear()
        for phim in phim_list:
            self.cbPhim.addItem(phim[1])

    def load_lich_chieu_list(self):
        lich_chieu_list = self.db.read_lich_chieu()
        self.cbLichChieu.clear()
        for lich_chieu in lich_chieu_list:
            self.cbLichChieu.addItem(lich_chieu[3])

    def display_ve_list(self, ve_list):
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(ve_list):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def select_row(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row != -1:
            id = self.tableWidget.item(selected_row, 0).text()
            ten_ve = self.tableWidget.item(selected_row, 1).text()
            loai_ve = self.tableWidget.item(selected_row, 2).text()
            vi_tri_ngoi = self.tableWidget.item(selected_row, 3).text()
            gia_ve = self.tableWidget.item(selected_row, 4).text()
            so_luong_ve = self.tableWidget.item(selected_row, 5).text()
            ve_da_ban = self.tableWidget.item(selected_row, 6).text()
            thoi_han_ve = self.tableWidget.item(selected_row, 7).text()
            id_phim = self.tableWidget.item(selected_row, 8).text()
            id_lich_chieu = self.tableWidget.item(selected_row, 9).text()

            self.txtIDVe.setText(id)
            self.txtTenVe.setText(ten_ve)
            self.txtLoaiVe.setText(loai_ve)
            self.txtViTriNgoi.setText(vi_tri_ngoi)
            self.txtGiaVe.setText(gia_ve)
            self.txtSoLuong.setText(so_luong_ve)
            self.txtDaBan.setText(ve_da_ban)
            self.dateThoiHanVe.setDate(QtCore.QDate.fromString(thoi_han_ve, "yyyy-MM-dd"))
            #check id_phim and id_lich_chieu
            if id_phim and id_lich_chieu:
                name_phim = self.db.select_phim_by_id(int(id_phim))
                name_lich_chieu = self.db.select_lich_chieu_by_id(int(id_lich_chieu))
                #check trong cbPhim va cbLichChieu co ton tai khong co thi chi dinh chon no
                if name_phim:
                    self.cbPhim.setCurrentText(name_phim[0])
                if name_lich_chieu:
                    self.cbLichChieu.setCurrentText(name_lich_chieu[0])



    def add_ve(self):
        # lay thong tin tu cac o nhap, voi combobox thi lay id
        ten_ve = self.txtTenVe.text()
        loai_ve = self.txtLoaiVe.text()
        vi_tri_ngoi = self.txtViTriNgoi.text()
        gia_ve = float(self.txtGiaVe.text())
        so_luong_ve = int(self.txtSoLuong.text())
        ve_da_ban = int(self.txtDaBan.text())
        thoi_han_ve = self.dateThoiHanVe.date().toString("yyyy-MM-dd")
        id_phim = self.db.select_id_by_name(self.cbPhim.currentText())
        id_lich_chieu = self.db.select_id_by_name_lich_chieu(self.cbLichChieu.currentText())
        print(id_phim, id_lich_chieu)
        #check xem co thieu thong tin nao khong neu co hien thong bao len man hinh
        if not all([ten_ve, loai_ve, vi_tri_ngoi, gia_ve, so_luong_ve, thoi_han_ve, id_phim, id_lich_chieu]):
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đủ thông tin để thêm vé.")
            return
        #thuc hien them ve
        try:
            self.db.insert_ve(ten_ve, loai_ve, vi_tri_ngoi, gia_ve, so_luong_ve, ve_da_ban, thoi_han_ve, id_phim, id_lich_chieu)
            QMessageBox.information(self, "Thông báo", "Đã thêm vé thành công.")
            self.load_data()
            #clear all input
            self.txtTenVe.clear()
            self.txtLoaiVe.clear()
            self.txtViTriNgoi.clear()
            self.txtGiaVe.clear()
            self.txtSoLuong.clear()

        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Lỗi khi thêm vé: {str(e)}")




    def update_selected_ve(self):
        # tuong tu them lam sua
        id = int(self.txtIDVe.text())
        ten_ve = self.txtTenVe.text()
        loai_ve = self.txtLoaiVe.text()
        vi_tri_ngoi = self.txtViTriNgoi.text()
        gia_ve = float(self.txtGiaVe.text())
        so_luong_ve = int(self.txtSoLuong.text())
        ve_da_ban = int(self.txtDaBan.text())
        thoi_han_ve = self.dateThoiHanVe.date().toString("yyyy-MM-dd")
        id_phim = self.db.select_id_by_name(self.cbPhim.currentText())
        id_lich_chieu = self.db.select_id_by_name_lich_chieu(self.cbLichChieu.currentText())
        if not all([ten_ve, loai_ve, vi_tri_ngoi, gia_ve, so_luong_ve, thoi_han_ve, id_phim, id_lich_chieu]):
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đủ thông tin để cập nhật vé.")
            return
        try:
            self.db.update_ve(id, ten_ve, loai_ve, vi_tri_ngoi, gia_ve, so_luong_ve, ve_da_ban, thoi_han_ve, id_phim, id_lich_chieu)
            QMessageBox.information(self, "Thông báo", "Đã cập nhật vé thành công.")
            self.load_data()
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Lỗi khi cập nhật vé: {str(e)}")



    def delete_ve(self):
        # tuong tu them lam xoa
        id = int(self.txtIDVe.text())
        try:
            self.db.delete_ve(id)
            QMessageBox.information(self, "Thông báo", "Đã xóa vé thành công.")
            self.load_data()
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Lỗi khi xóa vé: {str(e)}")

    def thoat_quan_ly_ve(self):
        widget.setCurrentIndex(1)
def ThoatTrangChu(self):
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
