"""
封装数据操作的公共方法

"""
import pandas
import os


class OperationFile:
    def __init__(self, filename: str):
        """
        os.path.dirname 表示当前目录
        os.path.abspath(__file__) 表示绝对路径
        os.path.dirname(os.path.dirname) 表示上级目录
        :param filename:  文件名
        """
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\\data"
        self.filepath = os.path.join(base_path, filename)  # 文件路径
        # 判断
        if filename.split(".")[-1] == "csv":
            self.file = pandas.read_csv(self.filepath)  # 读取格式为csv
        else:
            self.file = pandas.read_excel(self.filepath)  # 读取格式为excel

    def get_data_to_dict(self):
        """读取文件为列表嵌套字典"""
        return [self.file.loc[i].to_dict() for i in self.file.index.values]

    def get_data_to_list(self):
        """读取文件为列表嵌套列表格式"""
        return self.file.values.tolist()

    def write_data_to_excel(self, data: list):
        """
        更新表格
        将注册的新数据写入表格
        :param data:
        :return:
        """
        # 读取源数据
        old_data = self.get_data_to_list()
        # 添加新数据在第一行
        self.file.loc[0] = data  # 指定插入行行号
        # 将老数据追在在第一行 之 后
        for i in range(1, len(old_data) + 1):
            self.file.loc[i] = old_data[i - 1]
        self.file.to_excel(self.filepath, index=None)


if __name__ == '__main__':
    filename = "register.xls"
    o = OperationFile(filename)
    data = ["admin", "admin@qq.com", "123456", '', '', '', '', '']
    o.write_data_to_excel(data)
