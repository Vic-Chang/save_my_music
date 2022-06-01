import os
import shutil
import eyed3
from pathlib import Path


def get_all_files_path(music_folder_path: str) -> list:
    file_path_list = []
    for root, dir_names, file_names in os.walk(music_folder_path):
        for file_name in file_names:
            file_path_list.append(os.path.join(root, file_name))
    return file_path_list


if __name__ == '__main__':
    all_files_path_list = get_all_files_path('F:\iPod_Control\Music')
    local_files_path_list = get_all_files_path('D:\Music')

    print('All files count: ', len(all_files_path_list))
    print('Local files count: ', len(local_files_path_list))
    leak_mp3 = []
    for item in all_files_path_list:
        try:
            file_size = Path(item).stat().st_size
            local_file_size = Path(item.replace('F:\iPod_Control', 'D:\Music')).stat().st_size
            if file_size != local_file_size:
                leak_mp3.append(item.replace('F:\iPod_Control', 'D:\Music'))
        except:
            leak_mp3.append(item)

    print('缺少數量: ', len(leak_mp3))
    for item in leak_mp3:
        print(item)
        try:
            audiofile = eyed3.load(item)
            print(f'{audiofile.tag.artist} - {audiofile.tag.title}')
        except Exception as e:
            print(e)
        finally:
            print('___________')

    counter = 0
    final_music_path = r'C:\music'
    for item in local_files_path_list:
        if item not in leak_mp3:
            file_name_with = Path(item).stem
            # 該檔名重複
            if 'VTKU' in file_name_with:
                file_name_with = file_name_with + str(counter)
            file_name_with_extension = file_name_with + '.mp3'
            shutil.copy2(item, os.path.join(final_music_path, file_name_with_extension))
            counter += 1
