# -*- coding: utf-8 -*-

import os, csv, pandas

from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QMessageBox, QTableWidgetItem, QLabel
from main_csvloader import Ui_wndwCSVLoader

class App_csvloader(QMainWindow, Ui_wndwCSVLoader):
    # ----------------------------------------------------------- #
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()

        # Macetinho para mostrar informacoes na barra de status
        self.lblInfo = QLabel(text="")
        self.stsInformacoes.addWidget(self.lblInfo)
    # ----------------------------------------------------------- #

    # ----------------------------------------------------------- #
    def connectSignalsSlots(self):
        self.actionSair.triggered.connect(self.close)
        self.actionAbrir_arquivo.triggered.connect(self.abrirArquivo)
    # ----------------------------------------------------------- #
    
    # ----------------------------------------------------------- #
    def abrirArquivo(self):
        arq, _ = QFileDialog.getOpenFileName(self, 'Abrir arquivo CSV', QDir.currentPath(), "Arquivos CSV (*.csv)")
        
        if arq:
            df = pandas.read_csv(arq, header=None, delimiter='\t', keep_default_na=False, on_bad_lines='warn')
            header = df.iloc[0]

            ### o arquivo tem a primeira linha como cabeçalho?
            ret = QMessageBox.question(self,
                                       "CSV Loader", "usar a 1a linha de cabeçalho?\n\n" + str(header.values),
                                       QMessageBox.Ok | QMessageBox.No,
                                       defaultButton = QMessageBox.Ok)

            if ret == QMessageBox.Ok:
                df = df[1:]

                self.tblDados.setColumnCount(len(df.columns))
                self.tblDados.setRowCount(len(df.index))

                for i in range(len(df.index)):
                    for j in range(len(df.columns)):
                        self.tblDados.setItem(i, j, QTableWidgetItem(str(df.iat[i, j])))

                for j in range(len(df.columns)):
                    m = QTableWidgetItem(header[j])
                    self.tblDados.setHorizontalHeaderItem(j, m)

            else:
                self.tblDados.setColumnCount(len(df.columns))
                self.tblDados.setRowCount(len(df.index))

                for i in range(len(df.index)):
                    for j in range(len(df.columns)):
                        self.tblDados.setItem(i, j, QTableWidgetItem(str(df.iat[i, j])))

                for j in range(self.tblDados.columnCount()):
                    m = QTableWidgetItem(str(j))
                    self.tblDados.setHorizontalHeaderItem(j, m)

            self.tblDados.selectRow(0)
            self.tblDados.resizeColumnsToContents()
            self.tblDados.resizeRowsToContents()
            self.mostraInfo(nomeArquivo=arq)
    # ----------------------------------------------------------- #

    # ----------------------------------------------------------- #
    def mostraInfo(self, nomeArquivo):
        # A barra de status tem um widget QLabel para mostrar informacoes de "path do arquivo | n de linhas | n de colunas" do grid

        # Limpa a barra de status com informacoes passadas
        self.stsInformacoes.removeWidget(self.lblInfo)

        linhas = str(self.tblDados.rowCount())
        colunas = str(self.tblDados.columnCount())
        texto = "Arquivo: " + nomeArquivo + " | Linhas: " + linhas  + " | Colunas: " + colunas

        self.lblInfo = QLabel(text = texto)
        self.stsInformacoes.addWidget(self.lblInfo)
    # ----------------------------------------------------------- #