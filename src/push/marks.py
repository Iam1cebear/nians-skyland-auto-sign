# 推送用的固定标记。单独放一个文件，避免 push/__init__.py 和各个推送模块互相 import 造成循环。
FAILURE_MARK = '__WORKFLOW_FAILED__'
