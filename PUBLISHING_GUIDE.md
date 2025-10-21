# 🚀 Trayer v0.1.0 - Publishing Guide

This guide will help you complete the publication process for trayer on GitHub and PyPI.

## ✅ What's Already Done

- [x] Python package structure created
- [x] Documentation (README.md) with clear examples
- [x] MIT License added
- [x] Git repository initialized
- [x] Initial commit created
- [x] Git tag v0.1.0 created
- [x] Distribution packages built (`dist/trayer-0.1.0.tar.gz` and `.whl`)

## 📝 Next Steps

### Step 1: Create GitHub Repository

1. **Go to GitHub and create a new repository:**
   - URL: https://github.com/new
   - Repository name: `trayer`
   - Description: "System tray icons for GTK4 - betray GNOME 3's philosophy with style! 😈"
   - Make it **Public**
   - **DO NOT** initialize with README, .gitignore, or license (we already have them)
   - Click "Create repository"

2. **Push your code to GitHub:**
   ```bash
   cd /home/enne2/Sviluppo/trayer
   
   # Add GitHub as remote (replace YOUR_USERNAME with your GitHub username)
   git remote add origin https://github.com/YOUR_USERNAME/trayer.git
   
   # Push code and tags
   git push -u origin main
   git push origin v0.1.0
   ```

3. **Create GitHub Release:**
   - Go to your repository on GitHub
   - Click on "Releases" (right sidebar)
   - Click "Create a new release"
   - Choose tag: `v0.1.0`
   - Release title: `v0.1.0 - Initial Release`
   - Description:
     ```markdown
     # 🎉 First Release of Trayer!
     
     **Etymology:** From "tray" + "-er" (one who creates trays), and coincidentally 
     from Middle English "traitor" — because we gleefully betray GNOME 3's 
     philosophy of hiding tray icons! 😈
     
     ## ✨ Features
     
     - 🎯 Simple API - Add tray icons in 3 lines of code
     - 🖱️ Full Click Support - Left, right, and middle-click actions
     - 📋 Context Menus - Easy menu creation with separators
     - 🔄 Dynamic Updates - Change icons and menus at runtime
     - 🎨 Theme Integration - Uses system icon themes
     - 🐧 Linux Desktop Support - GNOME (with extension), KDE, XFCE, Cinnamon
     
     ## 📦 Installation
     
     ```bash
     pip install trayer
     ```
     
     ## 📚 Documentation
     
     See [README.md](https://github.com/YOUR_USERNAME/trayer#readme) for full documentation and examples.
     
     ## 🐛 Known Issues
     
     None yet! Please report any issues you find.
     ```
   - Attach files: Upload `dist/trayer-0.1.0.tar.gz` and `dist/trayer-0.1.0-py3-none-any.whl`
   - Click "Publish release"

### Step 2: Register on PyPI (if you haven't already)

1. **Create PyPI account:**
   - Go to: https://pypi.org/account/register/
   - Complete registration and verify email

2. **Enable 2FA (Two-Factor Authentication):**
   - Go to: https://pypi.org/manage/account/
   - Enable 2FA (required for uploading packages)

3. **Create API Token:**
   - Go to: https://pypi.org/manage/account/token/
   - Click "Add API token"
   - Token name: `trayer-upload`
   - Scope: "Entire account" (first time) or "Project: trayer" (after first upload)
   - Click "Add token"
   - **IMPORTANT:** Copy the token NOW (starts with `pypi-`)! You won't see it again!

### Step 3: Upload to PyPI

**Option A: Using Test PyPI First (Recommended for first time)**

Test PyPI lets you practice without affecting the real PyPI.

1. **Create TestPyPI account:**
   - Go to: https://test.pypi.org/account/register/
   - Create API token like above

2. **Upload to TestPyPI:**
   ```bash
   cd /home/enne2/Sviluppo/trayer
   
   # Upload to test PyPI
   .venv-build/bin/twine upload --repository testpypi dist/*
   
   # It will ask for:
   # Username: __token__
   # Password: <paste your TestPyPI token>
   ```

3. **Test installation from TestPyPI:**
   ```bash
   pip install --index-url https://test.pypi.org/simple/ trayer
   ```

4. **If everything works, upload to real PyPI:**
   ```bash
   .venv-build/bin/twine upload dist/*
   
   # Username: __token__
   # Password: <paste your PyPI token>
   ```

**Option B: Upload Directly to PyPI**

```bash
cd /home/enne2/Sviluppo/trayer

# Upload to PyPI
.venv-build/bin/twine upload dist/*

# It will ask for:
# Username: __token__
# Password: <paste your PyPI API token>
```

### Step 4: Verify Publication

1. **Check PyPI page:**
   - Go to: https://pypi.org/project/trayer/
   - Verify all information looks correct

2. **Test installation:**
   ```bash
   # In a new terminal or virtual environment
   pip install trayer
   python3 -c "from trayer import TrayIcon; print('Success!')"
   ```

3. **Update README badges:**
   - The badges in README.md will now work!
   - PyPI version badge will show v0.1.0

## 🎯 Quick Command Summary

```bash
# 1. Create repo on GitHub web interface first

# 2. Push to GitHub
cd /home/enne2/Sviluppo/trayer
git remote add origin https://github.com/YOUR_USERNAME/trayer.git
git push -u origin main
git push origin v0.1.0

# 3. Upload to PyPI (after creating account and API token)
.venv-build/bin/twine upload dist/*
# Username: __token__
# Password: pypi-YOUR_TOKEN_HERE
```

## 📋 Checklist

Before uploading to PyPI, verify:

- [ ] GitHub repository created and code pushed
- [ ] GitHub release v0.1.0 created with distribution files
- [ ] PyPI account created with 2FA enabled
- [ ] API token created and saved securely
- [ ] Tested package installation from TestPyPI (optional but recommended)
- [ ] Package uploaded to PyPI
- [ ] Installation from PyPI verified

## 🎉 Post-Publication

After successful publication:

1. **Announce it!**
   - Share on social media
   - Post on relevant forums/communities
   - Add to awesome-gtk or similar lists

2. **Set up issue templates:**
   - Create `.github/ISSUE_TEMPLATE/` for bug reports and features

3. **Add CI/CD:**
   - GitHub Actions for automated testing
   - Automated PyPI uploads on new tags

4. **Documentation improvements:**
   - Create GitHub Wiki
   - Add more examples

## 🆘 Troubleshooting

### "Package name already taken"
- Someone else registered `trayer` first
- Try: `trayer-gtk4`, `gtk4-trayer`, or `py-trayer`

### "Invalid credentials"
- Make sure you use `__token__` as username (exactly like that)
- Password should start with `pypi-`

### "File already exists"
- You can't re-upload the same version
- Bump version to 0.1.1 in `pyproject.toml` and `trayer/__init__.py`
- Rebuild: `.venv-build/bin/python -m build`

### Upload fails with 403
- Enable 2FA on PyPI
- Create a new API token

## 📞 Need Help?

If you encounter issues:
1. Check PyPI upload docs: https://packaging.python.org/tutorials/packaging-projects/
2. Twine documentation: https://twine.readthedocs.io/
3. Ask on Python Packaging Discord: https://discord.gg/pypa

---

**You're almost there! 🚀 Good luck with the publication!**
