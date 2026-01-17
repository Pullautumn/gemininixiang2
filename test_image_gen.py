"""
测试图片生成功能
"""
import json
import os

# 加载配置
with open("config_data.json", "r", encoding="utf-8") as f:
    config = json.load(f)

print("=" * 60)
print("图片生成测试")
print("=" * 60)

from client import GeminiClient

cookies = config.get("FULL_COOKIE", f"__Secure-1PSID={config['SECURE_1PSID']}")

print("\n正在创建客户端...")
client = GeminiClient(
    secure_1psid=config["SECURE_1PSID"],
    snlm0e=config["SNLM0E"],
    cookies_str=cookies,
    push_id=config.get("PUSH_ID"),
    debug=True,  # 开启调试查看详细信息
    media_base_url="http://localhost:23456",  # 本地媒体 URL
)
print("客户端创建成功!")

print("\n" + "=" * 60)
print("发送图片生成请求: 穿着钢铁侠战甲的马斯克")
print("=" * 60)

prompt = "请生成一张图片：一只可爱的橘猫在阳光下打盹"

response = client.chat(message=prompt)
print(f"\n用户: {prompt}")
print(f"\nGemini 响应:\n{response.choices[0].message.content}")

print("\n" + "=" * 60)
print("测试完成")
print("=" * 60)

# 检查是否有生成的图片
media_cache = os.path.join(os.path.dirname(__file__), "media_cache")
if os.path.exists(media_cache):
    files = os.listdir(media_cache)
    if files:
        print(f"\n生成的媒体文件 ({len(files)} 个):")
        for f in files[-5:]:  # 显示最近5个
            print(f"  - {f}")
