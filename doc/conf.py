# == 项目基本信息 ========================================================================
project = 'xyzstyle' # 项目名称
copyright = '2022, xinetzone' # 版权信息
author = 'xinetzone' # 作者信息

# == 主题设置 ============================================================================
html_theme = "xyzstyle" # 使用的HTML主题
# 静态资源配置
html_static_path = ['_static']  # 指定静态文件目录，用于存放CSS、JavaScript、图片等
html_logo = "_static/images/logo.jpg"  # 网站Logo路径，显示在页面顶部
html_favicon = "_static/images/favicon.jpg"  # 网站图标路径，显示在浏览器标签页
html_last_updated_fmt = '%Y-%m-%d, %H:%M:%S'  # 最后更新时间格式

# == 国际化与本地化设置 ==================================================================
language = 'zh_CN' # 文档语言（中文简体）
locale_dirs = ['../locales/'] # 翻译文件存放目录
gettext_compact = False # 是否合并子目录的PO文件（False表示不合并）

# == 扩展插件配置 ========================================================================
extensions = [
    "myst_nb",  # Markdown和Jupyter笔记本支持
] # 启用的Sphinx扩展
