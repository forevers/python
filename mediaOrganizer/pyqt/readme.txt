
// exif documentation
http://www.sno.phy.queensu.ca/~phil/exiftool/TagNames/EXIF.html

// ***** python virtual environments

// create some fresh venvs for 2.7 and 3.4
$ virtualenv --no-site-packages -p /usr/bin/python2.7 venv_2_7_qt4
$ virtualenv --no-site-packages -p /usr/bin/python3.4 venv_3_4_qt4
$ virtualenv --no-site-packages -p /usr/bin/python3.4 venv_3_4_qt5

// qt5 python 3.4 venv

$~source /venv_3_3_qt5/bin/activate
$cd venv_3_4_qt5
$mkdir build
$cd build
// download sip and qt5
// same sip as above
$tar -xvzf sip-4.19.tar.gz
$ cd sip-4.19
// http://pyqt.sourceforge.net/Docs/sip4/installation.html
// in regular shell perform $sudo apt-get install python3-dev 
python configure.py --qmake /path/to/Qt/5.2.1/gcc_64/bin/qmake --sip-incdir=/usr/include/python3.3m
(venv_3_4_qt5)/build/sip-4.19$ python configure.py
(venv_3_4_qt5)/build/sip-4.19$ sudo make install
//  pyqt5 into build dir https://www.riverbankcomputing.com/software/pyqt/download5
$tar -xvzf PyQt5_gpl-5.7.1.tar.gz
$ cd PyQt5_gpl-5.7.1
// select correct make and sip per this blog
https://michalcodes4life.wordpress.com/2014/03/16/pyqt5-python-3-3-in-virtualenv-on-ubuntu/
// The second path should point to the same path that SIP’s make install said it’s putting sip.h file in.
// first path is where is installed Qt
(venv_3_4_qt5)/build/PyQt5_gpl-5.7.1$ python configure.py --qmake ~/Qt/5.5/gcc_64/bin/qmake --sip-incdir=$HOME/python_venvs/venv_3_4_qt5/include/python3.4m
$ make
$ sudo make install
// there is a build error due to a packaging error
// qgeolocation.h was not packaged in PyQt
// see https://www.riverbankcomputing.com/pipermail/pyqt/2015-November/036584.html thread
// download Qt5 source or look into Qt5 install for this header and place into /venv_3_4_qt5/build/PyQt5_gpl-5.7.1/QtPositioning/qgeolocation.h
// steps for git clone source
$ git clone git://code.qt.io/qt/qt5.git
$ cd qt5
$ git checkout 5.5
$ perl init-repository
$ git checkout v5.5.0
$ git submodule update
// locate file at /qt5/qtlocation/src/positioning/qgeolocation.h and copy to PyQt location 
$ make
$ make install

// sequence for python 2.7 venv with qt4

$virtualenv --no-site-packages -p /usr/bin/python2.7 venv_2_7_qt4
$~source /venv_2_7_qt4/bin/activate
$cd venv_2_7_qt4
$mkdir build
$cd build
// download sip and qt4
http://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-4.12/PyQt4_gpl_x11-4.12.tar.gz
https://sourceforge.net/projects/pyqt/files/sip/sip-4.19/sip-4.19.tar.gz
// extract
$tar -xvzf PyQt4_gpl_x11-4.12.tar.gz
$tar -xvzf sip-4.19.tar.gz
$ cd sip-4.19
(venv_2_7_qt4)/build/sip-4.19$ sudo make install
$ python configure_ng.py 
$ make
$ sudo make install



// ***** Python Imaging Library
// PIL has not active development since 2009 … try Pillow Instead
// Pillow install directions
https://pillow.readthedocs.io/en/3.0.0/installation.html
http://docs.python-guide.org/en/latest/scenarios/imaging/
// note: must install some of the libraries (at least libjpeg) to pip install Pillow for Ubuntu 10-04


// ***** pyqt5 and uic module for dynamic loading of ui
http://pyqt.sourceforge.net/Docs/PyQt5/designer.html
// create python ui module from qt5 Qt Creator output
pyuic5 mediahomewindow.ui -o mediahomewindow.py
