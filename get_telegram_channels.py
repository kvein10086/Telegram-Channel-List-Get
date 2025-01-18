from telethon.sync import TelegramClient

# 输入您的 API ID 和 API Hash
api_id = '25624480'  # 替换为您的 API ID
api_hash = 'Ya2a415b7412da6a62e9f01273aadc36a'  # 替换为您的 API Hash

# 创建 Telegram 客户端对象
with TelegramClient('session_name', api_id, api_hash) as client:
    # 获取所有的对话（包括频道、群组、私聊等）
    dialogs = client.get_dialogs()
    
    # 遍历并打印所有频道的名称和链接
    for dialog in dialogs:
        # 确保这是一个频道（不是群组或私聊）
        if dialog.is_channel and not dialog.is_group:
            channel_name = dialog.name  # 获取频道名称
            channel_link = dialog.entity.username  # 获取频道链接 (如果是公开频道)
            
            # 如果是公开频道，打印链接；如果是私密频道，则打印 ID
            if channel_link:
                print(f"频道名称: {channel_name}, 频道链接: https://t.me/{channel_link}")
            else:
                print(f"频道名称: {channel_name}, 频道链接: 私密频道，无法显示链接")
