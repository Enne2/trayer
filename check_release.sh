#!/bin/bash
# Trayer - Quick check before publishing

echo "🔍 Trayer Pre-Publication Checklist"
echo "===================================="
echo ""

# Check if we're in the right directory
if [ ! -f "pyproject.toml" ]; then
    echo "❌ Error: Not in trayer directory (pyproject.toml not found)"
    exit 1
fi

echo "✅ Directory check passed"
echo ""

# Check version consistency
VERSION_PYPROJECT=$(grep '^version = ' pyproject.toml | cut -d'"' -f2)
VERSION_INIT=$(grep '__version__ = ' trayer/__init__.py | cut -d'"' -f2)

echo "📦 Version Check:"
echo "   pyproject.toml: $VERSION_PYPROJECT"
echo "   __init__.py:    $VERSION_INIT"

if [ "$VERSION_PYPROJECT" != "$VERSION_INIT" ]; then
    echo "❌ Version mismatch!"
    exit 1
else
    echo "✅ Versions match: $VERSION_PYPROJECT"
fi
echo ""

# Check git status
echo "📝 Git Status:"
if [ -n "$(git status --porcelain)" ]; then
    echo "⚠️  Warning: You have uncommitted changes:"
    git status --short
else
    echo "✅ Working directory clean"
fi
echo ""

# Check if tag exists
if git tag | grep -q "^v$VERSION_PYPROJECT$"; then
    echo "✅ Git tag v$VERSION_PYPROJECT exists"
else
    echo "⚠️  Git tag v$VERSION_PYPROJECT not found"
    echo "   Create it with: git tag -a v$VERSION_PYPROJECT -m 'Release v$VERSION_PYPROJECT'"
fi
echo ""

# Check if dist files exist
echo "📦 Distribution Files:"
if [ -f "dist/trayer-$VERSION_PYPROJECT.tar.gz" ] && [ -f "dist/trayer-$VERSION_PYPROJECT-py3-none-any.whl" ]; then
    echo "✅ Distribution files exist:"
    ls -lh dist/trayer-$VERSION_PYPROJECT*
else
    echo "❌ Distribution files not found. Build with:"
    echo "   .venv-build/bin/python -m build"
fi
echo ""

# Check remote
echo "🌐 Git Remote:"
REMOTE=$(git remote get-url origin 2>/dev/null)
if [ -n "$REMOTE" ]; then
    echo "✅ Remote configured: $REMOTE"
else
    echo "⚠️  No remote configured"
    echo "   Add with: git remote add origin https://github.com/USERNAME/trayer.git"
fi
echo ""

# Summary
echo "📋 Summary:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Version: $VERSION_PYPROJECT"
echo ""
echo "Next steps:"
echo "1. If changes uncommitted: git add . && git commit -m 'message'"
echo "2. If tag missing: git tag -a v$VERSION_PYPROJECT -m 'Release v$VERSION_PYPROJECT'"
echo "3. If dist missing: .venv-build/bin/python -m build"
echo "4. Push to GitHub: git push origin main && git push origin v$VERSION_PYPROJECT"
echo "5. Upload to PyPI: .venv-build/bin/twine upload dist/*"
echo ""
echo "For detailed instructions, see: PUBLISHING_GUIDE.md"
