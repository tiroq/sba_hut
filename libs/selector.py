from pathlib import Path

import yaml


class TemplateSelector:
    def __init__(self):
        self.path = Path('./')
        self.templates_folder_name = 'templates'
        self.__init_templates_folder()

    def __init_templates_folder(self, raise_not_exists=False):
        self.tmpts_folder = Path(self.templates_folder_name)
        if not self.tmpts_folder.exists():
            if raise_not_exists:
                raise FileNotFoundError
            local_env = yaml.safe_load('.settings.yaml').get('env', 'ru')
            self.templates_folder_name = yaml.safe_load('.mapping.yaml').get(local_env, {}).get('templates', 'Шаблоны')
            self.__init_templates_folder(raise_not_exists=True)


    @property
    def cwd(self):
        return self.path.cwd()
