# -*- coding: utf-8 -*-
project = "mystx 文档"
description = "mystx 主题的使用文档"
author = "xinetzone"
# == 国际化与本地化设置 ==================================================================
language = 'zh_CN' # 文档语言（中文简体）
locale_dirs = ['../locales/'] # 翻译文件存放目录
gettext_compact = False # 是否合并子目录的PO文件（False表示不合并）
# 插件
extensions = ['mystx']
html_last_updated_fmt = '%Y-%m-%d, %H:%M:%S'  # 文档的最后更新时间格式
# 排除文件和目录模式
exclude_patterns = [
    "_build",  # 构建输出目录
    "Thumbs.db",  # 缩略图数据库
    ".DS_Store",  # macOS 系统文件
]
static_path = ["_static"]  # 静态资源目录，用于存放CSS、JavaScript、图片等
html_theme = 'mystx'  # 使用的主题名称
html_logo = "_static/images/logo.jpg"
html_title = "Sphinx mystx Theme"
html_copy_source = True
html_favicon = "_static/images/favicon.jpg"
