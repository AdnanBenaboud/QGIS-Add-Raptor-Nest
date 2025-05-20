from qgis.PyQt.QtWidgets import *
from .impact_table_dialog import Ui_DlgImpact

class DlgTable(QDialog, Ui_DlgImpact):
    def __init__(self):
        super(DlgTable, self).__init__()
        self.setupUi(self)