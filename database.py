import MySQLdb as mdb

class Database:
    def __init__(self):
        self.con = None
        self.cur = None

    def open_connect(self):
        self.con = mdb.connect('localhost', 'root', '', 'quan_ly_quay_ban_ve_xem_phim')
        self.cur = self.con.cursor()

    def close_connect(self):
        if self.cur:
            self.cur.close()
        if self.con:
            self.con.close()

    def insert_phim(self, ten_phim, the_loai, danh_gia_phim, mo_ta, ngay_phat_hanh, do_tuoi, dao_dien, dien_vien, thoi_luong):
        self.open_connect()
        query = "INSERT INTO phim (ten_phim, the_loai, danh_gia_phim, mo_ta, ngay_phat_hanh, do_tuoi, dao_dien, dien_vien, thoi_luong) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        self.cur.execute(query, (ten_phim, the_loai, danh_gia_phim, mo_ta, ngay_phat_hanh, do_tuoi, dao_dien, dien_vien, thoi_luong))
        self.con.commit()
        self.close_connect()

    def read_phim(self):
        self.open_connect()
        self.cur.execute("SELECT * FROM phim")
        result = self.cur.fetchall()
        self.close_connect()
        return result

    def update_phim(self, id, ten_phim, the_loai, danh_gia_phim, mo_ta, ngay_phat_hanh, do_tuoi, dao_dien, dien_vien, thoi_luong):
        self.open_connect()
        query = "UPDATE phim SET ten_phim=%s, the_loai=%s, danh_gia_phim=%s, mo_ta=%s, ngay_phat_hanh=%s, do_tuoi=%s, dao_dien=%s, dien_vien=%s, thoi_luong=%s WHERE id=%s"
        values = (ten_phim, the_loai, danh_gia_phim, mo_ta, ngay_phat_hanh, do_tuoi, dao_dien, dien_vien, thoi_luong, id)
        self.cur.execute(query, values)
        self.con.commit()
        self.close_connect()

    def delete_phim(self, id):
        self.open_connect()
        query = "DELETE FROM phim WHERE id=%s"
        self.cur.execute(query, (id,))
        self.con.commit()
        self.close_connect()

    def insert_ve(self, ten_ve, loai_ve, vi_tri_ngoi, gia_ve, so_luong_ve, ve_da_ban, thoi_han_ve, id_phim, id_lich_chieu):
        self.open_connect()
        query = "INSERT INTO ve (ten_ve, loai_ve, vi_tri_ngoi, gia_ve, so_luong_ve, ve_da_ban, thoi_han_ve, id_phim, id_lich_chieu) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        self.cur.execute(query, (ten_ve, loai_ve, vi_tri_ngoi, gia_ve, so_luong_ve, ve_da_ban, thoi_han_ve, id_phim, id_lich_chieu))
        self.con.commit()
        self.close_connect()

    def read_ve(self):
        self.open_connect()
        self.cur.execute("SELECT * FROM ve")
        result = self.cur.fetchall()
        self.close_connect()
        return result

    def update_ve(self, id, ten_ve, loai_ve, vi_tri_ngoi, gia_ve, so_luong_ve, ve_da_ban, thoi_han_ve, id_phim, id_lich_chieu):
        self.open_connect()
        query = "UPDATE ve SET ten_ve=%s, loai_ve=%s, vi_tri_ngoi=%s, gia_ve=%s, so_luong_ve=%s, ve_da_ban=%s, thoi_han_ve=%s, id_phim=%s, id_lich_chieu=%s WHERE id=%s"
        values = (ten_ve, loai_ve, vi_tri_ngoi, gia_ve, so_luong_ve, ve_da_ban, thoi_han_ve, id_phim, id_lich_chieu, id)
        self.cur.execute(query, values)
        self.con.commit()
        self.close_connect()

    def delete_ve(self, id):
        self.open_connect()
        query = "DELETE FROM ve WHERE id=%s"
        self.cur.execute(query, (id,))
        self.con.commit()
        self.close_connect()

    def insert_dich_vu(self, ten_dich_vu, gia_dich_vu, phi_dich_vu, da_ban):
        self.open_connect()
        query = "INSERT INTO dich_vu (ten_dich_vu, gia_dich_vu, phi_dich_vu, da_ban) VALUES (%s, %s, %s, %s)"
        self.cur.execute(query, (ten_dich_vu, gia_dich_vu, phi_dich_vu, da_ban))
        self.con.commit()
        self.close_connect()

    def read_dich_vu(self):
        self.open_connect()
        self.cur.execute("SELECT * FROM dich_vu")
        result = self.cur.fetchall()
        self.close_connect()
        return result

    def update_dich_vu(self, id, ten_dich_vu, gia_dich_vu, phi_dich_vu, da_ban):
        self.open_connect()
        query = "UPDATE dich_vu SET ten_dich_vu=%s, gia_dich_vu=%s, phi_dich_vu=%s, da_ban=%s WHERE id=%s"
        values = (ten_dich_vu, gia_dich_vu, phi_dich_vu, da_ban, id)
        self.cur.execute(query, values)
        self.con.commit()
        self.close_connect()

    def delete_dich_vu(self, id):
        self.open_connect()
        query = "DELETE FROM dich_vu WHERE id=%s"
        self.cur.execute(query, (id,))
        self.con.commit()
        self.close_connect()

    def search_dich_vu(self, ten_dich_vu):
        self.open_connect()
        query = "SELECT * FROM dich_vu WHERE ten_dich_vu LIKE %s"
        self.cur.execute(query, (f'%{ten_dich_vu}%',))
        result = self.cur.fetchall()
        self.close_connect()
        return result

    def insert_lich_chieu(self, thoi_gian_chieu, phong_chieu, dia_diem_chieu, so_luong_cho_ngoi, id_phim):
        self.open_connect()
        query = "INSERT INTO lich_chieu (thoi_gian_chieu, phong_chieu, dia_diem_chieu, so_luong_cho_ngoi, id_phim) VALUES (%s, %s, %s, %s, %s)"
        self.cur.execute(query, (thoi_gian_chieu, phong_chieu, dia_diem_chieu, so_luong_cho_ngoi, id_phim))
        self.con.commit()
        self.close_connect()

    def read_lich_chieu(self):
        self.open_connect()
        self.cur.execute("SELECT * FROM lich_chieu")
        result = self.cur.fetchall()
        self.close_connect()
        return result

    def update_lich_chieu(self, id, thoi_gian_chieu, phong_chieu, dia_diem_chieu, so_luong_cho_ngoi, id_phim):
        self.open_connect()
        query = "UPDATE lich_chieu SET thoi_gian_chieu=%s, phong_chieu=%s, dia_diem_chieu=%s, so_luong_cho_ngoi=%s, id_phim=%s WHERE id=%s"
        values = (thoi_gian_chieu, phong_chieu, dia_diem_chieu, so_luong_cho_ngoi, id_phim, id)
        self.cur.execute(query, values)
        self.con.commit()
        self.close_connect()

    def delete_lich_chieu(self, id):
        self.open_connect()
        query = "DELETE FROM lich_chieu WHERE id=%s"
        self.cur.execute(query, (id,))
        self.con.commit()
        self.close_connect()

    def select_phim_by_id(self, id):
        self.open_connect()
        query = "SELECT ten_phim FROM phim WHERE id=%s"
        self.cur.execute(query, (id,))
        result = self.cur.fetchone()
        self.close_connect()
        return result

    def select_lich_chieu_by_id(self, id):
        self.open_connect()
        query = "SELECT dia_diem_chieu FROM lich_chieu WHERE id=%s"
        self.cur.execute(query, (id,))
        result = self.cur.fetchone()
        self.close_connect()
        return result

    def select_id_by_name(self, name):
        self.open_connect()
        query = "SELECT id FROM phim WHERE ten_phim=%s"
        self.cur.execute(query, (name,))
        result = self.cur.fetchone()
        self.close_connect()
        return result

    def select_id_by_name_lich_chieu(self, name):
        self.open_connect()
        query = "SELECT id FROM lich_chieu WHERE dia_diem_chieu=%s"
        self.cur.execute(query, (name,))
        result = self.cur.fetchone()
        self.close_connect()
        return result

    def tinh_doanh_thu_theo_ve(self):
        self.open_connect()
        query = "SELECT ten_ve, loai_ve, vi_tri_ngoi, gia_ve, so_luong_ve, ve_da_ban, thoi_han_ve, id_phim, id_lich_chieu, SUM(gia_ve * ve_da_ban) as doanh_thu, createAt, updateAt FROM ve GROUP BY loai_ve, id_phim"
        self.cur.execute(query)
        result = self.cur.fetchall()
        self.close_connect()
        return result

    def tinh_doanh_thu_theo_dich_vu(self):
        self.open_connect()
        query = "SELECT ten_dich_vu, gia_dich_vu, phi_dich_vu, da_ban, SUM(gia_dich_vu * da_ban) as doanh_thu, createAt, updateAt FROM dich_vu GROUP BY ten_dich_vu"
        self.cur.execute(query)
        result = self.cur.fetchall()
        self.close_connect()
        return result
