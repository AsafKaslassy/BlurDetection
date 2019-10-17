import sys
from BuildData import Version
from cx_Freeze import setup, Executable
from os.path import dirname

buildPath = r'..\..\..\bin\BlurDetection'

# import scipy
# includefiles_list = []
# scipy_path = dirname(scipy.__file__)
# includefiles_list.append(scipy_path)

# import os
# os.environ['TCL_LIBRARY'] = r"C:\Python27\envs\python35\tcl\tcl8.6"
# os.environ['TK_LIBRARY'] = r"C:\Python27\envs\python35\tcl\tk8.6"

buildOptions = dict(packages=["cv2", "numpy"],
                    excludes=["tcl", "tk"],
                    optimize=2,
                    include_msvcr=True,
                    silent=True,
                    build_exe=buildPath)

base = 'Console'
baseGui = 'Win32GUI' if sys.platform == 'win32' else None

executables = [
    Executable('BlurDetection.py', base=base)
]

setup(name='BlurDetection',
      version='{major}.{minor}.{fix}.{build}'.format(major=Version.major,
                                                     minor=Version.minor,
                                                     fix=Version.fix,
                                                     build=Version.build),
      description='',
      options=dict(build_exe=buildOptions),
      executables=executables, requires=["configReader", "cx_Freeze", "cv2", "numpy","replayLogger"])
