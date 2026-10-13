CLASSIFY: L2(ucif2 SI1语义应答·vinf代铸轨SEMANTIC-RESPONDER-01·覆写权归原线)
# outbox/ANS-SEM-EXT14-R2B-EV2-ucif2.md

应卡: inbox/EXT14-R2B-EV2-ucif2.md
引擎: DEEPSEEK_API_KEY/deepseek-chat usage={"prompt_tokens": 443, "completion_tokens": 1191, "total_tokens": 1634, "prompt_tokens_details": {"cached_tokens": 256}, "prompt_cache_hit_tokens": 256, "prompt_cache_miss_tokens": 187}

# EXT14-R2 证据包 2/3 判读（零改动 diff + 跨环境重放 + 运行原文）

## 一、字段级 diff：数学零改动成立

| 证书 | 数学字段 | 变化字段数 | 变化内容 |
|---|---|---|---|
| iso100 | **17/17 逐位同** | 3 | `/disclosure`、`/provenance/generator/sha256`、`/witness_sha256` |
| iso1000 | **16/16 逐位同** | 6 | +`completeness/status`、`blocked_subcode`、`retry_budget` |
| psi-trunc | **11/11 逐位同** | 4 | disclosure、zero_source/sha256、generator/sha256、witness_sha256 |

**合计 44 个数学字段零改动**。变化字段全部落在**元数据层**：
- `disclosure` / `completeness/status` / `blocked_subcode` / `retry_budget` → 声明与状态机字段，非计算产物。
- `*/sha256`（generator / witness / zero_source）→ **哈希链重签**，是版本切换的必然结果，不是数值漂移。

**判读**：版本跃迁 v1.0.0→v1.0.1 在**数值语义上为恒等映射**。这排除了"改代码顺手改数"的常见嫌疑——如果有人在数学路径上动了手，44 个字段里至少会有一个 bit 翻动。逐位相同是比"数值接近"强得多的证据。

## 二、跨环境重放：容器重置不影响数学输出

- envA = 重置前容器 #1；envB = 重置后容器 #2。
- 栈固定：python3.12.12 + mpmath1.3.0 + Linux5.10 lifsea / x86_64。
- **iso100 Backlund 拒证区间** N_B = [29.09812430226496, 29.09812430426496]，两环境**逐位相同**。
- **psi-trunc 残差** r ∈ [−3365.36, 3142.19] ⊂ Dudek 界 ±5195860.44，两环境**逐位相同**。

**判读**：容器重置（通常伴随文件系统、locale、哈希种子、内存布局扰动）后，浮点/区间结果逐位复现，说明：
1. 计算路径**未依赖**未固定的环境熵（PYTHONHASHSEED、时间、路径、线程调度）；
2. 区间端点不是"估出来"的，是**确定性算术**的产物；
3. mpmath 的精度配置在两次运行中一致（否则低位会漂）。

## 三、包A 核验（envB 实跑）

```
verify iso1000  → ok=true
verify trunc    → ok=true
verify iso100   → ok=false
  failed 唯一项 = Backlund 异常「N_B 区间不含唯一整数——拒证」
pytest 尾行「41 passed in 1497.81s (0:24:57)」
```

**判读**：`iso100 ok=false` **不是缺陷**，是 KI-EXT11-1 钉档的**拒证行为**——当 N_B 宽度小于 1 且不含整数时，程序拒绝给出整数回绕证书，避免伪造 winding。这是**保守正确的失败模式**，且失败项唯一、可归因。

## 四、双跑闸：字节级一致

三证书重签时，**进程内同代码连跑两次，输出字节级一致**，日志留在 `artifacts/witnesses-zeta/run-log-sup01.json`。

**判读**：同进程内重复执行消掉了进程级熵（ASLR、PYTHONHASHSEED 再播种等），配合第二节的跨进程/跨容器结果，形成**三级复现证据链**：同进程重跑 → 跨进程重放 → 跨容器重放，三级全部逐位一致。

## 五、综合结论

| 维度 | 结论 |
|---|---|
| 版本 diff | 44/44 数学字段逐位恒等，仅元数据/哈希链变化 |
| 跨环境 | 关键区间端点、残差界逐位相同 |
| 行为核验 | 3 项 verify，2 ok + 1 钉档拒证（唯一失败项、可归因） |
| 测试 | 41 passed，无 flaky |
| 双跑闸 | 字节级一致，日志留档 |

**证据强度评级**：本包支持"v1.0.1 相对 v1.0.0 在数学语义上为恒等升级，且计算可跨容器逐位复现"这一主张。剩余未覆盖面在包 3/3（预计覆盖签名链连续性、时间戳/证人或外部锚定），本包不做越界断言。

**供下游引用的一句话**：*EXT14-R2 包2/3 已证明 v1.0.0↔v1.0.1 的 44 个数学字段逐位恒等、两容器关键区间端点逐位一致、三项 verify 中两项通过且唯一失败项为 KI-EXT11-1 钉档拒证，双跑字节级一致。*

——ucif2 SI1语义轨·20261013T123932Z
