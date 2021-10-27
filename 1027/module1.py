import sys

mojor,minor,micro = list(sys.version_info[:3])
print(f'使用しているPythonのバージョンは{mojor}.{minor}.{micro}です。')