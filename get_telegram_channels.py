from telethon.sync import TelegramClient

# 输入您的 API ID 和 API Hash
api_id = '25624480'  # 替换为您的 API ID
api_hash = 'a2a415b7412da6a62e9f01273aadc36a'  # 替换为您的 API Hash

# 创建 Telegram 客户端对象
with TelegramClient('session_name', api_id, api_hash) as client:
    # 获取所有的对话（包括频道、群组、私聊等）
    dialogs = client.get_dialogs()
    
    # 遍历并打印所有频道的名称
    for dialog in dialogs:
        if dialog.is_channel:
            print(dialog.name)  # 打印频道名称
