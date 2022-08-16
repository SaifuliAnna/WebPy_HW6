from file_parser import *
from normalize import normalize
from time import time
import asyncio
from aiopath import AsyncPath


async def goodbye(*args):
    print('Good bye!')


async def handle_media(filename: Path, target_folder: Path):
    filename = AsyncPath(filename)
    target_folder = AsyncPath(target_folder)
    await target_folder.mkdir(exist_ok=True, parents=True)
    await filename.replace(target_folder / (normalize(filename.name[:-len(filename.suffix)]) + filename.suffix))


async def handle_other(filename: Path, target_folder: Path):
    filename = AsyncPath(filename)
    target_folder = AsyncPath(target_folder)
    try:
        await target_folder.mkdir(exist_ok=True, parents=True)
        await filename.replace(target_folder / (normalize(filename.name[:-len(filename.suffix)]) + filename.suffix))
    except IsADirectoryError:
        return 'IsADirectoryError'
    except FileNotFoundError:
        return 'FileNotFoundError'
    except PermissionError:
        return 'PermissionError'


async def handle_archive(filename: Path, target_folder: Path):
    filename = AsyncPath(filename)
    target_folder = AsyncPath(target_folder)
    await target_folder.mkdir(exist_ok=True, parents=True)
    await filename.replace(target_folder / (normalize(filename.name[:-len(filename.suffix)]) + filename.suffix))


async def handle_programs(filename: Path, target_folder: Path):
    filename = AsyncPath(filename)
    target_folder = AsyncPath(target_folder)
    try:
        await target_folder.mkdir(exist_ok=True, parents=True)
        await filename.replace(target_folder / (normalize(filename.name[:-len(filename.suffix)]) + filename.suffix))
    except IsADirectoryError:
        return 'IsADirectoryError'
    except FileNotFoundError:
        return 'FileNotFoundError'
    except PermissionError:
        return 'PermissionError'


async def handle_folder(folder: Path):
    folder = AsyncPath(folder)
    try:
        await folder.rmdir()
    except OSError:
        print(f"Folder deletion failed {folder}")


async def start(*args):
    await asyncio.gather(file_parser(*args))


async def file_parser(*args):
    star = '*' * 60
    try:
        folder_for_scan = Path(args[0])
        scan(folder_for_scan.resolve())
    except FileNotFoundError:
        return f"Not able to find '{args[0]}' folder. Please enter a correct folder name."
    except IndexError:
        return "Please enter a folder name."
    except IsADirectoryError:
        return 'Unknown file'
    for file in JPEG_IMAGES:
        await handle_media(file, Path(args[0] + '/' + 'images' + '/' + 'JPEG'))
    for file in JPG_IMAGES:
        await handle_media(file, Path(args[0] + '/' + 'images' + '/' + 'JPG'))
    for file in PNG_IMAGES:
        await handle_media(file, Path(args[0] + '/' + 'images' + '/' + 'PNG'))
    for file in SVG_IMAGES:
        await handle_media(file, Path(args[0] + '/' + 'images' + '/' + 'SVG'))
    for file in GIF_IMAGES:
        await handle_media(file, Path(args[0] + '/' + 'images' + '/' + 'GIF'))
    for file in MP3_AUDIO:
        await handle_media(file, Path(args[0] + '/' + 'audio' + '/' + 'MP3'))
    for file in OGG_AUDIO:
        await handle_media(file, Path(args[0] + '/' + 'audio' + '/' + 'OGG'))
    for file in WAV_AUDIO:
        await handle_media(file, Path(args[0] + '/' + 'audio' + '/' + 'WAV'))
    for file in AMR_AUDIO:
        await handle_media(file, Path(args[0] + '/' + 'audio' + '/' + 'AMR'))
    for file in AVI_VIDEO:
        await handle_media(file, Path(args[0] + '/' + 'video' + '/' + 'AVI'))
    for file in MP4_VIDEO:
        await handle_media(file, Path(args[0] + '/' + 'video' + '/' + 'MP4'))
    for file in MOV_VIDEO:
        await handle_media(file, Path(args[0] + '/' + 'video' + '/' + 'MOV'))
    for file in MKV_VIDEO:
        await handle_media(file, Path(args[0] + '/' + 'video' + '/' + 'MKV'))
    for file in DOC_DOCUMENT:
        await handle_media(file, Path(args[0] + '/' + 'documents' + '/' + 'DOC'))
    for file in DOCX_DOCUMENT:
        await handle_media(file, Path(args[0] + '/' + 'documents' + '/' + 'DOCX'))
    for file in TXT_DOCUMENT:
        await handle_media(file, Path(args[0] + '/' + 'documents' + '/' + 'TXT'))
    for file in PDF_DOCUMENT:
        await handle_media(file, Path(args[0] + '/' + 'documents' + '/' + 'PDF'))
    for file in XLSX_DOCUMENT:
        await handle_media(file, Path(args[0] + '/' + 'documents' + '/' + 'XLSX'))
    for file in XLS_DOCUMENT:
        await handle_media(file, Path(args[0] + '/' + 'documents' + '/' + 'XLS'))
    for file in CSV_DOCUMENT:
        await handle_media(file, Path(args[0] + '/' + 'documents' + '/' + 'CSV'))
    for file in PPTX_DOCUMENT:
        await handle_media(file, Path(args[0] + '/' + 'documents' + '/' + 'PPTX'))
    for file in OTHER:
        await handle_other(file, Path(args[0] + '/' + 'OTHER'))
    for file in OTHER:
        await handle_programs(file, Path(args[0] + '/' + 'programs' + '/' + 'APP'))
    for file in ZIP_ARCHIVES:
        await handle_archive(file, Path(args[0] + '/' + 'archives' + '/' + 'ZIP'))
    for file in GZ_ARCHIVES:
        await handle_archive(file, Path(args[0] + '/' + 'archives' + '/' + 'GZ'))
    for file in TAR_ARCHIVES:
        await handle_archive(file, Path(args[0] + '/' + 'archives' + '/' + 'TAR'))
    for file in RAR_ARCHIVES:
        await handle_archive(file, Path(args[0] + '/' + 'archives' + '/' + 'RAR'))
    for file in ARJ_ARCHIVES:
        await handle_archive(file, Path(args[0] + '/' + 'archives' + '/' + 'ARJ'))
    for folder in FOLDERS[::-1]:
        await handle_folder(folder)

    print(f'{star}''\n'f"Files in {args[0]} sorted successfully"'\n'f'{star}')


COMMANDS = {start: ['clean', 'clear'], goodbye: ['good bye', 'close', 'exit', '.']}


def unknown_command(*args):
    return 'Unknown command! Enter again!'


def command_parser(user_command: str, COMMANDS: dict) -> (str, list):
    for key, list_value in COMMANDS.items():
        for value in list_value:
            if user_command.lower().startswith(value):
                args = user_command[len(value):].split()
                return key, args
    else:
        return unknown_command, []


async def main():
    while True:
        print('Print clean and address your folder',
              'for MacOS: clean /Folder/Trash',
              'for Windows: clean C:\Folder\Trash', sep='\n')
        user_command = input('Enter you command >>> ')
        command, data = command_parser(user_command, COMMANDS)
        print(await command(*data))
        print('Do you have some folder for clean?')
        var = input('Press: y/n >>> ')
        if var == 'y':
            print('*' * 60)
            continue
        elif var == 'n':
            break
        elif command is goodbye:
            break


if __name__ == '__main__':
    timer_2 = time()
    asyncio.run(main())
    print(f'{round( time() - timer_2, 4)}')