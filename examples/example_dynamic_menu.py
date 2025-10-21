#!/usr/bin/env python3
"""
Example showing dynamic menu updates based on application state

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


class DynamicMenuApp(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="com.example.trayer.dynamenu")
        self.window = None
        self.tray = None
        self.connected = False
    
    def do_activate(self):
        if not self.window:
            self.window = Gtk.ApplicationWindow(application=self)
            self.window.set_title("Trayer Dynamic Menu Example")
            self.window.set_default_size(400, 300)
            
            # Add content
            box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
            box.set_margin_top(12)
            box.set_margin_bottom(12)
            box.set_margin_start(12)
            box.set_margin_end(12)
            
            label = Gtk.Label(
                label="Dynamic Menu Example\n\nConnect/disconnect to see menu change!"
            )
            label.set_wrap(True)
            box.append(label)
            
            self.status_label = Gtk.Label(label="Status: Disconnected")
            box.append(self.status_label)
            
            # Connect button
            btn_connect = Gtk.Button(label="Connect")
            btn_connect.connect("clicked", lambda w: self.connect_server())
            box.append(btn_connect)
            
            # Disconnect button
            btn_disconnect = Gtk.Button(label="Disconnect")
            btn_disconnect.connect("clicked", lambda w: self.disconnect_server())
            box.append(btn_disconnect)
            
            self.window.set_child(box)
        
        self.window.present()
    
    def connect_server(self):
        """Simulate connecting to a server"""
        self.connected = True
        self.status_label.set_text("Status: Connected ✅")
        self.update_tray_menu()
        print("✅ Connected! Menu updated.")
    
    def disconnect_server(self):
        """Simulate disconnecting"""
        self.connected = False
        self.status_label.set_text("Status: Disconnected ❌")
        self.update_tray_menu()
        print("❌ Disconnected! Menu updated.")
    
    def send_message(self):
        """Simulate sending a message"""
        print("📤 Message sent!")
        dialog = Gtk.AlertDialog()
        dialog.set_message("Message Sent!")
        dialog.set_detail("Your message was sent successfully.")
        dialog.show(self.window)
    
    def update_tray_menu(self):
        """Update tray menu based on connection state"""
        if not self.tray:
            return
        
        # Clear existing menu
        self.tray.menu_items.clear()
        
        # Add items based on state
        if self.connected:
            self.tray.add_menu_item("📡 Disconnect", callback=self.disconnect_server)
            self.tray.add_menu_item("📤 Send Message", callback=self.send_message)
            self.tray.add_menu_item("📊 View Stats", callback=lambda: print("Stats!"))
        else:
            self.tray.add_menu_item("🔌 Connect", callback=self.connect_server)
            self.tray.add_menu_item("⚙️ Settings", callback=lambda: print("Settings!"), enabled=False)
        
        self.tray.add_menu_separator()
        self.tray.add_menu_item("Show Window", callback=lambda: self.window.present())
        self.tray.add_menu_separator()
        self.tray.add_menu_item("Quit", callback=self.quit)
        
        # Refresh the menu
        self.tray.update_menu()
    
    def toggle_window(self):
        if self.window.is_visible():
            self.window.hide()
        else:
            self.window.present()


def main():
    # Create application
    app = DynamicMenuApp()
    
    # Create tray icon
    tray = TrayIcon(
        app_id="com.example.trayer.dynamenu",
        title="Dynamic Menu Example",
        icon_name="network-idle"
    )
    
    # Store tray reference
    app.tray = tray
    
    # Left-click toggles window
    tray.set_left_click(app.toggle_window)
    
    # Build initial menu
    app.update_tray_menu()
    
    # Setup and run
    tray.setup()
    app.run()


if __name__ == "__main__":
    main()
