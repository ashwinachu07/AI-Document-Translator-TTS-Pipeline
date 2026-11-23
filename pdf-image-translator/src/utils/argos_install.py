import os
from argostranslate import package

# Check for local model file first, or automatically download from package index
local_model = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "..", "models", "translate-en_hi-1_1.argosmodel")
)

if os.path.exists(local_model):
    print(f"Installing Argos model from local file: {local_model}")
    package.install_from_path(local_model)
    print("Model installed successfully.")
else:
    print("Local model file not found. Fetching models from Argos index...")
    try:
        package.update_package_index()
        available_packages = package.get_available_packages()
        pkg = next((p for p in available_packages if p.from_code == "en" and p.to_code == "hi"), None)
        if pkg:
            print("Downloading and installing English -> Hindi model...")
            download_path = pkg.download()
            package.install_from_path(download_path)
            print("Package installed successfully.")
        else:
            print("Model package not found in index.")
    except Exception as e:
        print(f"Error downloading package: {e}")
