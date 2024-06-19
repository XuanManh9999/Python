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
    def insert_ve(self, ten_ve, loai_ve, vi_tri_ngoi, gia_ve, so_luong_ve, thoi_han_ve, id_phim, id_lich_chieu):
        query = "INSERT INTO ve (ten_ve, loai_ve, vi_tri_ngoi, gia_ve, so_luong_ve, thoi_han_ve, id_phim, id_lich_chieu) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        self.cur.execute(query, (ten_ve, loai_ve, vi_tri_ngoi, gia_ve, so_luong_ve, thoi_han_ve, id_phim, id_lich_chieu))
        self.con.commit()

    def read_ve(self):
        self.cur.execute("SELECT * FROM ve")
        return self.cur.fetchall()

    def update_ve(self, id, ten_ve, loai_ve, vi_tri_ngoi, gia_ve, so_luong_ve, thoi_han_ve, id_phim, id_lich_chieu):
        query = "UPDATE ve SET ten_ve=%s, loai_ve=%s, vi_tri_ngoi=%s, gia_ve=%s, so_luong_ve=%s, thoi_han_ve=%s, id_phim=%s, id_lich_chieu=%s WHERE id=%s"
        values = (ten_ve, loai_ve, vi_tri_ngoi, gia_ve, so_luong_ve, thoi_han_ve, id_phim, id_lich_chieu, id)
        self.cur.execute(query, values)
        self.con.commit()

    def delete_ve(self, id):
        query = "DELETE FROM ve WHERE id=%s"
        self.cur.execute(query, (id,))
        self.con.commit()
