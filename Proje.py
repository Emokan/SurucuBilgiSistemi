from tkinter import *
from tkinter import ttk
import tkinter as tk

import sqlite3


def silmeformu():
    global silinecekkod,y2pos
    y2pos = y2pos + 20
    
    silinecekkod = StringVar()

    sil_win = Toplevel(win)
    sil_win.geometry("300x200")
    sil_win.title("Silme Sayfasi")

    ttk.Label(sil_win, text="Silmek istediğiniz şoförün kodunu giriniz.").place(x=40,y=20)
    ttk.Entry(sil_win, font=("Arial"), textvariable= silinecekkod ).place(x=40,y=50)
    # cur.execute('delete from sofor where Kod = silinecekkod ;')
   
    ttk.Button(sil_win, text = "Sil",command = lambda : [(silme(),close2(sil_win))]).place(x=100,y=120)

def silme():
    kod_değeri = silinecekkod.get()
    cur.execute('insert into silinecek (kod) values (?)', (kod_değeri,))
    # cur.execute('delete from sofor where Id = from  silinecek silId')
    # 
    cur.execute('DELETE FROM sofor WHERE kod = ?', (kod_değeri,))
    con.commit()
    # DELETE person, company
    # FROM person
    # INNER JOIN company ON person.company_id = company.id
    # WHERE company.id = 1;

def close(window):
    window.destroy()
    
    ttk.Label(win, text= "Yeni Eklenenler(Uygulamayi tekrar açtiginizda listeye eklenecekler):", style="BW.TLabel").place(x=550,y=60)
    
    ttk.Label(win, text = "Ad ", style="BW.TLabel").place(x=550,y=80)
    ttk.Label(win, text= "Soyad", style="BW.TLabel").place(x=640,y=80)
    ttk.Label(win, text = "Sürücü Kodu", style="BW.TLabel").place(x=740,y=80)

    ttk.Label(win, text = "#################################", style="BW.TLabel").place(x=550,y=100)

    
    ttk.Label(win, text = ""+isim.get()+"", style="BW.TLabel").place(x=550,y=ypos)
    ttk.Label(win, text = ""+soyisim.get()+"", style="BW.TLabel").place(x=640,y=ypos)
    ttk.Label(win, text = ""+şoförkod.get()+"", style="BW.TLabel").place(x=740,y=ypos)

       

def close2(sil_win):
    sil_win.destroy()
    
    ttk.Label(win, text= "Silinecekler (Uygulamayi tekrar açtiginizda silinecekler): ",style = "BW.TLabel").place(x=550,y=500)
    
    ttk.Label(win, text = "Ad ", style="BW.TLabel").place(x=550,y=520)
    ttk.Label(win, text= "Soyad", style="BW.TLabel").place(x=640,y=520)
    ttk.Label(win, text = "Sürücü Kodu", style="BW.TLabel").place(x=740,y=520)

    ttk.Label(win, text = "#################################", style="BW.TLabel").place(x=550,y=540)

    ttk.Label(win, text = ""+silinecekkod.get()+" No lu sürücü listeden kaldirilacaktir .", style="BW.TLabel").place(x=550,y=y2pos)
    
# def close3(win):
#      win.destroy()
    
# def update():
#     python = sys.executable
#     os.execl(python, python, * sys.argv)

def formukaydet(new_win):
        global kod
        kod = şoförkod.get()
        cur.execute(" Select kod from sofor ")
        result = cur.fetchall()
        length = len(result)
        
        for i in range(length):
                if kod == result[i][0]:
                    errortab(kod)
                else: 
                    cur.execute('insert into sofor (kod,ad,soyad) values (?,?,?)',(şoförkod.get(),isim.get(),soyisim.get()))
                     
                
        con.commit()

def errortab(kod):
    error_win = Toplevel(win)
    error_win.geometry("750x500")
    error_win.title("HATA!")

    ttk.Label(error_win, text=""+(kod)+" Numarali Kullanici Zaten Bulunuyor! Tekrar Deneyiniz.").place(x=20, y=20)
     
           
def yenibilgigir():
    global isim, soyisim, şoförkod, ypos
    ypos = ypos + 20
    
    
    isim = StringVar()
    soyisim = StringVar()
    şoförkod= StringVar()
    
    new_win = Toplevel(win)
    new_win.geometry("750x500")
    new_win.title("Bilgi Formlari Listesi")
    
    ttk.Label(new_win, text="Şoför İsmi : ").place(x=20, y=20)
    ttk.Entry(new_win, font=("Arial"), textvariable=isim).place(x=20, y=40)
    
    ttk.Label(new_win, text="Şoför Soyadi : ").place(x=20, y=70)
    ttk.Entry(new_win, font=("Arial"), textvariable=soyisim).place(x=20, y=90)

    ttk.Label(new_win, text="Şoför Kodu : ").place(x=20,y=120)
    ttk.Entry(new_win, font=("Arial"),textvariable=şoförkod).place(x=20,y=140)

    kaydet = ttk.Button(new_win, text="Kaydet", width=7, command=lambda: [formukaydet(new_win), close(new_win)])
    kaydet.place(x=620, y=460)

con = sqlite3.connect('C:\\Users\\emirh\\Masaüstü\\PY\\Py3\\Takip.db')

cur = con.cursor()

win = Tk()
# Define the geometry
win.geometry("1000x800")

#Application Title  
win.title("Sürücü Bilgileri")  
#Set App icon  

photo = PhotoImage(file = 'C:\\Users\\emirh\\Masaüstü\\PY\\Py3\\Caricon.png')
win.iconphoto(False, photo)
win.configure(bg='#D0CFE1')

style = ttk.Style()
style.configure("BW.TLabel", background="#D0CFE1",)

colour1 = '#020f12'
colour2 = '#05d7ff'
colour3 = '#65e7ff'
colour4 = 'BLACK'

y2pos=540
ypos=100
isim = StringVar()
soyisim = StringVar()
şoförkod= StringVar()

cur.execute('select * from sofor order by Id')

rows = cur.fetchall()

Yps = 120


for row in rows:
    
    ttk.Label(win, text = row[0],style="BW.TLabel").place(x=10,y=Yps)
    ttk.Label(win, text = row[1],style="BW.TLabel").place(x=90,y=Yps)
    ttk.Label(win, text = row[2],style="BW.TLabel").place(x=190,y=Yps)
    # ttk.Label(win, text = row[3],style="BW.TLabel").place(x=10,y=Yps)
    
    
    Yps = Yps + 20
ttk.Label(win, text = "**********************Güncel Liste*********************", style="BW.TLabel").place(x=10,y=60)
ttk.Label(win, text = "#####################################", style="BW.TLabel").place(x=10,y=100)
 

# Create Buttons in the frame
button1 = tk.Button(win, text="Yeni Bilgi gir",background=colour2,
                         foreground=colour4,
                         activebackground=colour3,
                         activeforeground=colour4,
                         highlightthickness=2,
                         highlightbackground=colour2,
                         highlightcolor='WHITE',
                         border=0,
                         cursor='hand1',
                         font=('Arial', 10,'bold'),
                         width=11,
                         height=1,
                         padx=8,
                         pady=3,
                         
                         command= yenibilgigir).place(x=650, y=10)

button2 = tk.Button(win, text="Bilgi Sil",background=colour1,
                         foreground=colour2,
                         activebackground=colour3,
                         activeforeground=colour4,
                         highlightthickness=2,
                         highlightbackground=colour2,
                         highlightcolor='WHITE',
                         border=0,
                         cursor='hand1',
                         font=('Arial', 10,'bold'),
                         width=11,
                         height=1,
                         padx=8,
                         pady=3,
                         
                         command= silmeformu).place(x=810, y=10)
# kaydetveçikbutton = tk.Button(win, text="Kaydet ve Çik",background=colour1,
#                          foreground=colour2,
#                          activebackground=colour3,
#                          activeforeground=colour4,
#                          highlightthickness=2,
#                          highlightbackground=colour2,
#                          highlightcolor='WHITE',
#                          border=0,
#                          cursor='hand1',
#                          font=('Arial', 10,'bold'),
#                          width=11,
#                          height=1,
#                          padx=8,
#                          pady=3,
                         
#                          ).place(x=810, y=600)  #command= close3

adlabel = ttk.Label(win, text = "Ad ", style="BW.TLabel").place(x=110,y=80)
soyadLabel =ttk.Label(win, text= "Soyad", style="BW.TLabel").place(x=190,y=80)
idlLabel= ttk.Label(win, text = "Sürücü Kodu", style="BW.TLabel").place(x=10,y=80)

label1 = ttk.Label(win, text="Şoför Bilgileri", font='Consolas 15', style="BW.TLabel").pack()


win.mainloop()

