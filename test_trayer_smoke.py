#!/usr/bin/env python3
"""
Smoke test for trayer module - verifies basic functionality without GTK/GUI
"""

import sys

print("=" * 60)
print("Trayer Module Smoke Test")
print("=" * 60)

# Test 1: Import the module
print("\n[Test 1] Importing trayer...")
try:
    from trayer import TrayIcon
    print("✅ Import successful")
except Exception as e:
    print(f"❌ Import failed: {e}")
    sys.exit(1)

# Test 2: Create TrayIcon instance
print("\n[Test 2] Creating TrayIcon instance...")
try:
    tray = TrayIcon(
        app_id="com.example.test",
        title="Test Application",
        icon_name="application-x-executable"
    )
    print("✅ TrayIcon instance created")
except Exception as e:
    print(f"❌ Failed to create TrayIcon: {e}")
    sys.exit(1)

# Test 3: Add menu items
print("\n[Test 3] Adding menu items...")
try:
    tray.add_menu_item("Test Item", callback=lambda: print("Clicked!"))
    tray.add_menu_separator()
    tray.add_menu_item("Another Item", callback=None, enabled=False)
    print(f"✅ Added {len(tray.menu_items)} menu items")
except Exception as e:
    print(f"❌ Failed to add menu items: {e}")
    sys.exit(1)

# Test 4: Set click handlers
print("\n[Test 4] Setting click handlers...")
try:
    tray.set_left_click(lambda: print("Left clicked"))
    tray.set_middle_click(lambda: print("Middle clicked"))
    print("✅ Click handlers set")
except Exception as e:
    print(f"❌ Failed to set click handlers: {e}")
    sys.exit(1)

# Test 5: Setup D-Bus (with error suppression since no display)
print("\n[Test 5] Setting up D-Bus (may produce warnings if no display)...")
try:
    tray.setup()
    print("✅ D-Bus setup complete")
except Exception as e:
    print(f"❌ Failed to setup D-Bus: {e}")
    sys.exit(1)

# Test 6: Verify module attributes
print("\n[Test 6] Checking module attributes...")
try:
    assert hasattr(tray, 'change_icon'), "Missing change_icon method"
    assert hasattr(tray, 'change_status'), "Missing change_status method"
    assert hasattr(tray, 'update_menu'), "Missing update_menu method"
    print("✅ All expected methods exist")
except Exception as e:
    print(f"❌ Method check failed: {e}")
    sys.exit(1)

# Test 7: Test dynamic updates (without GUI interaction)
print("\n[Test 7] Testing dynamic updates...")
try:
    tray.change_icon("mail-unread")
    print("  - Icon changed to 'mail-unread'")
    tray.change_status("NeedsAttention")
    print("  - Status changed to 'NeedsAttention'")
    tray.change_status("Active")
    print("  - Status changed back to 'Active'")
    tray.change_icon("mail-read")
    print("  - Icon changed to 'mail-read'")
    print("✅ Dynamic updates work")
except Exception as e:
    print(f"❌ Dynamic update failed: {e}")
    sys.exit(1)

print("\n" + "=" * 60)
print("✅ All tests passed! Trayer module is functional.")
print("=" * 60)
print("\nNote: To see the tray icon, run an example with GTK4 in a")
print("desktop environment that supports StatusNotifierItem (GNOME with")
print("extension, KDE, XFCE, Cinnamon, etc.)")
