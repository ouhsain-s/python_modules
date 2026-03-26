import sys
import os
import site


class Venv_conf:
    def is_virtual_environment() -> bool:
        return sys.prefix != sys.base_prefix

    def is_global_environment() -> bool:
        return sys.prefix == sys.base_prefix

    def get_python_path() -> str:
        return sys.executable + sys.version[1:4]

    def get_venv_name() -> str:
        return os.path.basename(sys.prefix)

    def get_env_path() -> str:
        return sys.prefix

    def get_site_packages() -> list:
        try:
            return site.getsitepackages()
        except Exception:
            return []


def print_outside_env():
    print("MATRIX STATUS: You're still plugged in\n")
    print(f"Current Python: {Venv_conf.get_python_path()}")
    print("Virtual Environment: None detected\n")

    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.\n")

    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate  # On Unix")
    print("matrix_env\nScripts\nactivate   # On Windows")
    print("\nThen run this program again.")


def print_inside_env():
    print("MATRIX STATUS: Welcome to the construct\n")
    print(f"Current Python: {Venv_conf.get_python_path()}")

    venv_name = Venv_conf.get_venv_name()
    env_path = Venv_conf.get_env_path()

    print(f"Virtual Environment: {venv_name}")
    print(f"Environment Path: {env_path}\n")

    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting the global system.\n")

    packages = Venv_conf.get_site_packages()
    if packages:
        print("Package installation path:")
        for path in packages:
            print(path)
    else:
        print("Could not determine site-packages location.")


def main():
    try:
        if Venv_conf.is_virtual_environment():
            print_inside_env()
        else:
            print_outside_env()
    except Exception as e:
        print("ERROR:", e)


if __name__ == "__main__":
    main()
