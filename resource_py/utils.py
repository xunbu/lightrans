import os
import subprocess
import sys
import platformdirs
import platform


app_name = "lightrans" # 你的应用程序名
# 获取用户配置目录
config_dir = platformdirs.user_config_dir(app_name)
# 确保目录存在
os.makedirs(config_dir, exist_ok=True)
# 构建配置文件的完整路径C:\Users\jxgm\AppData\Local\lightrans\lightrans\account.ini
config_file_path = os.path.join(config_dir, "account.ini") # 或者 .ini, .yaml 等

def resource_path(relative_path):
    """
    使用该方法打包时在app关闭时资源会被销毁，因此只适合初始化和只读的文件
    """
    try:
        base_path=sys._MEIPASS
    except Exception:
        base_path=os.path.abspath(".")
    return os.path.join(base_path,relative_path)

def open_folder_in_explorer(folder_path):
    """Opens the specified folder in the default file explorer."""
    if not os.path.isdir(folder_path):
        print(f"Error: Folder not found at {folder_path}")
        return

    current_platform = platform.system()

    if current_platform == "Windows":
        try:
            # Use explorer command
            subprocess.run(['explorer', os.path.normpath(folder_path)], check=True)
        except FileNotFoundError:
             print(f"Error: 'explorer' command not found. Cannot open folder on Windows.")
        except Exception as e:
            print(f"An error occurred while opening folder on Windows: {e}")

    elif current_platform == "Darwin": # macOS
        try:
            # Use open command
            subprocess.run(['open', folder_path], check=True)
        except FileNotFoundError:
             print(f"Error: 'open' command not found. Cannot open folder on macOS.")
        except Exception as e:
             print(f"An error occurred while opening folder on macOS: {e}")

    elif current_platform == "Linux":
        try:
            # Use xdg-open (standard way for most Linux desktops)
            subprocess.run(['xdg-open', folder_path], check=True)
        except FileNotFoundError:
            print(f"Error: 'xdg-open' command not found. Please install it or manually navigate to the folder.")
        except Exception as e:
             print(f"An error occurred while opening folder on Linux: {e}")

    else:
        print(f"Unsupported operating system: {current_platform}")
        print(f"Folder path: {folder_path}")

if __name__ == '__main__':
    open_folder_in_explorer(config_dir)



