# -*- mode: python -*-

block_cipher = None


a = Analysis(['Book_Search_App.py'],
             pathex=['D:\\Academics\\My_GitRepo_Academics\\Python\\tkinter'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Book_Search_App',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
