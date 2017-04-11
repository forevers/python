#include "mediahomewindow.h"
#include "ui_mediahomewindow.h"

MediaHomeWindow::MediaHomeWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MediaHomeWindow)
{
    ui->setupUi(this);
}

MediaHomeWindow::~MediaHomeWindow()
{
    delete ui;
}
