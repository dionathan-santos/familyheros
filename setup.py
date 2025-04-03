import subprocess
import sys

def install_dependencies():
    # First install numpy with the specific version
    subprocess.check_call([sys.executable, "-m", "pip", "install", "numpy==2.0.2"])
    
    # Then install pandas without specifying version to get a compatible one
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas"])
    
    # Install the rest of the dependencies
    dependencies = [
        "streamlit==1.32.0",
        "scikit-learn==1.4.0",
        "pydeck==0.8.1b0",
        "matplotlib==3.8.2",
        "seaborn==0.13.1",
        "openpyxl==3.1.2",
        "sentence-transformers==2.2.2",
        "transformers==4.38.1",
        "torch==2.2.0"
    ]
    
    for dep in dependencies:
        subprocess.check_call([sys.executable, "-m", "pip", "install", dep])

if __name__ == "__main__":
    install_dependencies()