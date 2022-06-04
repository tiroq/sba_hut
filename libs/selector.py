# -*- coding: utf-8 -*-
from pathlib import Path
from typing import List, Tuple

import yaml


class TemplateSelector:
    def __init__(self):
        self.path = Path('./')
        self.templates_folder_name = 'templates'
        self.__init_templates_folder()

    def __init_templates_folder(self, raise_not_exists=False):
        self.templates_folder = Path(self.templates_folder_name)
        if not self.templates_folder.exists():
            if raise_not_exists:
                raise FileNotFoundError
            with open('.settings.yaml', encoding="utf8") as settings_file:
                local_env = yaml.safe_load(settings_file).get('env', 'ru')
            with open('.mapping.yaml', encoding="utf8") as mapping_file:
                self.templates_folder_name = yaml.safe_load(mapping_file).get(local_env, {}).get('templates', 'Шаблоны')
            self.__init_templates_folder(raise_not_exists=True)

    def __iter_path(self, path: Path) -> Tuple[List[Path], List[Path]]:
        return [_path for _path in path.iterdir() if _path.is_dir()], \
               [_path for _path in path.iterdir() if _path.is_file()]

    def select_template(self, target_path: Path = None):
        target_path = self.templates_folder if target_path is None else target_path
        folders, files = self.__iter_path(target_path)
        paths = folders + files
        for i, path in enumerate(paths):
            print(f" {i:3}: {'d' if path.is_dir() else 'f'} - {str(path)}")
        try:
            selected_path = int(input(f"Select path[0-{len(paths)-1}]: "))
        except ValueError:
            return self.select_template(target_path)
        if 0 <= selected_path <= len(paths) - 1:
            if paths[selected_path].is_file():
                return paths[selected_path]
            else:
                return self.select_template(paths[selected_path])
        else:
            return self.select_template(target_path)

    @property
    def cwd(self):
        return self.path.cwd()
