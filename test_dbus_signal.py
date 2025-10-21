#!/usr/bin/env python3
"""Minimal test to reproduce the D-Bus NoneType error"""

import dbus
import dbus.service
import dbus.mainloop.glib
from gi.repository import GLib, Gtk

SNI_INTERFACE = "org.kde.StatusNotifierItem"
SNI_PATH = "/StatusNotifierItem"

class TestSNI(dbus.service.Object):
    def __init__(self, bus, object_path):
        self.bus_name = dbus.service.BusName("org.test.trayer", bus)
        super().__init__(self.bus_name, object_path)
        self.status_val = "Active"
    
    @dbus.service.signal(dbus_interface=SNI_INTERFACE, signature='s')
    def NewStatus(self, status):
        pass
    
    def emit_status(self, status_str):
        print(f"Emitting status: {status_str}")
        self.status_val = status_str
        # This should trigger the error
        self.NewStatus(status_str)

# Setup D-Bus
dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
bus = dbus.SessionBus()

# Create object
obj = TestSNI(bus, SNI_PATH)

# Try to emit signal
print("Test 1: Emit with string")
obj.emit_status("NeedsAttention")

print("Test 2: Emit with dbus.String")
obj.emit_status(dbus.String("NeedsAttention"))

print("Success!")
