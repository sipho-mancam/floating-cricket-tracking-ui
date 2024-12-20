from .view import CricketTrackingWidget, load_style_sheet
from PyQt5.QtWidgets import QApplication
import sys


def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(load_style_sheet('./main_styles.qss'))
    cricket_view = CricketTrackingWidget(None)
    cricket_view.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()