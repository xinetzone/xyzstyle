# XYZStyle 主题测试指南

本目录包含了 XYZStyle Sphinx 主题的测试脚本。这些测试用于确保主题的核心功能正常工作，包括配置管理、主题注册和初始化等。

## 测试结构

测试目录包含以下文件：

- `conftest.py` - 提供全局测试配置和fixture
- `test_config_manager.py` - 测试配置管理器的功能
- `test_theme_registration.py` - 测试主题注册和初始化
- `__init__.py` - Python包初始化文件

## 安装测试依赖

在运行测试之前，需要安装以下依赖：

```bash
pip install pytest pytest-mock sphinx sphinx_book_theme
```

## 运行测试

### 运行所有测试

在项目根目录下执行以下命令：

```bash
cd /media/pc/data/lxw/ai/tasks/xyzstyle
pytest
```

### 运行特定测试文件

```bash
pytest tests/test_config_manager.py
pytest tests/test_theme_registration.py
```

### 运行特定测试函数

```bash
pytest tests/test_config_manager.py::test_config_manager_initialization
```

## 测试选项

测试框架支持以下命令行选项：

- `--run-slow` - 运行标记为慢速的测试
- `--run-integration` - 运行集成测试

示例：

```bash
pytest --run-slow
pytest --run-integration
```

## 测试类型

1. **单元测试** - 测试各个组件的独立功能
   - 配置管理器的初始化和配置加载
   - 主题注册和事件连接

2. **集成测试** (如果启用) - 测试组件之间的交互
   - 主题与Sphinx应用的集成
   - 配置加载与应用的端到端测试

## 测试覆盖率

目前的测试覆盖了以下功能：

1. **ConfigManager**
   - 初始化和基本功能
   - 直接路径加载配置
   - 错误处理
   - 配置映射

2. **XYZStyleTheme**
   - 主题初始化和注册
   - 主题目录验证
   - 错误处理
   - 配置加载器事件创建

3. **Sphinx扩展集成**
   - setup函数功能
   - 并行处理支持

## 添加新测试

要添加新的测试：

1. 创建新的测试文件，文件名以`test_`开头
2. 使用pytest风格编写测试函数，函数名以`test_`开头
3. 可以使用`conftest.py`中定义的fixture
4. 对于慢速测试或集成测试，使用相应的标记：
   ```python
   @pytest.mark.slow
   def test_slow_feature():
       # 测试代码
       pass
       
   @pytest.mark.integration
   def test_integration():
       # 测试代码
       pass
   ```

## 测试注意事项

- 所有测试都是隔离的，使用mock对象避免实际文件操作和外部依赖
- 对于需要实际文件操作的测试，使用临时目录和文件
- 测试应该快速、可靠，避免长时间运行的测试