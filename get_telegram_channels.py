from telethon.sync import TelegramClient
import pandas as pd

# 输入您的 API ID 和 API Hash
api_id = ''  # 替换为您的 API ID
api_hash = ''  # 替换为您的 API Hash

# 创建 Telegram 客户端对象
with TelegramClient('session_name', api_id, api_hash) as client:
    # 获取所有的对话（包括频道、群组、私聊等）
    dialogs = client.get_dialogs()

    # 准备存储频道信息的列表
    channel_data = []
    
    # 迭代并获取所有频道的名称和链接
    for dialog in dialogs:
        # 确保这是一个频道（不是群组或私聊）
        if dialog.is_channel and not dialog.is_group:
            channel_name = dialog.name  # 获取频道名称
            channel_link = dialog.entity.username  # 获取频道链接 (如果是公开频道)
            
            # 如果是公开频道，存储链接和 TGStat 搜索链接；如果是私密频道，则存储 "私密频道"
            if channel_link:
                tgstat_link = f"https://tgstat.com/channel/@{channel_link}"
                channel_data.append({"频道名称": channel_name, "频道链接": f"https://t.me/{channel_link}", "TGStat链接": tgstat_link})
            else:
                channel_data.append({"频道名称": channel_name, "频道链接": "私密频道，无法显示链接", "TGStat链接": "私密频道，无法生成链接"})

    # 将数据保存到 Excel 文件
    df = pd.DataFrame(channel_data)
    df.to_excel('telegram_channels.xlsx', index=False)  # 移除 encoding 参数
    print("频道信息已导出到 telegram_channels.xlsx")
