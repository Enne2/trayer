# Quick Commands for Trayer Publication

## 📦 Package is ready! Here's what you need to do:

### 1️⃣ Create GitHub Repository
Go to: https://github.com/new
- Name: `trayer`
- Description: "System tray icons for GTK4 - betray GNOME 3's philosophy with style! 😈"
- Public repository
- DON'T add README/License/gitignore (we have them)

### 2️⃣ Push to GitHub (REPLACE YOUR_USERNAME!)
```bash
cd /home/enne2/Sviluppo/trayer

# Add remote (REPLACE YOUR_USERNAME with your GitHub username!)
git remote add origin https://github.com/YOUR_USERNAME/trayer.git

# Push everything
git push -u origin main
git push origin v0.1.0
```

### 3️⃣ Create GitHub Release
- Go to: https://github.com/YOUR_USERNAME/trayer/releases/new
- Choose tag: v0.1.0
- Title: "v0.1.0 - Initial Release"
- Copy description from PUBLISHING_GUIDE.md
- Attach files: dist/trayer-0.1.0.tar.gz and dist/trayer-0.1.0-py3-none-any.whl

### 4️⃣ Register on PyPI (if you don't have account)
- Go to: https://pypi.org/account/register/
- Verify email
- Enable 2FA: https://pypi.org/manage/account/
- Create API token: https://pypi.org/manage/account/token/
  - Name: "trayer-upload"
  - Scope: "Entire account"
  - **COPY THE TOKEN!** (starts with pypi-)

### 5️⃣ Upload to TestPyPI (recommended first time)
```bash
cd /home/enne2/Sviluppo/trayer

# Create TestPyPI account first: https://test.pypi.org/account/register/
# Then upload:
.venv-build/bin/twine upload --repository testpypi dist/*

# When prompted:
# Username: __token__
# Password: <your TestPyPI token>

# Test it:
python3 -m venv /tmp/test-trayer
/tmp/test-trayer/bin/pip install --index-url https://test.pypi.org/simple/ trayer
```

### 6️⃣ Upload to PyPI (THE REAL THING!)
```bash
cd /home/enne2/Sviluppo/trayer

.venv-build/bin/twine upload dist/*

# When prompted:
# Username: __token__
# Password: <your PyPI token>
```

### 7️⃣ Verify It Works!
```bash
# Install from PyPI
pip install trayer

# Test import
python3 -c "from trayer import TrayIcon; print('🎉 Success!')"
```

### 8️⃣ Check Your Package
- PyPI page: https://pypi.org/project/trayer/
- Installation: `pip install trayer`
- GitHub: https://github.com/YOUR_USERNAME/trayer

## 🎉 DONE! Your package is live!

---

## 📝 For Future Releases

When you want to release v0.2.0:

1. Update version in:
   - `pyproject.toml` (line 6)
   - `trayer/__init__.py` (line 22)

2. Build and release:
```bash
# Commit changes
git add .
git commit -m "Bump version to 0.2.0"

# Create tag
git tag -a v0.2.0 -m "Release v0.2.0"

# Build
.venv-build/bin/python -m build

# Check everything
./check_release.sh

# Push to GitHub
git push origin main
git push origin v0.2.0

# Upload to PyPI
.venv-build/bin/twine upload dist/*
```

---

## 🆘 Problems?

Check PUBLISHING_GUIDE.md for detailed troubleshooting!
