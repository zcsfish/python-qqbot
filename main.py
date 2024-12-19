#!/usr/bin/env python3
from qg_botsdk import BOT, ApiModel, Model, Proto
def deliver(data: Model.MESSAGE):
    bot.logger.info("检测到消息发送。")
    if "邀请" in data.treated_msg:
        # SDK版本 >= v2.4.0 可直接使用reply()
        bot.api.send_ark_24(channel_id=f"{data.channel_id}", title="邀请机器人加入频道", desc="邀请机器人加入你的私有频道，使用我们的功能。")
        bot.logger.info(f"发送消息到子频道{data.channel_id}")
    elif "菜单" in data.treated_msg:
        # 菜单项
        data.reply("菜单\n1.邀请机器人\n2.查看运行状态\n3.小游戏系统\n4.积分系统")
        bot.logger.info(f"在子频道{data.channel_id}中有人调用了菜单。")
if __name__ == "__main__":
    bot = BOT(bot_id="102567401", bot_token="yn85n2fTNZxSJGMgBD8EKrtGYEqjJT3Y", is_private=False, is_sandbox=False)
    bot.load_default_msg_logger()
    bot.bind_msg(deliver, treated_data=True)
    bot.start()
