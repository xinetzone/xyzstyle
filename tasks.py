"""任务配置文件

此模块配置项目文档构建任务，用于生成 Sphinx 文档。
"""

import inspect
from typing import Any

# 兼容性修复：确保 inspect 模块具有 getargspec 方法
if not hasattr(inspect, 'getargspec'):
    inspect.getargspec = inspect.getfullargspec  # type: ignore


# 导入文档构建工具
try:
    from taolib.flows.tasks import sites
except ImportError as e:
    raise ImportError("请确保已安装 taolib 包: pip install taolib") from e


# 配置文档构建任务
namespace: Any = sites(
    source='./doc',  # 文档源代码目录
    target='./doc/_build/html'  # 生成的 HTML 文档输出目录
)
