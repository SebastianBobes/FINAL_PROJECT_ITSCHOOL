# qpixmap = QPixmap("EUROAVIA_Logo.png")
#         self.label_BACKGROUND.setPixmap(qpixmap)
#         qpixmap = QPixmap("plane-semi-flat-b2d996.webp")
#         self.label_plane_logo.setPixmap(qpixmap)
#         qpixmap = QPixmap("EUROAVIA_Logo.png")
#         self.label_9_LOGO.setPixmap(qpixmap)
#         qpixmap = QPixmap("1643641029799.png")
#         self.label_upb_logo.setPixmap(qpixmap)
#         self.pushButton.clicked.connect(self.add_student)
#
#     def add_student(self):
#         last_name = self.NUME_lineEdit.text()
#         first_name = self.PRENUME_lineEdit.text()
#         middle_name = self.PRENUME_2_lineEdit.text()
#         telephone_number = self.NUMAR_DE_TELEFON_lineEdit.text()
#         study_year = self.AN_DE_STUDIU_comboBox.currentText()
#         college = self.FACULTATE_comboBox.currentText()
#         department = self.DEPARTAMENT_comboBox.currentText()
#         student1 = Student(last_name,first_name,middle_name,telephone_number,study_year,college,department)
#         print(student1.department)
#         print(student1.college)