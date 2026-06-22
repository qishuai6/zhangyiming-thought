#!/usr/bin/env python3
import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


THEMES = {
    "求真与独立思考": [
        "真问题",
        "求证",
        "独立思考",
        "真实",
        "客套",
        "尊重科学",
        "不绕弯",
        "不侥幸",
        "不鸵鸟",
    ],
    "用户价值与产品完成度": [
        "用户",
        "体验",
        "产品",
        "反馈",
        "做好了",
        "信噪比",
        "效果",
    ],
    "延迟满足与长期主义": [
        "延迟满足",
        "耐心",
        "长期",
        "不装B",
        "惰性",
        "满足感",
    ],
    "速度质量执行": [
        "速度",
        "质量",
        "成本",
        "迭代",
        "bug",
        "效率",
        "节奏",
    ],
    "人才密度与挑战": [
        "优秀的人",
        "挑战",
        "学习能力",
        "兴趣",
        "不降级",
        "投机",
        "产品sense",
        "优秀",
    ],
    "组织与文化": [
        "组织",
        "管理",
        "文化",
        "有话直说",
        "虚伪的和谐",
        "mentor",
        "成果",
    ],
    "数据与平台": [
        "数据",
        "算法",
        "推荐",
        "平台",
        "分发",
        "信息",
    ],
}

NOISE_PATTERNS = [
    r"添加微信\s*\d*领取200个互联网创业项目",
    r"O 网页链接",
    r"抱歉，此微博已被作者删除。查看帮助：",
    r"抱歉，作者已设置仅展示半年内微博，此微博已不可见。",
]


def clean_text(text: str) -> str:
    text = text.replace("\f", "\n")
    for pattern in NOISE_PATTERNS:
        text = re.sub(pattern, "", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


def split_posts(text: str):
    lines = text.splitlines()
    posts = []
    i = 0
    while i < len(lines):
        if lines[i].strip() == "张一鸣" and i + 1 < len(lines) and re.search(
            r"20\d{2}-\d{1,2}-\d{1,2}", lines[i + 1]
        ):
            header = lines[i + 1].strip()
            match = re.search(r"(20\d{2}-\d{1,2}-\d{1,2})\s+(\d{1,2}:\d{2})", header)
            j = i + 2
            body = []
            while j < len(lines):
                current = lines[j].strip()
                if current == "张一鸣" and j + 1 < len(lines) and re.search(
                    r"20\d{2}-\d{1,2}-\d{1,2}", lines[j + 1]
                ):
                    break
                if current and not current.isdigit():
                    body.append(current)
                j += 1
            content = re.sub(r"\s+", " ", " ".join(body)).strip()
            posts.append(
                {
                    "date": match.group(1) if match else "",
                    "time": match.group(2) if match else "",
                    "content": content,
                }
            )
            i = j
        else:
            i += 1
    return posts


def build_report(posts):
    years = Counter(p["date"].split("-")[0] for p in posts if p["date"])
    theme_hits = defaultdict(list)

    for post in posts:
        content = post["content"]
        for theme, keywords in THEMES.items():
            score = sum(1 for keyword in keywords if keyword in content)
            if score:
                theme_hits[theme].append((score, len(content), post["date"], content))

    lines = []
    lines.append("# 张一鸣思想信号报告")
    lines.append("")
    lines.append("## 语料统计")
    lines.append("")
    lines.append(f"- post_count: {len(posts)}")
    if posts:
        avg_length = round(sum(len(p["content"]) for p in posts) / len(posts))
        lines.append(f"- avg_post_length: {avg_length}")
    lines.append("- year_distribution:")
    for year, count in sorted(years.items(), reverse=True):
        lines.append(f"  - {year}: {count}")

    lines.append("")
    lines.append("## 主题证据")
    lines.append("")
    for theme, keywords in THEMES.items():
        evidence = sorted(theme_hits.get(theme, []), key=lambda item: (-item[0], item[1], item[2]))
        lines.append(f"### {theme}")
        lines.append("")
        lines.append(f"- hit_count: {len(theme_hits.get(theme, []))}")
        for score, _, date, content in evidence[:6]:
            lines.append(f"- [{date}] score={score} {content[:160]}")
        lines.append("")

    lines.append("## 候选变化")
    lines.append("")
    for theme, keywords in THEMES.items():
        count = len(theme_hits.get(theme, []))
        if count >= 8:
            lines.append(f"- reinforce: `{theme}` has repeated evidence.")
        elif count == 0:
            lines.append(f"- inspect: `{theme}` has no direct keyword hit and may need manual review.")
        else:
            lines.append(f"- review: `{theme}` has light evidence and should not be overclaimed.")
    lines.append("")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Extract deterministic Zhang Yiming thought signals from a corpus.")
    parser.add_argument("input", help="Path to a plain text corpus")
    parser.add_argument("-o", "--output", help="Optional output markdown path")
    parser.add_argument("--dump-json", help="Optional path to dump parsed posts JSON")
    args = parser.parse_args()

    input_path = Path(args.input)
    text = clean_text(input_path.read_text(encoding="utf-8"))
    posts = split_posts(text)
    report = build_report(posts)

    if args.dump_json:
        Path(args.dump_json).write_text(
            json.dumps(posts, ensure_ascii=False, indent=2), encoding="utf-8"
        )

    if args.output:
        Path(args.output).write_text(report, encoding="utf-8")
    else:
        print(report)


if __name__ == "__main__":
    main()
