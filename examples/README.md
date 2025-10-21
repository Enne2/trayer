# Trayer Examples

This directory contains working examples of the trayer library.

## Running Examples

Make sure trayer is installed:
```bash
pip install trayer
```

Then run any example:
```bash
python3 example_minimal.py
python3 example_dynamic_icon.py
python3 example_dynamic_menu.py
```

## Examples

### 1. `example_minimal.py`
Basic integration showing:
- Simple tray icon creation
- Left-click to toggle window
- Basic context menu

### 2. `example_dynamic_icon.py`
Shows how to change icons dynamically:
- Change icon on state change (mail-read → mail-unread)
- Use status changes (Active, NeedsAttention)
- Simulate notifications

### 3. `example_dynamic_menu.py`
Shows how to update menus dynamically:
- Change menu items based on app state
- Enable/disable menu items
- Use `update_menu()` to refresh

## System Requirements

See main [README.md](../README.md) for installation instructions.
