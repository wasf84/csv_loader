# -*- coding: utf-8 -*-

import os, csv, pandas

from PyQt5.QtWidgets import QFileDialog, QMainWindow, QMessageBox, QTableWidgetItem
from main_csvloader import Ui_wndwCSVLoader

class App_csvloader(QMainWindow, Ui_wndwCSVLoader):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()

        self.hasHeaders = False

    def connectSignalsSlots(self):
        self.actionSair.triggered.connect(self.close)
        self.actionAbrir_arquivo.triggered.connect(self.abrirArquivo)
    
    def abrirArquivo(self):
        arq = QFileDialog.getOpenFileName(self, 'Abrir arquivo CSV', '', "Arquivos CSV (*.csv)")
        
        #with arq:
        df = pandas.read_csv(arq, header=None, delimiter='\t', keep_default_na=False, on_bad_lines='warn')
            #header = df.iloc[0]
            
            #print(df)

        #--------------------------------------------------------------- if arq:
            # df = pandas.read_csv(arq, header=None, delimiter=',', keep_default_na=False, on_bad_lines='skip')
            #----------------------------------------------- header = df.iloc[0]
#------------------------------------------------------------------------------ 
        #-------------------- ### o arquivo tem a primeira linha como cabeçalho?
            #---------------------------------- ret = QMessageBox.question(self,
                                       # "CSV Loader", "usar a 1a linha de cabeçalho?\n\n" + str(header.values),
                                       #------- QMessageBox.Ok | QMessageBox.No,
                                       #-------- defaultButton = QMessageBox.Ok)
            #----------------------------------------- if ret == QMessageBox.Ok:
                #--------------------------------------------------- df = df[1:]
#------------------------------------------------------------------------------ 
                #----------------- self.tblDados.setColumnCount(len(df.columns))
                #---------------------- self.tblDados.setRowCount(len(df.index))
#------------------------------------------------------------------------------ 
                #-------------------------------- for i in range(len(df.index)):
                    #-------------------------- for j in range(len(df.columns)):
                        # self.tblDados.setItem(i, j, QTableWidgetItem(str(df.iat[i, j])))
#------------------------------------------------------------------------------ 
                #------------------------------ for j in range(len(df.columns)):
                    #--------------------------- m = QTableWidgetItem(header[j])
                    #--------------- self.tblDados.setHorizontalHeaderItem(j, m)
#------------------------------------------------------------------------------ 
                #---------------------------------------- self.hasHeaders = True
#------------------------------------------------------------------------------ 
            #------------------------------------------------------------- else:
                #----------------- self.tblDados.setColumnCount(len(df.columns))
                #---------------------- self.tblDados.setRowCount(len(df.index))
#------------------------------------------------------------------------------ 
                #-------------------------------- for i in range(len(df.index)):
                    #-------------------------- for j in range(len(df.columns)):
                        # self.tblDados.setItem(i, j, QTableWidgetItem(str(df.iat[i, j])))
#------------------------------------------------------------------------------ 
                #------------------ for j in range(self.tblDados.columnCount()):
                    #------------------------------ m = QTableWidgetItem(str(j))
                    #--------------- self.tblDados.setHorizontalHeaderItem(j, m)
#------------------------------------------------------------------------------ 
                #--------------------------------------- self.hasHeaders = False
#------------------------------------------------------------------------------ 
            #---------------------------------------- self.tblDados.selectRow(0)
            #--------------------------- self.tblDados.resizeColumnsToContents()
            #------------------------------ self.tblDados.resizeRowsToContents()