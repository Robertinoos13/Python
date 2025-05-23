import sys
from PyQt6.QtWidgets import QApplication, QPushButton, QWidget, QLabel, QSlider, QLineEdit
from PyQt6.QtCore import Qt
import torch
import model_ai # The script for AI outputs

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(500, 200, 600, 300)
        self.setWindowTitle("Phone Classifier App")

        # Main Variables
        self.ram_input = 1
        self.rom_input = 2
        self.nm_input = 90
        self.g_input = 3
        self.hz_input = 30
        self.cam_res_input = 360
        self.mah_input = 1000
        self.year = 2025

        self.output_ai = 0

        # General Setup
        self.init()

    def init(self):
        self.main_text = QLabel("Choose phone specifications", parent=self)
        self.main_text.setGeometry(155, 10, 265, 40)
        self.main_text.setStyleSheet("font-size: 20px; border: 2px solid black")

        # RAM part
        self.ram_text = QLabel("RAM (GB)", parent=self)
        self.ram_text.setGeometry(0, 230, 70, 40)

        self.ram_slider = QSlider(Qt.Orientation.Vertical, self)
        self.ram_slider.setMinimum(1)
        self.ram_slider.setMaximum(32)
        self.ram_slider.setValue(self.ram_input)
        self.ram_slider.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.ram_slider.setTickInterval(4)
        self.ram_slider.valueChanged.connect(self.change_ram)
        self.ram_slider.setGeometry(15, 90, 20, 155)
        
        self.ram_show = QLabel(f"{self.ram_input}", parent=self)
        self.ram_show.setGeometry(19, 260, 15, 15)
        self.ram_show.setStyleSheet("background-color: orange; color: black; text-align: center;")
        self.ram_show.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # ROM part
        self.rom_text = QLabel("ROM (GB)", parent=self)
        self.rom_text.setGeometry(70, 230, 70, 40)

        self.rom_slider = QSlider(Qt.Orientation.Vertical, self)
        self.rom_slider.setMinimum(1)
        self.rom_slider.setMaximum(2048)
        self.rom_slider.setValue(self.rom_input)
        self.rom_slider.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.rom_slider.setTickInterval(64)
        self.rom_slider.valueChanged.connect(self.change_rom)
        self.rom_slider.setGeometry(85, 90, 20, 155)
        
        self.rom_show = QLabel(f"{self.rom_input}", parent=self)
        self.rom_show.setGeometry(85, 260, 25, 15)
        self.rom_show.setStyleSheet("background-color: orange; color: black; text-align: center;")
        self.rom_show.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # NM part
        self.nm_text = QLabel("NM (CPU)", parent=self)
        self.nm_text.setGeometry(140, 230, 70, 40)

        self.nm_slider = QSlider(Qt.Orientation.Vertical, self)
        self.nm_slider.setMinimum(1)
        self.nm_slider.setMaximum(90)
        self.nm_slider.setValue(self.nm_input)
        self.nm_slider.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.nm_slider.setTickInterval(10)
        self.nm_slider.valueChanged.connect(self.change_nm)
        self.nm_slider.setGeometry(155, 90, 20, 155)
        
        self.nm_show = QLabel(f"{self.nm_input}", parent=self)
        self.nm_show.setGeometry(155, 260, 25, 15)
        self.nm_show.setStyleSheet("background-color: orange; color: black; text-align: center;")
        self.nm_show.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # G part
        self.g_text = QLabel("G (NET)", parent=self)
        self.g_text.setGeometry(215, 230, 70, 40)

        self.g_slider = QSlider(Qt.Orientation.Vertical, self)
        self.g_slider.setMinimum(3)
        self.g_slider.setMaximum(5)
        self.g_slider.setValue(self.g_input)
        self.g_slider.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.g_slider.setTickInterval(1)
        self.g_slider.valueChanged.connect(self.change_g)
        self.g_slider.setGeometry(225, 90, 20, 155)
        
        self.g_show = QLabel(f"{self.g_input}", parent=self)
        self.g_show.setGeometry(225, 260, 25, 15)
        self.g_show.setStyleSheet("background-color: orange; color: black; text-align: center;")
        self.g_show.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # HZ part
        self.hz_text = QLabel("HZ (display)", parent=self)
        self.hz_text.setGeometry(275, 230, 70, 40)

        self.hz_slider = QSlider(Qt.Orientation.Vertical, self)
        self.hz_slider.setMinimum(30)
        self.hz_slider.setMaximum(240)
        self.hz_slider.setValue(self.hz_input)
        self.hz_slider.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.hz_slider.setTickInterval(30)
        self.hz_slider.valueChanged.connect(self.change_hz)
        self.hz_slider.setGeometry(295, 90, 20, 155)
        
        self.hz_show = QLabel(f"{self.hz_input}", parent=self)
        self.hz_show.setGeometry(295, 260, 25, 15)
        self.hz_show.setStyleSheet("background-color: orange; color: black; text-align: center;")
        self.hz_show.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Camera Resolution part
        self.cam_res_text = QLabel("CAM Res (p)", parent=self)
        self.cam_res_text.setGeometry(355, 230, 70, 40)

        self.cam_res_slider = QSlider(Qt.Orientation.Vertical, self)
        self.cam_res_slider.setMinimum(360)
        self.cam_res_slider.setMaximum(8640)
        self.cam_res_slider.setValue(self.cam_res_input)
        self.cam_res_slider.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.cam_res_slider.setTickInterval(1080)
        self.cam_res_slider.valueChanged.connect(self.change_cam_res)
        self.cam_res_slider.setGeometry(370, 90, 20, 155)
        
        self.cam_res_show = QLabel(f"{self.cam_res_input}", parent=self)
        self.cam_res_show.setGeometry(370, 260, 25, 15)
        self.cam_res_show.setStyleSheet("background-color: orange; color: black; text-align: center;")
        self.cam_res_show.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # mAh part
        self.mah_text = QLabel("mAh", parent=self)
        self.mah_text.setGeometry(440, 230, 70, 40)

        self.mah_slider = QSlider(Qt.Orientation.Vertical, self)
        self.mah_slider.setMinimum(1000)
        self.mah_slider.setMaximum(9999)
        self.mah_slider.setValue(self.mah_input)
        self.mah_slider.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.mah_slider.setTickInterval(500)
        self.mah_slider.valueChanged.connect(self.change_mah)
        self.mah_slider.setGeometry(440, 90, 20, 155)
        
        self.mah_show = QLabel(f"{self.mah_input}", parent=self)
        self.mah_show.setGeometry(440, 260, 25, 15)
        self.mah_show.setStyleSheet("background-color: orange; color: black; text-align: center;")
        self.mah_show.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Year Part
        self.year_edit = QLineEdit("", parent=self)
        self.year_edit.setGeometry(500, 100, 100, 30)
        self.year_edit.setPlaceholderText("year when rating")

        # Input Button Part
        self.predict_button = QPushButton("PREDICT", self)
        self.predict_button.setGeometry(500, 240, 90, 50)
        self.predict_button.clicked.connect(self.make_predict)

        # Result Text Part
        self.output_text = QLabel("  Its a simple app with AI what predict if a phone with some specifications its a LOW-END, MID-ENTRY LEVEL, MID-RANGE, MID-SUPERIOR or HIGH-END on X year", self)
        self.output_text.setGeometry(500, 140, 100, 100)
        self.output_text.setWordWrap(True)
        self.output_text.setStyleSheet("border: 1px solid black; font-size: 9px")
    
    def make_predict(self):
        try:
            self.output_text.setText("Loading...")
            self.year = int(self.year_edit.text())
            input_ai =  model_ai.torch.tensor([[self.ram_input,self.rom_input,self.nm_input,self.g_input,self.hz_input,self.cam_res_input,self.mah_input,self.year]],dtype=torch.float32)
            self.output_ai = model_ai.model(input_ai)
            self.output_text.setText(f"I think, your specifications in {self.year} was a {self.rate_final_output()} phone")
        except Exception as e:
            self.output_text.setText("An error occurred. Please check the inputs.")
            print(f"Error: {e}")

    def change_ram(self, value):
        self.ram_input = value
        print(f"RAM seted to: {self.ram_input}")
        self.ram_show.setText(f"{self.ram_input}")

    def change_rom(self, value):
        self.rom_input = value
        print(f"ROM seted to: {self.rom_input}")
        self.rom_show.setText(f"{self.rom_input}")
        self.rom_slider.setValue(self.rom_input)

    def change_nm(self, value):
        self.nm_input = value
        print(f"NM seted to: {self.nm_input}")
        self.nm_show.setText(f"{self.nm_input}")
        self.nm_slider.setValue(self.nm_input)

    def change_g(self, value):
        self.g_input = value
        print(f"G seted to: {self.g_input}")
        self.g_show.setText(f"{self.g_input}")
        self.g_slider.setValue(self.g_input)

    def change_hz(self, value):
        #if value % 5 == 0:
            self.hz_input = value
            print(f"HZ seted to: {self.hz_input}")
            self.hz_show.setText(f"{self.hz_input}")
            self.hz_slider.setValue(self.hz_input)
        #else:
            self.hz_slider.setValue(self.hz_input)

    def change_cam_res(self, value):
        self.cam_res_input = value
        print(f"Camera Resolution seted to: {self.cam_res_input}")
        self.cam_res_show.setText(f"{self.cam_res_input}")
        self.cam_res_slider.setValue(self.cam_res_input)  

    def change_mah(self, value):
        self.mah_input = value
        print(f"Camera Resolution seted to: {self.mah_input}")
        self.mah_show.setText(f"{self.mah_input}")
        self.mah_slider.setValue(self.mah_input)  

    def rate_final_output(self):
        if self.output_ai > 0 and self.output_ai < 1.5:
            self.final_output = "Low End"
            return self.final_output
        elif self.output_ai > 1.5 and self.output_ai < 2.5:
            self.final_output = "Mid Entry Level"
            return self.final_output
        elif self.output_ai > 2.5 and self.output_ai < 3.5:
            self.final_output = "Mid Range"
            return self.final_output
        elif self.output_ai > 3.5 and self.output_ai < 4.5:
            self.final_output = "Mid Superior"
            return self.final_output
        elif self.output_ai > 4.5 and self.output_ai < 5.5:
            self.final_output = "High End"
            return self.final_output
        else:
            self.final_output = f"TRY OTHER SPECS"
            return self.final_output
        
#if __name__ == "__main__":
app = QApplication(sys.argv)

window = MyApp()
window.show()

sys.exit(app.exec())