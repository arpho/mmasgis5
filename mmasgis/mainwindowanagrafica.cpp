#include "mainwindowanagrafica.h"
#include "ui_anagrafica.h"

MainWindowAnagrafica::MainWindowAnagrafica(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindowAnagrafica)
{
    ui->setupUi(this);
}

MainWindowAnagrafica::~MainWindowAnagrafica()
{
    delete ui;
}
