from PySide6.QtWidgets import QApplication,QWidget,QLabel ,QPushButton ,QLineEdit , QFrame, QGraphicsDropShadowEffect
from PySide6.QtGui import QColor,QFontDatabase, QFont ,QPixmap
import sys
import random

app = QApplication(sys.argv)
window = QWidget()
window.resize(1000,600)
window.setWindowTitle("Malar Recistancy")
window.setObjectName("w1")
window.setStyleSheet("""
    QWidget#w1{
        background-color: rgb(17, 19, 27);

    }
""")

class componands:
    
    
    def font_style(self,n):
        
        self.font_db = ["ds","lux"]
        self.load_font = QFontDatabase.addApplicationFont(f"../assets/fonts/{self.font_db[n-1]}.ttf")
        self.font_fname = QFontDatabase.applicationFontFamilies(self.load_font)[0]
        self.font_styl = QFont(self.font_fname)
       
        return self.font_styl     

    def sw(self):
        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(25)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(3)
        self.shadow.setColor(QColor(100, 90, 200, 130))
        return self.shadow
    
    def button_comp(self,name,obname,x,y,w,h,window):
        
        self.button = QPushButton(name,window)
        self.button.setObjectName(obname)
        self.button.move(x,y)
        self.button.resize(w,h)
        self.button.setStyleSheet(f"""
            
    QPushButton#{obname} {{
                color: white;
                font-size: 20px;
                font-weight: bold;
        
                background: qlineargradient(
                    x1:0, y1:0,
                    x2:1, y2:1,
                    stop:0 #5F5D70,
                    stop:0.5 #525360,
                    stop:1 #3E4145
                );
        
                border: 1px solid #474747;
                border-radius: 25px;
                
                }}
                QPushButton#{obname}:hover {{
                    border: 1px solid #5F5F5F;
                }}
            
        """)
        self.shadow = self.sw()
        self.button.setGraphicsEffect(self.shadow)
        return self.button
    
    def frame_comp(self,obname,x,y,w,h,window):
        
        self.f_shadow = QGraphicsDropShadowEffect()
        self.f_shadow.setBlurRadius(30)
        self.f_shadow.setXOffset(0)
        self.f_shadow.setYOffset(0)
        self.f_shadow.setColor(QColor(112, 112, 112, 255))
        
            
        self.frame = QFrame(window)
        self.frame.setObjectName(obname)
        self.frame.move(x,y)
        self.frame.resize(w,h)
        self.frame.setGraphicsEffect(self.f_shadow)
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
        self.font_design = self.font_style(fs)
        self.lable.setFont(self.font_design)
        self.font_design.setPointSize(size)
        
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
    
        

if __name__ == "__main__":
    
    comp = componands()
    
    #Let's Build 
    
    
    window.show()
    sys.exit(app.exec())

