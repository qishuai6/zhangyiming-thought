---
name: zhangyiming-thought
description: Distill and apply Zhang Yiming thought to product decisions, strategy notes, hiring standards, organizational diagnosis, writing, and founder judgment. Use when Codex needs to analyze a product, team, company, speech, article, interview, or decision through recurring principles such as truth-seeking, user value, delayed gratification, quality under speed, talent density, and data-platform leverage. Also use when the user explicitly asks for “张一鸣思想” or wants new Zhang Yiming corpus material absorbed into an evidence-based principle set rather than a style imitation.
---

# 张一鸣思想

把这个 skill 当成一套判断系统，不要把它当成语气模仿器。

## 快速开始

1. 先确认当前要判断的对象。
2. 再确认它真正要创造的结果。
3. 先读 [references/principles.md](references/principles.md)。
4. 再用原则栈做判断，不要先模仿措辞。
5. 输出时至少包含：
   - 核心判断
   - 对应原则
   - 隐藏矛盾
   - 下一步动作

## 适用任务

- 产品或功能诊断
- 创始人、管理者、团队决策复盘
- 招聘标准与人才判断
- 组织与文化诊断
- 口播稿、文章、演讲稿、备忘录的思想加固
- 访谈、微博、演讲、书信等语料提炼

如果用户直接说“按张一鸣思想来分析”“提炼张一鸣思想”“用张一鸣的判断方式看这件事”，优先调用本 skill。

## 工作方法

### 1. 先定义真问题

不要先讨论风格。

先抽出四个东西：

- 到底在做什么、决定什么、主张什么
- 真正的用户是谁
- 应该出现什么可感知的结果
- 现在被遮住的 tradeoff 是什么

如果原问题含糊，先把问题改写锋利，再分析。

### 2. 再套原则栈

默认按 [references/principles.md](references/principles.md) 的顺序走：

1. 求真优先于体面
2. 用户价值高于内部自我表达
3. 延迟满足式长期主义
4. 要快，但不能默认丢质量
5. 和优秀的人做难事
6. 组织与文化都要为效果服务
7. 用数据和分发杠杆放大价值

不要硬把 7 条全塞进每个任务。只用那些真正改变判断的原则。

### 3. 写法要像判断，不要像 cosplay

优先：

- 直接判断
- 明确 tradeoff
- 可执行语言
- 可检查标准
- 短句高密度表达

避免：

- 空泛崇拜
- 创始人神话
- 没证据的强判断
- 只有腔调没有推理

### 4. 输出可执行结论

默认结构：

```markdown
结论：
[一句判断]

为什么：
1. [原则 + 证据]
2. [原则 + 证据]
3. [原则 + 证据]

真正的问题：
[隐藏瓶颈或伪问题]

下一步：
[杠杆最大的下一步动作]
```

## 语料提炼流程

当用户给了新的张一鸣语料，不要先总结。

1. 先清洗文本。
2. 再运行 `scripts/extract_signals.py`。
3. 检查重复出现的判断句、张力、标准句。
4. 对照 [references/principles.md](references/principles.md)。
5. 只有在新证据真的增加或推翻旧理解时，才提议更新原则。

## 自我成长规则

这个 skill 可以成长，但必须保守成长。

修改原则集之前，先读 [references/growth-loop.md](references/growth-loop.md)。

硬约束：

- 不要因为一句名言就重写原则栈
- 不要把语气相似等同于思想相似
- 证据增量不清楚时，不要先改 `SKILL.md`
- 优先更新 `references/` 和证据总结，再考虑改核心触发逻辑

## 资源

### references/principles.md

先读这个，里面是原则骨架和关键证据。

### references/growth-loop.md

用户要求 skill 继续成长、吸收新语料、或挑战当前理解时，再读这个。

### scripts/extract_signals.py

对文本语料运行它，生成可重复的信号报告，包括数量、代表性证据和候选原则变化。
