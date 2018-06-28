# MenuTitle: TypArichive

__doc__="""
Moves the current font to an `_archive` directory and opens a new timestamped
copy.
"""

# Copyright (c) 2018  Teddy Wing
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

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
