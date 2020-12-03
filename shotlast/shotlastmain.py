#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
shotlast
Watches clipboard and automatically saves any new images.
"""


# pylint: disable=missing-docstring
# pylint: disable=empty-docstring
# pylint: disable=invalid-name
# pylint: disable=line-too-long

import argparse
import datetime
import os
import pathlib
import platform
import time
from PIL import ImageChops
from PIL import ImageGrab
import click


def get_datetime_stamp(sep_date="", sep_group="_", sep_time="", moment=None):
    """
    Returns string representation of datetime objects.
    By default, the value will look like "20121212_120102" and it
    is safe to use it on file names.
    sep_date:
        string, separator between year, month and day
    sep_group:
        string, separator between the date and time.
    sep_time:
        string, separator between hour, minute and second
    moment:
        an instance of datetime.datetime.
        if it is None(the default), now() will be used.
    Requires:
        import datetime
    >>> import datetime
    >>> some_date = datetime.datetime(2012, 12, 12, 12, 1, 2)
    >>> print(get_datetime_stamp(moment=some_date))
    20121212_120102
    >>> print(get_datetime_stamp(sep_date="/", sep_group="-", moment=some_date))
    2012/12/12-120102
    >>> print(get_datetime_stamp(sep_group="-", sep_time=":", moment=some_date))
    20121212-12:01:02
    """
    date_format = (sep_date.join(["%Y", "%m", "%d"]) +
                   sep_group +
                   sep_time.join(["%H", "%M", "%S"]))
    if moment is None:
        moment = datetime.datetime.now()
    stamp = moment.strftime(date_format)
    return stamp


def build_file_name():
    """
    Returns a string like "clip_20121212_120102" without file extension.
    """
    file_name = "clip_" + get_datetime_stamp()
    return file_name


def is_same_image(image1, image2):
    """
    Returns True if 2 images are the same, False otherwise.
    https://stackoverflow.com/questions/35176639/compare-images-python-pil/56280735
    requires:
        from PIL import ImageChops
    """
    if image1 is None and image2 is None:  # pylint: disable=no-else-return
        # both is None, so 2 "images" are "equal".
        return True
    elif image1 is None:
        return False
    elif image1 is None:
        return False

    same = True
    image1_rgb = image1.convert('RGB')
    image2_rgb = image2.convert('RGB')
    diff = ImageChops.difference(image1_rgb, image2_rgb)
    if diff.getbbox():
        # there is a difference.
        same = False
    return same


def start_shots(target_dir, sleep_duration=2):
    print("started shotlast.")
    print("target_dir:", target_dir)
    print("sleep_duration:", sleep_duration)
    print("press ctrl c to end.")
    image0 = None  # previous
    while True:
        time.sleep(sleep_duration)

        image1 = ImageGrab.grabclipboard()
        if image1 is None:
            # could not find an image, possibly we have text.
            continue

        file_format = "png"
        full_file_name = os.path.join(
            target_dir, build_file_name()) + "." + file_format
        if not is_same_image(image0, image1):
            image1.save(full_file_name, file_format.upper())
            print("saved image:", full_file_name)
        image0 = image1


def get_candidate_dir():
    """
    Returns a valid directory name to store the pictures.
    If it can not be determined, "" is returned.

    requires:
        import os
        import pathlib
        import platform

    https://docs.python.org/3/library/pathlib.html#pathlib.Path.home
    New in version 3.5.

    https://docs.python.org/3.8/library/platform.html#platform.system
    Returns the system/OS name, such as 'Linux', 'Darwin', 'Java', 'Windows'.
    An empty string is returned if the value cannot be determined.

    """
    home_dir = pathlib.Path().home()
    target_dir = home_dir
    system = platform.system()
    if system == "Windows":
        target_dir = os.path.join(home_dir, "Pictures")
    elif system == "Darwin":
        # TODO: 5 Pictures directory for Mac?
        pass
    elif system == "Linux":
        # TODO: 5 Pictures directory for Linux?
        pass

    if os.path.isdir(target_dir):  # pylint: disable=no-else-return
        return target_dir
    elif os.path.isdir(home_dir):
        return home_dir
    else:
        return ""


def choose_target_dir(default_dir):
    chosen_dir = default_dir
    marker = '# Everything below is ignored\n'
    message = click.edit(default_dir + '\n\n' + marker)

    if message is not None:
        chosen_dir = message.split(marker, 1)[0].rstrip('\n')
    return chosen_dir


def get_settings():
    """

    requires:
        import argparse
    """
    parser = argparse.ArgumentParser()

    help1 = "Target directory to store the saved clipboard files."
    parser.add_argument('target_dir', nargs='?', help=help1)

    help1 = 'Sleep duration (in seconds) between two clipboard checks.'
    parser.add_argument('--period', nargs='?', help=help1, default="2")

    # help1 = 'If provided, automatically confirms overwrite.'
    # parser.add_argument('--overwrite', action='store_true', help=help1)

    args = parser.parse_args()

    settings = {}
    settings["sleep_duration"] = args.period
    settings["target_dir"] = args.target_dir

    # for file_name in args.target_dir:
    #     if os.path.isfile(file_name):
    #         settings["input"] = file_name
    #         convert_file(file_name, settings)
    #     else:
    #         print("NOT a file: ", file_name)

    return settings


def main():
    """
    entry point of the module.
    """
    # os.chdir(os.path.abspath(os.path.dirname(__file__)))
    settings = get_settings()
    sleep_duration = int(settings["sleep_duration"])
    if settings["target_dir"]:
        target_dir = settings["target_dir"]
    else:
        candidate_target_dir = get_candidate_dir()
        target_dir = choose_target_dir(default_dir=candidate_target_dir)
        settings["target_dir"] = target_dir

    start_shots(target_dir=target_dir, sleep_duration=sleep_duration)


if __name__ == '__main__':
    main()
