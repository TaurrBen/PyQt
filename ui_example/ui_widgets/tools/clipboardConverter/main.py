# – coding:UTF-8 –
import re
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

# class clipboardConverter(QMainWindow):
#
#     def __init__(self, parent=None):
#         super(clipboardConverter, self).__init__(parent)
#         self.clipboard = QApplication.clipboard()
#         match = self.getOracleDate()
#         if not match:
#             QMessageBox.warning(self, "提示", "未匹配到转换内容，转换失败！")
#
#     def getOracleDate(self):
#         # oracle日期转换 to_date
#         clipboard_text = self.clipboard.text()
#         if clipboard_text is not None:
#             oracle_date_pattern = ".*\d\d\d\d-\d+-\d+ \d+:\d+:\d+.\d+.*"
#             results = re.findall(oracle_date_pattern, clipboard_text)
#             if len(results) > 0:
#                 result = results[0]
#                 if "'" in result:
#                     result = result.replace(re.findall("\.\d", result)[0], "")
#                     self.clipboard.setText(f"to_date({result} , 'yyyy-mm-dd hh24:mi:ss')")
#                 else:
#                     result = result.replace(re.findall("\.\d", result)[0], "")
#                     self.clipboard.setText(f"to_date('{result}' , 'yyyy-mm-dd hh24:mi:ss')")
#                 QMessageBox.information(self, "提示", "转换oracle日期格式成功！")
#                 return True
#             else:
#                 return False
#         else:
#             QMessageBox.warning(self, "提示", "剪贴板内容为空，转换失败！")
#             return True

class clipboardConverter(QMainWindow):

    def __init__(self, parent=None):
        super(clipboardConverter, self).__init__(parent)
        self.clipboard = QApplication.clipboard()
        self.defaultSourceCode = """
def getOracleDate(clipboard_text):
    import re
    # oracle日期转换 to_date
    if clipboard_text is not None:
        oracle_date_pattern = ".*('\d\d\d\d-\d+-\d+ \d+:\d+:\d+.\d').*"
        replace_date_pattern = "('\d\d\d\d-\d+-\d+ \d+:\d+:\d+).\d+'"
        results = re.findall(oracle_date_pattern, clipboard_text)
        if len(results) > 0:
            for result in results:
                print(result)
                replace_date_results = re.findall(replace_date_pattern, result)
                if len(replace_date_results) > 0:
                    print(replace_date_results[0])
                    clipboard_text = clipboard_text.replace(result, f"to_date({replace_date_results[0]}' , 'yyyy-mm-dd hh24:mi:ss')")
            return clipboard_text, "转换oracle日期格式成功！"
    return None, ""
"""
        if not os.path.exists("SourceCode.conf"):
            with open("SourceCode.conf", "w") as f:
                f.write(self.defaultSourceCode)
        with open("SourceCode.conf", "r") as f:
            self.sourceCode = f.read()
        match, info = self.convert()
        if match:
            QMessageBox.information(self, "提示", info)
        else:
            QMessageBox.warning(self, "提示", "未匹配到转换内容，转换失败！")

    def convert(self):
        clipboard_text = self.clipboard.text()
        converters = {}
        try:
            exec(self.sourceCode, {
                'clipboard_text': clipboard_text
            }, converters)
        except Exception as e:
            with open("error.log", "w") as f:
                f.write(str(e))
            QMessageBox.critical(self, "错误", "转换时发生错误，错误详情请查看error.log日志！")
        for name, converter in converters.items():
            result, info = converter(clipboard_text)
            if result is not None:
                self.clipboard.setText(result)
                return True, info
            else:
                continue
        return False, None

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = clipboardConverter()
