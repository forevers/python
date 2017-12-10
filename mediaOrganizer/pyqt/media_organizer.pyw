'''
 MIT License

Copyright (c) 2017 Steve Evers

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import sys
from os import path
from mediahomewindow import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QGraphicsScene, QGraphicsPixmapItem, QProgressBar
from named_media import NamedMedia
import shutil, os
import pickle


class TimeOffset(QtWidgets.QWidget):
    """Widget for accumulating a time offset value.

        A time offset value entered into this widget will emit a signal on update_time.

        Attributes:
            show(self, visible):
                visible - visibility boolean

        Signals:
            upate_time: cumulative time offset signal
    """

    def __init__(self, parent = None):
        """Initializer for TimeOffset widget.
        """

        QtWidgets.QWidget.__init__(self, parent)

        # hour offset
        self._hour_label = QtWidgets.QLabel(self.tr("H"))
        self._hour_spin_box = QtWidgets.QSpinBox()
        self._hour_spin_box.setRange(-59, 59)
        self._hour_spin_box.setFixedWidth(40)
        self._hour_line_edit = QtWidgets.QLineEdit()
        self._hour_line_edit.setText('0')
        # minute offsets
        self._minute_label = QtWidgets.QLabel(self.tr("M"))
        self._minute_spin_box = QtWidgets.QSpinBox()
        self._minute_spin_box.setRange(-59, 59)
        self._minute_spin_box.setFixedWidth(40)
        self._minute_line_edit = QtWidgets.QLineEdit()
        self._minute_line_edit.setText('0')
        # second offset
        self._sec_label = QtWidgets.QLabel(self.tr("S"))
        self._sec_spin_box = QtWidgets.QSpinBox()
        self._sec_spin_box.setRange(-50, 59)
        self._sec_spin_box.setFixedWidth(40)
        self._sec_line_edit = QtWidgets.QLineEdit()
        self._sec_line_edit.setText('0')
        # msec offset
        self._msec_label = QtWidgets.QLabel(self.tr("MS"))
        self._msec_spin_box = QtWidgets.QSpinBox()
        self._msec_spin_box.setRange(-59, 59)
        self._msec_spin_box.setFixedWidth(40)
        self._msec_line_edit = QtWidgets.QLineEdit()
        self._msec_line_edit.setValidator(QtGui.QIntValidator(-59, 59))
        self._msec_line_edit.setText('0')

        # hour signals
        self._hour_spin_box.valueChanged.connect(self._hour_spinner)
        self._hour_line_edit.returnPressed.connect(self._hour_edit)
        self._hour_line_edit.editingFinished.connect(self._hour_edit)
        # minute signals
        self._minute_spin_box.valueChanged.connect(self._minute_spinner)
        self._minute_line_edit.returnPressed.connect(self._minute_edit)
        self._minute_line_edit.editingFinished.connect(self._minute_edit)
        # second signals
        self._sec_spin_box.valueChanged.connect(self._sec_spinner)
        self._sec_line_edit.returnPressed.connect(self._sec_edit)
        self._sec_line_edit.editingFinished.connect(self._sec_edit)
        # msec signals
        self._msec_spin_box.valueChanged.connect(self._msec_spinner)
        self._msec_line_edit.returnPressed.connect(self._msec_edit)
        self._msec_line_edit.editingFinished.connect(self._msec_edit)

        # offset widget render
        self._layout = QtWidgets.QGridLayout(self)
        self._layout.addWidget(self._hour_label, 0, 0)
        self._layout.addWidget(self._hour_spin_box, 1, 0)
        self._layout.addWidget(self._hour_line_edit, 2, 0)
        self._layout.addWidget(self._minute_label, 0, 1)
        self._layout.addWidget(self._minute_spin_box, 1, 1)
        self._layout.addWidget(self._minute_line_edit, 2, 1)
        self._layout.addWidget(self._sec_label, 0, 2)
        self._layout.addWidget(self._sec_spin_box, 1, 2)
        self._layout.addWidget(self._sec_line_edit, 2, 2)
        self._layout.addWidget(self._msec_label, 0, 3)
        self._layout.addWidget(self._msec_spin_box, 1, 3)
        self._layout.addWidget(self._msec_line_edit, 2, 3)

        # TODO - configure via api
        # TODO - plugin for QT Creator
        self.setGeometry(200, 15, 180, 100)

        self.show(False)


    def show(self, visible):
        """ Visibility control.

        Shows or hides widget elements.

        Args:
            visible: visibility boolean.from calendar import monthrange

        Returns:
            none

        Raises:
            none
        """

        # TODO - iterate
        if (visible):
            self._hour_label.show()
            self._hour_spin_box.show()
            self._hour_line_edit.show()
            self._minute_label.show()
            self._minute_spin_box.show()
            self._minute_line_edit.show()
            self._sec_label.show()
            self._sec_spin_box.show()
            self._sec_line_edit.show()
            self._msec_label.show()
            self._minute_spin_box.show()
            self._msec_line_edit.show()
        else:
            self._hour_label.hide()
            self._hour_spin_box.hide()
            self._hour_line_edit.hide()
            self._minute_label.hide()
            self._minute_spin_box.hide()
            self._minute_line_edit.hide()
            self._sec_label.hide()
            self._sec_spin_box.hide()
            self._sec_line_edit.hide()
            self._msec_label.hide()
            self._msec_spin_box.hide()
            self._msec_line_edit.hide()

    # time changed signal
    upate_time = QtCore.pyqtSignal(int, int, int, int)

    def _hour_edit(self):
        # hour edits emit signal
        value = int(self._hour_line_edit.text())
        if (value != self._hour_spin_box.value()):
            self._hour_spin_box.setValue(value)
            self.emit_time_chage()
    def _hour_spinner(self, value):
        self._hour_line_edit.setText(str(value))

    def _minute_spinner(self, value):
        self._minute_line_edit.setText(str(value))
    def _minute_edit(self):
        # minute edits emit signal
        value = int(self._minute_line_edit.text())
        if (value != self._msec_spin_box.value()):
            self._minute_spin_box.setValue(value)
            self.emit_time_chage()

    def _sec_spinner(self, value):
        self._sec_line_edit.setText(str(value))
    def _sec_edit(self):
        # second edits emit signal
        value = int(self._sec_line_edit.text())
        if (value != self._sec_spin_box.value()):
            self._sec_spin_box.setValue(value)
            self._emit_time_change()

    def _msec_spinner(self, value):
        self._msec_line_edit.setText(str(value))
    def _msec_edit(self):
        # msec edits emit signal
        value = int(self._msec_line_edit.text())
        if (value != self._msec_spin_box.value()):
            self._msec_spin_box.setValue(value)
            self.emit_time_chage()

    def _emit_time_change(self):
        # emit signal with cumulative time change
        self.upate_time.emit(self._hour_spin_box.value(),
                             self._minute_spin_box.value(),
                             self._sec_spin_box.value(),
                             self._msec_spin_box.value())


class ClickableGraphicsScene(QtWidgets.QGraphicsScene):
    """GraphicsScene with mouse intercepts.

        A GraphicsScene widget which intercepts mouse move and click events.

        Attributes:
            none

        Signals:
            pixmap_selected()
    """

    pixmap_selected = QtCore.pyqtSignal(QtGui.QPixmap, int, int)

    def __init__(self, parent):

        # QGraphicsScene.__init__(self, QtCore.QRectF(QtCore.QPointF(0, 0), QtCore.QPointF(450, 350)), parent)
        QGraphicsScene.__init__(self, parent)

        self._itemToAdd = 0
        self._mode = 0  # 0: add mode, 1:select mode
        # self.view = graphicsView

    def mouseMoveEvent(self, event):
        print("mouse_moved()")

    def mousePressEvent(self, event):

        # could try using  a button
        # QPushButton * button = new
        # QPushButton;
        # button->setIcon(QIcon(myQPixmap));
        # buttonWidget = MySceneClass->scene()->addWidget(button);
        # QObject::connect(button, SIGNAL(clicked()), this, SLOT(clickedSlot()));

        # QtGui.QWidget.QGraphicsScene.mousePressEvent(self, event)
        # QtWidgets.QGraphicsScene.mousePressEvent(self, event)
        if (event.button() == QtCore.Qt.LeftButton):
            x = event.scenePos().x()
            y = event.scenePos().y()

            point = QtCore.QPointF(x, y)
            transform = QtGui.QTransform()

            item_list =  self.items()
            # self.itemAt(int(x), int(y))
            selected = self.itemAt(point, transform)

            if (selected):
                # find pixmap in sorted render list
                selected_pixmap = selected.pixmap()
                # signal a pixmap selection
                self.pixmap_selected.emit(selected_pixmap, x, y)

                # ptest = selected_pixmap.parent()
                # test = selected_pixmap.test_data
                # test_2 = 1

            if selected:
                print("You clicked on item: {0}".format(selected))
            else:
                print("You didn't click on an item.")

            print(selected)
            if selected:
                selected.setSelected(True)


class MyForm(QMainWindow):
    """Main window for application.

        Collects and sorts multiple directories of images, creating names based on exif data.

        Attributes:
            none

        Signals:
            none
    """


    def __init__(self, scale, frame_thickness, screen_width, screen_height, parent=None):

        QMainWindow.__init__(self, parent)

        self.media_dictionary = dict()
        self.shifted_media_dictionary = dict()
        self.media_concatenated_list = []

        # cache image scale and border thickness
        self.scale = scale
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.frame_thickness = frame_thickness
        self.pen = QtGui.QPen(QtGui.QColor(255, 0, 0, 255), frame_thickness)

        # construct base UI object
        self.ui = Ui_MediaHomeWindow()
        self.ui.setupUi(self)
        # TODO - can Qt layout tool enforce window width and heigth rules during resize?
        self.resize(screen_width, 600)
        self.move(0, screen_height-600)

        # progress bar in status
        self.progress = QProgressBar(self.statusBar())
        self.progress.hide()
        self.statusBar().addPermanentWidget(self.progress)

        # add media button
        self.ui.addMediaButton.clicked.connect(self.add_directory)

        # select destination directory button
        self.ui.setDesinationButton.clicked.connect(self.set_destination_directory)

        # Pixmap object for image load
        self.pixmap = QtGui.QPixmap()

        # QGraphicsScene to manage images within view
        self.scene = QGraphicsScene(self)
        self.scene.addText("Hello, world!")

        # Qt layout tool - graphicsView
        self.graphicsview = self.ui.graphicsView

        self.graphicsview_pos_x = self.graphicsview.pos().x()
        self.graphicsview_pos_y = self.graphicsview.pos().y()
        self.graphicsview_width = (self.screen_width - 2 * self.graphicsview_pos_x)
        self.graphicsview_height = self.graphicsview.size().height()
        self.scale = self.graphicsview_height / 1.5

        self.graphicsview.setGeometry(QtCore.QRect(self.graphicsview_pos_x, self.graphicsview_pos_y, self.graphicsview_width, self.graphicsview_height))
        self.graphicsview.setObjectName("graphicsview")
        self.graphicsview.setInteractive(True)
        self.graphicsview.setMouseTracking(True)
        self.scene_runtime = ClickableGraphicsScene(self)
        self.scene_runtime.addText("dynamic scene!")
        self.graphicsview.setScene(self.scene_runtime)

        self.radio_grid = self.ui.radioGrid
        if(self.radio_grid.isChecked()):

            # runtime QGridLayout
            # self.grid_layout = QtWidgets.QGridLayoutView(self.ui.centralWidget)

            # Qt layout tool - grid layout
            self.pixmap.load("DSC06550.JPG")
            self.pixmap = self.pixmap.scaled(scale, scale, QtCore.Qt.KeepAspectRatio)
            label = QtWidgets.QLabel(self)
            label.setFixedSize(self.pixmap.size());
            label.setPixmap(self.pixmap)
            self.ui.gridLayoutWidget.setGeometry(QtCore.QRect(20, 340, 271, 3*1.5*scale))
            self.ui.gridLayout.addWidget(label, 0, 0)
            self.pixmap.load("DSC06559.JPG")
            self.pixmap = self.pixmap.scaled(scale, scale, QtCore.Qt.KeepAspectRatio)
            label = QtWidgets.QLabel(self)
            label.setFixedSize(self.pixmap.size());
            label.setPixmap(self.pixmap)
            self.ui.gridLayout.addWidget(label, 1, 2)
            self.ui.gridLayoutWidget.setLayout(self.ui.gridLayout)
            self.ui.gridLayoutWidget.adjustSize()

            self.gridview_pos_x = self.ui.gridLayoutWidget.pos().x()
            self.gridview_pos_y = self.ui.gridLayoutWidget.pos().y()
            self.gridview_width = (self.screen_width - 2 * self.gridview_pos_x)
            self.gridview_height = self.graphicsview.size().height()
            self.ui.gridLayoutWidget.setGeometry(QtCore.QRect(self.gridview_pos_x, self.gridview_pos_y, self.gridview_width, self.gridview_height))

            self.ui.gridLayout.setColumnMinimumWidth(0, self.scale)
            self.ui.gridLayout.setColumnStretch(0, 10)
            self.ui.gridLayout.setColumnMinimumWidth(1, self.scale)
            self.ui.gridLayout.setColumnStretch(1, 10)
            self.ui.gridLayout.setColumnMinimumWidth(2, self.scale)
            self.ui.gridLayout.setColumnStretch(2, 10)

            # scrolling gridview
            self.ui.gridLayoutScroll.setColumnMinimumWidth(0, self.scale)
            self.ui.gridLayoutScroll.setColumnStretch(0, 10)
            self.ui.gridLayoutScroll.setColumnMinimumWidth(1, self.scale)
            self.ui.gridLayoutScroll.setColumnStretch(1, 10)
            self.ui.gridLayoutScroll.setColumnMinimumWidth(2, self.scale)
            self.ui.gridLayoutScroll.setColumnStretch(2, 10)

            self.pixmap.load("DSC06550.JPG")
            self.pixmap = self.pixmap.scaled(scale, scale, QtCore.Qt.KeepAspectRatio)
            label = QtWidgets.QLabel(self)
            label.setFixedSize(self.pixmap.size());
            label.setPixmap(self.pixmap)
            # self.ui.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 340, 271, 3*1.5*scale))
            self.ui.gridLayoutScroll.addWidget(label, 0, 0)
            self.pixmap.load("DSC06559.JPG")
            self.pixmap = self.pixmap.scaled(scale, scale, QtCore.Qt.KeepAspectRatio)
            label = QtWidgets.QLabel(self)
            label.setFixedSize(self.pixmap.size());
            label.setPixmap(self.pixmap)
            self.ui.gridLayoutScroll.addWidget(label, 1, 2)
            self.ui.gridLayoutWidget_2.setLayout(self.ui.gridLayout)
            # self.ui.gridLayoutWidget_2.adjustSize()

            # another scroll gv attempt
            # QGridLayout * layout = new QGridLayout;
            self.grid_layout = QtWidgets.QGridLayout()
            self.pixmap.load("DSC06550.JPG")
            self.pixmap = self.pixmap.scaled(scale, scale, QtCore.Qt.KeepAspectRatio)
            label = QtWidgets.QLabel(self)
            label.setFixedSize(self.pixmap.size());
            label.setPixmap(self.pixmap)
            self.grid_layout.setGeometry(QtCore.QRect(20, 340, 271, 3*1.5*scale))
            self.grid_layout.addWidget(label, 0, 0)
            self.pixmap.load("DSC06559.JPG")
            self.pixmap = self.pixmap.scaled(scale, scale, QtCore.Qt.KeepAspectRatio)
            label = QtWidgets.QLabel(self)
            label.setFixedSize(self.pixmap.size());
            label.setPixmap(self.pixmap)
            self.grid_layout.addWidget(label, 1, 2)
            # self.gridLayoutWidget.setLayout(self.gridLayout)
            # self.gridLayoutWidget.adjustSize()
            self.scroll_area = QtWidgets.QScrollArea()
            self.container_widget = QtWidgets.QWidget()
            self.container_widget.setLayout(self.grid_layout);
            self.scroll_area.setWidgetResizable(True);
            self.scroll_area.setWidget(self.container_widget);

        else:

            self.ui.scrollArea.hide()

        # time-offset widget for shifting one fileset wrt others
        self.time_offset = TimeOffset(self)
        # time-offset widget signal will resort and re-render images
        self.time_offset.upate_time.connect(self.offset)

        # TODO - would like to identify image via pixmap subclass ... but a copy of the origional pixmap seems to be returned
        self.scene_runtime.pixmap_selected.connect(self.handle_pixmap_selected)


    def handle_pixmap_selected(self, pixmap, x_position, y_position):
        """Identifies selected pixmap.

        Identifies selected pixmap.

        Args:
            pixmap: the selected pixmap.
            x_position: mouse x position
            y_position: mouse y position

        Returns:
            none

        Raises:
            none
        """

        # this is a new pixmap, not a ref to the old
        # selected_pixmap = pixmap
        # for element in self.media_concatenated_list:
        #     if (element[2] is selected_pixmap):
        #         print("found pixmap")
        #         break

        # identify list index by x position
        index = int(x_position / self.scale)
        print("index: {0}".format(index))
        selected_image = self.media_concatenated_list[index]

        label = QtWidgets.QLabel(self.tr(selected_image[0]))
        label.setGeometry(QtCore.QRect(x_position, y_position, 100, 1.5 * self.scale))

        # scene_item.setOffset(index * self.scale, 0)
        # self.scene_runtime.addItem(scene_item)

        # scene_item = QtWidgets.QGraphicsSimpleTextItem(selected_image[2])
        # scene_item = QtWidgets.QGraphicsSimpleTextItem("test")
        # scene_item.setPos(x_position, y_position)
        scene_item = self.scene_runtime.addSimpleText("test")
        scene_item.setPos(x_position, 100)


    def offset(self, hour, minute, sec, msec):
        """Apply time offset to filenames and re-render.

        Apply time offset to filenames and re-render.

        Args:
            hour: hour offset
            minute: minute offset
            sec: second offset
            msec: msec offset

        Returns:
            none

        Raises:
            none
        """

        test_key = list(self.media_dictionary.keys())[1];

        test_1 = self.media_dictionary[test_key]
        test_2 = test_1[2]
        test_3 = test_2[1]
        test_4 = test_3[1]

        #  add offset to original time
        # { [offset year, month, day, h, m, s, msec], color,  [ Y_M_D_H_M_S_MSEC, [fname, [year, date, time_hour, time_min, time_sec, time_msec]] ] }
        # time offset
        self.media_dictionary[test_key][0][3] = hour
        self.media_dictionary[test_key][0][4] = minute
        self.media_dictionary[test_key][0][5] = sec
        self.media_dictionary[test_key][0][6] = msec

        current_offset = self.media_dictionary[test_key][0]

        # create offset filenames for specified key directory
        # media_dictionary[key] = [ offset, color, [(Y_M_D_H_M_S<a> : filename), ...] ]
        for media_element in self.media_dictionary[test_key][2]:

            shifted_name = NamedMedia.shifted_name(media_element[1][1], current_offset,  media_element[0].split(".")[-1])
            media_element[0] = shifted_name

        self.render_images()


    def render_images(self):
        """Render Image.

        Sort images from multiple directories according to sorted timestamped name.

        Args:
            none

        Returns:
            none

        Raises:
            none
        """

        self.scene_runtime = ClickableGraphicsScene(self)
        self.scene_runtime.pixmap_selected.connect(self.handle_pixmap_selected)
        self.graphicsview.setScene(self.scene_runtime)

        self.media_concatenated_list = []

        for dir_key, file_data in self.media_dictionary.items():
            # [ [Y_M_D_H_M_S<a> offset name, key, pixmap], ... ]
            self.media_concatenated_list = self.media_concatenated_list + file_data[2]

        self.media_concatenated_list.sort()

        # render images in view
        self.progress.setRange(0, len(self.media_concatenated_list) - 1)
        self.progress.setValue(0)
        for index, name_dated in enumerate(self.media_concatenated_list):
            self.progress.setValue(index)
            scene_item = QGraphicsPixmapItem(name_dated[2])
            scene_item.setOffset(index * self.scale, 0)
            self.scene_runtime.addItem(scene_item)
            font = QtGui.QFont('Courier', 7)
            scene_text = self.scene_runtime.addSimpleText(name_dated[0].rsplit(".", 1)[0])
            scene_text.setFont(font)
            scene_text.setPos(index * self.scale, self.scale)

        self.progress.hide()
        self.graphicsview.setGeometry(QtCore.QRect(self.graphicsview_pos_x, self.graphicsview_pos_y, self.graphicsview_width, self.graphicsview_height))

    def set_destination_directory(self):
        """Save image set to selected directory.

        Save sorted fileset to a selected set of directory.

        Args:
            none

        Returns:
            none

        Raises:
            none
        """

        # select media directory
        dest_path = QtWidgets.QFileDialog.getExistingDirectory(self,
                                                               "Select Destination Directory",
                                                               "",
                                                               QtWidgets.QFileDialog.ShowDirsOnly)

        for key, list in self.media_dictionary.items():
            for file in list[2]:
                print("save {0}".format(file[0]))
                # { [offset year, month, day, h, m, s, msec], color,  [ Y_M_D_H_M_S_MSEC, [fname, [year, date, time_hour, time_min, time_sec, time_msec]] ] }
                shutil.copyfile(os.path.join(key, file[1][0]), os.path.join(dest_path, file[0]))



    def add_directory(self):
        """Render Image.

        Open a newly selected set of directory images. Sort and display images according to timestamped name.

        Args:
            none

        Returns:
            none

        Raises:
            none
        """

        #  create the scene
        self.scene_runtime = ClickableGraphicsScene(self)
        self.scene_runtime.pixmap_selected.connect(self.handle_pixmap_selected)
        self.scene_runtime.addText("dynamic scene!")
        self.graphicsview.setScene(self.scene_runtime)

        try:
            last_media_dir_dict = pickle.load(open("save.p", "rb"))
            last_media_dir = last_media_dir_dict['media_dir']
        except:
            last_media_dir = ""

        # select media directory
        media_dir = QtWidgets.QFileDialog.getExistingDirectory(self,
                                                               "Select Media Directory",
                                                               last_media_dir,
                                                               QtWidgets.QFileDialog.ShowDirsOnly)

        last_media_dir_dict = {"media_dir": media_dir}
        pickle.dump(last_media_dir_dict, open("save.p", "wb"))

        # default destination path
        # dest_path = path.join(media_dir, 'renamed')

        # media filenames based off exif data
        self.progress.show()
        named_media = NamedMedia(media_dir, self.progress)
        # sorted modified name list - [ Y_M_D_H_M_S_MSEC : [fname, [year, date, time_hour, time_min, time_sec, time_msec]] ]
        self.named_media_list = named_media.get_named_media()

        # multiple media directories mapped in dictionary
        number_directories = len(self.media_dictionary)
        if (number_directories == 0):
            color = QtGui.QColor(255, 0, 0, 255)
        elif (number_directories == 1):
            color = QtGui.QColor(0, 255, 0, 255)
            self.time_offset.show(True)
        else:
            color = QtGui.QColor(0, 0, 255, 255)

        # { [offset year, month, day, h, m, s, msec], color,  [ Y_M_D_H_M_S_MSEC, [fname, [year, date, time_hour, time_min, time_sec, time_msec]] ] }
        self.media_dictionary[media_dir] = [[0, 0, 0, 0, 0, 0, 0], color, self.named_media_list]

        self.progress.setValue(0)
        self.progress.setRange(0, len(self.named_media_list) - 1)
        list_shifted_names = []

        for index, media_element in enumerate(self.named_media_list):
            self.progress.setValue(index)
            # start with original exif timestamp name
            offset_name = media_element[0];
            # load image into pixmap
            pixmap = QtGui.QPixmap()
            pixmap.load(path.join(media_dir, self.named_media_list[index][1][0]))
            pixmap = pixmap.scaled(self.scale, self.scale, QtCore.Qt.KeepAspectRatio)
            # paint border
            painter = QtGui.QPainter(pixmap)
            pen = QtGui.QPen(color, self.frame_thickness)
            painter.setPen(pen)
            painter.drawRect(self.frame_thickness-1, self.frame_thickness-1, pixmap.width()-self.frame_thickness, pixmap.height()-self.frame_thickness);
            media_element.append(pixmap)
            # [ [Y_M_D_H_M_S<a> offset name, media_dictionary{} key, pixmap], ... ]
            list_shifted_names.append([offset_name, index, pixmap])

        # [ [Y_M_D_H_M_S<a> offset name, key, pixmap], ... ]
        self.media_concatenated_list = self.media_concatenated_list + list_shifted_names
        self.media_concatenated_list.sort()

        # render images in view
        self.progress.setRange(0, len(self.media_concatenated_list) - 1)
        self.progress.setValue(0)
        for index, name_dated in enumerate(self.media_concatenated_list):
            self.progress.setValue(index)

            scene_item = QGraphicsPixmapItem(name_dated[2])
            scene_item.setOffset(index * self.scale, 0)
            self.scene_runtime.addItem(scene_item)

            font = QtGui.QFont('Courier', 7)
            scene_text = self.scene_runtime.addSimpleText( name_dated[0].rsplit(".", 1)[0])
            scene_text.setFont(font)
            scene_text.setPos(index * self.scale, self.scale)
            # painter.end()

        self.progress.hide()
        number_images = len(self.media_concatenated_list)
        width_total = number_images*self.scale
        if (width_total < (self.screen_width-20)):
            view_width = width_total
        else:
            view_width = (self.screen_width-2*20)

        # self.graphicsview.setObjectName("graphicsview")
        # self.graphicsview.setInteractive(True)
        # self.graphicsview.setMouseTracking(True)
        self.graphicsview.setGeometry(QtCore.QRect(self.graphicsview_pos_x, self.graphicsview_pos_y, self.graphicsview_width, self.graphicsview_height))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # remove gtk warnings
    # http: // stackoverflow.com / questions / 35351024 / pyqt5 - gtk - critical - ia - gtk - widget - style - get - assertion - gtk - is -widget - widg
    app.setStyle("fusion")
    # available screen size
    screen_resolution = app.desktop().availableGeometry()
    screen_width, screen_height = screen_resolution.width(), screen_resolution.height()
    myapp = MyForm(150, 2, screen_width, screen_height)
    myapp.show()

    sys.exit(app.exec_())