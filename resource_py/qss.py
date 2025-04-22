lightqss= '''
QWidget:window {
	    background: #eef3f7;
	    color: #000000;
	    border-radius: 30px;
	}

	QtextEdit {
	    background-color: #D7DFE7;
	    color: #000000;
	    border-radius: 30px;
	}

	QPushButton {
	    border-radius: 5px;
	    border:none
	}

    #pushButton {
        background-color: #D7DFE7;
        padding: 1px;
	    border-radius: 5px;
        border-style: solid;
        border-width: 1px;
	}

    #pushButton:hover {
	    background-color: #DF7020;
	}

	#Form2 QPushButton {
        padding: 1px;
	    border-radius: 5px;
        border-style: solid;
        border-width: 1px;

	}

	QPushButton:hover {
	    background-color: #DF7020;
	}

	QComboBox{
	    background-color: #D7DFE7;
	    color: #000000;
	    border-radius: 10px;
	    padding-left: 10px;
	    border-width: 3px;
	    border-style: solid;
	    border-color: #eef3f7;
	}
	QComboBox:hover {
	    background-color: #DF7020;
	    color: #ffffff
	}
	QComboBox QAbstractItemView {
	    color: #000000;
	    background-color: #eef3f7;
	}
	QComboBox::drop-down {
	    border-radius: 20px;
	}

	QCheckBox::indicator {
	    background-color: #0F367E;
	    width: 7px;
	    height:7px;
	    border-radius: 2px;
	    border: 2px solid #0F367E;
	}


	QCheckBox::indicator:checked{
	    background-color: #0F367E;
	}
	QCheckBox::indicator:unchecked{
	    background-color: #eef3f7;
	}

	QLabel{
	    background-color: #eef3f7;
	    color: #000000;
	}
    QTextEdit{
        border:none;
    }
'''

darkqss = '''
QWidget:window {
    background: #181F25;
    color: #ffffff;
    font-family: "Consola";
}
 
QTextBrowser {
    background-color: #202932;
    color: #ffffff;
    border-radius: 30px;
}
 
QPushButton {
    background-color: #00001b;
    border:none
}
QPushButton:hover {
    background-color: #DF7020;
}
 
QComboBox{
    background-color: #181F25;
    color: #ffffff;
    border-radius: 10px;
    padding-left: 10px;
    border-width: 1px;
    border-style: solid;
    border-color: #202932;
}
QComboBox:hover {
    background-color: #DF7020;
}
QComboBox QAbstractItemView {
    color: #ffffff;
    background-color: #202932;
}
QComboBox::drop-down {
    border-radius: 20px;
}
 
QCheckBox::indicator {
    background-color: #00006d;
    width: 30px;
    height: 30px;
    border-radius: 5px;
    border: 2px solid #202932;
}
QCheckBox::indicator:checked:hover {
    background-color: #DF7020;
}
QCheckBox::indicator:unchecked:hover {
    background-color: #DF7020;
}
QCheckBox::indicator:checked{
    background-color: #296EB3;
}
QCheckBox::indicator:unchecked{
    background-color: #eff3ff;
}
 
QLabel{
background-color: #181F25;
color: #ffffff;
}
'''

