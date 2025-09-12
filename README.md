# XYZStyle Theme for Sphinx

XYZStyle 是一个基于 sphinx_book_theme 的 Sphinx 文档主题扩展，提供了优雅的 UI 设计、配置管理和丰富的自定义选项。

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
├── config/              # 配置管理模块
│   ├── __init__.py      # 配置模块导出
│   └── manager.py       # 配置管理器实现
└── theme/xyzstyle/      # 主题资源文件
    ├── theme.toml       # 主题配置
    ├── layout.html      # 主题布局模板
    └── static/          # 静态资源文件
        ├── css/         # CSS 样式文件
        └── js/          # JavaScript 文件
```

## 核心功能

### 1. 主题注册与初始化

XYZStyleTheme 类负责查找主题目录、注册主题到 Sphinx 应用，并连接配置初始化事件。通过 `__post_init__` 方法，确保主题目录存在并成功注册。

### 2. 配置管理

ConfigManager 类提供了配置加载和更新功能，支持从 TOML 文件加载配置，并将配置应用到 Sphinx 应用实例中。它包含配置验证、类型检查和增量更新机制。

### 3. Sphinx 扩展集成

通过 `setup` 函数，XYZStyle 主题被注册为 Sphinx 扩展，支持并行处理，并提供完整的主题功能。

## 安装

使用 pip 安装 XYZStyle 主题：

```bash
pip install xyzstyle
```

## 依赖

- sphinx_book_theme (主题继承)
- Sphinx (文档生成引擎)
- Python 3.12+ (运行环境)

## 使用方法

在你的 Sphinx 项目的 `conf.py` 文件中，添加以下配置：

```python
# 设置主题
html_theme = 'xyzstyle'

# 导入主题模块
import xyzstyle

# 主题配置选项
html_theme_options = {
    "use_download_button": "True",
    "use_fullscreen_button": "True",
    "use_repository_button": "True",
    "repository_url": "https://github.com/yourusername/yourproject",
    "path_to_docs": "doc",
    # 其他 sphinx_book_theme 支持的选项
}
```

## 主题配置选项

XYZStyle 主题支持以下核心配置选项（在 theme.toml 中定义）：

| 选项 | 描述 | 默认值 |
|------|------|--------|
| announcement | 页面顶部公告内容 | "" |
| use_download_button | 是否显示下载按钮 | "True" |
| use_fullscreen_button | 是否显示全屏按钮 | "True" |
| use_repository_button | 是否显示仓库按钮 | "False" |
| repository_url | 项目仓库URL | "" |
| path_to_docs | 文档路径 | "doc" |
| pygments_style | 代码高亮样式 | { default = "perldoc" } |
| footer_content_items | 页脚内容项 | "author.html, copyright.html, last-updated.html, extra-footer.html" |

## 配置文件加载

XYZStyle 支持通过在 Sphinx 项目源码目录中的 default.toml 文件加载配置。配置管理器会自动映射 TOML 配置到 Sphinx 配置项。

## 自定义样式

主题包含以下自定义 CSS 文件：
- custom.css
- tippy.css
- try_examples.css
- sphinx-book-theme.css (继承自基础主题)

## 扩展与开发

如果你想扩展或修改 XYZStyle 主题，可以：
1. 修改主题目录下的静态资源文件
2. 扩展 ConfigManager 类以支持更多配置选项
3. 在 layout.html 中添加自定义模板覆盖

## 许可证

XYZStyle 主题采用 Apache License 2.0。
