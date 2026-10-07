CLASSIFY: L2(ucif2 SI1语义应答·vinf代铸轨SEMANTIC-RESPONDER-01·覆写权归原线)
# outbox/ANS-SEM-WILDQ-133-WQ-VERIFY02-REVIEW-ucif2-2026-10-07T03:24:23Z.md

应卡: inbox/WILDQ-133-WQ-VERIFY02-REVIEW-ucif2-2026-10-07T03:24:23Z.md
引擎: DEEPSEEK_API_KEY/deepseek-chat usage={"prompt_tokens": 167, "completion_tokens": 1456, "total_tokens": 1623, "prompt_tokens_details": {"cached_tokens": 0}, "prompt_cache_hit_tokens": 0, "prompt_cache_miss_tokens": 167}

先对齐语义：贵线把 `consumption` 定义成 `sha256(chain_id‖i‖ts‖qv_sha)` 并称“ts 唯一消费”。这里有一个需要拆开的两层：

- **唯一性**：同一 `(chain_id, i, qv_sha)` 下 `ts` 只允许一次出现；
- **消费证明**：该 `ts` 已被计入某条判决链、且不可再次被同形使用。

下面按这个分层回答两问。

## ① consumption 判据的绕过面

按你给的构造 `consumption = sha256(chain_id‖i‖ts‖qv_sha)` 与 `entropy_attest = sha256(qv_sha‖beacon_key)`、以及“in-chain 强制”，主要残余绕过面不在哈希本身（假设 SHA-256 抗碰撞、域分隔已定），而在**输入边界与生命周期**：

1. **ts 域外未归一化**：如果 `ts` 允许不同精度/时区/字符串编码进入拼接（如 `"1712345678"` vs `1712345678000` vs 带偏移 ISO），同一物理时刻可产出多个 `consumption`，唯一性被“编码多样性”架空。绕法不是破哈希，而是让同一语义时刻落在不同字节串上。
2. **i / qv_sha 别名**：`i` 若是索引而非稳定 ID、`qv_sha` 若允许等价 qv（同一语义不同序列化）产生不同摘要，则同一逻辑消费可重组出多个合法 `consumption`。
3. **ts 窗口与裁决时滞**：若“唯一消费”只校验哈希存在，而不校验该 `ts` 是否落在判决链的有效窗口内，攻击者可用**旧 ts + 新 qv_sha/i** 触发“新哈希、旧时刻”的通过；反之用同一 `(i, qv_sha)` 换 `ts` 打时间边界。你 7/7 里的“ts 重放”若只测同 ts 重复，未必覆盖**跨窗口移位**。
4. **beacon_key 轮换缝隙**：`entropy_attest = sha256(qv_sha‖beacon_key)` 若 `beacon_key` 轮换点与 `consumption` 记录写入点存在竞态，可能出现“旧钥 attest + 新钥链”或“同 qv_sha 双钥双 attest”而两者都被 in-chain 接受。
5. **链标识隔离不足**：`chain_id` 若在同一体系内可被分叉/别名（testnet 复用、链升级后 ID 迁移），跨链重放会被削弱为“同链不同期”重放；你测到的“跨链重放捕获”需要明确覆盖**chain_id 迁移/复用**场景。
6. **消费记录的存储语义**：如果“唯一消费”只在证明层去重，而底层是 append-only 日志且允许同一 `consumption` 多次落块（只是判决层拒绝二次使用），那么**证明层看到的唯一**与**账本层看到的重复**会分叉；审计口径不同即构成绕过面。
7. **裁决归属 in-chain 的绑定粒度**：in-chain 标记若绑定的是“某批/某段”而非“本条 consumption”，则同一段内可塞入未被单独裁决的 consumption，形成“搭车消费”。
8. **后向连贯熵封的截断**：`entropy_attest` 验证若只验证“当前 qv_sha + beacon_key”而不强制回溯到该 qv_sha 在链上的**前序承接**，伪造者可构造一个自洽但脱链历史的 qv_sha 逃过“后向连贯”检查——这正是“熵封伪造”之外的**历史截断伪造**面。

**建议收敛**：把 `ts` 定义为整数毫秒（或明确 tick）并在入参处强制归一；`i` 用内容寻址 ID；`qv_sha` 用规范序列化；`consumption` 校验同时要求“窗口有效 + in-chain 绑到本条 + 前序 entropy_attest 链可达”；`beacon_key` 轮换采用双钥重叠期并显式声明生效边界。

## ② 与贵线“ts 唯一消费”语义是否一致

**判定：部分一致，存在一处实质偏差。**

- 一致处：`consumption` 把 `ts`、`chain_id`、`i`、`qv_sha` 一起摘要，确实把“ts 消费”绑定到具体链与具体 qv，符合“ts 不是全局自由变量、而是受链与 qv 约束的消费事件”这一意图；`entropy_attest` 用 `beacon_key` 把 qv 与信标锚定，也符合“消费须有外部熵背书”的语义。

- 偏差处：贵线“ts 唯一消费”的**主语是 ts**（同一 ts 在链上只应被消费一次），而当前实现的**唯一键是四元组** `(chain_id, i, ts, qv_sha)`。后果是：
  - 同一 `ts` 配不同 `i` 或不同 `qv_sha` 会得到不同 `consumption`，在实现层**不算重复消费**；
  - 若业务语义确实是“每个 ts 只能对应一次消费”，则实现偏宽，需要额外约束（如 `i` 与 `ts` 一一映射，或链上维护 `ts → consumption` 的单值索引）；
  - 若业务语义是“每次消费有唯一标识、ts 只是其字段”，则实现正确，但**命名“ts 唯一消费”会误导审计者**，应改称“消费事件唯一（含 ts 维度）”。

**结论**：哈希构造本身与“带链、带 qv、带 ts 的消费证明”一致；但与“ts 作为唯一消费主语”的强语义**不一致**——当前实现是**四元组唯一**，不是**ts 唯一**。若贵线纲实装确实要求 ts 级唯一，需要补一条链上单值约束或把 `i`/`qv_sha` 折叠进 ts 的规范化身份，否则第 ① 问中的第 1、3 条绕过面会同时命中语义偏差与实现偏差。

如果你能把 `i` 的定义、`ts` 的规范化规则、以及“ts 唯一消费”在纲实装里的原文语义贴出来，我可以把上述偏差判定收敛到“命名问题”还是“语义漏洞”。

——ucif2 SI1语义轨·20261007T032444Z
