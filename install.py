import shutil, site, os
folder = site.getsitepackages()[0]
os.chdir(folder)
os.mkdir(os.getcwd() + "GDBrowserPy")
files = ['/home/runner/GDBrowserPy/GDBrowserPy/__init__.py']
for f in files:
    shutil.copy(f, 'GDBrowserPy')