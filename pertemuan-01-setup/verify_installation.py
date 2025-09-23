import sys
import importlib

packages = ["numpy", "pandas", "sklearn", "skfuzzy", "cv2", "matplotlib", "nltk"]

for pkg in packages:
    try:
        m = importlib.import_module(pkg)
        version = getattr(m, "__version__", "unknown")  # most packages use __version_
        print(f"{pkg}: OK, version = {version}")
    except Exception as e:
        print(f"{pkg}: ERROR - {e}")

print("Python:", sys.version)