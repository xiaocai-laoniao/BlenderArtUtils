# Mac: /Applications/Blender.app/Contents/Resources/{version}/scripts/startup
# Windows: C:\Program Files\Blender Foundation\Blender\{version}\scripts\startup

# Path: ChildhoodAndy/install.py

import os
import shutil

BLENDER_VERSION = '4.1'

def install():
    # 获取脚本目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    dir_name = os.path.basename(script_dir)
    print(f"Script directory: {script_dir}, dir name: {dir_name}")

    dest_dir = os.path.join(startup_dir(), dir_name)
    replace_directory(script_dir, dest_dir)


def startup_dir():
    # 获取启动目录
    # get os type
    startup_dir = None
    if os.name == 'posix':
        # Mac
        startup_dir = f"/Applications/Blender.app/Contents/Resources/{BLENDER_VERSION}/scripts/startup"
    elif os.name == 'nt':
        # Windows
        startup_dir = f"C:\\Program Files\\Blender Foundation\\Blender\\{BLENDER_VERSION}\\scripts\\startup"
    else:
        print("Unsupported operating system")

    print(f"Startup directory: {startup_dir}")
    return startup_dir

def replace_directory(src, dst):
    # 检查目标目录是否存在
    if os.path.exists(dst) and os.path.isdir(dst):
        # 如果存在，则先删除目标目录
        shutil.rmtree(dst)
    
    # 现在目标目录已不存在，可以安全复制
    shutil.copytree(src, dst)
    print(f"Copy from {src} to {dst}")
    print(f"Install completed")

if __name__ == "__main__":
    install()