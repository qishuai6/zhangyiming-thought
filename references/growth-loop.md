# 成长回路

当这个 skill 需要吸收新语料、但又不能漂移成“想象中的张一鸣”时，用这个文件。

## 目标

基于证据更新原则栈，而不是基于崇拜更新。

## 允许输入

- interviews
- speeches
- internal letters
- essays
- social posts
- transcripts
- secondary commentary only when the original source is unavailable

优先使用一手文本。

## 更新流程

1. Clean and normalize the corpus.
2. Run `scripts/extract_signals.py`.
3. Compare the new report against `references/principles.md`.
4. Classify changes:
   - `reinforcement`: more evidence for an existing principle
   - `refinement`: an existing principle needs sharper wording
   - `addition`: a truly new principle appears
   - `contradiction`: old interpretation may be wrong or too broad
5. Draft the smallest possible update.
6. Re-run validation after any skill edit.

## 证据门槛

至少满足下面一条，才允许改原则栈：

- three or more independent excerpts support the same new principle,
- a long-form source explains a principle more precisely than short posts did,
- repeated evidence contradicts a current principle framing.

下面这些理由都不够：

- one quote sounds cool,
- the wording is more viral,
- the tone feels more “like him,”
- a secondary article praises him in broad terms.

## 安全更新规则

- Prefer updating `references/principles.md` before editing `SKILL.md`.
- Keep `SKILL.md` stable unless the triggering conditions or workflow have clearly changed.
- Preserve old interpretations when the new evidence only narrows scope; revise wording instead of rewriting the whole model.
- Record corpus caveats when extraction quality is imperfect.

## 什么算是好的成长

好的成长会让这个 skill：

- more falsifiable,
- more operational,
- more stable across different tasks,
- less dependent on tone imitation.

坏的成长会让这个 skill：

- broader but fuzzier,
- more inspirational and less checkable,
- more attached to slogans than evidence.
