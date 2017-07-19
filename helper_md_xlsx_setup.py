from distutils.core import setup
import py2exe, sys, os
from distutils.filelist import findall
import matplotlib

packages =  ['pandas', 'matplotlib', 'pytz']
excludes = ['_gtkagg', '_tkagg', 'bsddb', 'curses', 'pywin.debugger',
            'pywin.debugger.dbgcon', 'pywin.dialogs', 'tcl',
            'Tkconstants', 'Tkinter', 'pydoc', 'doctest', 'test', 'sqlite3'
            ]
dll_excludes = ["MSVCP90.dll",'libgdk-win32-2.0-0.dll', 'libgobject-2.0-0.dll', 'tcl84.dll',
                'tk84.dll']


sys.argv.append('py2exe')
setup(
  options = {
    'py2exe' : {
    	'packages': packages,
        'compressed': 1,
        'optimize': 2,
        'bundle_files': 3, #Options 1 & 2 do not work on a 64bit system
        'dist_dir': 'dist',  # Put .exe in dist/
        'xref': False,
        'skip_archive': False,
        'ascii': False,
        "dll_excludes": dll_excludes,
        'excludes': excludes,
          }
        },
  zipfile=None,
  data_files=matplotlib.get_py2exe_datafiles(),
  console = ['helper_md_xlsx.py'],
)