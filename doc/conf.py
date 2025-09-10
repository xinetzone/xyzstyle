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

# 主题选项配置
html_theme_options = {
    "use_sidenotes": True,        # 启用侧边注释/页边注释
    # "repository_url": "https://github.com/yourusername/yourproject",  # 仓库地址
    "repository_url": "https://github.com/xinetzone/xyzstyle",  # 仓库地址
    "use_repository_button": True,  # 显示"在 GitHub 上查看"按钮
    "announcement": "欢迎使用 xyzstyle 主题！",  # 公告横幅
    "back_to_top_button": True,     # 显示"返回顶部"按钮
    "use_source_button": True,      # 显示"查看源代码"按钮
    "use_edit_page_button": True,   # 显示"编辑此页"按钮
    "use_issues_button": True,      # 显示"报告问题"按钮
    "path_to_docs": "doc",          # 文档目录路径
}

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
