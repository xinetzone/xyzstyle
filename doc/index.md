# 欢迎使用 MySTX 主题文档

## 📑 文档概览

本文档将帮助您快速上手 MySTX 主题，了解其核心功能和配置方法，以及如何在您的项目中充分利用它的强大特性。

## 📖 文档导航

使用左侧导航栏或以下链接浏览完整文档：

```{toctree}
:hidden:

readme
```

## 🚀 快速入门指南

### 基础配置示例

以下是一个最小化的 Sphinx 项目配置示例，展示如何使用 MySTX 主题：

```python
# conf.py
project = "您的项目名称"
authors = "您的名字"
version = "0.1.0"
release = "0.1.0"

# 使用 MySTX 主题
html_theme = "mystx"

# 主题配置选项
html_theme_options = {
    "repository_url": "https://github.com/您的用户名/您的项目",
    "use_repository_button": True,
    "use_issues_button": True,
    "home_page_in_toc": True,
}

# 必要的扩展
extensions = [
    "mystx",
]
```

### TOML 配置示例

MySTX 支持通过 `default.toml` 文件管理配置：

```toml
# default.toml
[html_theme_options]
repository_url = "https://github.com/您的用户名/您的项目"
use_repository_button = true
use_issues_button = true
use_edit_page_button = true
path_to_docs = "docs/"
```

## 💡 核心功能亮点

MySTX 主题为您的文档提供了以下关键增强：

* **现代化界面设计**：基于 Sphinx Book Theme，提供清晰、专业的阅读体验
* **TOML 配置支持**：简化配置管理，提高项目可维护性
* **完整的 Markdown 支持**：通过 MyST 解析器支持扩展 Markdown 语法
* **Notebook 集成**：原生支持 Jupyter Notebook 内容展示
* **丰富的扩展生态**：可与多种 Sphinx 扩展无缝协作

## 🔧 进阶使用

### 主题自定义

MySTX 主题提供了丰富的自定义选项，您可以通过 `html_theme_options` 或 `default.toml` 文件配置各种视觉和功能特性。详情请参阅文档中的配置部分。

### 扩展集成

MySTX 与多个常用 Sphinx 扩展兼容，包括但不限于：

* `sphinx.ext.napoleon` - 支持 Google 和 NumPy 风格的文档字符串
* `sphinx_thebe` - 提供交互式代码执行功能
* `sphinx_comments` - 添加评论功能
* `ablog` - 支持博客功能

## 🔗 官方资源

* [GitHub 仓库](https://github.com/xinetzone/mystx) - 获取源代码和最新更新
* [PyPI 项目页面](https://pypi.org/project/mystx/) - 安装包信息
* [ReadTheDocs 文档](https://mystx.readthedocs.io/) - 完整的在线文档
* [问题反馈](https://github.com/xinetzone/mystx/issues) - 报告问题或提出建议

## 📊 索引与搜索

* {ref}`genindex` - 查看所有索引条目
* {ref}`modindex` - 查看模块索引
* {ref}`search` - 搜索文档内容