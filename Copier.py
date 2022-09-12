import os
import time
import threading
# python3.9 -m pip install pyperclip
# python3.9 -m pip uninstall pyperclip
import pyperclip
from PublicTools import FileH, MemoryKey, g_memoryDict, MemoryDictController


class Copier(threading.Thread):
    def __init__(self, callback, pause, textSaveTo):
        super(Copier, self).__init__()
        self._callback = callback
        self._pause = pause
        self._textSaveTo = textSaveTo
        self._stopping = False

    def run(self):
        recent_value = ""
        while not self._stopping:
            time.sleep(self._pause)
            tmp_value = pyperclip.paste()
            if tmp_value == recent_value:
                continue
            recent_value = tmp_value
            self._callback(self._textSaveTo, recent_value)

    def stop(self):
        self._stopping = True


WriteStat = {"writingTimes": 0, "charsCount": 0}


def SaveToInTime(pth: str, contents: str) -> bool:
    if not pth or not contents:
        return False
    with open(file=pth, mode="a", encoding="UTF-8") as f:
        f.write(contents)

    nChar = len(contents)
    WriteStat["writingTimes"] += 1
    WriteStat["charsCount"] += nChar
    print(f'''WriteTimes { WriteStat["writingTimes"] }, {nChar} chars writed''')
    return True


def GetTextSaveToAbsPath() -> str:
    textSaveTo = g_memoryDict[MemoryKey.TEXT_SAVE_TO_DEFAULT_PATH.name]
    textBaseName = FileH.GetTextNamedTimeStamps()
    textAbsPath = os.path.join(textSaveTo, FileH.JoinBaseNameFormat(textBaseName, "txt"))
    FileH.touchByAbsPath(textAbsPath)
    return textAbsPath


def main():
    FileH.ReadFromJsonFile()
    sleepTime = g_memoryDict[MemoryKey.MONITORING_INTERVAL.name]
    textAbsPath = GetTextSaveToAbsPath()
    watcher = Copier(SaveToInTime, sleepTime, textAbsPath)
    watcher.start()
    memDictCon = MemoryDictController()
    memDictCon()
    watcher.stop()
    FileH.WriteIntoJsonFile()
    
    print(f"Contents have write into [{textAbsPath}]. {WriteStat}")
    print("Program will quit within 5 seconds")
    time.sleep(5)


if __name__ == "__main__":
    main()