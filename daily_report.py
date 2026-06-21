#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
import os
from datetime import datetime

# ===== CẤU HÌNH =====
# Thay bằng API Key thật của anh
DEEPSEEK_API_KEY = "sk-..."           # API Key DeepSeek
OPENAI_API_KEY = "sk-proj-..."        # API Key ChatGPT

# ===== DỮ LIỆU MẪU =====
sample_data = """
DỰ ÁN PARC HÀ NỘI - DỮ LIỆU THỬ NGHIỆM (21/06/2026)

1. RFI:
- RFI #P-012: HVAC tầng 5, ngày gửi 10/06, chờ phản hồi (quá hạn 5 ngày)
- RFI #P-015: Ống nước tầng B1, ngày gửi 15/06, đã phản hồi, đang triển khai
- RFI #P-018: Điện tầng 3, ngày gửi 18/06, mới tạo

2. NCR:
- NCR #N-005: Ống nước tầng 2 - rò rỉ mối hàn, mức độ: Nghiêm trọng, đã xử lý xong
- NCR #N-007: Điều hòa tầng 4 - sai thông số, mức độ: Trung bình, đang xử lý
- NCR #N-009: Phòng cháy tầng 1 - sai vị trí đầu báo, mức độ: Nhẹ, đang kiểm tra

3. Tiến độ tuần 25/2026:
- HVAC: 65% (kế hoạch 75%) - chậm 10%
- Plumbing: 80% (kế hoạch 80%) - đúng tiến độ
- Electrical: 70% (kế hoạch 75%) - chậm 5%
- Fire: 60% (kế hoạch 65%) - chậm 5%

4. Dòng tiền tháng 6:
- Hợp đồng: 150 tỷ VND
- Giải ngân đến hết tháng 5: 90 tỷ
- Giải ngân dự kiến tháng 6: 15 tỷ
- Giải ngân thực tế đến 21/06: 8 tỷ (chậm 7 tỷ)
"""

def call_deepseek(text):
    url = "https://api.deepseek.com/chat/completions"
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": "Bạn là kỹ sư MEPF 20 năm kinh nghiệm, chuyên phân tích dữ liệu dự án."},
            {"role": "user", "content": f"Phân tích dữ liệu sau:\n\n{text}"}
        ],
        "stream": False
    }
    try:
        resp = requests.post(url, headers=headers, json=payload, timeout=60)
        resp.raise_for_status()
        return resp.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"[Lỗi DeepSeek] {str(e)}"

def call_chatgpt(analysis):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "gpt-4o",
        "messages": [
            {"role": "system", "content": "Bạn là trợ lý tổng hợp báo cáo dự án."},
            {"role": "user", "content": f"Tổng hợp báo cáo sau (1 trang A4, bullet point, tiếng Việt):\n\n{analysis}"}
        ],
        "max_tokens": 2000,
        "stream": False
    }
    try:
        resp = requests.post(url, headers=headers, json=payload, timeout=60)
        resp.raise_for_status()
        return resp.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"[Lỗi ChatGPT] {str(e)}"

def save_report(content):
    filename = f"report_{datetime.now().strftime('%Y%m%d')}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    return filename

def print_report(content):
    print("\n" + "="*60)
    print(f"BÁO CÁO PARC HÀ NỘI - {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    print("="*60)
    print(content)
    print("="*60 + "\n")

if __name__ == "__main__":
    print("🚀 Bắt đầu...")
    analysis = call_deepseek(sample_data)
    report = call_chatgpt(analysis)
    filename = save_report(report)
    print_report(report)
    print(f"✅ Đã lưu: {filename}")
