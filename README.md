# XYZStyle Theme for Sphinx

XYZStyle 是一个基于 sphinx-book-theme 的现代化 Sphinx 文档主题，提供了优雅的 UI 设计和丰富的自定义选项。

## 主要特点

- **现代化界面**：基于 sphinx-book-theme 的优雅设计
- **响应式支持**：完美适配桌面和移动设备
- **丰富的自定义选项**：包括页面布局、样式、内容等多个方面的自定义能力
- **高度可扩展性**：支持额外的 CSS、JavaScript 和自定义内容块
- **主题继承优化**：保留 sphinx-book-theme 的优点，同时添加特有的增强功能

## 安装

使用 pip 安装 XYZStyle 主题：

```bash
pip install xyzstyle
```

## 依赖

- sphinx-book-theme>=0.4.0
- Python>=3.12

## 使用方法

在你的 Sphinx 项目的 `conf.py` 文件中，添加以下配置：

```python
# 设置主题
html_theme = 'xyzstyle'

# 添加主题路径（如果需要）
import xyzstyle
html_theme_path = [xyzstyle.get_html_theme_path()]

# 主题配置选项
html_theme_options = {
    # sphinx-book-theme 原始选项
    "use_download_button": "True",
    "use_fullscreen_button": "True",
    "use_repository_button": "True",
    "repository_url": "https://github.com/yourusername/yourproject",
    "path_to_docs": "doc",
    
    # XYZStyle 特有选项
    "xyzstyle_header_announcement": "欢迎访问我的文档网站！",  # 页面顶部的公告内容
    "xyzstyle_footer_content": "© 2023 版权所有",  # 页脚的自定义内容
    "xyzstyle_sidebar_footer": "联系我们: support@example.com",  # 侧边栏底部的自定义内容
    "xyzstyle_article_header_content": "<p>本文档最后更新于 2023-01-01</p>",  # 文章头部的自定义内容
    "xyzstyle_article_footer_content": "<p>感谢您阅读本文档</p>",  # 文章底部的自定义内容
    "xyzstyle_after_content": "<div class='related-articles'><h3>相关文章</h3><ul><li><a href='#'>文章1</a></li><li><a href='#'>文章2</a></li></ul></div>",  # 内容区域之后的自定义内容
    "xyzstyle_enable_top_toc": "True",  # 是否在文章顶部显示目录
    "xyzstyle_extra_meta": "<meta name='description' content='我的项目文档'>",  # 额外的 HTML meta 标签
    "xyzstyle_extra_css": ["_static/custom_extra.css"],  # 额外的 CSS 文件路径列表
    "xyzstyle_extra_js": ["_static/custom_extra.js"],  # 额外的 JavaScript 文件路径列表
    "xyzstyle_inline_js": "console.log('XYZStyle theme loaded successfully!');"  # 内联 JavaScript 代码
}
```

## 自定义功能

XYZStyle 主题提供了多种自定义功能，让你可以根据自己的需求定制文档的外观和行为：

### 1. 自定义内容块

可以在文档的不同位置添加自定义内容，包括：
- 页面顶部公告 (`xyzstyle_header_announcement`)
- 页脚自定义内容 (`xyzstyle_footer_content`)
- 侧边栏底部内容 (`xyzstyle_sidebar_footer`)
- 文章头部内容 (`xyzstyle_article_header_content`)
- 文章底部内容 (`xyzstyle_article_footer_content`)
- 内容区域之后内容 (`xyzstyle_after_content`)

### 2. 资源扩展

可以添加额外的 CSS 和 JavaScript 文件，或者直接添加内联 JavaScript 代码：
- 额外的 CSS 文件 (`xyzstyle_extra_css`)
- 额外的 JavaScript 文件 (`xyzstyle_extra_js`)
- 内联 JavaScript 代码 (`xyzstyle_inline_js`)

### 3. 布局控制

可以控制文档的布局，例如：
- 在文章顶部显示目录 (`xyzstyle_enable_top_toc`)
- 添加额外的 HTML meta 标签 (`xyzstyle_extra_meta`)

## 贡献

欢迎对 XYZStyle 主题进行贡献！如果你有任何建议或问题，请在 GitHub 上提交 issue 或 pull request。

## 许可证

XYZStyle 主题采用 Apache License 2.0。
