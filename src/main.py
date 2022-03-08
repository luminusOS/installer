# main.py
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

import sys
import gi
import os

gi.require_version('Gtk', '4.0')

from gi.repository import Gtk, Gio, Gdk

from .window import InstallerWindow, AboutDialog


class Application(Gtk.Application):
    def __init__(self):
        super().__init__(application_id='dev.luminus.Installer',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)
        #self.init_style()

    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = InstallerWindow(application=self)
        self.create_action('about', self.on_about_action)
        self.create_action('preferences', self.on_preferences_action)
        win.present()

    def init_style(self):
        css_provider = Gtk.CssProvider()
        css_file = '/dev/luminus/Installer/dev.luminus.Installer.css'
        if not os.path.exists(css_file):
            mypath = os.path.dirname(os.path.abspath(__file__))
            print(os.path.dirname(os.path.abspath(__file__)))
            onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
            print(onlyfiles)
            sys.exit(css_file + ' CSS file missing!')
        css_provider.load_from_resource('/dev/luminus/Installer/dev.luminus.Installer.css')
        get_display = Gdk.Display.get_default()
        style_context = Gtk.StyleContext()
        style_context.add_provider_for_display(get_display, css_provider, Gtk.STYLE_PROVIDER_PRIORITY_USER)

    def on_about_action(self, widget, _):
        about = AboutDialog(self.props.active_window)
        about.present()

    def on_preferences_action(self, widget, _):
        print('app.preferences action activated')

    def create_action(self, name, callback):
        """ Add an Action and connect to a callback """
        action = Gio.SimpleAction.new(name, None)
        action.connect("activate", callback)
        self.add_action(action)


def main(version):
    app = Application()
    return app.run(sys.argv)
