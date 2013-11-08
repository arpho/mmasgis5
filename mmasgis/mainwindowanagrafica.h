#ifndef MAINWINDOWANAGRAFICA_H
#define MAINWINDOWANAGRAFICA_H

#include <QMainWindow>

namespace Ui {
class MainWindowAnagrafica;
}

class MainWindowAnagrafica : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindowAnagrafica(QWidget *parent = 0);
    ~MainWindowAnagrafica();
    
private:
    Ui::MainWindowAnagrafica *ui;
};

#endif // MAINWINDOWANAGRAFICA_H
