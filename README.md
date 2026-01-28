## [uv 菜鸟教程](https://www.runoob.com/python3/uv-tutorial.html)

## 版本管理工具

- uv
  - [安装](https://github.com/astral-sh/uv)
    - mac 安装
      - `brew install uv`
  - 常用命令
    - 安装最新稳定版本: `uv python install`
    - 安装指定版本: `uv python install 3.12`
    - 查看已通过 uv 安装的所有 Python 版本: `uv python list`
    - 卸载指定版本的 Python: `uv python uninstall 3.12`
    - 初始化项目: `uv init [项目名]`
      - 已有项目: 进入项目目录, 执行 `uv init`
    - 新建虚拟环境: `uv venv`
      - 创建指定版本的虚拟环境: `uv venv --python 3.12`
    - 进入虚拟环境
      - win: `.\.venv\Scripts\Activate.ps1`
      - mac: `source .venv/bin/activate`
    - 安装依赖: `uv add [依赖名]`

- pyenv

## 基础操作

- 进行命令行 `python3`
- 退出命令行 `exit()`
- 执行 python 文件 `python3 [文件名]`

## pyenv 版本管理工具(mac)

```sh
# 安装Pyenv（如果尚未安装）
brew install pyenv

# 在shell配置文件中初始化Pyenv（如~/.zshrc或~/.bash_profile）
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
source ~/.zshrc

# 在shell配置文件中初始化Pyenv（如~/.zshrc或~/.bash_profile）
pyenv install 3.9.18


# 全局或局部设置Python版本为3.9.18
pyenv global 3.9.18

# 或者在项目目录下设置
pyenv local 3.9.18

# 确保node-gyp使用这个Python版本
npm config set python /Users/wumo/.pyenv/versions/3.9.18/bin/python
```
