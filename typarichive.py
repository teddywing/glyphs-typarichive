# MenuTitle: TypArichive

__doc__="""
TODO
"""

from datetime import datetime
from os import path
import re
import shutil


def new_font_name(filename):
    time_string = datetime.now().strftime('%Y%m%d%H%M')

    return re.sub(r'\d{12}', time_string, filename)


font = Glyphs.font
filepath = font.filepath

font_directory = path.dirname(filepath)
archive_directory = path.join(font_directory, '_archive')
new_font_path = path.join(
    font_directory,
    new_font_name(
        path.basename(filepath)))

shutil.copy2(filepath, new_font_path)

shutil.move(filepath, archive_directory)

font.close()
Glyphs.open(new_font_path)

Glyphs.font.familyName = new_font_name(Glyphs.font.familyName)
