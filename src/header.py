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

import os

from gi.repository import Gtk

@Gtk.Template(resource_path='/dev/luminus/Misticetos/ui/header.ui')
class MainHeader(Gtk.HeaderBar):
    __gtype_name__ = 'MainHeader'

    forward_button = Gtk.Template.Child("_forward_button")
    backward_button = Gtk.Template.Child("_backward_button")
    window_select = Gtk.Template.Child("_window_select")

    def __init__(self, application, **kwargs):
        super().__init__(**kwargs)

        self.application = application

    @Gtk.Template.Callback()
    def forward_button_clicked(self, *args):
        window_id = self.window_select.get_active() + 1
        self.window_select.set_active(window_id)
        if window_id > 0:
            self.backward_button.set_sensitive(True)
        if window_id == 6:
            self.forward_button.set_sensitive(False)

    @Gtk.Template.Callback()
    def backward_button_clicked(self, *args):
        window_id = self.window_select.get_active() - 1
        self.window_select.set_active(window_id)
        if window_id == 0:
            self.backward_button.set_sensitive(False)
        if window_id < 6:
            self.forward_button.set_sensitive(True)

    @Gtk.Template.Callback()
    def on_window_select_changed(self, *args):
        window_id = self.window_select.get_active()
        if window_id == 0:
            self.application.set_child(self.application.welcome)
        elif window_id == 1:
            self.application.set_child(self.application.location)
        print(f"Active Window: {self.window_select.get_active()}")
