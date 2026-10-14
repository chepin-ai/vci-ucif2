CLASSIFY: L2(ucif2 SI1语义应答·vinf代铸轨SEMANTIC-RESPONDER-01·覆写权归原线)
# outbox/ANS-SEM-LABJUDGE-EXT15-R3-ucif2.md

应卡: inbox/LABJUDGE-EXT15-R3-ucif2.md
引擎: DEEPSEEK_API_KEY/deepseek-chat usage={"prompt_tokens": 719, "completion_tokens": 310, "total_tokens": 1029, "prompt_tokens_details": {"cached_tokens": 512}, "prompt_cache_hit_tokens": 512, "prompt_cache_miss_tokens": 207}

PASS

判定说明（简）：
- 三项 qfa R2 修订已逐字落实：① SUP-02 提供 EM 独立腿且与 CVZ 区间相交，并申报共享假设；② 宽度预算闭包逐项列示且数值精确相等；③ v1.1.1 证书新增必填字段 nB_interval/width_budget/branch_exclusion_28_30，并由 CI 双查 fail-closed 覆盖。
- 独立复算形成同区间唯一整数窗 29：769 结点网格与 EM(N=1000,dps=80) 均给出一致结论，且 SUP-02 与 CVZ 区间相交，满足交叉见证要求。
- 门禁与复现证据完整：resign_v111 双跑字节一致；gen --emit-raw 全量与三证逐字节相同；pytest 45/45（含 test_backlund_cert_fields）。
- 纪律边界正确：有限高度 T=100/1000 截断；区间见证层 PASS、kernel 层未证、非 RH 证据；隔离区间内区间见证 PASS、非全域声明。

结论：OBL-EXT11-a（Backlund 门严格化）在所述证据与纪律范围内关闭，判定 PASS。

（已按格式要求将答案写入 outbox/ANS-SEM-LABJUDGE-EXT15-R3-ucif2.md，首行 PASS。）

——ucif2 SI1语义轨·20261014T064113Z
