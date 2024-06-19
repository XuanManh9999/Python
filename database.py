import MySQLdb as mdb

class Database:
    def __init__(self):
        self.con = mdb.connect('localhost', 'root', '', 'quan_ly_quay_ban_ve_xem_phim')
        self.cur = self.con.cursor()

    def insert_phim(self, ten_phim, the_loai, danh_gia_phim, mo_ta, ngay_phat_hanh, do_tuoi, dao_dien, dien_vien, thoi_luong):
        query = "INSERT INTO phim(ten_phim, the_loai, danh_gia_phim, mo_ta, ngay_phat_hanh, do_tuoi, dao_dien, dien_vien, thoi_luong) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        self.cur.execute(query, (ten_phim, the_loai, danh_gia_phim, mo_ta, ngay_phat_hanh, do_tuoi, dao_dien, dien_vien, thoi_luong))
        self.con.commit()

    def read_phim(self):
        self.cur.execute("SELECT * FROM phim")
        return self.cur.fetchall()

    def update_phim(self, id, ten_phim, the_loai, danh_gia_phim, mo_ta, ngay_phat_hanh, do_tuoi, dao_dien, dien_vien, thoi_luong):
        query = "UPDATE phim SET ten_phim=%s, the_loai=%s, danh_gia_phim=%s, mo_ta=%s, ngay_phat_hanh=%s, do_tuoi=%s, dao_dien=%s, dien_vien=%s, thoi_luong=%s WHERE id=%s"
        values = (ten_phim, the_loai, danh_gia_phim, mo_ta, ngay_phat_hanh, do_tuoi, dao_dien, dien_vien, thoi_luong, id)
        self.cur.execute(query, values)
        self.con.commit()

    def delete_phim(self, id):
        query = "DELETE FROM phim WHERE id=%s"
        self.cur.execute(query, (id,))
        self.con.commit()

    # CRUD operations for 've' table
    def insert_ve(self, ten_ve, loai_ve, vi_tri_ngoi, gia_ve, so_luong_ve, ve_da_ban, thoi_han_ve, id_phim, id_lich_chieu):
        query = "INSERT INTO ve (ten_ve, loai_ve, vi_tri_ngoi, gia_ve, so_luong_ve, ve_da_ban, thoi_han_ve, id_phim, id_lich_chieu) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        self.cur.execute(query, (ten_ve, loai_ve, vi_tri_ngoi, gia_ve, so_luong_ve, ve_da_ban, thoi_han_ve, id_phim, id_lich_chieu))
        self.con.commit()

    def read_ve(self):
        self.cur.execute("SELECT * FROM ve")
        return self.cur.fetchall()

    def update_ve(self, id, ten_ve, loai_ve, vi_tri_ngoi, gia_ve, so_luong_ve, ve_da_ban, thoi_han_ve, id_phim, id_lich_chieu):
        query = "UPDATE ve SET ten_ve=%s, loai_ve=%s, vi_tri_ngoi=%s, gia_ve=%s, so_luong_ve=%s, ve_da_ban=%s, thoi_han_ve=%s, id_phim=%s, id_lich_chieu=%s WHERE id=%s"
        values = (ten_ve, loai_ve, vi_tri_ngoi, gia_ve, so_luong_ve, ve_da_ban, thoi_han_ve, id_phim, id_lich_chieu, id)
        self.cur.execute(query, values)
        self.con.commit()

    def delete_ve(self, id):
        query = "DELETE FROM ve WHERE id=%s"
        self.cur.execute(query, (id,))
        self.con.commit()

    #CRUD dich vu
    def insert_dich_vu(self, ten_dich_vu, gia_dich_vu, phi_dich_vu, da_ban):
        query = "INSERT INTO dich_vu (ten_dich_vu, gia_dich_vu, phi_dich_vu, da_ban) VALUES (%s, %s, %s, %s)"
        self.cur.execute(query, (ten_dich_vu, gia_dich_vu, phi_dich_vu, da_ban))
        self.con.commit()
    def read_dich_vu(self):
        self.cur.execute("SELECT * FROM dich_vu")
        return self.cur.fetchall()
    def update_dich_vu(self, id, ten_dich_vu, gia_dich_vu, phi_dich_vu, da_ban):
        query = "UPDATE dich_vu SET ten_dich_vu=%s, gia_dich_vu=%s, phi_dich_vu=%s, da_ban=%s WHERE id=%s"
        values = (ten_dich_vu, gia_dich_vu, phi_dich_vu, da_ban, id)
        self.cur.execute(query, values)
        self.con.commit()
    def delete_dich_vu(self, id):
        query = "DELETE FROM dich_vu WHERE id=%s"
        self.cur.execute(query, (id,))
        self.con.commit()
    #tim kiem dich vu
    def search_dich_vu(self, ten_dich_vu):
        query = "SELECT * FROM dich_vu WHERE ten_dich_vu LIKE %s"
        self.cur.execute(query, (f'%{ten_dich_vu}%',))
        return self.cur.fetchall()
    #CRUD lich chieu
    def insert_lich_chieu(self, thoi_gian_chieu, phong_chieu, dia_diem_chieu, so_luong_cho_ngoi, id_phim):
        query = "INSERT INTO lich_chieu (thoi_gian_chieu, phong_chieu, dia_diem_chieu, so_luong_cho_ngoi, id_phim) VALUES (%s, %s, %s, %s, %s)"
        self.cur.execute(query, (thoi_gian_chieu, phong_chieu, dia_diem_chieu, so_luong_cho_ngoi, id_phim))
        self.con.commit()
    def read_lich_chieu(self):
        self.cur.execute("SELECT * FROM lich_chieu")
        return self.cur.fetchall()
    def update_lich_chieu(self, id, thoi_gian_chieu, phong_chieu, dia_diem_chieu, so_luong_cho_ngoi, id_phim):
        query = "UPDATE lich_chieu SET thoi_gian_chieu=%s, phong_chieu=%s, dia_diem_chieu=%s, so_luong_cho_ngoi=%s, id_phim=%s WHERE id=%s"
        values = (thoi_gian_chieu, phong_chieu, dia_diem_chieu, so_luong_cho_ngoi, id_phim, id)
        self.cur.execute(query, values)
        self.con.commit()
    def delete_lich_chieu(self, id):
        query = "DELETE FROM lich_chieu WHERE id=%s"
        self.cur.execute(query, (id,))
        self.con.commit()
    def select_phim_by_id(self, id):
        query = "SELECT ten_phim FROM phim WHERE id=%s"
        self.cur.execute(query, (id,))
        return self.cur.fetchone()
    def select_lich_chieu_by_id(self, id):
        query = "SELECT dia_diem_chieu FROM lich_chieu WHERE id=%s"
        self.cur.execute(query, (id,))
        return self.cur.fetchone()
    def select_id_by_name(self, name):
        query = "SELECT id FROM phim WHERE ten_phim=%s"
        self.cur.execute(query, (name,))
        return self.cur.fetchone()
    def select_id_by_name_lich_chieu(self, name):
        query = "SELECT id FROM lich_chieu WHERE dia_diem_chieu=%s"
        self.cur.execute(query, (name,))
        return self.cur.fetchone()
    #CRUD lich chieu

    def read_lich_chieu(self):
        self.cur.execute("SELECT * FROM lich_chieu")
        return self.cur.fetchall()

    def delete_lich_chieu(self, id):
        query = "DELETE FROM lich_chieu WHERE id=%s"
        self.cur.execute(query, (id,))
        self.con.commit()
    def select_phim_by_id(self, id):
        query = "SELECT ten_phim FROM phim WHERE id=%s"
        self.cur.execute(query, (id,))
        return self.cur.fetchone()
    def select_lich_chieu_by_id(self, id):
        query = "SELECT dia_diem_chieu FROM lich_chieu WHERE id=%s"
        self.cur.execute(query, (id,))
        return self.cur.fetchone()
    def select_id_by_name(self, name):
        query = "SELECT id FROM phim WHERE ten_phim=%s"
        self.cur.execute(query, (name,))
        return self.cur.fetchone()