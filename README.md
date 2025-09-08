# xyzstyle

<div align="center">
  <img src="https://raw.githubusercontent.com/xinetzone/xyzstyle/main/doc/_static/images/logo.jpg" alt="xyzstyle Logo" width="200"/>
</div>

[![PyPI][pypi-badge]][pypi-link]
[![GitHub issues][issue-badge]][issue-link]
[![GitHub forks][fork-badge]][fork-link]
[![GitHub stars][star-badge]][star-link]
[![GitHub license][license-badge]][license-link]
[![contributors][contributor-badge]][contributor-link]
[![Documentation Status][status-badge]][status-link]
[![Downloads][download-badge]][download-link]
[![PyPI - Downloads][install-badge]][install-link]

**xyzstyle** 是一个基于 Sphinx Book Theme 的现代化、可定制的 Sphinx HTML 主题，为技术文档提供优雅美观的展示效果。它结合了现代Web设计理念与优秀的阅读体验，使您的文档既专业又易于阅读。

> 💡 **提示**：您可以在 `doc/_static/images/` 目录下添加 `theme-preview.png` 文件，以在 README 中展示主题预览图。

## 功能特点

- **基于流行的 Sphinx Book Theme 构建**：继承其强大功能并添加自定义扩展
- **简洁优雅的文档布局**：专注于内容的清晰展示，减少视觉干扰
- **高度可定制**：支持丰富的配置选项，可以根据项目需求灵活调整
- **响应式设计**：完美适配桌面端、平板和移动设备，提供一致的阅读体验
- **增强的文档功能**：支持侧边注释、代码块复制、社交链接等多种扩展
- **多语言支持**：内置国际化框架，轻松创建多语言文档
- **API文档自动生成**：集成 autoapi 扩展，自动从源代码生成API文档
- **交互式代码演示**：支持 Thebe 实时代码执行，提升学习体验

## 适用场景

- 技术文档网站
- 项目API文档
- 教程和指南
- 学术论文和报告
- 知识库和帮助中心

## 快速入门

### 安装

安装 xyzstyle 包：

```shell
pip install xyzstyle
```

### 创建示例项目

快速创建一个使用 xyzstyle 主题的 Sphinx 项目：

```shell
# 创建一个新目录
mkdir my-docs && cd my-docs

# 初始化 Sphinx 项目
sphinx-quickstart

# 安装 xyzstyle
pip install xyzstyle

# 修改 conf.py 使用 xyzstyle 主题
sed -i "s/html_theme = .*/html_theme = 'xyzstyle'/" source/conf.py

# 构建文档
make html
```

### 查看效果

构建完成后，可以在浏览器中打开生成的文档：

```shell
# Linux/macOS
open build/html/index.html

# Windows
start build/html/index.html
```

## 安装指南

### 基本安装

需要安装 `xyzstyle` 包：

```shell
pip install xyzstyle
```

### 文档开发安装

如果需要参与主题开发或构建文档，可以安装开发依赖：

```shell
pip install xyzstyle[doc]
```

### 开发环境安装

对于开发人员，可以安装完整的开发环境：

```shell
pip install xyzstyle[dev]
```

## 使用说明

### 基本配置

在 Sphinx 项目的 `conf.py` 文件中配置使用 xyzstyle 主题：

```python
# 使用 xyzstyle 主题
html_theme = 'xyzstyle'

# 主题选项配置
html_theme_options = {
    "use_sidenotes": True,        # 启用侧边注释/页边注释
    "repository_url": "https://github.com/yourusername/yourproject",  # 仓库地址
    "use_repository_button": True,  # 显示"在 GitHub 上查看"按钮
    "announcement": "欢迎使用 xyzstyle 主题！",  # 公告横幅
    "back_to_top_button": True,     # 显示"返回顶部"按钮
    "use_source_button": True,      # 显示"查看源代码"按钮
    "use_edit_page_button": True,   # 显示"编辑此页"按钮
    "use_issues_button": True,      # 显示"报告问题"按钮
    "path_to_docs": "doc",          # 文档目录路径
}

# 添加必要的扩展
extensions = [
    "myst_nb",                      # 支持Markdown和Jupyter Notebook
    "sphinx_design",                # 增强设计元素
    "sphinx.ext.viewcode",          # 添加到高亮源代码的链接
    "sphinx.ext.intersphinx",       # 链接到其他文档
    "sphinx_copybutton",            # 为代码块添加复制按钮
    "sphinx_comments",              # 添加评论功能
    "autoapi.extension",            # 自动生成API文档
    # 其他需要的扩展...
]

# 配置API文档自动生成
autoapi_dirs = ["../src/"]         # 源代码目录
autoapi_root = "autoapi"            # API文档输出目录
autoapi_generate_api_docs = True    # 启用API文档生成
```

### 高级配置

#### 图标链接配置

可以添加自定义图标链接，例如社交媒体图标、GitHub徽章或项目标志：

```python
# 在conf.py文件的开头添加
from utils.links import icon_links  # 或者直接定义

# 自定义图标链接
html_theme_options.update({
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/yourusername/yourproject",
            "icon": "fab fa-github",
            "type": "fontawesome",
        },
        {
            "name": "Twitter",
            "url": "https://twitter.com/yourusername",
            "icon": "fab fa-twitter",
            "type": "fontawesome",
        },
        # 更多图标链接...
    ],
})
```

#### 启动按钮配置

添加交互式代码演示启动按钮：

```python
html_theme_options.update({
    "repository_branch": "main",
    "launch_buttons": {
        "binderhub_url": "https://mybinder.org",
        "colab_url": "https://colab.research.google.com/",
        "deepnote_url": "https://deepnote.com/",
        "notebook_interface": "jupyterlab",
        "thebe": True,
    },
})

# Thebe 配置
thebe_config = {
    "repository_url": "https://github.com/yourusername/yourproject",
    "repository_branch": "main",
    "selector": "div.highlight",
}
```

#### 自定义样式

可以通过添加自定义CSS文件来覆盖默认样式：

```python
# 添加自定义CSS文件
html_static_path = ['_static']
html_css_files = ["css/custom.css"]
```

然后在 `_static/css/custom.css` 文件中添加自定义样式：

```css
/* 自定义公告横幅样式 */
.announcement {
    background-color: #4078c0;
    color: white;
    padding: 10px 0;
    text-align: center;
}

/* 自定义代码块样式 */
div.highlight {
    border-radius: 5px;
}

/* 更多自定义样式... */
```

## 文档

完整的文档可以在 [ReadTheDocs](https://xyzstyle.readthedocs.io/) 上查看，包括详细的配置指南、API文档和使用示例。

## 贡献指南

我们非常欢迎社区贡献！如果您有兴趣参与 xyzstyle 主题的开发，请按照以下步骤操作：

1. Fork 项目仓库
2. 创建一个新的分支用于您的功能或修复
3. 提交您的更改
4. 确保代码通过所有测试
5. 提交 Pull Request

请参阅 [CONTRIBUTING.md](CONTRIBUTING.md) 文件了解更多详细信息。

## 常见问题

### 1. 安装后无法找到 xyzstyle 主题

**解决方案**：确保您使用的是正确的 Python 环境，并且已经正确安装了 xyzstyle 包。可以使用 `pip show xyzstyle` 命令来验证安装。

### 2. API 文档没有生成

**解决方案**：检查 `conf.py` 文件中的 `autoapi_generate_api_docs` 配置是否设置为 `True`，并确保 `autoapi_dirs` 指向正确的源代码目录。

### 3. 主题样式显示不正确

**解决方案**：清除浏览器缓存，或尝试使用 `make clean` 命令清理构建目录后重新构建文档。

### 4. 自定义配置不生效

**解决方案**：确保您的配置项名称正确无误，并且放在 `html_theme_options` 字典中。可以参考文档中的配置示例。

## 许可证

本项目采用 [MIT 许可证](LICENSE)。

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
[status-badge]: https://readthedocs.org/projects/xyzstyle/badge/?version=latest
[status-link]: https://xyzstyle.readthedocs.io/zh-cn/latest/?badge=latest
[download-badge]: https://pepy.tech/badge/xyzstyle
[download-link]: https://pepy.tech/project/xyzstyle
[install-badge]: https://img.shields.io/pypi/dw/xyzstyle?label=pypi%20installs
[install-link]: https://pypistats.org/packages/xyzstyle
