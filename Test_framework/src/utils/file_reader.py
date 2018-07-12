"""
文件读取。YamlReader读取yaml文件，ExcelReader读取excel。
"""
import yaml
import os
from xlrd import open_workbook
# from Test_framework.src.utils.config import CONFIG_FILE, DATA_PATH


class YamlReader:
    def __init__(self, yamlf):
        if os.path.exists(yamlf):
            self.yamlf = yamlf
        else:
            # 输入关键字raise，后跟要引发的异常的名称。异常名称标识出具体的类： Python异常处理是那些类的对象。
            raise FileNotFoundError('文件不存在！')
        self._data = None

    @property
    def data(self):
        # 如果是第一次调用data，读取yaml文档，否则直接返回之前保存的数据
        if not self._data:
            with open(self.yamlf, 'rb') as f:
                # 'r': 默认值，表示从文件读取数据。
                # 'w': 表示要向文件写入数据，并截断以前的内容
                # 'a': 表示要向文件写入数据，添加到当前内容尾部
                # 'r+': 表示对文件进行可读写操作（删除以前的所有数据）
                # 'r+a'：表示对文件可进行读写操作（添加到当前文件尾部）
                # 'b': 表示要读写二进制数据
                # 二进制文件就用二进制方法读取'rb'
                # 紧跟with后面的语句被求值后，返回对象的__enter__()
                # 方法被调用，这个方法的返回值将被赋值给as后面的变量。当with后面的代码块全部被执行完之后，将调用前面返回对象的__exit__()
                # 方法。
                self._data = list(yaml.safe_load_all(f))  # load后是个generator，用list组织成列表
        return self._data


class SheetTypeError(Exception):
    pass


class ExcelReader:
    """
    读取excel文件中的内容。返回list。

    如：
    excel中内容为：
    | A  | B  | C  |
    | A1 | B1 | C1 |
    | A2 | B2 | C2 |

    如果 print(ExcelReader(excel, title_line=True).data)，输出结果：
    [{A: A1, B: B1, C:C1}, {A:A2, B:B2, C:C2}]

    如果 print(ExcelReader(excel, title_line=False).data)，输出结果：
    [[A,B,C], [A1,B1,C1], [A2,B2,C2]]

    可以指定sheet，通过index或者name：
    ExcelReader(excel, sheet=2)
    ExcelReader(excel, sheet='BaiDuTest')
    """
    def __init__(self, excel, sheet=0, title_line=True):
        if os.path.exists(excel):
            self.excel = excel
        else:
            raise FileNotFoundError('文件不存在！')
        self.sheet = sheet
        self.title_line = title_line
        self._data = list()

    @property
    def data(self):
        if not self._data:
            workbook = open_workbook(self.excel)
            if type(self.sheet) not in [int, str]:
                raise SheetTypeError('Please pass in <type int> or <type str>, not {0}'.format(type(self.sheet)))
            elif type(self.sheet) == int:
                s = workbook.sheet_by_index(self.sheet)
            else:
                s = workbook.sheet_by_name(self.sheet)

            if self.title_line:
                title = s.row_values(0)  # 首行为title
                for col in range(1, s.nrows):
                    # 依次遍历其余行，与首行组成dict，拼到self._data中
                    self._data.append(dict(zip(title, s.row_values(col))))
            else:
                for col in range(0, s.nrows):
                    # 遍历所有行，拼到self._data中
                    self._data.append(s.row_values(col))
        return self._data


if __name__ == '__main__':
    CONFIG_FILE = os.path.split(os.path.dirname(os.path.dirname(__file__)))[0]
    print(CONFIG_FILE)
    y = os.path.join(CONFIG_FILE, 'config', 'config.yml')
    reader = YamlReader(y)
    print(reader.data)

    e = os.path.join(CONFIG_FILE, 'data', 'TestLogin.xlsx')
    print(e)
    reader = ExcelReader(e, title_line=True)
    print(reader.data)