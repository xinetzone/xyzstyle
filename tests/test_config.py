"""Tests for the XYZStyle configuration system."""

import os
import sys
from pathlib import Path

# 添加项目根目录到路径，以便导入模块
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.xyzstyle.config import ConfigManager, get_final_config, validate_config

def test_config_manager():
    """Test the ConfigManager class."""
    print("=== Testing ConfigManager ===")
    
    # 创建配置管理器实例
    config_manager = ConfigManager()
    
    # 测试加载默认配置
    default_config = config_manager.load_config()
    print(f"Default config loaded: {default_config is not None}")
    if default_config:
        print(f"Default config keys: {list(default_config.keys())}")
    
    # 测试获取配置
    config = config_manager.get_config()
    print(f"Config obtained: {config is not None}")
    
    # 测试获取 Sphinx 格式的配置
    sphinx_config = config_manager.get_sphinx_config()
    print(f"Sphinx config obtained: {sphinx_config is not None}")
    if sphinx_config:
        print(f"Sphinx config keys: {list(sphinx_config.keys())[:10]}...")


def test_get_final_config():
    """Test the get_final_config function."""
    print("\n=== Testing get_final_config ===")
    
    # 测试不带参数调用
    final_config = get_final_config()
    print(f"Final config obtained without parameters: {final_config is not None}")
    if final_config:
        print(f"Final config keys: {list(final_config.keys())[:10]}...")
    
    # 测试带 CLI 配置调用
    cli_config = {"html_title": "Test Title", "extensions": ["sphinx.ext.autosummary"]}
    final_config_with_cli = get_final_config(cli_config=cli_config)
    print(f"Final config with CLI options obtained: {final_config_with_cli is not None}")
    if final_config_with_cli:
        print(f"HTML title from CLI: {final_config_with_cli.get('html_title')}")
        print(f"Extensions include autosummary: {'sphinx.ext.autosummary' in final_config_with_cli.get('extensions', [])}")


def test_validation():
    """Test configuration validation."""
    print("\n=== Testing Configuration Validation ===")
    
    # 测试有效的配置
    valid_config = {"html_theme_options": {"announcement": "Test announcement"}}
    validation_result = validate_config(valid_config)
    print(f"Valid config validation result: {validation_result}")
    
    # 测试无效的配置（根据JSON schema的要求）
    # 注意：这里的"无效"取决于你的schema定义
    # 这只是一个示例，可能需要根据实际schema进行调整
    invalid_config = {"html_theme_options": {"unknown_option": "value"}}
    validation_result = validate_config(invalid_config)
    print(f"Invalid config validation result: {validation_result is not None}")
    if validation_result:
        print(f"Validation error: {validation_result}")


def test_example_config():
    """Test the example configuration file."""
    print("\n=== Testing Example Configuration ===")
    
    # 检查示例配置文件是否存在
    example_config_path = Path(__file__).parent.parent / "doc" / "example_config.toml"
    if example_config_path.exists():
        print(f"Example config file found: {example_config_path}")
        
        # 使用示例配置文件创建最终配置
        final_config = get_final_config(user_toml=example_config_path)
        print(f"Final config from example file: {final_config is not None}")
        if final_config:
            print(f"Keys from example config: {list(final_config.keys())[:10]}...")
            if "html_theme_options" in final_config:
                print(f"HTML theme options keys: {list(final_config['html_theme_options'].keys())[:10]}...")
    else:
        print(f"Example config file not found at {example_config_path}")


def run_all_tests():
    """Run all tests."""
    print("Running XYZStyle configuration system tests...\n")
    
    try:
        test_config_manager()
        test_get_final_config()
        test_validation()
        test_example_config()
        
        print("\nAll tests completed successfully!")
    except Exception as e:
        print(f"\nTest failed with error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    run_all_tests()