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

import os
import sys

from os import listdir, path
import shutil
from PIL import Image
from PIL.ExifTags import TAGS
import datetime
import re
from PyQt5.QtWidgets import QProgressBar, QProgressDialog

class NamedMedia():

    def __init__(self, source_path, progress=None, parent=None):
        # dest_path = os.path.join(source_path, 'renamed34')
        # TODO - handle dialog to remove existing renamed34 directory
        self.unique_file_names = {}

        # if not os.path.exists(dest_path):
            # create directory
            # os.makedirs(dest_path)

        # video containers to search for
        mediaExtensions = "jpg", "JPG", "mts"

        numFilesFound = 0
        numFilesParsed = 0

        # all files in specified directoryNamedMedia
        fnames = listdir(source_path)

        if (progress != None):
            progress.setRange(0, len(fnames)-1)
            progress.setValue(0)
        else:
            dest_path = os.path.join(source_path, 'renamed')
            if not os.path.exists(dest_path):
                # create directory
                os.makedirs(dest_path)

        for index, fname in enumerate(fnames):

            if (progress):
                progress.setValue(index)

            fnameModified = 'MISSED IT'
            fileSuffix = fname.split(".")

            # list of files with specified extensions
            if fileSuffix[-1] in mediaExtensions:

                if fileSuffix[-1] == "mts":

                    numFilesFound += 1
                    fnameModified = '{0}_{1}_{2}_{3}_{4}_{5}.{6}'.format(fname[0:4], fname[4:6], fname[6:8], fname[8:10], fname[10:12], fname[12:14], fileSuffix[-1])
                    # shutil.copyfile('{0}\{1}'.format(source_path, fname), '{0}\{1}'.format(dest_path, fnameModified))
                    numFilesParsed += 1

                else:

                    numFilesFound += 1

                    img = Image.open(os.path.join(source_path, fname));
                    exif_data = img._getexif()
                    if (exif_data != None):
                        for tag, value in exif_data.items():
                            tagString = TAGS.get(tag, tag)
                            if tagString == 'DateTimeOriginal':
                                value_ = re.sub('[:]', '_', value)
                                year = value_[0:4]
                                date = value_[5:10]
                                date_month = value_[5:7]
                                date_day = value_[8:10]
                                # time = value_[11:19]
                                time_hour = value_[11:13]
                                time_min = value_[14:16]
                                time_sec = value_[17:19]
                                time_msec = '00'
                                fnameModified = '{0}_{1}_{2}_{3}_{4}_{5}.{6}'.format(year, date, time_hour, time_min, time_sec, time_msec, fileSuffix[-1])

                                # create unique filename for those with the same timestamp
                                # dummy_msec = 1
                                while fnameModified in self.unique_file_names:
                                    time_msec += 1
                                    fnameModified = '{0}_{1}_{2}_{3}_{4}_{5}.{6}'.format(year, date, time_hour,
                                                                                         time_min, time_sec,
                                                                                         time_msec, fileSuffix[-1])

                                # todo collections.OrderedDict
                                self.unique_file_names[fnameModified] = [fname, [int(year), int(date_month), int(date_day), int(time_hour), int(time_min), int(time_sec), int(time_msec)]]

                                # copy file with unique name
                                if (progress == None):
                                    shutil.copyfile(os.path.join(source_path, fname), os.path.join(dest_path, fnameModified))

                                numFilesParsed += 1

                                break
                    else:
                        print('{0} has no exif data'.format(fname))

                img.close()

                print(fnameModified)

        if numFilesParsed == numFilesFound:
            print('parsed all {0} files'.format(numFilesFound))
        else:
            print("PARSING FILE ERROR: missed {0} files".format(numFilesFound-numFilesParsed))

    # TODO handle command line usage
    # else:
    #     print('{0} already exists'.format(dest_path))

        # for filename in self.unique_file_names:
        #     self.unique_file_names[filename].close()

        print('done')

    def shifted_name(exif, offset, suffix):
        """Create name from exif timestamp and offset.

        Create name from exif timestamp and offset.

        Args:
            exif: exif from file
            offset: offset time
            suffix: filename suffix

        Returns:
            none

        Raises:
            none
        """

        current_datetime = datetime.datetime(exif[0], exif[1], exif[2], exif[3], exif[4], exif[5], exif[6])
        offset_time = datetime.timedelta(offset[2], offset[5], offset[6], 0, offset[4], offset[3])
        shifted_datetime = current_datetime + offset_time

        msec_shift = shifted_datetime.microsecond
        sec_shift = shifted_datetime.second
        minute_shift = shifted_datetime.minute
        hour_shift = shifted_datetime.hour
        day_shift = shifted_datetime.day
        month_shift = shifted_datetime.month
        year_shift = shifted_datetime.year

        name = '{0:04}_{1:02}_{2:02}_{3:02}_{4:02}_{5:02}_{6:02}.{7}'.format(year_shift, month_shift, day_shift, hour_shift, minute_shift, sec_shift, msec_shift, str(suffix))

        return name


    def get_named_media(self):
        """Create filename from image exif timestamp.

        Create name from exif timestamp and offset.

        Args:
            none

        Returns:
            none

        Raises:
            none
        """

        # list of key value pairs
        list_key_value = [[k, v] for k, v in self.unique_file_names.items()]
        return sorted(list_key_value)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print("Remaining media located in %s", sys.argv[1])
        # path = os.path.join(sys.argv[1])
        namedMedia = NamedMedia(sys.argv[1])
    else:
        print("usage: photo_rename <directory path>")
