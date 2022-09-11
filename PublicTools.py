from curses.ascii import isdigit
import os
import sys
import json
import enum
import time

PROJECT_PATH = os.path.dirname(__file__)

# os.environ["USERPROFILE"] if sys.platform == "win32" else os.environ["HOME"]


class MemoryKey(enum.Enum):
    TEXT_SAVE_TO_DEFAULT_PATH = os.path.join(PROJECT_PATH, "TextSaveTo")
    MONITORING_INTERVAL = 0.5
    JSON_FILE_PATH = os.path.join(PROJECT_PATH, "bin/PrefereceSetting.json")


g_memoryDict = {v.name: v.value for _, v in MemoryKey.__members__.items()}


class MemoryDictController:
    def Display():
        i = 0
        for k, v in MemoryKey.__members__.items():
            print(f"{i}. {k} {g_memoryDict[k]}|{v.value}")
            i += 1

    def SetValueInIndex(ind: str, newValue: str) -> bool:
        if not ind.isnumeric():
            return False
        ind = int(ind)

        if not (0 <= ind < len(MemoryKey)):
            raise IndexError(f"{ind} must in [0, {len(MemoryKey)})")
        i = 0
        for k, _ in MemoryKey.__members__.items():
            if i == ind:
                beforeType = type(g_memoryDict[k])
                try:
                    g_memoryDict[k] = beforeType(newValue)
                except ValueError:
                    print(f"Input Must be type of {beforeType}. it cannot not converted from str")
                    return False
                break
            i += 1
        print(f"value on index{ind}={newValue}.")
        print("It would not take effect next time until time")
        return True


class FileH:
    @staticmethod
    def IsDriveExist(_rootDir: str) -> bool:
        if sys.platform != "win32":  # Only windows sys have the drive
            return True
        disk = os.path.splitdrive(_rootDir)[0]
        if not os.path.exists(disk):
            print(f"[Drive not exist] [{disk}]")
            return False
        return True

    @staticmethod
    def JoinBaseNameFormat(_basename: str = "test", _format: str = "txt"):
        return _basename + ('.' if (_format and _format[0] != '.') else '') + _format

    @staticmethod
    def MakeDir(p: str):
        if os.path.exists(p):
            print(f"[Dir already exist] [{p}]")
            return
        print(f"[Dir make] [{p}]")
        os.makedirs(p)

    @staticmethod
    def touch(_rootDir: str, _basename: str = "test", _format: str = "txt", _contents="") -> bool:
        if not FileH.IsDriveExist(_rootDir):
            return False

        absPath = os.path.join(_rootDir, FileH.JoinBaseNameFormat(_basename, _format))

        if os.path.exists(absPath) and os.path.isfile(absPath):
            print(f"[File Already Exist] [{absPath}]")
            return True

        FileH.MakeDir(_rootDir)
        with open(file=absPath, mode="w", encoding="UTF-8") as fw:
            if _contents:
                fw.write(_contents)
        print(f"[File Create Succeed] [{absPath}]")
        return True

    @staticmethod
    def touchByAbsPath(_absP: str, _contents="") -> bool:
        _rootDir = os.path.dirname(_absP)
        _basename = os.path.basename(_absP)
        _format = str()
        FileH.touch(_rootDir, _basename, _format, _contents)
        return True

    @staticmethod
    def GetTextNamedTimeStamps() -> str:
        nm = time.strftime("COPYCONTENTS%Y%m%d%H%M%S")
        return nm

    @staticmethod
    def WriteIntoJsonFile() -> bool:
        jsonPth = g_memoryDict[MemoryKey.JSON_FILE_PATH.name]
        if not os.path.exists(jsonPth):
            FileH.touchByAbsPath(jsonPth)

        with open(file=g_memoryDict[MemoryKey.JSON_FILE_PATH.name], mode="w", encoding="UTF-8") as f:
            json.dump(g_memoryDict, fp=f)
        print("WriteIntoJsonFile")

    @staticmethod
    def ReadFromJsonFile():
        if not os.path.isfile(g_memoryDict[MemoryKey.JSON_FILE_PATH.name]):
            FileH.WriteIntoJsonFile()
            return
        try:
            k1 = g_memoryDict.keys()
            with open(file=g_memoryDict[MemoryKey.JSON_FILE_PATH.name], mode="r", encoding="UTF-8") as f:
                recentMemoryDict: dict = json.load(fp=f)
                k2 = recentMemoryDict.keys()
                if k1 != k2:
                    FileH.WriteIntoJsonFile()
                    return
                for k, v in recentMemoryDict.items():
                    g_memoryDict[k] = v
        except json.JSONDecodeError:
            FileH.WriteIntoJsonFile()
        return


if __name__ == "__main__":
    print("Hello world")
    print({1, 2} == {2, 1})
