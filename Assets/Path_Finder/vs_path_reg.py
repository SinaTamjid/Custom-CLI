# Main/vscode_path.py
import winreg
import os

def get_vscode_exe_path() -> str | None:
    """
    Searches Windows Registry for VSCode install path and returns full path to VSCode.exe.
    Returns None if not found.
    """
    registry_paths = [
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
        r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"
    ]
    for root in [winreg.HKEY_LOCAL_MACHINE, winreg.HKEY_CURRENT_USER]:
        for reg_path in registry_paths:
            try:
                with winreg.OpenKey(root, reg_path) as uninstall_key:
                    for i in range(winreg.QueryInfoKey(uninstall_key)[0]):
                        subkey_name = winreg.EnumKey(uninstall_key, i)
                        with winreg.OpenKey(uninstall_key, subkey_name) as subkey:
                            try:
                                name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                                if "Visual Studio Code" in name:
                                    install_path = winreg.QueryValueEx(subkey, "InstallLocation")[0]
                                    exe_path = os.path.join(install_path, "Code.exe")
                                    if os.path.exists(exe_path):
                                        return exe_path
                            except FileNotFoundError:
                                continue
            except FileNotFoundError:
                continue
    return None

def get_git_exe_path() -> str | None:
    """
    Searches Windows Registry for Git install path and returns full path to git.exe.
    Returns None if not found.
    """
    registry_paths = [
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
        r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"
    ]
    for root in [winreg.HKEY_LOCAL_MACHINE, winreg.HKEY_CURRENT_USER]:
        for reg_path in registry_paths:
            try:
                with winreg.OpenKey(root, reg_path) as uninstall_key:
                    for i in range(winreg.QueryInfoKey(uninstall_key)[0]):
                        subkey_name = winreg.EnumKey(uninstall_key, i)
                        with winreg.OpenKey(uninstall_key, subkey_name) as subkey:
                            try:
                                name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                                if "Git" in name:
                                    install_path = winreg.QueryValueEx(subkey, "InstallLocation")[0]
                                    exe_path = os.path.join(install_path, "bin", "git.exe")
                                    if os.path.exists(exe_path):
                                        return exe_path
                            except FileNotFoundError:
                                continue
            except FileNotFoundError:
                continue
    return None

def get_maya_exe_path():
    """Finds Maya's .exe File dynamically."""
    maya_versions = ["2025", "2024", "2023", "2022", "2021"]

    for version in maya_versions:
        try:
            key_path = rf"SOFTWARE\Autodesk\Maya\{version}\Setup\InstallPath"
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path) as key:
                install_path, _ = winreg.QueryValueEx(key, "MAYA_INSTALL_LOCATION")
                mayapy_path = os.path.join(install_path, "bin", "maya.exe")

                # Validate path
                if os.path.exists(mayapy_path):
                    return mayapy_path
        except Exception as e:
            print(f"Failed to find Maya {version}: {e}")

    return None  