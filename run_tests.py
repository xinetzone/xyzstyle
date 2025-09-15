#!/usr/bin/env python3
"""
XYZStyle 主题测试运行脚本

此脚本提供了一种简便的方式来运行XYZStyle主题的所有测试，并可选择性地生成测试覆盖率报告。

使用方法:
    python run_tests.py [选项]

选项:
    --coverage    生成并显示测试覆盖率报告
    --html        生成HTML格式的覆盖率报告（与--coverage一起使用）
"""

import os
import sys
import argparse
import subprocess
import shutil
from pathlib import Path

# 项目根目录
PROJECT_ROOT = Path(__file__).parent

# 测试目录
TESTS_DIR = PROJECT_ROOT / "tests"

# 源码目录
SRC_DIR = PROJECT_ROOT / "src"

# 覆盖率报告目录
COVERAGE_DIR = PROJECT_ROOT / "coverage_report"


def setup_path():
    """设置Python路径以确保可以正确导入模块"""
    # 添加src目录到路径
    sys.path.insert(0, str(SRC_DIR))
    
    # 添加项目根目录到路径
    sys.path.insert(0, str(PROJECT_ROOT))


def check_dependencies():
    """检查运行测试所需的依赖"""
    try:
        # 检查pytest是否安装
        subprocess.run([sys.executable, "-m", "pytest", "--version"], 
                      capture_output=True, check=True)
        
        return True
    except (subprocess.SubprocessError, ImportError):
        print("错误: 未找到pytest。请先安装测试依赖：")
        print("  pip install pytest pytest-cov")
        return False


def run_tests(coverage=False, html_coverage=False):
    """运行测试并可选生成覆盖率报告"""
    # 确保测试目录存在
    if not TESTS_DIR.exists():
        print(f"错误: 测试目录 {TESTS_DIR} 不存在")
        return False

    # 构建测试命令
    cmd = [sys.executable, "-m", "pytest", str(TESTS_DIR)]
    
    # 如果需要覆盖率报告
    if coverage:
        cmd.extend(["--cov=xyzstyle", "--cov-report=term-missing"])
        
        # 如果需要HTML格式的覆盖率报告
        if html_coverage:
            # 清理旧的覆盖率报告目录
            if COVERAGE_DIR.exists():
                shutil.rmtree(COVERAGE_DIR)
            
            cmd.extend(["--cov-report", f"html:{COVERAGE_DIR}"])

    try:
        # 运行测试命令
        result = subprocess.run(cmd, check=True)
        
        # 如果生成了HTML覆盖率报告，提示用户
        if coverage and html_coverage:
            print(f"\nHTML覆盖率报告已生成: {COVERAGE_DIR}/index.html")
            
            # 检查是否有可用的浏览器来打开报告
            if sys.platform == 'darwin':  # macOS
                open_cmd = 'open'
            elif sys.platform == 'win32':  # Windows
                open_cmd = 'start'
            else:  # Linux和其他Unix-like系统
                open_cmd = 'xdg-open'
                
            try:
                # 尝试打开覆盖率报告
                subprocess.run([open_cmd, str(COVERAGE_DIR / "index.html")], 
                              capture_output=True)
                print("覆盖率报告已在浏览器中打开")
            except subprocess.SubprocessError:
                print("无法自动打开浏览器，请手动打开覆盖率报告")
                
        return True
    except subprocess.CalledProcessError:
        print("测试失败")
        return False


def main():
    """主函数"""
    # 设置Python路径
    setup_path()
    
    # 解析命令行参数
    parser = argparse.ArgumentParser(description="XYZStyle主题测试运行器", 
                                    formatter_class=argparse.RawDescriptionHelpFormatter, 
                                    epilog=__doc__)
    parser.add_argument("--coverage", action="store_true", 
                       help="生成并显示测试覆盖率报告")
    parser.add_argument("--html", action="store_true", 
                       help="生成HTML格式的覆盖率报告（与--coverage一起使用）")
    
    args = parser.parse_args()
    
    # 检查依赖
    if not check_dependencies():
        return 1
    
    # 运行测试
    success = run_tests(coverage=args.coverage, html_coverage=args.html)
    
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())