#include <QtGui/QApplication>
#include "mainwindowanagrafica.h"

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    MainWindowAnagrafica w;
    w.show();
    
    return a.exec();
}
