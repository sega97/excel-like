'''
Author      : Muhamad Aliyin Nur
Refference  : stackoverflow.com, daniweb.com, docs.python.org, google.com.
Notes       : The basic of this script is "individual lines coloured" which is coded by zoe. 
              Here : https://www.daniweb.com/software-development/python/threads/128350/starting-wxpython-gui-code/8#post1221367
'''
import wx,os,sys,ast,math
from decimal import *
from wx.lib.mixins.listctrl import ColumnSorterMixin
import wx.lib.mixins.listctrl  as  listmix
global data
#load data nilai dan nama siswa
dbs = "ips.txt"
nama_siswa = "nama_siswa.txt"

class EditableListCtrl(wx.ListCtrl, listmix.TextEditMixin):
    ''' TextEditMixin allows any column to be edited. ''' 
    #TextEditMixin memperbolehkan kolom untuk di edit  
    #----------------------------------------------------------------------
    def __init__(self, parent, ID=wx.ID_ANY, pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=0):
        """Constructor"""
        #inisialisasi gui ListCtrl
        wx.ListCtrl.__init__(self, parent, ID, pos, size, style)
        listmix.TextEditMixin.__init__(self)

class Core(wx.Frame):
    def __init__(self,parent,id):
        # mengatur tinggi dan lebar aplikasi
        APPWIDTH = 1200
        APPHEIGHT = 550
        w = wx.SystemSettings.GetMetric(wx.SYS_SCREEN_X)
        h = wx.SystemSettings.GetMetric(wx.SYS_SCREEN_Y)
        # Centre of the screen
        # mengambil titik tengah layar
        x = w / 2
        y = h / 2
        # Minus application offset
        # dikurangi tinggi dan lebar app , dibagi 2
        x -= (APPWIDTH / 2)
        y -= (APPHEIGHT / 2)
        # titik tengah
        center=(x, y)
        # inisialisasi Gui. judul, posisi, dll.
        wx.Frame.__init__(self,parent,id,'Shinichi{Nilai Rata-Rata}',pos=center,size = (1200,550),style = wx.DEFAULT_FRAME_STYLE & ~wx.MAXIMIZE_BOX ^ wx.RESIZE_BORDER)
        panel = wx.Panel(self)
        self.data = data
        self.nama_ = nama_
        # create the list control
        # membuat list control / list box
        self.lc = EditableListCtrl(panel, wx.ID_ANY,(1,22), size=(1192, 480),
        style=wx.LC_REPORT|wx.SUNKEN_BORDER|wx.LC_HRULES|wx.LB_SINGLE)
        # memanggil fungsi loadlist
        self.loadList()
        # setting label, tombol, dkk.
        set1text = wx.StaticText(panel, label = "SDN Majumundur - ",pos=(2,4))
        set2text = wx.StaticText(panel, label = "Kelas 100 - ",pos=(108,4))
        set3text = wx.StaticText(panel, label = "2030/2031 ",pos=(160,4))
        set4text = wx.StaticText(panel, label = "DAFTAR NILAI RAPORT",pos=(2,505))
        self.button1 = wx.Button(panel, label="HITUNG RATA-RATA",pos=(1053,0),size=(140,22))
        # mengkaitkan tombol hitung rata-rata dengan fungsi hitung_
        self.button1.Bind( wx.EVT_LEFT_DOWN, self.hitung_ )

    def loadList(self):
        # first the columns with header titles
        # setting kolom dan judulnya
        self.lc.InsertColumn(col=0,heading="Nama Siswa",width=170)
        self.lc.InsertColumn(col=1,heading="T.1",width=50,format=wx.LIST_FORMAT_CENTER)
        self.lc.InsertColumn(col=2,heading="T.2",format=wx.LIST_FORMAT_CENTER,width=50)
        self.lc.InsertColumn(col=3,heading="T.3",width=80,format=wx.LIST_FORMAT_CENTER)
        self.lc.InsertColumn(col=4,heading="T.4",width=80,format=wx.LIST_FORMAT_CENTER)
        self.lc.InsertColumn(col=5,heading="PAI",format=wx.LIST_FORMAT_CENTER,width=50)
        self.lc.InsertColumn(col=6,heading="Penjas",width=50,format=wx.LIST_FORMAT_CENTER)
        self.lc.InsertColumn(col=7,heading="SBDP",format=wx.LIST_FORMAT_CENTER,width=50)
        self.lc.InsertColumn(col=8,heading="Mulok Jaseng",width=90,format=wx.LIST_FORMAT_CENTER)
        self.lc.InsertColumn(col=9,heading="B.Indonesia",width=80,format=wx.LIST_FORMAT_CENTER)
        self.lc.InsertColumn(col=10,heading="B.Arab",format=wx.LIST_FORMAT_CENTER,width=80)
        self.lc.InsertColumn(col=11,heading="B.Jepang",width=60,format=wx.LIST_FORMAT_CENTER)
        self.lc.InsertColumn(col=12,heading="Jumlah",format=wx.LIST_FORMAT_CENTER,width=80)
        self.lc.InsertColumn(col=13,heading="Rata-Rata",width=200,format=wx.LIST_FORMAT_CENTER)
        #self.lc.InsertColumn(col=14,heading="4",width=40)
        #self.lc.InsertColumn(col=15,heading="R3",format=wx.LIST_FORMAT_CENTER,width=60)
        #self.lc.InsertColumn(col=16,heading="R",format=wx.LIST_FORMAT_CENTER,width=140)
        # now each data row
        # setting tiap baris/row
        indexes = 0
        # mendefinisikan variable indexes, dan nol
        nol = "0"
        # mengisi row dengan nama, dari file text yang sudah di load
        for keys, namas in self.nama_.items():
            # set max_rows, change if need be
            # set jumlah maksimum row
            max_rowss = 1000
            # also sets/updates row index starting at 0
            # mengisi row
            self.lc.InsertStringItem(max_rowss, namas.upper())
        self.lc.InsertStringItem(28, "JUMLAH")
        self.lc.InsertStringItem(29, "RATA - RATA")
        # mengisi row dengan nilai, dari file text yang sudah di load
        for key, val in self.data.items():
            index_ = -1
            # memberi warna pada tiap kolom, hijau dan putih
            if indexes % 2:
                self.lc.SetItemBackgroundColour(indexes, "white")
            else:
                self.lc.SetItemBackgroundColour(indexes, "green")
            # proses pengisian row dengan nilai, total 13 kolom
            # kolom 11 keatas di isi dengan nilai nol
            for x in range(1,14):
                if x < 13:
                    if index_ < 12:
                        index_ += 1
                        isi = val[index_]
                    else:
                        isi = nol
                self.lc.SetStringItem(indexes, x, isi)
            indexes += 1
#manual :   self.lc.SetStringItem(indexes, 1, val[0]), self.lc.SetStringItem(indexes, 2, val[1]), dst...


    def hitung_(self, event):
        #r1 = 5, r2 = 10, r3 = 15
        count = self.lc.GetItemCount()
        column = -1
        jumlah = 0
        semua = []
        halaman = -1
        jumlah_2 = 0
        semua_2 = []
        # proses menghitung 11 kolom yg terisi nilai
        # variable count berisi total seluruh baris/row (dari atas kebawah)
        for kolom in range(1,12):
            for row in range(count):
                # pengecualian baris 29 dan 30
                if row < 28:
                    item = self.lc.GetItem(itemId=row, col=kolom)
                    jumlah_2 += int(item.GetText())
                    #print item.GetText()
            semua_2.append(jumlah_2)
            jumlah_2 = 0
        #print semua_2
        # penjumlahan tiap kolom(dari kiri ke kanan)
        for rows in range(count):
            for row in range(count):
                column += 1
                item = self.lc.GetItem(itemId=rows, col=column)
                # hanya menjumlahkan tipe int, jika string(nama), lewat
                try:
                    if column < 12:
                        jumlah += int(item.GetText())
                except:
                    pass
                #print item.GetText()
            semua.append(jumlah)
            jumlah = 0
            column = -1
        #print semua
        # r1_ dan r2_ mengisi seluruh baris di kolom 12 dan 13
        # r1_ hasil jumlah, r2_ rata rata
        # anggap saja r1_ dan r2_ buku :D
        for r1_ in self.data.items():
            halaman += 1
            #print str(semua[halaman])
            self.lc.SetStringItem(halaman, 12, str(semua[halaman]))
        halaman = -1
        for r2_ in self.data.items():
            halaman += 1
            self.lc.SetStringItem(halaman, 13, str(Decimal(Decimal(semua[halaman])/Decimal(11)).quantize(Decimal('.01'), rounding=ROUND_DOWN)))
        # mengisi baris 28 dan 29, jumlah dan rata-rata
        # index semua_2 hanya ada 11 (dihitung dari 0)
        for xx in range(1,12):
            self.lc.SetStringItem(28, xx, str(semua_2[xx-1]))
            self.lc.SetStringItem(29, xx, str(Decimal(Decimal(semua_2[xx-1])/Decimal(28)).quantize(Decimal('.01'), rounding=ROUND_DOWN)))
            
        
    def onAction(self, event):
        print "tes"
    

def baca():
    global whip,nama_
    with open(dbs, "rb") as f:
        isi_lama = f.read()
        whip = ast.literal_eval("{"+isi_lama+"}")
    with open(nama_siswa, "rb") as f:
        isi_nama = f.read()
        nama_ = ast.literal_eval("{"+isi_nama+"}")


if __name__=='__main__':
    baca()
    data = whip
    app = wx.App(False)
    frame = Core(parent=None,id=-1)
    frame.Show()
    app.MainLoop()
