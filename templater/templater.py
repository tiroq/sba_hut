from pathlib import Path
from docxtpl import DocxTemplate


class DocxTemplater:
    def __init__(self, path):
        self._file = Path(path)
        self.path = self._file.resolve()
        if not self._file.exists():
            raise FileNotFoundError
        self.doc = DocxTemplate(self._file.as_posix())
        self.doc.render_init()

    @property
    def undeclared_variables(self):
        return self.doc.get_undeclared_template_variables()


if __name__ == '__main__':
    doc = DocxTemplater('../Шаблоны/Договоры/Трудовой_договор.docx')
    print(doc.undeclared_variables)
    print(doc.path)
