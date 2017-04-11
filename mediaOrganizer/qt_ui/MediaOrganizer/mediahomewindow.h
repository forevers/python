#ifndef MEDIAHOMEWINDOW_H
#define MEDIAHOMEWINDOW_H

#include <QMainWindow>

namespace Ui {
class MediaHomeWindow;
}

class MediaHomeWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MediaHomeWindow(QWidget *parent = 0);
    ~MediaHomeWindow();

private:
    Ui::MediaHomeWindow *ui;
};

#endif // MEDIAHOMEWINDOW_H
