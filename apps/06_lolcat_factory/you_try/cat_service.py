import os
import shutil

import requests


class CatService:
    """
    This class provides access to downloading lolcat images.
    """
    def __init__(self, save_folder: str, service_url: str):
        """
        :param save_folder: The folder in which the cat images are to be stored
        :param service_url: The URL from which to get the cat images
        """
        self.save_folder = save_folder
        self.service_url = service_url

    def download(self, n_images: int, prefix: str, extension: str):
        """
        Downloads a number of images from the "cat server" and stores them
        locally.

        :param n_images: The number of images to download.
        :param prefix: What the local file names should start with.
        :param extension: The file extension of the local files.

        :raises FileExistsError: If the path to the local save folder exists
                                 but is not a directory.
        :raises ValueError: If number of images is lower than 1.
        """
        if n_images < 1:
            raise ValueError(
                "Number of images (n_images) must be equal to or greater "
                "than 1.")

        print("Contacting lolcat service to download images.")

        for i in range(1, n_images + 1):
            image_full_path = self._get_full_image_path(
                prefix + str(i) + extension
            )
            self._save_image(self.service_url, image_full_path)

        print("Finished downloading images.")

    @classmethod
    def _save_image(cls, source_file: str, target_filename: str):
        """
        Reads a binary file and copies it to another file.

        :param source_file: The file from which to copy.
        :param target_filename: The file to which to copy.
        """
        print("Downloading image...", end=" ")

        read_data_stream = requests.get(source_file, stream=True)
        read_data_file = read_data_stream.raw

        with open(target_filename, "wb") as fout:
            shutil.copyfileobj(read_data_file, fout)

        print("done.")

    def _get_full_image_path(self, filename: str) -> str:
        """
        First determines whether or not the class attribute save_folder exists.
        If not, it will be created. Then returns the save folder plus the
        filename.

        :param filename: The basename for a file.

        :return: The basename of the file appended to the save folder.

        :raises FileExistError: If the path to the local save folder exists
                                but is not a directory.
        """
        if os.path.exists(self.save_folder):
            if not os.path.isdir(self.save_folder):
                raise FileExistsError(
                    "The path already exists and is not a directory."
                )
        else:
            print("Creating the directory {}.".format(self.save_folder))
            os.mkdir(self.save_folder)

        full_path = os.path.join(self.save_folder, filename)
        return full_path
