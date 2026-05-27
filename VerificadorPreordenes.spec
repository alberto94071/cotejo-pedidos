# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['cotejo_pedidos.py'],
    pathex=[],
    binaries=[],
    datas=[('igss_logo.png', '.'), ('igss_azul-removebg-preview.png', '.'), ('cotejo_icon.ico', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='VerificadorPreordenes',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['cotejo_icon.ico'],
)
