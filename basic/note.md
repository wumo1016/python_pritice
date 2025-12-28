## 版本管理工具

- uv

  - [安装](https://github.com/astral-sh/uv)
  - 常用命令
    - 安装全局版本: `uv python install --global`
    - 安装最新稳定版本: `uv python install`
    - 安装指定版本: `uv python install 3.12`
    - 查看已通过 uv 安装的所有 Python 版本: `uv python list`
    - 卸载指定版本的 Python: `uv python uninstall 3.12`
    - 初始化项目: `uv init [项目名]`
    - 新建虚拟环境: `uv venv`
    - 进入虚拟环境
      - win: `.\.venv\Scripts\Activate.ps1`
      - mac: `source .venv/bin/activate`
    - 安装依赖: `uv add [依赖名]`

- pyenv

## 基础操作

- 进行命令行 `python3`
- 退出命令行 `exit()`
- 执行 python 文件 `python3 [文件名]`
