import subprocess
import sys
import os

# Try to install numpy first
try:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--no-cache-dir", "numpy==2.0.2"])
    print("Successfully installed numpy 2.0.2")
except Exception as e:
    print(f"Error installing numpy: {e}")

# Then try to install a compatible pandas version
try:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--no-cache-dir", "pandas==2.0.3"])
    print("Successfully installed pandas")
except Exception as e:
    print(f"Error installing pandas: {e}")
    # Try an alternative approach
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--no-cache-dir", "pandas"])
        print("Successfully installed pandas (unversioned)")
    except Exception as e2:
        print(f"Error installing pandas (unversioned): {e2}")

# Now run the main application
if os.path.exists("overview.py"):
    print("Starting the main application...")
    os.system(f"{sys.executable} -m streamlit run overview.py")
else:
    print("Main application file not found!")