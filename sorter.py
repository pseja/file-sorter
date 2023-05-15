from os import mkdir, rmdir, listdir
from os.path import isfile, isdir, splitext
from shutil import move

FILE_EXTENSIONS = {
    "HTML": [".html5", ".html", ".htm", ".xhtml"],
    "IMAGES": [".jpeg", ".jpg", ".jpe", ".jif", ".jfif", ".jfi", ".tiff", ".tif", ".gif", ".bmp", ".png", ".bpg", ".svg", ".heif", ".psd", ".ico", ".svgz", ".webp"],
    "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng", ".qt", ".mpg", ".mpeg", ".3gp", ".3g2"],
    "DOCUMENTS": [".pdf", ".oxps", ".pages", ".docx", ".doc", ".fdf", ".ods", ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox", ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".csv"],
    "ARCHIVES": [".a", ".ar", ".cpio", ".tar", ".gz", ".rz", ".7z", ".rar", ".xar", ".zip", ".bz2", ".xz"],
    "AUDIO": [".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3", ".msv", ".ogg", ".oga", ".raw", ".vox", ".wav", ".wma", ".flac", ".alac"],
    "PLAINTEXT": [".txt", ".cfg", ".conf", ".ini"],
    "EXECUTABLES": [".exe", ".bat", ".cmd", ".jar", ".msc", ".app"],
    "DATA": [".csv", ".json", ".log", ".dat", ".db", ".dump"],
    "SCRIPTS": [".vue", ".php", ".rb", ".pl", ".cgi", ".py", ".sh", ".bash", ".xml"],
    "PRESENTATIONS": [".ppt", ".pptx", ".odp", ".key"],
    "SPREADSHEETS": [".xlsm", ".numbers", ".ods", ".xlr"],
    "DATABASE": [".sql", ".mdb", ".accdb", ".dbf", ".sqlitedb", ".sqlite"],
    "EBOOKS": [".mobi", ".azw", ".azw3", ".epub", ".ibooks", ".pdb", ".fb2"],
    "FONTS": [".ttf", ".otf", ".fon", ".fnt", ".woff", ".woff2"],
    "INSTALLERS": [".msi", ".pkg", ".deb", ".rpm", ".dmg"],
    "SOURCE_CODE": [".c", ".cpp", ".java", ".scala", ".go", ".js", ".ts", ".jsx", ".tsx", ".scss", ".less"],
    "BACKUPS": [".backup"],
    "VIRTUAL_MACHINES": [".ova", ".ovf", ".vdi", ".vmdk"],
    "SYSTEM_FILES": [".dll", ".sys", ".drv", ".inf"],
    "GAME_FILES": [".sav", ".gam", ".rom"],
    "CONFIG_BACKUPS": [".cfg.bak", ".conf.bak", ".ini.bak"],
    "LOG_FILES": [".log"],
    "DISK_IMAGES": [".iso", ".img"],
    "VIRTUAL_ENVIRONMENTS": [".venv"],
    "SETTINGS_FILES": [".settings"],
    "SYSTEM_CONFIGURATION": [".plist", ".yaml", ".yml"],
    "MAIL_FILES": [".eml", ".msg", ".pst", ".ost", ".mbox"],
    "VIRTUAL_REALITY": [".vr"]
}


def make_folders():
    for folder in FILE_EXTENSIONS.keys():
        try:
            mkdir(folder)
        except:
            print(f"{folder} already exists")
            pass

    mkdir("OTHER")


def get_extension_and_move_files():
    for file in listdir():
        if isfile(file):
            file_extension = splitext(file)[1]

            for folder, extensions in FILE_EXTENSIONS.items():
                if file_extension in extensions:
                    try:
                        move(f"{file}", f"./{folder}")
                    except:
                        print(f"Error moving {file}")
                        pass
                else:
                    try:
                        move(f"{file}", f"./OTHER")
                    except:
                        print(f"Error moving {file}")
                        pass


def delete_empty_folders():
    for object in listdir():
        if isdir(object):
            try:
                rmdir(object)
            except:
                pass


def main():
    make_folders()
    get_extension_and_move_files()
    delete_empty_folders()


if __name__ == "__main__":
    main()