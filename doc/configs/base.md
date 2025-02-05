# Sphinx 基础配置

```{rubric} 基础配置
```

```{code-block} python
:caption: conf.py

# == Project 信息 ================================================================
project = 'xyzstyle' # 项目名称，方便使用
copyright = '2022, xinetzone' # 版权信息
author = 'xinetzone' # 作者信息

# == 国际化输出 ========================================================================
language = 'zh_CN'
locale_dirs = ['../locales/']  # po files will be created in this directory
gettext_compact = False  # optional: avoid file concatenation in sub directories.

# 通用配置
# =========================================================================================
# 表示 Sphinx 扩展的模块名称的字符串列表。它们可以是
# Sphinx 自带的插件（命名为 'sphinx.ext.*'）或您自定义的插件。
# 对于第一方插件，有两种选择。配置文件本身可以是插件；为此，你只需要在其中提供 {func}`setup` 函数。
# 否则，你必须确保你的自定义扩展是可导入的，并且位于 Python 路径中的某个目录下。
# 在修改 `sys.path` 时，请确保使用绝对路径。
# 如果你的自定义扩展位于相对于配置目录的某个目录中，可以使用 `pathlib.Path.resolve()` 
extensions = [
    "myst_nb",
]

# 相对于源目录的模式列表，用于匹配在查找源文件时要忽略的文件和目录。
# 此模式还会影响 html_static_path 和 html_extra_path。
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# == HTML输出选项 ================================================================
# 这些选项影响 HTML 输出。其他各种生成器也源自 HTML 输出，并且也使用这些选项。
html_theme = 'xyzstyle' # 使用的主题名称
# 使用 Sphinx 自带模板生成的 HTML 文档的“标题”。
# 它会被附加到各个页面的 <title> 标签中，并在导航栏中作为“最顶层”的元素使用。
html_title = "Sphinx xyzstyle Theme" 
# 包含自定义静态文件（如样式表或脚本文件）的路径列表。
# 相对路径被视为相对于配置目录。
# 它们在主题的静态文件之后被复制到输出的 `_static` 目录中，
# 因此名为 `default.css` 的文件将覆盖主题的 `default.css`。
html_static_path = ['_static']
# 如果提供了此项，它必须是文档徽标的图像文件的名称（相对于配置目录的路径），
# 或者是指向徽标图像文件的URL。它放置在侧边栏的顶部；因此，其宽度不应超过 200 像素。
# 图像文件将被复制到 `_static` 目录，但仅当该文件尚不存在于该目录中时才会复制。
html_logo = "_static/images/logo.jpg" 
# 如果提供，这必须是图像文件的名称（相对于配置目录的路径），
# 该图像是文档的 favicon，或者是指向 favicon 图像文件的URL。
# 浏览器使用它作为标签、窗口和书签的图标。
# 它应该是 16x16 像素的图标，格式为 PNG、SVG、GIF 或 ICO。
# 图像文件将被复制到 `_static` 目录，但仅当该文件尚不存在于该目录中时才会复制。
html_favicon = "_static/images/favicon.jpg"
# CSS文件列表。条目必须是文件名字符串，或者是包含文件名字符串和属性字典的元组。
# 文件名必须相对于html_static_path，
# 或者是带有方案的完整 URI，例如'https://example.org/style.css'。
# 属性字典用于 `<link>` 标签的属性，例如 `('print.css', {'media': 'print'})`。
html_css_files = ["custom.css"]
# 如果设置，将使用给定的 {func}`time.strftime()` 格式在页面页脚中插入一个“上次更新时间：”的时间戳。
# 空字符串等同于 `'%b %d, %Y'` （或依赖于本地化的等效格式）。
html_last_updated_fmt = '%Y-%m-%d, %H:%M:%S'
```

详细配置信息见：{external:ref}`Sphinx 配置 <build-config>`。
