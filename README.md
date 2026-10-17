# 💃 舞蹈视频教学平台 (Dance Video Teaching Platform)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![PyQt5](https://img.shields.io/badge/GUI-PyQt5-green)
![MySQL](https://img.shields.io/badge/Database-MySQL-orange)

一个基于 Python + PyQt5 开发的桌面端舞蹈教学管理平台。本项目由经典的“名片管理系统”升级扩展而来，集成了学员管理、课程管理、视频教学、学习追踪和作业提交批改等核心功能，旨在帮助舞蹈培训机构实现数字化、信息化的教学管理。

## 📸 界面预览
![学员管理界面](business_card/docs/images/main.png)
![视频管理界面](business_card/docs/images/video_manage.png)
![作业评分界面](business_card/docs/images/grading.png)


## ✨ 功能特性

*   📋 **学员管理**：支持学员信息的增删改查（姓名、昵称、手机号、微信号、舞龄等级、擅长舞种）。
*   📚 **课程管理**：支持课程信息的增删改查（舞种、难度、价格、授课老师、简介），删除课程时支持级联删除关联视频。
*   🎬 **视频管理**：按课程分类筛选视频，支持本地视频播放与网络链接跳转，一键记录学员观看进度。
*   📊 **学习记录**：追踪指定学员的观看记录，展示已观看时长、完成状态及观看次数。
*   📝 **作业管理**：学员可提交本地视频作业，系统自动重命名防冲突；教师可在线预览、打分（0-10分）并进行文字点评。

## 🛠️ 技术栈

*   **开发语言**：Python 3.8+ (推荐 3.11)
*   **GUI 框架**：PyQt5 (界面高度定制化，暗黑主题)
*   **数据库**：MySQL 8.0+
*   **数据处理与 ORM**：pandas, SQLAlchemy
*   **数据库驱动**：PyMySQL
*   **内置模块**：shutil (文件操作), webbrowser (网页跳转), datetime (时间处理), os (路径管理)

## 🚀 快速开始

### 前置要求

- Python 3.8+（推荐 3.11）
- MySQL 8.0+ 已安装并启动
- Git

### 1. 克隆项目

```bash
git clone https://github.com/你的用户名/仓库名.git
cd 仓库名/business_card

```


> 注意：主程序代码位于 business_card/ 目录下，后续所有终端操作（除导入 SQL 外）都必须先进入该目录后再执行。

### 2. 创建虚拟环境并安装依赖

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

> 💡 若下载缓慢（如国内网络），可改用镜像源：
> ```bash
> pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
> ```

### 3. 初始化数据库

推荐使用图形化工具（如 Navicat）进行导入，操作更直观：

1. 打开 Navicat，连接到你的本地 MySQL。
2. 右键点击你的连接，选择“新建数据库”：
   - 数据库名填写：`business_card`
   - 字符集选择：`utf8mb4`
   - 排序规则选择：`utf8mb4_0900_ai_ci` (或默认)
3. 双击打开新建的 `business_card` 数据库。
4. **关键步骤**：右键点击该数据库（或空白处），选择 **“运行 SQL 文件...”**。
5. 在弹出的窗口中，找到项目根目录下的 `business_card.sql` 文件并选中，点击“开始”即可完成建表和测试数据的导入。
> 💡 如果你更习惯命令行，也可以使用下面的方式。注意命令行不会自动建库，需要先创建数据库，并且需要在项目根目录执行（若当前在 business_card/ 内，先 cd .. 回到上一级）：

```bash
mysql -u root -p -e "CREATE DATABASE business_card CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;"
mysql -u root -p business_card < business_card.sql
```

### 4. 配置数据库连接

复制配置模板并填入你自己的数据库信息：

```bash
# Windows
copy config.example.py config.py

# macOS / Linux
cp config.example.py config.py
```
(注：此步骤必须在 business_card 目录下执行)

编辑生成的 config.py，修改 host、user、password、database 等字段，使其与你本地 MySQL 一致。

config.py 含有明文密码，已被 .gitignore 忽略，不要提交到仓库。

### 5. 运行程序
确保当前所在目录是 business_card，执行：

```bash
python dance_app.py
```

### 常见问题

- **`ModuleNotFoundError: No module named 'PyQt5'`**：虚拟环境未激活，或依赖未安装，回到第 2 步。
- **连接数据库失败**：检查 MySQL 服务是否启动、`config.py` 中的账号密码和库名是否正确、`business_card.sql` 是否已导入。
- **PowerShell 下执行 `venv\Scripts\activate` 报“禁止运行脚本”**：这是 PowerShell 的执行策略限制，可执行 `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` 后重开终端，或改用 CMD 执行 `venv\Scripts\activate.bat`。
- **视频无法播放**：本地播放依赖系统解码器，网络视频依赖默认浏览器，请确认链接有效。

## 📁 项目结构

```text
舞蹈视频教学平台/ (项目根目录)
├── business_card/            # 核心代码目录 (运行程序需进入此目录)
│   ├── docs/                 # README 用到的界面截图
│   ├── res/                  # 静态资源文件夹 (datafile, img, ui)
│   ├── config.example.py     # 数据库配置模板
│   ├── dance_app.py          # 主程序入口 (包含所有界面与业务逻辑)
│   └── requirements.txt      # Python 依赖清单
├── .gitignore                # Git 忽略配置（保护密码、忽略视频和缓存）
├── business_card.sql         # MySQL 数据库备份文件
└── README.md                 # 项目说明文档

# 说明：以下文件/文件夹由安装或运行过程生成，已被 .gitignore 忽略
# business_card/
# ├── config.py               # 真实数据库配置（含密码，严禁上传）
# ├── assignments_videos/     # 学员提交的作业视频
# └── venv/                   # Python 虚拟环境