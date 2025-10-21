#!/usr/bin/env python3
"""
Example showing dynamic icon changes based on application state
"""

from trayer import TrayIcon
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, GLib


class DynamicIconApp(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="com.example.trayer.dynamic")
        self.window = None
        self.tray = None
        self.has_notifications = False
    
    def do_activate(self):
        if not self.window:
            self.window = Gtk.ApplicationWindow(application=self)
            self.window.set_title("Trayer Dynamic Icon Example")
            self.window.set_default_size(400, 300)
            
            # Add content
            box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
            box.set_margin_top(12)
            box.set_margin_bottom(12)
            box.set_margin_start(12)
            box.set_margin_end(12)
            
            label = Gtk.Label(
                label="Dynamic Icon Example\n\nClick buttons to change the tray icon!"
            )
            label.set_wrap(True)
            box.append(label)
            
            # Button to simulate notification
            btn_notify = Gtk.Button(label="Simulate Notification")
            btn_notify.connect("clicked", lambda w: self.on_notification())
            box.append(btn_notify)
            
            # Button to clear
            btn_clear = Gtk.Button(label="Clear Notification")
            btn_clear.connect("clicked", lambda w: self.on_clear())
            box.append(btn_clear)
            
            self.window.set_child(box)
        
        self.window.present()
    
    def on_notification(self):
        """Simulate receiving a notification"""
        self.has_notifications = True
        if self.tray:
            self.tray.change_icon("mail-unread")
            self.tray.change_status("NeedsAttention")
        print("📬 Notification received! Icon changed to 'mail-unread'")
    
    def on_clear(self):
        """Clear notifications"""
        self.has_notifications = False
        if self.tray:
            self.tray.change_icon("mail-read")
            self.tray.change_status("Active")
        print("✅ Notifications cleared! Icon changed to 'mail-read'")
    
    def toggle_window(self):
        if self.window.is_visible():
            self.window.hide()
        else:
            self.window.present()


def main():
    # Create application
    app = DynamicIconApp()
    
    # Create tray icon (start with "no mail" icon)
    tray = TrayIcon(
        app_id="com.example.trayer.dynamic",
        title="Dynamic Icon Example",
        icon_name="mail-read"
    )
    
    # Store tray reference in app
    app.tray = tray
    
    # Left-click toggles window
    tray.set_left_click(app.toggle_window)
    
    # Add menu items
    tray.add_menu_item("Show Window", callback=lambda: app.window.present())
    tray.add_menu_item("Simulate Notification", callback=app.on_notification)
    tray.add_menu_item("Clear Notification", callback=app.on_clear)
    tray.add_menu_separator()
    tray.add_menu_item("Quit", callback=app.quit)
    
    # Setup and run
    tray.setup()
    app.run()


if __name__ == "__main__":
    main()
