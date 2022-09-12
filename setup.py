from PublicTools import PROJECT_PATH
import os

PROJECT_PATH = os.path.abspath(PROJECT_PATH)


class Setup:
    FORCE_OVERRIDE_MODE = True

    def GetForceMode(self):
        return " --noconfirm" if Setup.FORCE_OVERRIDE_MODE else str()

    def GetAppIcon(self):
        return "--icon=" + self.appIconPath if self.appIconPath else str()

    def Checker(self) -> bool:
        if not os.path.isfile(self.pyinstaller):
            return False
        if not os.path.isfile(self.mainPyScript):
            return False
        if not os.path.isdir(self.specpath):
            return False
        if not os.path.isdir(os.path.dirname(self.workpath)):
            return False
        if not os.path.isdir(os.path.dirname(self.distpath)):
            return False
        return True

    def __init__(self):
        self.pyinstaller = r"C:\Users\costa\AppData\Local\Programs\Python\Python310\Scripts\pyinstaller.exe"
        self.mainPyScript = os.path.join(PROJECT_PATH, "Copier.py")
        self.specpath = PROJECT_PATH
        self.appIconPath = str()
        self.addData = ("bin/*;bin/",)

        self.workpath = os.path.join(PROJECT_PATH, "build")
        self.distpath = os.path.join(PROJECT_PATH, "dist")

    def GetAddData(self) -> str:
        addDataStr = ' '.join([f'''--add-data "{p2p}"''' for p2p in self.addData])
        return addDataStr

    def __call__(self) -> bool:
        if not self.Checker():
            return False
        # it would not use pipenv
        cmdFormat = f"{self.pyinstaller} --onedir {self.mainPyScript} {self.GetAppIcon()} {self.GetAddData()} --specpath={self.specpath} --workpath={self.workpath} --distpath={self.distpath} {self.GetForceMode()}"
        os.system(cmdFormat)


if __name__ == "__main__":
    setup = Setup()
    setup()

# C:\Users\costa\AppData\Local\Programs\Python\Python310\Scripts\pyinstaller.exe --onedir c:\Users\costa\Documents\python\CopierCMD\Copier.py --add-data "bin/*;bin/" --specpath=c:\Users\costa\Documents\python\CopierCMD --workpath=c:\Users\costa\Documents\python\CopierCMD\build --distpath=c:\Users\costa\Documents\python\CopierCMD\dist
#
