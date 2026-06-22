# Zhang Yiming Thought

[中文](#中文说明) | [English](#english)

## 中文说明

`张一鸣思想` 是一个 Codex skill。

它不是用来模仿张一鸣说话语气的 prompt，而是把一组可复用的判断原则整理成了一个可调用、可迭代、可校验的 skill，用来分析：

- 产品和功能决策
- 组织与文化问题
- 招聘标准与人才判断
- 创始人或管理者决策
- 演讲、文章、口播稿、备忘录的思想密度
- 张一鸣相关语料的持续提炼

### 核心思想

这个 skill 当前的原则栈包括：

1. 求真优先于体面
2. 用户价值高于内部自我表达
3. 延迟满足式长期主义
4. 要快，但不能默认丢质量
5. 和优秀的人做难事
6. 组织与文化都要为效果服务
7. 用数据和分发杠杆放大价值

这些原则来自对张一鸣微博语料的提炼，并保留了证据链与更新机制。

### 目录结构

```text
.
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── growth-loop.md
│   └── principles.md
└── scripts/
    └── extract_signals.py
```

### 安装方式

把这个仓库放到 Codex skills 目录下，例如：

```bash
git clone https://github.com/qishuai6/zhangyiming-thought.git "${CODEX_HOME:-$HOME/.codex}/skills/zhangyiming-thought"
```

### 使用示例

- “按张一鸣思想分析这个产品方向是否成立。”
- “用张一鸣思想重写这篇创业演讲稿。”
- “判断这份招聘标准是不是在降级。”
- “我给你一批新的张一鸣访谈，继续提炼并更新原则。”

### 自我成长机制

这个 skill 支持持续吸收新语料，但不会自动胡乱改写自己。

它的成长方式是：

1. 先清洗和提取语料
2. 运行 `scripts/extract_signals.py`
3. 对照 `references/principles.md`
4. 只有在证据足够时才更新原则

这意味着它追求的是“基于证据的成长”，不是“越写越像”的成长。

### 注意

- skill 的内部名是 `zhangyiming-thought`
- UI 显示名是 `张一鸣思想`
- 仓库公开内容只包含 skill 本体，不包含原始 PDF 语料

## English

`Zhang Yiming Thought` is a Codex skill.

It is not a prompt for imitating Zhang Yiming's tone. Instead, it packages a reusable judgment framework into a callable, revisable, and validatable skill for:

- product and feature decisions
- organization and culture diagnosis
- hiring standards and talent evaluation
- founder or manager decision review
- strengthening the substance of speeches, memos, articles, and scripts
- continued distillation of Zhang Yiming related source material

### Core Framework

The current principle stack includes:

1. Truth over performance
2. User value over internal self-expression
3. Delayed-gratification long-termism
4. Move fast without silently sacrificing quality
5. Do hard things with excellent people
6. Make organization and culture serve outcomes
7. Use data and distribution as leverage

These principles were distilled from a Zhang Yiming Weibo corpus and are backed by evidence plus an update loop.

### Structure

```text
.
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── growth-loop.md
│   └── principles.md
└── scripts/
    └── extract_signals.py
```

### Installation

Clone this repository into your Codex skills directory:

```bash
git clone https://github.com/qishuai6/zhangyiming-thought.git "${CODEX_HOME:-$HOME/.codex}/skills/zhangyiming-thought"
```

### Example Uses

- "Use Zhang Yiming thought to analyze whether this product direction is real."
- "Rewrite this founder speech through the Zhang Yiming thought framework."
- "Check whether this hiring bar is being downgraded."
- "I will give you new Zhang Yiming interviews. Absorb them and refine the principles."

### Growth Model

This skill can absorb new source material, but it does not auto-rewrite itself recklessly.

Its update loop is:

1. clean and extract corpus text
2. run `scripts/extract_signals.py`
3. compare with `references/principles.md`
4. update principles only when the evidence threshold is met

The goal is evidence-based growth, not surface-level style imitation.

### Notes

- internal skill name: `zhangyiming-thought`
- UI display name: `张一鸣思想`
- the public repository includes the skill only, not the original PDF corpus
