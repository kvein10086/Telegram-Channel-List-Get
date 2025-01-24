# Telegram 频道提取

该 Python 脚本允许您提取并保存您加入的 Telegram 频道的信息，并将其保存为 Excel 文件。脚本使用 Telethon 库访问您的 Telegram 帐号，并获取有关频道的详细数据，包括频道名称和链接。

## 功能

- 获取所有对话（包括频道、群组和私聊）。
- 过滤并提取仅包含频道的信息。
- 对于每个公开频道，提取以下信息：
  - 频道名称
  - 频道链接
  - TGStat 链接（提供进一步的统计分析）
- 对于私密频道，保存提示信息，表明该频道为私密频道且无法显示链接。
- 将提取的数据保存到 Excel 文件 (`telegram_channels.xlsx`) 中。

## 前提条件

在运行脚本之前，您需要设置以下内容：

1. **安装所需的库**： 该脚本依赖 `telethon` 和 `pandas` 库。如果未安装，请使用 pip 安装：

   ```bash
   pip install telethon pandas
   ```

2. **Telegram API 设置**： 您需要从 Telegram 获取自己的 `API ID` 和 `API Hash`。步骤如下：

   - 访问 https://my.telegram.org/auth。
   - 使用您的 Telegram 帐号登录。
   - 点击 **API 开发工具**，创建一个新的应用程序。
   - 记录下您的 `API ID` 和 `API Hash`。

## 使用方法

1. **下载脚本**

   您可以通过以下链接下载最新版本的脚本：

   [Telegram Channel Extractor Script](https://raw.githubusercontent.com/kvein10086/Telegram-Channel-List-Get/master/get_telegram_channels.py)

2. **配置 API 凭证**

   在脚本中找到以下部分，并替换为您从 Telegram 获取的 API ID 和 API Hash：

   ```python
   api_id = ''  # 替换为您的 API ID
   api_hash = ''  # 替换为您的 API Hash
   ```

3. **运行脚本**

   将修改后的脚本保存在本地，打开终端或命令提示符，导航到脚本所在的目录，并运行以下命令：

   ```bash
   python get_telegram_channels.py
   ```

4. **查看输出文件**

   脚本运行完毕后，提取的频道信息将保存到一个名为 `telegram_channels.xlsx` 的 Excel 文件中。此文件将包含以下列：

   - **频道名称**: 频道的名称。
   - **频道链接**: 频道的链接，如果是私密频道，则显示 "私密频道，无法显示链接"。
   - **TGStat链接**: 该频道的 TGStat 链接，如果是私密频道，则显示 "私密频道，无法生成链接"。

   输出文件示例如下：

   | 频道名称   | 频道链接               | TGStat链接                          |
   | ---------- | ---------------------- | ----------------------------------- |
   | 示例频道 1 | https://t.me/example   | https://tgstat.com/channel/@example |
   | 示例频道 2 | 私密频道，无法显示链接 | 私密频道，无法生成链接              |

## 许可证

本项目使用 MIT 许可证。

## 致谢

该脚本由 ChatGPT（OpenAI）编写。