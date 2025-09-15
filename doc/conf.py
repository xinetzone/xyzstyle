# -*- coding: utf-8 -*-
project = "xyzstyle 文档"
description = "xyzstyle 主题的使用文档"
author = "xinetzone"
# == 国际化与本地化设置 ==================================================================
language = 'zh_CN' # 文档语言（中文简体）
locale_dirs = ['../locales/'] # 翻译文件存放目录
gettext_compact = False # 是否合并子目录的PO文件（False表示不合并）
# 插件
extensions = [
    'xyzstyle',
    "myst_nb",  # Markdown和Jupyter笔记本支持
]
html_last_updated_fmt = '%Y-%m-%d, %H:%M:%S'  # 文档的最后更新时间格式
html_theme_options = {
    "content_footer_items": ["last-updated"],
}
static_path = ["_static"]  # 静态资源目录，用于存放CSS、JavaScript、图片等
html_theme = 'xyzstyle'  # 使用的主题名称
html_logo = "_static/images/logo.jpg"
html_title = "Sphinx xyzstyle Theme"
html_copy_source = True
html_favicon = "_static/images/favicon.jpg"
# 可选插件
extensions.extend([
    "sphinx_design",                # 增强设计元素
    "sphinx.ext.viewcode",          # 添加到高亮源代码的链接
    "sphinx.ext.intersphinx",       # 链接到其他文档
    "sphinx_copybutton",            # 为代码块添加复制按钮
    "sphinx_comments",              # 添加评论和注释功能
])
# =============================================================================
# 可选功能配置
# =============================================================================
# 1. 代码复制按钮配置
copybutton_exclude = '.linenos, .gp'  # 排除行号和提示符
# 选择器配置，避免复制按钮出现在笔记本单元格编号上
copybutton_selector = ":not(.prompt) > div.highlight pre"
# 2. 评论系统配置
comments_config = {
   "hypothesis": True,  # 启用 Hypothesis 注释
   "utterances": {
      "repo": "xinetzone/xyzstyle",
      "optional": "config",
   }  # 启用 Utterances 评论
}
