#include "mediahomewindow.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    MediaHomeWindow w;
    w.show();

    return a.exec();
}
