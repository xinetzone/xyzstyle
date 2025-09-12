# xyzstyle

[![PyPI][pypi-badge]][pypi-link]
[![GitHub issues][issue-badge]][issue-link]
[![GitHub forks][fork-badge]][fork-link]
[![GitHub stars][star-badge]][star-link]
[![GitHub license][license-badge]][license-link]
[![Documentation Status][status-badge]][status-link]
[![Downloads][download-badge]][download-link]

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
[status-badge]: https://readthedocs.org/projects/xyzstyle/badge/?version=latest
[status-link]: https://xyzstyle.readthedocs.io/zh-cn/latest/?badge=latest
[download-badge]: https://pepy.tech/badge/xyzstyle
[download-link]: https://pepy.tech/project/xyzstyle

`xyzstyle` 是一款精心设计的基于 [Sphinx](https://www.sphinx-doc.org/) 的文档主题，基于 `sphinx-book-theme` 进行定制，提供美观、专业且易于使用的文档展示解决方案。该主题注重用户体验和视觉设计，同时保持了良好的可访问性和可定制性。

## 主题特点

- **现代化界面设计**：简洁清晰的布局，专业的配色方案
- **完善的响应式支持**：适配各种设备屏幕尺寸
- **基于 sphinx-book-theme**：在其基础上进行定制和增强
- **支持多格式内容**：支持Markdown、Jupyter笔记本等内容格式
- **易于定制**：提供多种配置选项满足不同需求
- **TOML配置支持**：通过doc.toml文件简化配置过程

## 项目依赖

- **核心依赖**：
  - sphinx-book-theme>=0.4.0
- **Python版本**：>=3.12

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
pip install -e .
```

这种安装方式会在安装包时创建一个指向源代码的链接，使您对源码的修改能够立即反映到已安装的包中，无需重新安装。

### 激活主题

安装完成后，需要在您的 Sphinx 项目配置文件（通常为 `conf.py` ）中进行设置以激活主题：

```python
# 启用 xyzstyle 扩展
extensions = ["xyzstyle"]

# 使用 xyzstyle 主题
html_theme = "xyzstyle"
```

### 使用 TOML 配置文件

`xyzstyle` 支持通过 `doc.toml` 文件进行配置，简化传统的 `conf.py` 配置过程。在您的文档目录中创建一个 `doc.toml` 文件：

```toml
[project]
name = "项目名称"
description = "项目描述"
author = "作者名称"
version = "0.1.0"

[html]
theme = "xyzstyle"
static_path = ["_static"]
```

通过这种方式，`xyzstyle` 会自动加载 `doc.toml` 中的配置并应用到 Sphinx 构建过程中。

## 主题配置选项

`xyzstyle` 主题提供了丰富的配置选项，可以在 `doc.toml` 文件中进行设置：

```toml
[html.theme_options]
use_sidenotes = true        # 启用侧边注释/页边注释
repository_url = "https://github.com/yourusername/yourproject"  # 仓库地址
use_repository_button = true  # 显示"在 GitHub 上查看"按钮
announcement = "欢迎使用 xyzstyle 主题！"  # 公告横幅
use_source_button = true      # 显示"查看源代码"按钮
use_edit_page_button = false  # 显示"编辑此页"按钮
use_issues_button = false     # 显示"报告问题"按钮
path_to_docs = "doc"          # 文档目录路径
secondary_sidebar_items = "page-toc.html" # 次要侧边栏项目
toc_title = "目录"             # 目录标题
use_download_button = true    # 使用下载按钮
use_fullscreen_button = true  # 使用全屏按钮
repository_branch = "main"    # 仓库分支
footer_content_items = "author.html, copyright.html, last-updated.html, extra-footer.html" # 页脚内容
```

## 项目目录结构

```
xyzstyle/
├── src/                  # 源代码目录
│   └── xyzstyle/         # 主题源码
│       ├── __init__.py   # 主题初始化文件
│       ├── config_loader.py  # 配置加载模块
│       └── theme/        # 主题模板和样式
│           └── xyzstyle/ # 主题文件
│               ├── layout.html    # 主布局模板
│               ├── theme.toml     # 主题配置
│               └── static/        # 静态资源
│                   ├── css/       # CSS样式
│                   ├── js/        # JavaScript
│                   └── styles/    # 自定义样式
├── doc/                  # 文档目录
│   ├── conf.py           # Sphinx配置文件
│   ├── doc.toml          # TOML配置文件
│   ├── _static/          # 静态资源目录
│   └── _build/           # 构建输出目录
├── pyproject.toml        # 项目配置和依赖
├── LICENSE               # 许可证文件
└── README.md             # 项目说明文档
```

## 开发指南

### 安装开发依赖

项目使用 PDM 作为构建后端，您可以安装开发依赖进行主题开发：

```shell
# 安装开发依赖
pip install -e "[dev]"

# 安装文档构建依赖
pip install -e "[doc]"
```

### 构建文档

要构建文档进行测试，您可以使用以下命令：

```shell
# 进入文档目录
cd doc

# 构建文档
sphinx-build -b html . _build/html
```

### 主题定制

如果您想要进一步定制主题，可以修改 `src/xyzstyle/theme/xyzstyle/` 目录下的文件：
- `theme.toml`：主题的基本配置
- `layout.html`：HTML布局模板
- `static/css/` 和 `static/styles/`：自定义样式文件

## 已知功能

当前版本的 `xyzstyle` 主题支持以下功能：

- 自动加载和应用 `doc.toml` 中的配置
- 基于 sphinx-book-theme 的现代化界面
- 响应式设计，适配不同设备
- 侧边注释功能
- 丰富的主题选项配置
- 自定义静态资源支持

## 许可证

该项目采用 Apache License 2.0 - 详见 [LICENSE](LICENSE) 文件

## 贡献指南

请阅读 [CONTRIBUTING.md](CONTRIBUTING.md) 文件了解如何参与项目开发。

## 版本历史

请查看 [CHANGELOG.md](CHANGELOG.md) 文件了解项目的版本变更历史。
