#!/usr/bin/env python3
"""
Minimal example of trayer integration with GTK4

License: MIT
Author: Matteo Benedetto <me@enne2.net>
Copyright © 2025 Matteo Benedetto

This file is part of the trayer project: https://github.com/enne2/trayer
See LICENSE file for complete license information.
"""

from trayer import TrayIcon
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, GLib


class MinimalApp(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="com.example.trayer.minimal")
        self.window = None
    
    def do_activate(self):
        if not self.window:
            self.window = Gtk.ApplicationWindow(application=self)
            self.window.set_title("Trayer Minimal Example")
            self.window.set_default_size(400, 300)
            
            # Add some content
            box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
            box.set_margin_top(12)
            box.set_margin_bottom(12)
            box.set_margin_start(12)
            box.set_margin_end(12)
            
            label = Gtk.Label(label="This is a minimal trayer example!\n\nCheck the system tray for the icon.")
            label.set_wrap(True)
            box.append(label)
            
            button = Gtk.Button(label="Hide to Tray")
            button.connect("clicked", lambda w: self.window.hide())
            box.append(button)
            
            self.window.set_child(box)
        
        self.window.present()
    
    def toggle_window(self):
        """Toggle window visibility"""
        if self.window.is_visible():
            self.window.hide()
        else:
            self.window.present()


def main():
    # Create application
    app = MinimalApp()
    
    # Create tray icon
    tray = TrayIcon(
        app_id="com.example.trayer.minimal",
        title="Trayer Minimal Example",
        icon_name="application-x-executable"
    )
    
    # Left-click toggles window
    tray.set_left_click(app.toggle_window)
    
    # Add menu items
    tray.add_menu_item("Show Window", callback=lambda: app.window.present())
    tray.add_menu_item("Hide Window", callback=lambda: app.window.hide())
    tray.add_menu_separator()
    tray.add_menu_item("Quit", callback=app.quit)
    
    # Setup tray BEFORE running app
    tray.setup()
    
    # Run application
    app.run()


if __name__ == "__main__":
    main()
