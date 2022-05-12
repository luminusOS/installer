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

@Gtk.Template(resource_path='/dev/luminus/Misticetos/ui/welcome.ui')
class WelcomeWindow(Gtk.Box):
    __gtype_name__ = 'WelcomeWindow'

    intro_message = Gtk.Template.Child("_intro_message")
    welcome_message = Gtk.Template.Child("_welcome_message")

    def __init__(self, application, **kwargs):
        super().__init__(**kwargs)

        self.check_lang_var()

    def check_lang_var(self):
        message = self.welcome_message.get_label().replace("%product_name%", "Luminus OS")
        self.welcome_message.set_markup("<b><span font_desc='Purisa 20'>%s</span></b>" % message)

        message = self.intro_message.get_label().replace("%versioned_name%", "Luminus OS 2022.05")
        self.intro_message.set_markup("%s" % message)

