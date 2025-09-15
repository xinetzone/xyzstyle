# xyzstyle

[![PyPI][pypi-badge]][pypi-link]
[![GitHub issues][issue-badge]][issue-link]
[![GitHub forks][fork-badge]][fork-link]
[![GitHub stars][star-badge]][star-link]
[![GitHub license][license-badge]][license-link]
[![contributors][contributor-badge]][contributor-link]
[![Documentation Status][status-badge]][status-link]
[![Downloads][download-badge]][download-link]
[![PyPI - Downloads][install-badge]][install-link]

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

**xyzstyle** 是基于 Sphinx Book Theme 的现代化、可定制的 Sphinx HTML 主题，为技术文档提供优雅美观的展示效果。它结合了现代Web设计理念与优秀的阅读体验，使您的文档既专业又易于阅读。


## 主要特点

- **主题继承**：完美继承并扩展 sphinx_book_theme 的功能
- **配置管理**：支持通过 TOML 文件加载和管理配置
- **事件集成**：与 Sphinx 的配置初始化事件无缝集成
- **样式定制**：提供自定义 CSS 文件和主题选项
- **响应式设计**：适配桌面和移动设备的响应式布局

## 项目结构

```
src/xyzstyle/
├── __init__.py          # Sphinx 扩展入口点
├── set_theme.py         # 主题管理类
└── theme/xyzstyle/      # 主题资源文件
    ├── theme.toml       # 主题配置
    ├── layout.html      # 主题布局模板
    └── static/          # 静态资源文件
        ├── css/         # CSS 样式文件
        └── js/          # JavaScript 文件
```

## 安装

使用 pip 安装 XYZStyle 主题：

```bash
pip install xyzstyle
```

## 依赖

- sphinx_book_theme (主题继承)
- Sphinx (文档生成引擎)
- Python 3.12+ (运行环境)

## 配置文件加载

XYZStyle 支持通过在 Sphinx 项目源码目录中的 `default.toml` 文件加载 `html_theme_options` 等配置。

