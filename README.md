# xyzstyle

[![PyPI][pypi-badge]][pypi-link]
[![GitHub issues][issue-badge]][issue-link]
[![GitHub forks][fork-badge]][fork-link]
[![GitHub stars][star-badge]][star-link]
[![GitHub license][license-badge]][license-link]
[![contributors][contributor-badge]][contributor-link]
[![watcher][watcher-badge]][watcher-link]
[![Binder][binder-badge]][binder-link]
[![Downloads][download-badge]][download-link]
[![Documentation Status][status-badge]][status-link]
[![PyPI - Downloads][install-badge]][install-link]
![repo size](https://img.shields.io/github/repo-size/xinetzone/xyzstyle.svg)
[![Downloads Week](https://pepy.tech/badge/xyzstyle/week)](https://pepy.tech/project/xyzstyle)

[pypi-badge]: https://img.shields.io/pypi/v/xyzstyle.svg
[pypi-link]: https://pypi.org/project/xyzstyle/
[issue-badge]: https://img.shields.io/github/issues/xinetzone/xyzstyle
[issue-link]: https://github.com/xinetzone/xyzstyle/issues
[fork-badge]: https://img.shields.io/github/forks/xinetzone/xyzstyle
[fork-link]: https://github.com/xinetzone/xyzstyle/network
[star-badge]: https://img.shields.io/github/stars/xinetzone/xyzstyle
[star-link]: https://github.com/xinetzone/xyzstyle/stargazers
[license-badge]: https://img.shields.io/github/license/xinetzone/xyzstyle
[license-link]: https://github.com/xinetzone/xyzstyle/LICENSE
[contributor-badge]: https://img.shields.io/github/contributors/xinetzone/xyzstyle
[contributor-link]: https://github.com/xinetzone/xyzstyle/contributors
[watcher-badge]: https://img.shields.io/github/watchers/xinetzone/xyzstyle
[watcher-link]: https://github.com/xinetzone/xyzstyle/watchers
[binder-badge]: https://mybinder.org/badge_logo.svg
[binder-link]: https://mybinder.org/v2/gh/xinetzone/xyzstyle/main
[install-badge]: https://img.shields.io/pypi/dw/xyzstyle?label=pypi%20installs
[install-link]: https://pypistats.org/packages/xyzstyle
[status-badge]: https://readthedocs.org/projects/xyzstyle/badge/?version=latest
[status-link]: https://xyzstyle.readthedocs.io/zh-cn/latest/?badge=latest
[download-badge]: https://pepy.tech/badge/xyzstyle
[download-link]: https://pepy.tech/project/xyzstyle

`xyzstyle` 是一款精心设计的基于 [Sphinx](https://www.sphinx-doc.org/) 的文档主题，旨在提供美观、专业且易于使用的文档展示解决方案。该主题基于 `sphinx-book-theme` 进行定制，注重用户体验和视觉设计，同时保持了良好的可访问性和可定制性。

## 主题特点

- **现代化界面设计**：简洁清晰的布局，专业的配色方案
- **完善的响应式支持**：适配各种设备屏幕尺寸
- **丰富的内容展示**：支持Markdown、Jupyter笔记本等多种内容格式
- **国际化支持**：内置多语言翻译机制
- **易于定制**：提供多种配置选项满足不同需求

## 安装并激活主题

### 安装步骤

使用 Python 的包管理工具 `pip` 安装 `xyzstyle`：

```shell
pip install xyzstyle
```

如需安装特定版本，可以使用：

```shell
pip install xyzstyle==版本号
```

#### 开发模式安装（可编辑模式）

如果您需要对主题进行开发或修改，可以使用可编辑模式安装：

```shell
# 首先进入项目根目录
cd xyzstyle项目路径
# 然后以可编辑模式安装
pip install -ve .
```

其中参数含义：
- `-v` 表示详细输出
- `-e` 表示可编辑模式（开发模式）
- `.` 表示当前目录

这种安装方式会在安装包时创建一个指向源代码的链接，使您对源码的修改能够立即反映到已安装的包中，无需重新安装。

### 激活主题

安装完成后，需要在您的 Sphinx 项目配置文件（通常为 `conf.py` ）中进行设置以激活主题：

```python
# == 项目基本信息 ========================================================================
project = 'xyzstyle' # 项目名称
copyright = '2022, xinetzone' # 版权信息
author = 'xinetzone' # 作者信息

# == 主题设置 ============================================================================
html_theme = "xyzstyle" # 使用的HTML主题
# 静态资源配置
html_static_path = ['_static']  # 指定静态文件目录，用于存放CSS、JavaScript、图片等
html_logo = "_static/images/logo.jpg"  # 网站Logo路径，显示在页面顶部
html_favicon = "_static/images/favicon.jpg"  # 网站图标路径，显示在浏览器标签页
html_last_updated_fmt = '%Y-%m-%d, %H:%M:%S'  # 最后更新时间格式

# == 国际化与本地化设置 ==================================================================
language = 'zh_CN' # 文档语言（中文简体）
locale_dirs = ['../locales/'] # 翻译文件存放目录
gettext_compact = False # 是否合并子目录的PO文件（False表示不合并）

# == 扩展插件配置 ========================================================================
extensions = [
    "myst_nb",  # Markdown和Jupyter笔记本支持
] # 启用的Sphinx扩展
```

通过设置 `html_theme = "xyzstyle"` 即可在您的项目中激活 `xyzstyle` 主题，使生成的文档采用该主题的样式和布局。

### 其他选项

```python
# 主题选项配置
html_theme_options = {
    "use_sidenotes": True,        # 启用侧边注释/页边注释
    "repository_url": "https://github.com/yourusername/yourproject",  # 仓库地址
    "use_repository_button": True,  # 显示"在 GitHub 上查看"按钮
    "announcement": "欢迎使用 xyzstyle 主题！",  # 公告横幅
    "use_source_button": True,      # 显示"查看源代码"按钮
    "use_edit_page_button": True,   # 显示"编辑此页"按钮
    "use_issues_button": True,      # 显示"报告问题"按钮
    "path_to_docs": "doc",          # 文档目录路径
}
# 可选插件
extensions.extend([
    "sphinx_design",                # 增强设计元素
    "sphinx.ext.viewcode",          # 添加到高亮源代码的链接
    "sphinx.ext.intersphinx",       # 链接到其他文档
    "sphinx_copybutton",            # 为代码块添加复制按钮
    "sphinx_comments",              # 添加评论和注释功能
])
# =============================================================================
# 可选功能配置
# =============================================================================
# 1. 代码复制按钮配置
copybutton_exclude = '.linenos, .gp'  # 排除行号和提示符
# 选择器配置，避免复制按钮出现在笔记本单元格编号上
copybutton_selector = ":not(.prompt) > div.highlight pre"

# 2. 评论系统配置
comments_config = {
   "hypothesis": True,  # 启用 Hypothesis 注释
   "utterances": {
      "repo": "xinetzone/xyzstyle",
      "optional": "config",
   }  # 启用 Utterances 评论
}
```

### 下一步

配置完成后，您可以使用标准的 Sphinx 命令生成文档：

```shell
# 基本文档生成命令
sphinx-build -b html 源目录 输出目录

# 例如
sphinx-build -b html doc/source doc/build/html
```

生成的文档将使用 `xyzstyle` 主题的样式呈现，为您的项目提供专业、美观的文档界面。

## 项目目录结构

```
xyzstyle/
├── src/                  # 源代码目录
│   └── xyzstyle/         # 主题源码
│       ├── __init__.py   # 主题初始化文件
│       └── theme/        # 主题模板和样式
│           └── xyzstyle/ # 主题文件
├── doc/                  # 文档目录
│   ├── conf.py           # Sphinx配置文件
│   └── ...               # 其他文档源文件
├── pyproject.toml        # 项目配置和依赖
├── LICENSE               # 许可证文件
└── README.md             # 项目说明文档
```

## 开发指南

### 安装开发依赖

```shell
# 安装开发依赖
pip install -e "[dev]"

# 或安装文档构建依赖
pip install -e "[doc]"
```

### 构建文档

```shell
# 进入文档目录
cd doc

# 构建文档
sphinx-build -b html . _build/html
```
