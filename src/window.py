# window.py
#
# Copyright 2021 Leandro Marques
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from gi.repository import Gtk


@Gtk.Template(resource_path='/dev/luminus/Installer/ui/window.ui')
class InstallerWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'InstallerWindow'

    butaocontinua = Gtk.Template.Child()
    logo = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.logo.set_resource("/dev/luminus/Installer/images/logo.png")
        """row = Gtk.ListBoxRow()
        row2 = Gtk.ListBoxRow()
        hbox = Gtk.Box()
        hbox2 = Gtk.Box()
        row.set_child(hbox)
        row2.set_child(hbox2)
        labeltest = Gtk.Label()
        labeltest.set_label("Testing")
        labeltest2 = Gtk.Label()
        labeltest2.set_label("Testing2")
        hbox.append(labeltest)
        hbox2.append(labeltest2)
        self.listbox.append(row)
        self.listbox.append(row2)"""


class AboutDialog(Gtk.AboutDialog):

    def __init__(self, parent):
        Gtk.AboutDialog.__init__(self)
        self.props.program_name = 'installer'
        self.props.version = "0.1.0"
        self.props.authors = ['Leandro Marques']
        self.props.copyright = '(C) 2021 Leandro Marques'
        self.props.logo_icon_name = 'dev.luminus.Installer'
        self.set_transient_for(parent)
