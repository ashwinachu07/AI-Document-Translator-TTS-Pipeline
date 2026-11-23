import argparse
from argostranslate import package


def install_language_pair(source_code, target_code):
    package.update_package_index()
    available_packages = package.get_available_packages()
    language_package = next(
        (
            item
            for item in available_packages
            if item.from_code == source_code and item.to_code == target_code
        ),
        None,
    )

    if language_package is None:
        print(
            f"Argos package not found for {source_code} -> {target_code}. "
            "Check the supported language codes or use an Argos .argosmodel file."
        )
        return False

    print(
        f"Downloading and installing Argos model: "
        f"{source_code} -> {target_code}"
    )
    download_path = language_package.download()
    package.install_from_path(download_path)
    print("Argos model installed successfully.")
    return True


def main():
    parser = argparse.ArgumentParser(
        description="Download and install Argos Translate language packages."
    )
    parser.add_argument(
        "--from",
        dest="source_code",
        default="en",
        help="Source language code, for example en",
    )
    parser.add_argument(
        "--to",
        dest="target_code",
        default="hi",
        help="Target language code, for example hi, ml, ta, or es",
    )
    args = parser.parse_args()
    install_language_pair(args.source_code, args.target_code)


if __name__ == "__main__":
    main()
