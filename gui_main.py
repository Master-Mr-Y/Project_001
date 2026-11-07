from PySide6.QtWidgets import(
    QApplication,
    QWidget,
    QLabel ,
    QPushButton ,
    QLineEdit ,
    QFrame,
    QGraphicsDropShadowEffect,
    QDateEdit,
    QCalendarWidget,
    QComboBox
)
from PySide6.QtGui import QColor,QFontDatabase, QFont ,QPixmap
from PySide6.QtCore import QDate,Qt
import sys
import random

app = QApplication(sys.argv)
window = QWidget()
window.resize(1100,600)
window.setWindowTitle("Malar Recistancy")
window.setObjectName("w1")
window.setStyleSheet("""
    QWidget#w1{
        background-color: rgb(17, 19, 27);

    }
""")
window2 = QWidget()
window2.resize(350,450)
window2.setWindowTitle("Submit")
window2.setObjectName("w2")
window2.setStyleSheet("""
    QWidget#w2{
        background-color: rgb(17, 19, 27);

    }
""")
window3 = QWidget()
window3.resize(350,450)
window3.setWindowTitle("Preview")
window3.setObjectName("w3")
window3.setStyleSheet("""
    QWidget#w3{
        background-color: rgb(17, 19, 27);

    }
""")
class componands:
    
    
    def font_style(self,n,size):
        
        self.font_db = ["ds","lux","Amar","pop","ren","zyd","ply","digi"]
        self.load_font = QFontDatabase.addApplicationFont(f"../assets/fonts/{self.font_db[n-1]}.ttf")
        self.font_fname = QFontDatabase.applicationFontFamilies(self.load_font)[0]
        self.font_styl = QFont(self.font_fname)
        self.font_styl.setPointSize(size)
       
        return self.font_styl     

    def sw(self):
        
        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(25)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(3)
        self.shadow.setColor(QColor(100, 90, 200, 130))
        return self.shadow
    def sw_frm(self):
        self.f_shadow = QGraphicsDropShadowEffect()
        self.f_shadow.setBlurRadius(30)
        self.f_shadow.setXOffset(0)
        self.f_shadow.setYOffset(0)
        self.f_shadow.setColor(QColor(0, 0, 0, 255))
        return self.f_shadow
    def in_sw_frm(self):
            self.f_shadow = QGraphicsDropShadowEffect()
            self.f_shadow.setBlurRadius(30)
            self.f_shadow.setXOffset(0)
            self.f_shadow.setYOffset(0)
            self.f_shadow.setColor(QColor(0, 0, 0, 255))
            return self.f_shadow 
    
    def button_comp(self,name,obname,x,y,w,h,size,fs,window):
        
        self.button = QPushButton(name,window)
        self.button.setObjectName(obname)
        self.button.move(x,y)
        self.button.resize(w,h)
        self.font_design = self.font_style(fs,size)
        self.button.setFont(self.font_design)
        return self.button
    
    
    def frame_comp(self,obname,x,y,w,h,window):
        
        
        
            
        self.frame = QFrame(window)
        self.frame.setObjectName(obname)
        self.frame.move(x,y)
        self.frame.resize(w,h)
        
        self.frame.setStyleSheet("""
            QFrame {
                background-color: rgb(22, 25, 33);
                border-radius: 12px;
            }
        """)
        return self.frame
    
    def lable_comp(self,name,obname,size,fs,x,y,window):
        self.lable = QLabel(name,window)
        self.lable.setObjectName(obname)
        self.lable.move(x,y)
        self.font_design = self.font_style(fs,size)
        self.lable.setFont(self.font_design)
       # self.font_design.setPointSize(size)
        
        return self.lable
    
    def img_comp(self,img_name,obname,x,y,w,h,window):
        self.img_lable = QLabel(window)
        self.img_lable.setObjectName(obname)
        self.load_img = QPixmap(f"../assets/{img_name}")
        self.img_lable.setPixmap(self.load_img)
        self.img_lable.setScaledContents(True)
        self.img_lable.setGeometry(x,y,w,h)
        
        return self.img_lable
         
    def input_comp(self,plcehol,obname,x,y,w,h,window):
        self.input_box = QLineEdit(window)
        self.input_box.setObjectName(obname)
        self.input_box.setPlaceholderText(plcehol)
        self.input_box.setGeometry(x,y,w,h)
        self.input_box.setStyleSheet(f"""
            QLineEdit#{obname}{{
                padding:3px;
                padding-left:5px;
                color:white;
                border:none;
                background-color: transparent;
            }}
        """)
        return self.input_box
    def calander_design(self):
        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(False)
        self.calendar.setVerticalHeaderFormat(
            QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader
        )
        self.calendar.setFixedSize(380, 300)
        self.calendar.setStyleSheet("""
            QCalendarWidget {
                background-color: #2D2D2D;
                color: white;
                border: 1px solid #FFFFFF;
                border-radius: 15px;
            }
             QCalendarWidget QWidget {
                    background-color: #1C1C1C;
                    color: white;
                }
            QCalendarWidget QToolButton {
                    color: white;
                    background-color:#1C1C1C;
                    border: none;
                    border-radius: 3px;
                    padding: 5px;
                    font-size: 15px;
                    font-weight: bold;
                }
            QCalendarWidget QMenu {
                    background-color:#1C1C1C;
                    color: white;
                }
            QCalendarWidget QAbstractItemView {
                    background-color: rgb(17, 19, 27);
                    color: white;
                    selection-background-color:rgb(17, 19, 27) ;
                    selection-color: white;
                    outline: none;
                    font-size: 14px;
                    
                }    
            QCalendarWidget QAbstractItemView:enabled {
                    color: white;
                }    
            """
            )
        return self.calendar
    
    def calander_comp(self,obname,x,y,w,h,fs,window):    
        self.date = QDateEdit(window)
        self.date.setGeometry(x,y,w,h)
        self.date.setObjectName(obname)
        # Calendar popup enable
        self.date.setCalendarPopup(True)
        # Current date set
        self.date.setDate(QDate.currentDate())
        self.date.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.date.setStyleSheet("""
        QDateEdit {
            background-color: transparent;
            color: white;
            
            border-radius: 30px;
            padding:0px;
            
            font-weight: bold;
        } """)
        self.date.setCalendarWidget(self.calander_design())
        self.date.setFont(self.font_style(fs,12))
        return self.date
    def choice_box(self,obname,fs,size,x,y,w,h,itms,window):
        self.box = QComboBox(window)
        self.box.setGeometry(x,y,w,h)
        self.box.addItems(itms)
        self.box.setObjectName(obname)
        self.box.setStyleSheet(f"""
           QComboBox#{obname}{{
               background-color: transparent;
               border: none; 
           }}
        """)
        self.box.setFont(self.font_style(fs,size))
        return self.box
        

if __name__ == "__main__":
    
    comp = componands()

    #shadow get
    
    #frame shadow
    frm_sw1 = comp.sw_frm()
    frm_sw2 = comp.sw_frm()
    frm_sw3 = comp.sw_frm()
    frm_sw4 = comp.sw_frm()
    #btn shadow
    btn_sw1 = comp.sw_frm()
    btn_sw2 = comp.sw_frm()
    btn_sw3 = comp.sw_frm()
    btn_sw4 = comp.sw_frm()
    btn_sw5 = comp.sw_frm()
    btn_sw6 = comp.sw_frm()
    btn_sw7 = comp.sw_frm()
    btn_sw8 = comp.sw_frm()
    btn_sw9 = comp.sw_frm()
    btn_sw10 = comp.sw_frm()
    btn_sw11 = comp.sw_frm()
    btn_sw12 = comp.sw_frm()
    
    
    #input frame shwdow
    in_sw1 = comp.in_sw_frm()
    in_sw2 = comp.in_sw_frm()
    in_sw3 = comp.in_sw_frm()
    in_sw4 = comp.in_sw_frm()
    in_sw5 = comp.in_sw_frm()
    in_sw6 = comp.in_sw_frm()
    in_sw7 = comp.in_sw_frm()
    in_sw8 = comp.in_sw_frm()
        
    #Let's Build
    
    #frames
    side_frame = comp.frame_comp("side_frame",20,20,200,570,window)
    main_frame = comp.frame_comp("main_frame",240,20,840,470,window)
    botm_frame = comp.frame_comp("botm_frame",240,520,840,60,window)
    side_frame.setGraphicsEffect(frm_sw1)
    main_frame.setGraphicsEffect(frm_sw2) 
    botm_frame.setGraphicsEffect(frm_sw3) 
    
    
    #side frame inside         
    logo = comp.img_comp("../assets/mr_logo.png","logo",55,50,75,110,side_frame)
    side_btm_img = comp.img_comp("../assets/side_btm1.png","side_btm",0,450,250,100,side_frame)
    logo_name = comp.lable_comp("MALAR","logo_name",25,3,47,175,side_frame)
    logo_name = comp.lable_comp("RESIDENCY","logo_name",25,3,23,205,side_frame)
    
    #main edit
    
    button_clicked_cound = 0 
    rooms = ""
    s1 = comp.button_comp("S1","r1",40,20,60,60,15,3,main_frame)
    s2 = comp.button_comp("S2","r2",140,20,60,60,15,3,main_frame)
    s3 = comp.button_comp("S3","r3",240,20,60,60,15,3,main_frame)
    s4 = comp.button_comp("S4","r4",340,20,60,60,15,3,main_frame)
    s5 = comp.button_comp("S5","r5",440,20,60,60,15,3,main_frame)
    s6 = comp.button_comp("S6","r6",540,20,60,60,15,3,main_frame)
    s7 = comp.button_comp("S7","r7",640,20,60,60,15,3,main_frame)
    s8 = comp.button_comp("S8","r8",740,20,60,60,15,3,main_frame)
    
    s1.setStyleSheet("""
      QPushButton#r1{
          color:white;
          border-radius:30px;
          border: 1px solid rgb(34, 33, 33);
          background-color: rgb(22, 25, 33);
          
      }
    """)
    def s1_clicked():
        global button_clicked_cound
        global rooms
        s1.setStyleSheet("""
        QPushButton#r1{
            color:white;
            border-radius:30px;
            border: 1px solid rgb(0, 0, 0);
            background-color: rgb(61, 61, 61);
            
        }
        """)
        button_clicked_cound+=1
        rooms += "S1 "
        
    s2.setStyleSheet("""
      QPushButton#r2{
          color:white;
          border-radius:30px;
          border: 1px solid rgb(34, 33, 33);
          background-color: rgb(22, 25, 33);
      }
    """)
    def s2_clicked():
        global button_clicked_cound
        global rooms
        s2.setStyleSheet("""
        QPushButton#r2{
            color:white;
            border-radius:30px;
            border: 1px solid rgb(0, 0, 0);
            background-color: rgb(61, 61, 61);
            
        }
        """)
        button_clicked_cound+=1
        rooms += "S2 "
    s3.setStyleSheet("""
      QPushButton#r3{
          color:white;
          border-radius:30px;
          border: 1px solid rgb(34, 33, 33);
          background-color: rgb(22, 25, 33);
          
      }
    """)
    def s3_clicked():
        global button_clicked_cound
        global rooms
        s3.setStyleSheet("""
        QPushButton#r3{
            color:white;
            border-radius:30px;
            border: 1px solid rgb(0, 0, 0);
            background-color: rgb(61, 61, 61);
            
        }
        """)
        button_clicked_cound+=1
        rooms += "S3 "
    s4.setStyleSheet("""
      QPushButton#r4{
          color:white;
          border-radius:30px;
          border: 1px solid rgb(34, 33, 33);
          background-color: rgb(22, 25, 33);
          
      }
    """)
    def s4_clicked():
        global button_clicked_cound
        global rooms
        s4.setStyleSheet("""
        QPushButton#r4{
            color:white;
            border-radius:30px;
            border: 1px solid rgb(0, 0, 0);
            background-color: rgb(61, 61, 61);
        }
        """)
        button_clicked_cound+=1
        rooms += "S4 "
    s5.setStyleSheet("""
      QPushButton#r5{
          color:white;
          border-radius:30px;
          border: 1px solid rgb(34, 33, 33);
          background-color: rgb(22, 25, 33);
          
          
      }
    """)
    def s5_clicked():
        global button_clicked_cound
        global rooms
        s5.setStyleSheet("""
        QPushButton#r5{
            color:white;
            border-radius:30px;
            border: 1px solid rgb(0, 0, 0);
            background-color: rgb(61, 61, 61);
        }
        """)
        button_clicked_cound+=1
        rooms += "S5 "
    s6.setStyleSheet("""
      QPushButton#r6{
          color:white;
          border-radius:30px;
          border: 1px solid rgb(34, 33, 33);
          background-color: rgb(22, 25, 33);
          
          
      }
    """)
    def s6_clicked():
        global button_clicked_cound
        global rooms
        s6.setStyleSheet("""
        QPushButton#r6{
            color:white;
            border-radius:30px;
            border: 1px solid rgb(0, 0, 0);
            background-color: rgb(61, 61, 61);
        }
        """)
        button_clicked_cound+=1
        rooms += "S6 "
    s7.setStyleSheet("""
      QPushButton#r7{
          color:white;
          border-radius:30px;
          border: 1px solid rgb(34, 33, 33);
          background-color: rgb(22, 25, 33);
          
      }
    """)
    def s7_clicked():
        global button_clicked_cound
        global rooms
        s7.setStyleSheet("""
        QPushButton#r7{
            color:white;
            border-radius:30px;
            border: 1px solid rgb(0, 0, 0);
            background-color: rgb(61, 61, 61);
        }
        """)
        button_clicked_cound+=1
        rooms += "S7 "
    s8.setStyleSheet("""
      QPushButton#r8{
          color:white;
          border-radius:30px;
          border: 1px solid rgb(34, 33, 33);
          background-color: rgb(22, 25, 33);
          
      }
    """)
    def s8_clicked():
        global button_clicked_cound
        global rooms
        s8.setStyleSheet("""
        QPushButton#r8{
            color:white;
            border-radius:30px;
            border: 1px solid rgb(0, 0, 0);
            background-color: rgb(61, 61, 61);
            
        }
        """)
        button_clicked_cound+=1
        rooms += "S8 "

        
        
    s1.setGraphicsEffect(btn_sw1)
    s2.setGraphicsEffect(btn_sw2)
    s3.setGraphicsEffect(btn_sw3)
    s4.setGraphicsEffect(btn_sw4)
    s5.setGraphicsEffect(btn_sw5)
    s6.setGraphicsEffect(btn_sw6)
    s7.setGraphicsEffect(btn_sw7)
    s8.setGraphicsEffect(btn_sw8)
    
    s1.clicked.connect(s1_clicked)
    s2.clicked.connect(s2_clicked)
    s3.clicked.connect(s3_clicked)
    s4.clicked.connect(s4_clicked)
    s5.clicked.connect(s5_clicked)
    s6.clicked.connect(s6_clicked)
    s7.clicked.connect(s7_clicked)
    s8.clicked.connect(s8_clicked)
        
        
    
    """ dummy = comp.button_comp("dummy","dm",20,300,50,50,15,3,main_frame)
    def dmy():
        global button_clicked_cound
        global rooms
        print("btn clickd coun:",button_clicked_cound)
        print(rooms)
    dummy.clicked.connect(dmy)   """  
    
    #40,20,60,60,
    #input btns
    in_frame01 = comp.frame_comp("in1",10,120,400,60,main_frame)
    in_frame02 = comp.frame_comp("in2",450,120,380,60,main_frame)
    in_frame03 = comp.frame_comp("in3",10,200,580,60,main_frame)
    in_frame04 = comp.frame_comp("in4",630,200,200,60,main_frame)
    
    def cal_design(obname):
        cal = f"""
         QLabel#{obname}{{
                 color:gray;
            }}
        """
        return cal
    
    arr_date_lab = comp.lable_comp("Arr.date","ad",12,3,70,280,main_frame)
    arr_date_lab.setStyleSheet(cal_design("ad"))
    arr_time_lab = comp.lable_comp("Arr.time","at",12,3,290,280,main_frame)
    arr_time_lab.setStyleSheet(cal_design("at"))
        
    dep_date_lab = comp.lable_comp("Dep.date","dd",12,3,490,280,main_frame)
    dep_date_lab.setStyleSheet(cal_design("dd"))
    dep_time_lab = comp.lable_comp("Dep.time","dt",12,3,690,280,main_frame)
    dep_time_lab.setStyleSheet(cal_design("dt"))
        
    
    in_frame05 = comp.frame_comp("in5",10,320,200,60,main_frame)
    in_frame06 = comp.frame_comp("in6",220,320,200,60,main_frame)
    in_frame07 = comp.frame_comp("in7",430,320,200,60,main_frame)
    in_frame08 = comp.frame_comp("in8",640,320,190,60,main_frame)
    
    
    
    usr_logo = comp.img_comp("../assets/usr.png","usr_logo",10,15,30,30,in_frame01)
    id_logo = comp.img_comp("../assets/id.png","id_logo",10,15,30,30,in_frame02)
    add_logo = comp.img_comp("../assets/loc.png","add_logo",10,15,30,30,in_frame03)
    per_logo = comp.img_comp("../assets/add_mem.png","per_logo",10,15,30,30,in_frame04)
    arr_date = comp.img_comp("../assets/arr_date.png","arr_date_logo",10,15,30,30,in_frame05)
    arr_time = comp.img_comp("../assets/arr_time.png","arr_time_logo",10,15,30,30,in_frame06)
    dep_date = comp.img_comp("../assets/dep_date.png","dep_date_logo",10,15,30,30,in_frame07)
    dep_time = comp.img_comp("../assets/dep_time.png","dep_time_logo",10,15,30,30,in_frame08)
    
    
    user_name = comp.input_comp("Enter User Name..!","usr_nm",45,10,300,40,in_frame01)
    user_id = comp.input_comp("Enter User GSTIN/AADHAR..!","usr_id",45,10,300,40,in_frame02)
    user_add = comp.input_comp("Enter User Address..!","usr_loc",45,10,500,40,in_frame03)
    tot_per = comp.input_comp("Total Persons..!","tot_per",45,10,150,40,in_frame04)
    date_arr = comp.calander_comp("date_arr",40,10,130,40,8,in_frame05)
    time_items = ["07:00 PM","07:00 AM","12:00 AM","12:00 PM",]
    time_arr = comp.choice_box("time_arr",8,12,60,10,100,40,time_items,in_frame06)
    date_dep = comp.calander_comp("date_dep",40,10,130,40,8,in_frame07)
    time_dep = comp.choice_box("time_dep",8,12,60,10,100,40,time_items,in_frame08)
    
    
    #ac non ac block
    
    #ac_label = comp.lable_comp("AC","ac_lable",15,3,50,420,main_frame)
    room_type = ""
    ac_btn = comp.button_comp("|    AC","ac_btn",60,400,150,50,13,3,main_frame)
    non_ac_btn = comp.button_comp("  |  Non-AC","non_ac_btn",600,400,150,50,13,3,main_frame)
    
    
    ac_logo = comp.img_comp("../assets/ac.png","ac_logo",10,11,30,30,ac_btn)
    ac_btn.setStyleSheet("""
         QPushButton#ac_btn{
             background-color:rgb(22, 25, 33) ;
             border:1px solid rgb(17, 19, 27);
             border-radius:20px;
             padding-left:10px;
         }
    """)
    ac_logo.setStyleSheet("""
        QLabel#ac_logo{
            background-color: transparent;
        }
     """)
    def ac_btn_clicked():
        global room_type
        room_type = "AC"
        print("selected Room type is:",room_type)
        ac_btn.setStyleSheet("""
             QPushButton#ac_btn{
                 background-color:#414141;
                 border:1px solid rgb(17, 19, 27);
                 border-radius:20px;
                 padding-left:10px;
             }
        """)
        non_ac_btn.setStyleSheet("""
                 QPushButton#non_ac_btn{
                     background-color:rgb(22, 25, 33) ;
                     border:1px solid rgb(17, 19, 27);
                     border-radius:20px;
                     padding-left:10px;
                 }
            """)
        
    
    non_ac_logo = comp.img_comp("../assets/fan.png","non_ac_logo",10,11,30,30,non_ac_btn)
    non_ac_btn.setStyleSheet("""
         QPushButton#non_ac_btn{
             background-color:rgb(22, 25, 33) ;
             border:1px solid rgb(17, 19, 27);
             border-radius:20px;
             padding-left:10px;
         }
    """)
    non_ac_logo.setStyleSheet("""
        QLabel#non_ac_logo{
            background-color: transparent;
            
        }
     """)
    def non_ac_btn_clicked():
        global room_type
        room_type = "NONAC"
        print("selected Room type is:",room_type)
        non_ac_btn.setStyleSheet("""
             QPushButton#non_ac_btn{
                 background-color:#414141;
                 border:1px solid rgb(17, 19, 27);
                 border-radius:20px;
                 padding-left:10px;
             }
             
        """)    
        ac_btn.setStyleSheet("""
             QPushButton#ac_btn{
                 background-color:rgb(22, 25, 33) ;
                 border:1px solid rgb(17, 19, 27);
                 border-radius:20px;
                 padding-left:10px;
             }
        """)
        
    ac_btn.clicked.connect(ac_btn_clicked)   
    non_ac_btn.clicked.connect(non_ac_btn_clicked)   
    
    #bottom bar design
    
    reset_btn = comp.button_comp("Reset","reset_btn",40,10,150,40,13,3,botm_frame)
    
    reset_logo = comp.img_comp("../assets/reset.png","reset_logo",10,9,25,25,reset_btn)
    reset_btn.setStyleSheet("""
         QPushButton#reset_btn{
             background-color:#687EB1 ;
             border:1px solid rgb(17, 19, 27);
             border-radius:20px;
             padding-left:10px;
         }
    """)
    reset_logo.setStyleSheet("""
        QLabel#reset_logo{
            background-color: transparent;
        }
     """)
    def reset_btn_clicked():
        global window
        global room_type
        global rooms
        room_type = ""
        rooms = ""
        user_name.clear()
        user_add.clear()
        user_id.clear()
        tot_per.clear()
        def s_btn_design(props,n):
            if n == 0:
                design = f"""
                  QPushButton#{props}{{
                        color:white;
                        border-radius:30px;
                        border: 1px solid rgb(34, 33, 33);
                        background-color: rgb(22, 25, 33);
                        
                    }}
                """
            
                return design
            else:
                design = f"""
                      QPushButton#{props}{{
                            color:white;
                            border-radius:30px;
                            border: 1px solid rgb(34, 33, 33);
                            background-color: rgb(22, 25, 33);
                            border-radius:20px;
                            padding-left:10px;
                        }}
                    """
                return design
        s1.setStyleSheet(s_btn_design("r1",0))
        s2.setStyleSheet(s_btn_design("r2",0))
        s3.setStyleSheet(s_btn_design("r3",0))
        s4.setStyleSheet(s_btn_design("r4",0))
        s5.setStyleSheet(s_btn_design("r5",0))
        s6.setStyleSheet(s_btn_design("r6",0))
        s7.setStyleSheet(s_btn_design("r7",0))
        s8.setStyleSheet(s_btn_design("r8",0))
        ac_btn.setStyleSheet(s_btn_design("ac_btn",1))
        non_ac_btn.setStyleSheet(s_btn_design("non_ac_btn",1))
        
        print("Reset btn Clicked")
    
    
    reset_btn.clicked.connect(reset_btn_clicked)

#submit btn    


    sub_btn = comp.button_comp("Submit","sub_btn",450,10,150,40,13,3,botm_frame)
        
    sub_logo = comp.img_comp("../assets/submit.png","sub_logo",10,7,22,22,sub_btn)
    sub_btn.setStyleSheet("""
         QPushButton#sub_btn{
             background-color:#69B168 ;
             border:1px solid rgb(17, 27, 17);
             border-radius:20px;
             padding-left:10px;
         }
    """)
    sub_logo.setStyleSheet("""
        QLabel#sub_logo{
            background-color: transparent;
        }
     """)

#priview btn    


    prw_btn = comp.button_comp("Preview","prw_btn",650,10,150,40,13,3,botm_frame)
        
    prw_logo = comp.img_comp("../assets/think.png","prw_logo",10,7,22,22,prw_btn)
    prw_btn.setStyleSheet("""
         QPushButton#prw_btn{
             background-color:#BB5353 ;
             border:1px solid rgb(17, 27, 17);
             border-radius:20px;
             padding-left:10px;
         }
    """)
    prw_logo.setStyleSheet("""
        QLabel#prw_logo{
            background-color: transparent;
        }
     """)
    
    l1=""
    def prw_clicked():
        global l1
    
        try:
            l1.deleteLater()
        except:
            pass
    
        name = user_name.text()
    
        l1 = comp.lable_comp(
            f"Name:  {name}",
            "l1", 15, 3, 30, 50, window3
        )
    
        window3.show()

    
        
        
    prw_btn.clicked.connect(prw_clicked) 
       




    
    
    
    in_frame01.setGraphicsEffect(in_sw1)
    in_frame02.setGraphicsEffect(in_sw2)
    in_frame03.setGraphicsEffect(in_sw3)
    in_frame04.setGraphicsEffect(in_sw4)
    in_frame05.setGraphicsEffect(in_sw5)
    in_frame06.setGraphicsEffect(in_sw6)
    in_frame07.setGraphicsEffect(in_sw7)
    in_frame08.setGraphicsEffect(in_sw8)
    ac_btn.setGraphicsEffect(btn_sw9)
    non_ac_btn.setGraphicsEffect(btn_sw10)
    reset_btn.setGraphicsEffect(btn_sw11)
    
        
    window.show()
    sys.exit(app.exec())

