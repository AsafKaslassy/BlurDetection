import sys
from os import path

import imp

versionDataTemplate = \
"""
major = {major}
minor = {minor}
fix = {fix}
build = {build}
""".strip("\n")

versionFileFolder = path.dirname(sys.argv[0])
versionFileName = "Version.py"

versionFilePath = path.join(versionFileFolder, versionFileName)

versionModule = imp.load_source("version", versionFilePath)

versionData = versionDataTemplate.format(major = versionModule.major, minor = versionModule.minor,
                                         fix = versionModule.fix, build = versionModule.build + 1)

with open(versionFilePath, "w") as versionFile:
    versionFile.write(versionData)
