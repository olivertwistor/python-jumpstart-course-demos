"""
Main program file for the lolcat factory app.
"""

from cat_service import CatService
import lolcat_ui as ui


def main():
    img_folder = "cat-pictures"
    ui.print_header()
    cat_service = CatService(
        img_folder,
        "http://consuming-python-services-api.azurewebsites.net/cats/random")
    try:
        cat_service.download(8, "cat-", ".jpg")
    except (FileExistsError, ValueError) as e:
        print(e.strerror)
        exit(1)

    ui.show_files(img_folder)


if __name__ == '__main__':
    main()
