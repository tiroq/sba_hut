from pathlib import Path
from docxtpl import DocxTemplate


class DocxTemplater:
    def __init__(self, path):
        self.sub_path = path
        self._file = Path(path)
        if not self._file.exists():
            raise FileNotFoundError
        self.doc = DocxTemplate(self._file.as_posix())
        self.doc.render_init()

    @property
    def undeclared_variables(self):
        return self.doc.get_undeclared_template_variables()

    @property
    def path(self):
        return str(self._file.absolute())

    @property
    def absolute(self):
        return self._file.absolute()

    @property
    def cwd(self):
        return self._file.cwd()
