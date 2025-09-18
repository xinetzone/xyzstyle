#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sphinx 文档配置文件

该文件包含了 mystx 文档的所有配置项，包括项目信息、国际化设置、扩展插件、主题配置等。
"""
from taolib import get_version  # 引入获取版本号的函数
# ================================= 项目基本信息 =================================
project = "mystx"  # 文档项目名称
author = "xinetzone"    # 文档作者
release = get_version("mystx")  # 获取mystx主题的版本号
# ================================= 国际化与本地化设置 ==============================
language = 'zh_CN'       # 文档语言（中文简体）
locale_dirs = ['../locales/']  # 翻译文件存放目录
gettext_compact = False  # 是否合并子目录的PO文件（False表示不合并）

# ================================= 扩展插件配置 =================================
extensions = ['mystx']

# ================================= 文档构建配置 =================================
# 排除文件和目录模式
exclude_patterns = [
    "_build",      # 构建输出目录
    "Thumbs.db",   # 缩略图数据库
    ".DS_Store",    # macOS 系统文件
]

# 静态资源目录，用于存放CSS、JavaScript、图片等
html_static_path = ["_static"]

# 文档的最后更新时间格式
html_last_updated_fmt = '%Y-%m-%d, %H:%M:%S'

# ================================= 主题与外观配置 ================================
html_theme = 'mystx'            # 使用的主题名称
html_title = "Sphinx mystx Theme"  # 文档标题
html_logo = "_static/images/logo.jpg"  # 文档logo
html_favicon = "_static/images/favicon.jpg"  # 文档favicon
html_copy_source = True  # 是否在文档中包含源文件链接

# ================================= thebe 交互式功能配置 =================================
# use_thebe = True  # 是否开启Thebe功能（默认关闭）
# thebe_config = {
#     "repository_url": f"https://github.com/xinetzone/{project}",
#     "repository_branch": "main",
#     "selector": "div.highlight",
#     # "selector": ".thebe",
#     # "selector_input": "",
#     # "selector_output": "",
#     # "codemirror-theme": "blackboard",  # Doesn't currently work
#     # "always_load": True,  # To load thebe on every page
# }

# ================================= 版本切换器配置 =================================
version_switcher = True  # 是否开启版本切换器（默认关闭）
