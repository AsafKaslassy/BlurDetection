@echo off

set BUILDPATH="..\..\..\bin\BlurDetection"
set PYTHONOPTIMIZE=True

IF EXIST %BUILDPATH% (
rd /S /Q %BUILDPATH%

)

python BuildData\VersionUpdate.py

python setup.py build

copy BuildData\README.txt %BUILDPATH%
copy BuildData\ReleaseNotes.txt %BUILDPATH%
copy BlurDetectionConfig.ini %BUILDPATH%
copy "C:\Python27\Lib\site-packages\llvmlite\binding\llvmlite.dll" %BUILDPATH%
