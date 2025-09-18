# MySTX

![repo size](https://img.shields.io/github/repo-size/xinetzone/mystx.svg)
[![PyPI][pypi-badge]][pypi-link]
[![GitHub issues][issue-badge]][issue-link]
[![GitHub forks][fork-badge]][fork-link]
[![GitHub stars][star-badge]][star-link]
[![GitHub license][license-badge]][license-link]
[![contributors][contributor-badge]][contributor-link]
[![Documentation Status][status-badge]][status-link]
[![Downloads][download-badge]][download-link]
[![PyPI - Downloads][install-badge]][install-link]

[pypi-badge]: https://img.shields.io/pypi/v/mystx.svg
[pypi-link]: https://pypi.org/project/mystx/
[issue-badge]: https://img.shields.io/github/issues/xinetzone/mystx
[issue-link]: https://github.com/xinetzone/mystx/issues
[fork-badge]: https://img.shields.io/github/forks/xinetzone/mystx
[fork-link]: https://github.com/xinetzone/mystx/network
[star-badge]: https://img.shields.io/github/stars/xinetzone/mystx
[star-link]: https://github.com/xinetzone/mystx/stargazers
[license-badge]: https://img.shields.io/github/license/xinetzone/mystx
[license-link]: https://github.com/xinetzone/mystx/LICENSE
[contributor-badge]: https://img.shields.io/github/contributors/xinetzone/mystx
[contributor-link]: https://github.com/xinetzone/mystx/contributors
[status-badge]: https://readthedocs.org/projects/mystx/badge/?version=latest
[status-link]: https://mystx.readthedocs.io/zh-cn/latest/?badge=latest
[download-badge]: https://pepy.tech/badge/mystx
[download-link]: https://pepy.tech/project/mystx
[install-badge]: https://img.shields.io/pypi/dw/mystx?label=pypi%20installs
[install-link]: https://pypistats.org/packages/mystx

**mystx** 是基于 Sphinx Book Theme 的现代化、可定制的 Sphinx HTML 主题，为技术文档提供优雅美观的展示效果。它结合了现代Web设计理念与优秀的阅读体验，使您的文档既专业又易于阅读。

## ✨ 特性

- 🎨 基于 Sphinx Book Theme 的现代化设计风格
- 🛠️ 灵活的配置系统，支持从 TOML 文件加载默认配置
- 📝 完善的 MyST Markdown 和 Jupyter Notebook 支持
- 🚀 简单易用的主题注册和配置应用流程
- 📚 丰富的可选扩展，用于增强文档功能

## 🔧 安装

### 基本安装

使用 pip 安装 mystx 主题：

```bash
pip install mystx
```

### 安装文档扩展

如果需要使用文档扩展功能，可以安装可选依赖：

```bash
pip install "mystx[doc]"
```

### 开发环境安装

对于开发者，可以安装开发依赖：

```bash
pip install -ve .[dev]
```

## 📋 依赖

### 核心依赖

- `sphinx-book-theme>=1.1.4` (主题继承)
- `sphinx>=8.0.0` (文档生成引擎)
- `myst-nb` (Jupyter Notebook 支持)
- `myst-parser` (MyST Markdown 解析器)
- Python 3.12+ (运行环境)

### 可选依赖

文档扩展依赖包括：`ablog`, `ipywidgets`, `numpy`, `matplotlib`, `sphinx-comments` 等多个扩展，用于增强文档功能。

## 🚀 快速开始

在您的 Sphinx 项目的 `conf.py` 文件中，添加以下配置来使用 mystx 主题：

```python
# 设置 HTML 主题
html_theme = "mystx"

# 主题选项配置
html_theme_options = {
    # 您的主题选项配置
}

# 配置插件
extensions = [
    "mystx",
    "sphinx.ext.napoleon",  # 支持 Google 和 NumPy 风格的文档字符串
    "sphinx_thebe",  # 支持 Thebe 交互式代码执行
    # 其他需要的扩展
]
```

## ⚙️ 配置指南

### 主题选项

mystx 主题支持通过 `html_theme_options` 配置各种选项，例如：

```python
html_theme_options = {
    "repository_url": "https://github.com/yourusername/yourproject",
    "use_repository_button": True,
    "use_issues_button": True,
    "use_edit_page_button": True,
    "path_to_docs": "docs/",
    "home_page_in_toc": True,
    # 更多配置选项...
}
```

### 默认配置文件

mystx 支持通过 `default.toml` 文件加载默认配置。在您的 Sphinx 项目根目录创建 `default.toml` 文件：

```toml
[html_theme_options]
repository_url = "https://github.com/yourusername/yourproject"
use_repository_button = true
use_issues_button = true
# 更多配置选项...
```

## 📚 文档

请访问 [mystx 官方文档](https://mystx.readthedocs.io/zh-cn/latest/) 了解更多详细信息和使用示例。

## 🔗 链接

- [GitHub 仓库](https://github.com/xinetzone/mystx)
- [PyPI 项目页面](https://pypi.org/project/mystx/)
- [官方文档](https://mystx.readthedocs.io/)
- [问题反馈](https://github.com/xinetzone/mystx/issues)
