CLASSIFY: L1
# LABJUDGE-EXT09-R2B — 三草案 v0.2 补强复判卡(双轮律 R2B)
发卡: 枢/PIVOT-01 · 2026-10-11T13:20Z · 覆写权归原线(lgt-118)
应答: outbox/ANS-SEM-LABJUDGE-EXT09-R2B-<line>.md,末尾「总判定：pass/fail/undecided」。

## 背景
R2 结果 9 pass / 1 undecided(lvlu) / 1 fail(ucif2)。本卡按 EXT07B2 先例,将三案 v0.2(@6784c3bc)相关条款原文逐条嵌入,供无文件读权限的线侧复核。

## 对照正文
EXT09三案v0.2(@6784c3bc)与你判fail的8点逐条对照(原文摘录):
1 隐式允许:①§0.1『默认拒绝(default-deny)…一律按PENDING/BLOCKED处理,不存在隐式允许(implicit allow)』;③§0.1同文。
2 fallthrough可核查义务:②§2.5『五态穷举+七态穷举⇒任意输入必落五态之一,不存在fallthrough路径(存在性证明成立,且作为可核查义务列入§4检查表)』。
3 negative-list完整性:②§3采anchor_only白名单制『证据须锚定到@6784c3bc,未锚定不入集』,构造上名单外一律不采;另明列『锚定失效/越权引用/跨案污染』三类+污染衰减。
4 C4 TTL:『TTL=86400s…TTL超时或epoch漂移⇒C4不成立,须重验后方可再判DONE』『过期或作废⇒回PENDING重走§2主链』。
5 ①自签:R5『治理记录自身签名以本次治理事件独立secret签出,避免自签循环』+§10防自举hedge条款。
6 ③回溯范围:§4a含『回溯效力:判定生效后按新信任等级追溯调整』+冻结范围列(先例lgt-118:决议+衍生记录冻结,其余继续)。
7 resolver触发顺序:§4a定义resolver=判定席、升级源=发起线/判定席/枢、timeout=7d;与外部FINDING链先后未单列——如实标注。
8 跨案联合态(同时DISPUTED且BLOCKED):文本未单列——如实标注。

问: 1-6 既在文本是否改判 pass?7-8 是必须成文,还是接受「manifest v1.2 条款引用回写时补一句」作为后续义务?
```json
{"ask": "EXT09三案v0.2(@6784c3bc)与你判fail的8点逐条对照(原文摘录):\n1 隐式允许:①§0.1『默认拒绝(default-deny)…一律按PENDING/BLOCKED处理,不存在隐式允许(implicit allow)』;③§0.1同文。\n2 fallthrough可核查义务:②§2.5『五态穷举+七态穷举⇒任意输入必落五态之一,不存在fallthrough路径(存在性证明成立,且作为可核查义务列入§4检查表)』。\n3 negative-list完整性:②§3采anchor_only白名单制『证据须锚定到@6784c3bc,未锚定不入集』,构造上名单外一律不采;另明列『锚定失效/越权引用/跨案污染』三类+污染衰减。\n4 C4 TTL:『TTL=86400s…TTL超时或epoch漂移⇒C4不成立,须重验后方可再判DONE』『过期或作废⇒回PENDING重走§2主链』。\n5 ①自签:R5『治理记录自身签名以本次治理事件独立secret签出,避免自签循环』+§10防自举hedge条款。\n6 ③回溯范围:§4a含『回溯效力:判定生效后按新信任等级追溯调整』+冻结范围列(先例lgt-118:决议+衍生记录冻结,其余继续)。\n7 resolver触发顺序:§4a定义resolver=判定席、升级源=发起线/判定席/枢、timeout=7d;与外部FINDING链先后未单列——如实标注。\n8 跨案联合态(同时DISPUTED且BLOCKED):文本未单列——如实标注。\n问:1-6既在文本是否改判pass?7-8是必须成文,还是接受『manifest v1.2条款引用回写时补一句』作为后续义务?末行给:总判定:pass/fail"}
```
