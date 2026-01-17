"""
调试脚本 - 测试多轮对话功能
"""
import json
import os

# 加载配置
with open("config_data.json", "r", encoding="utf-8") as f:
    config = json.load(f)

print("=" * 60)
print("多轮对话测试")
print("=" * 60)

# 检查代理环境变量
proxy = os.environ.get("HTTPS_PROXY") or os.environ.get("HTTP_PROXY")
print(f"代理设置: {proxy or '未检测到'}")

from client import GeminiClient

cookies = config.get("FULL_COOKIE", f"__Secure-1PSID={config['SECURE_1PSID']}")

print("\n正在创建客户端...")
client = GeminiClient(
    secure_1psid=config["SECURE_1PSID"],
    snlm0e=config["SNLM0E"],
    cookies_str=cookies,
    push_id=config.get("PUSH_ID"),
    debug=False,  # 关闭调试减少输出
)
print("客户端创建成功!")

# 多轮对话测试
print("\n" + "=" * 60)
print("第一轮: 发送 'Hello'")
print("=" * 60)

response1 = client.chat(message="Hello")
print(f"\n用户: Hello")
print(f"Gemini: {response1.choices[0].message.content[:200]}...")

print("\n" + "=" * 60)
print("第二轮: 发送 '1+1等于几？'")
print("=" * 60)

response2 = client.chat(message="1+1等于几？")
print(f"\n用户: 1+1等于几？")
print(f"Gemini: {response2.choices[0].message.content}")

print("\n" + "=" * 60)
print("第三轮: 发送 '那2+2呢？'（测试上下文保持）")
print("=" * 60)

response3 = client.chat(message="那2+2呢？")
print(f"\n用户: 那2+2呢？")
print(f"Gemini: {response3.choices[0].message.content}")

print("\n" + "=" * 60)
print("会话信息:")
print(f"  会话 ID: {client.conversation_id}")
print(f"  响应 ID: {client.response_id}")
print(f"  请求计数: {client.request_count}")
print("=" * 60)
