import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QMessageBox, QListWidgetItem
)
from PyQt5.uic import loadUi

class ExpenseCalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("edit.ui", self)

        self.total = 0

        # Signals and slots
        self.btnTambah.clicked.connect(self.tambah_pengeluaran)
        self.btnTentang.clicked.connect(self.tampilkan_tentang)

    def tambah_pengeluaran(self):
        jumlah = self.inputJumlah.text()
        kategori = self.comboKategori.currentText()
        metode = ""

        if self.radioTunai.isChecked():
            metode = "Tunai"
        elif self.radioEwallet.isChecked():
            metode = "E-Wallet"
        elif self.radioKartu.isChecked():
            metode = "Kartu"

        kuantitas = self.spinJumlah.value()

        if not jumlah.isdigit():
            QMessageBox.warning(self, "Peringatan", "Masukkan jumlah yang valid!")
            return

        jumlah_int = int(jumlah) * kuantitas
        self.total += jumlah_int

        item_teks = f"{kategori} - {metode} - {kuantitas} x Rp{jumlah} = Rp{jumlah_int}"
        self.listPengeluaran.addItem(QListWidgetItem(item_teks))

        self.labelTotal.setText(f"Total Pengeluaran: Rp {self.total}")
        self.inputJumlah.clear()

    def tampilkan_tentang(self):
        QMessageBox.information(self, "Tentang", "Aplikasi Kalkulator Pengeluaran ini dibuat untuk tidak boros dan yang pasti untuk mini project Visual Programming menggunakan PyQt5 guyss.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExpenseCalculator()
    window.show()
    sys.exit(app.exec_())
