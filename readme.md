# Generate exe with min size for Win

> find the pythonx.exe path

- For Linux
  - `whereis python`

- For Win
  - `where python`
  - `python -m site`
  - in vscode `ctrl+shift+P`, select `interpreter`, e.g., `C:\Users\l00613497\AppData\Local\Programs\Python\Python310`
```sh
cd C:\Users\l00613497\AppData\Local\Programs\Python\Python310
./python.exe -m pip list
./python.exe -m pip install pyinstaller
# or in win
.\\python.exe -m pip list
.\\python.exe -m pip install pyinstaller

cd C:\Users\l00613497\AppData\Local\Programs\Python\Python310\Scripts
./pyinstaller.exe --onedir "D:\Markdown\Learning\TaskMD5\MD5Manager.py" --specpath="D:\Markdown\Learning\TaskMD5" --workpath="D:\Markdown\Learning\TaskMD5\build" --distpath="D:\Markdown\Learning\TaskMD5\dist"
```
18.3MB

## Decreasing package size
- Method 1: 
.spec -> Analysis -> excludes, to exclude some packages manually
- Method 2: virtual env
```sh
./python.exe -m pip install pipenv
# or in win
.\\python.exe -m pip install pipenv

# go to a specified path, e.g. C:\Users\costa\Documents\python\CopierCMD
cd /path/you/specified/to/generate/env
pipenv install
```

### Q1: FileNotFoundError 'C:/Python27/Scripts/python.exe'
Traceback (most recent call last):
  File "C:\Users\l00613497\AppData\Local\Programs\Python\Python310\Lib\site-packages\pipenv\vendor\pythonfinder\models\python.py", line 620, in parse_executable
    result_version = get_python_version(path)
  File "C:\Users\l00613497\AppData\Local\Programs\Python\Python310\Lib\site-packages\pipenv\vendor\pythonfinder\utils.py", line 97, in get_python_version
    c = subprocess.Popen(version_cmd, **subprocess_kwargs)
  File "C:\Users\l00613497\AppData\Local\Programs\Python\Python310\lib\subprocess.py", line 966, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "C:\Users\l00613497\AppData\Local\Programs\Python\Python310\lib\subprocess.py", line 1435, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
  File "C:\Users\l00613497\AppData\Local\Programs\Python\Python310\Lib\site-packages\pipenv\vendor\pythonfinder\models\python.py", line 622, in parse_executable
raise ValueError("Not a valid python path: %r" % path)
FileNotFoundError: [WinError 2] 系统找不到指定的文件。
ValueError: Not a valid python path: 'C:/Python27/Scripts/python.exe'
### A1: go to regedit, delete python2 or python3 folder by the error msg
delete python3 folder here: HKLM\SOFTWARE\Python\PythonCore\
delete python3 folder here: HKCU\SOFTWARE\Python\PythonCore\
delete python2 folder here: HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Python 

Then go to a **specified** directory to execute:
`pipenv install`

```sh
Creating a virtualenv for this project...
Pipfile: C:\Users\l00613497\AppData\Local\Programs\Python\Python310\Pipfile
Using C:/Users/l00613497/AppData/Local/Programs/Python/Python310/python.exe (3.10.2) to create virtualenv...
[=   ] Creating virtual environment...created virtual environment CPython3.10.2.final.0-64 in 1112ms
  creator CPython3Windows(dest=C:\Users\l00613497\.virtualenvs\Python310-2cq2Kyig, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=C:\Users\l00613497\AppData\Local\pypa\virtualenv)
    added seed packages: pip==22.2.2, setuptools==65.3.0, wheel==0.37.1
  activators BashActivator,BatchActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

Successfully created virtual environment!
Virtualenv location: C:\Users\l00613497\.virtualenvs\Python310-2cq2Kyig
Creating a Pipfile for this project...
Pipfile.lock not found, creating...
Locking [packages] dependencies...
Locking [dev-packages] dependencies...
Updated Pipfile.lock (e4eef2)!
Installing dependencies from Pipfile.lock (e4eef2)...
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
```

now Pipfile created in current folder

```sh
pipenv shell
# rememeber here pip and python is in pipenv, so python3.x is not essential, execute it to find the dependency
python xxx.py
pip list

# to meet the dependency copy the essential package from local downloaded package 
pip install xxx
# or from internet
pip install xxx -i https://pypi.tuna.tsinghua.edu.cn/simple
# gen exe
C:\Users\l00613497\AppData\Local\Programs\Python\Python310\Scripts\pyinstaller.exe --onedir "D:\Markdown\Learning\TaskMD5\MD5Manager.py" --specpath="D:\Markdown\Learning\TaskMD5" --workpath="D:\Markdown\Learning\TaskMD5\build" --distpath="D:\Markdown\Learning\TaskMD5\dist"
```

e.g.
```sh
(CopierCMD-HUFoCig3) C:\Users\costa\Documents\python\CopierCMD>python Copier.py
Traceback (most recent call last):
  File "C:\Users\costa\Documents\python\CopierCMD\Copier.py", line 6, in <module>
    import pyperclip
ModuleNotFoundError: No module named 'pyperclip'

(CopierCMD-HUFoCig3) C:\Users\costa\Documents\python\CopierCMD>pip install pyperclip
Collecting pyperclip
  Using cached pyperclip-1.8.2-py3-none-any.whl
Installing collected packages: pyperclip
Successfully installed pyperclip-1.8.2

C:\Users\costa\AppData\Local\Programs\Python\Python310\Scripts\pyinstaller.exe ...
```