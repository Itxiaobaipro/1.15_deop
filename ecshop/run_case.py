import unittest
import HTMLTestRunnerPlugins
import time
import os

# 确定存放测试用例的文件夹路径
current_dir = os.path.dirname(os.path.realpath(__file__))
print(current_dir)
# 添加测试用例路径
case_dir = os.path.join(current_dir, "script")
print(case_dir)
# 添加测试报告存放路径
report_dir = os.path.join(current_dir, "report")
print(report_dir)

# 将测试用例添加到测试套件中
discover = unittest.defaultTestLoader.discover(case_dir, pattern="test*.py")
# 命名测试报告名称
# 以时间格式命名报告
now = time.strftime("%Y-%m-%d %H-%M-%S")
report_file_name = report_dir + "\\" + now + "report.html"
with open(report_file_name, "wb") as fp:
    runner = HTMLTestRunnerPlugins.HTMLTestRunner(
        title="自动化测试报告",
        description="报告描述",
        stream=fp)
    runner.run(discover)


if __name__ == '__main__':
    unittest.main()
