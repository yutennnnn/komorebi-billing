import csv
import math
import sys
from collections import defaultdict
from datetime import datetime

# 30分あたりの料金（円）
RATES = {"小会議室A": 600, "中会議室B": 1000, "セミナールームC": 1800}
UNIT_MINUTES = 30
MEMBER_DISCOUNT_PERCENT = 10


def used_minutes(start, end):
    fmt = "%H:%M"
    delta = datetime.strptime(end, fmt) - datetime.strptime(start, fmt)
    return int(delta.total_seconds() // 60)


def calc_fee(room, minutes, member_type="visitor"):
    # 30分単位で切り上げる（例: 70分 → 3コマ）。Issue #1の修正
    units = math.ceil(minutes / UNIT_MINUTES)
    fee = RATES[room] * units
    # 月額会員は各予約の料金を10%引きにする。Issue #2の追加
    if member_type == "member":
        fee = fee * (100 - MEMBER_DISCOUNT_PERCENT) // 100
    return fee


def summarize(csv_path):
    totals = defaultdict(int)
    with open(csv_path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            minutes = used_minutes(row["start"], row["end"])
            totals[row["customer"]] += calc_fee(
                row["room"], minutes, row["member_type"]
            )
    return dict(totals)


def main():
    csv_path = sys.argv[1] if len(sys.argv) > 1 else "reservations_202609.csv"
    totals = summarize(csv_path)
    print("こもれび会議室 2026年9月 請求一覧")
    for customer, amount in sorted(totals.items(), key=lambda x: -x[1]):
        print(f"  {customer}: {amount:,}円")
    print(f"合計: {sum(totals.values()):,}円")


if __name__ == "__main__":
    main()
