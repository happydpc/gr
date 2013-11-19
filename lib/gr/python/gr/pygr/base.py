# -*- coding: utf-8 -*-
"""..."""

# local library
import gr
from gr.pygr.helper import ColorIndexGenerator

__author__ = "Christian Felder <c.felder@fz-juelich.de>"
__date__ = "2013-11-13"
__version__ = "0.3.0"
__copyright__ = """Copyright 2012, 2013 Forschungszentrum Juelich GmbH

This file is part of GR, a universal framework for visualization applications.
Visit https://iffwww.iff.kfa-juelich.de/portal/doku.php?id=gr for the latest
version.

GR was developed by the Scientific IT-Systems group at the Peter Grünberg
Institute at Forschunsgzentrum Jülich. The main development has been done
by Josef Heinen who currently maintains the software.

GR is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This framework is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with GR. If not, see <http://www.gnu.org/licenses/>.
 
"""

class GRMeta(object):

    def drawGR(self):
        raise NotImplementedError

class GRDrawAttributes(object):

    def __init__(self, linetype=gr.LINETYPE_SOLID, markertype=gr.MARKERTYPE_DOT,
                 linecolor=None, markercolor=1):
        self._linetype, self._markertype = linetype, markertype
        self._linecolor, self._markercolor = linecolor, markercolor
        if linecolor is None:
            self._linecolor = ColorIndexGenerator.nextColorIndex()
        else:
            self._linecolor = linecolor

    @property
    def linetype(self):
        """Get current linetype."""
        return self._linetype

    @linetype.setter
    def linetype(self, value):
        self._linetype = value

    @property
    def markertype(self):
        """Get current markertype."""
        return self._markertype

    @markertype.setter
    def markertype(self, value):
        self._markertype = value

    @property
    def linecolor(self):
        """Get current linecolor."""
        return self._linecolor

    @linecolor.setter
    def linecolor(self, value):
        self._linecolor = value

    @property
    def markercolor(self):
        """Get current markercolor."""
        return self._markercolor

    @markercolor.setter
    def markercolor(self, value):
        self._markercolor = value