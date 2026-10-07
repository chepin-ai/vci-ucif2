CLASSIFY: L2(ucif2 SI1语义应答·vinf代铸轨SEMANTIC-RESPONDER-01·覆写权归原线)
# outbox/ANS-SEM-WILDQ-BOOTLOOPS-UCIF2-01-20261001T0000Z.md

应卡: inbox/WILDQ-BOOTLOOPS-UCIF2-01-20261001T0000Z.md
引擎: 〈RED〉/deepseek-chat usage={"prompt_tokens": 57, "completion_tokens": 1468, "total_tokens": 1525, "prompt_tokens_details": {"cached_tokens": 0}, "prompt_cache_hit_tokens": 0, "prompt_cache_miss_tokens": 57}

结论先说：**可以耦合，但耦合点不在“把 BootLoops 当定理证明器”，而在“把 BootLoops 当可复算的约束/证书编译器，把 oblig_view 当义务视图的闭环检查器”。** 联盟清单的筛选判据应围绕**可判定性、可复算性、闭环可观测性、失败可归因性**四条硬轴，而不是围绕“重要性”或“哲学深度”。

---

## 1. 耦合结构：三层接口

**Layer A — BootLoops 标准层（可机检任意精度复算）**
- 输入：状态 \(s\)、转移规则 \(R\)、精度参数 \(p\)、复算预算 \(B\)。
- 输出：要么是 `(verdict, certificate, cost)`，要么是 `(unknown, reason, cost)`。
- 关键要求：**相同输入 + 相同精度 ⇒ 相同输出**，且证书可被独立第三方在任意精度下重放。

**Layer B — oblig_view 闭环层（义务视图）**
- 对每个目标 \(G\)，把证明义务拆成视图 \(O = \{o_1,...,o_n\}\)。
- 每个 \(o_i\) 必须绑定一个 **witness**：或是 BootLoops 证书，或是显式假设/公理标记。
- 闭环条件：\(\forall o_i\)，要么被 witness  discharg，要么被显式登记为 open obligation 且带预算/期限。

**Layer C — 耦合契约（关键）**

```
oblig_view: obligation → {bootloops_query, accept_condition, reject_condition}
bootloops:  query → (cert | unknown | refuted)
oblig_view: 根据返回更新 obligation 状态，并检查闭环
```

耦合的**唯一硬约束**是：

> 任何 oblig_view 中被标记为“已闭环”的义务，其 witness 必须能降级为 BootLoops 可复算对象；否则只能标为“假设闭环”，不得计入联盟级结论。

这条约束把“任意精度复算”从口号变成**闭环的准入条件**。

---

## 2. 为什么这样耦合可行

- **方向正确**：BootLoops 擅长“给定规则下的可复算判定”，oblig_view 擅长“证明义务的结构化追踪”。两者是正交能力，不是竞争关系。
- **失败可分离**：BootLoops 返回 `unknown` 时，oblig_view 不会误判为“已证”，而是转为 open obligation，闭环状态可观测。
- **精度可调**：任意精度复算意味着同一义务可以在不同精度档位下重复验证，形成**精度阶梯上的闭环证据链**。
- **不依赖强假设**：不需要假设 BootLoops 完备，只需要它**可靠**（sound）且**可复算**。

风险点只有一个：**如果 BootLoops 的规则集本身不可判定或不可复算，耦合退化为形式装饰。** 这正是下面筛选判据要挡住的。

---

## 3. 清单筛选判据（四条硬轴 + 两条软轴）

### 硬轴（不满足即淘汰）

**H1. 可判定性/可半判定性**
- 问题必须能归约为某个判定过程，或至少是半判定过程且带明确终止条件。
- 判据：能否写出 `decide(instance, precision) → {yes, no, unknown, timeout}`？
- 淘汰：纯开放语义问题、无终止判据的问题。

**H2. 可复算性**
- 结论必须能由独立第三方在给定精度下重放。
- 判据：是否存在 `replay(certificate, precision) → bool`？
- 淘汰：依赖不可复现启发式、私有数据、不可观测内部状态的问题。

**H3. 闭环可观测性**
- 必须能定义“什么算闭环”“什么算未闭环”“什么算失败”。
- 判据：能否给出 oblig_view 的 obligation 分解 + witness 绑定方案？
- 淘汰：无法定义闭环条件的问题。

**H4. 失败可归因性**
- 失败必须能定位到：规则缺失、精度不足、预算不足、假设未证、还是问题本身不可判定。
- 判据：`unknown` 是否带 reason code？
- 淘汰：失败只能归因为“不知道”的问题。

### 软轴（用于排序，不淘汰）

**S1. 杠杆率**：解决后能解锁多少下游义务。
**S2. 精度敏感度**：提高精度是否能显著改变结论；若是，优先级上调。

---

## 4. 对“枢形问题 / AI形问题”的具体建议

- **枢形问题**：优先选那些**卡住多个下游义务**、且**可被 BootLoops 半判定**的问题。典型形态是“某类不变量是否在规则集下保持”。
- **AI形问题**：优先选那些**涉及 AI 系统自身可验证性**、且**能构造出可复算证书**的问题。典型形态是“某推理步骤是否在给定精度下可复现”。
- **共同淘汰线**：任何无法写出 `decide` 或 `replay` 签名的问题，先移入“待形式化”池，不进入主清单。

---

## 5. 首步（最小可行第一步）

**首步不是写规范，而是做一个端到端的最小闭环样例。**

具体三件事：

1. **选一个最小问题**：例如“某有限状态转移系统在精度 \(p\) 下，某不变量是否保持”。
2. **写 BootLoops 侧**：`decide(instance, p) → cert | unknown`，并实现 `replay(cert, p) → bool`。
3. **写 oblig_view 侧**：把该问题拆成 2–3 个 obligation，绑定上述 cert，跑一次闭环检查，输出 `closed / open / failed` 三态。

**验收标准**：
- 同一输入在不同精度下可复算；
- 证书可被独立脚本重放；
- `unknown` 能带 reason code 并转为 open obligation；
- 闭环状态可导出为机器可读清单。

**首步失败模式**：如果连这个最小样例都无法做到 `replay → bool`，说明当前 BootLoops 规则集还不具备被 oblig_view 耦合的资格，应先修规则集，而不是扩清单。

---

## 6. 一句话总结

**BootLoops 提供“可复算的判定与证书”，oblig_view 提供“义务分解与闭环状态机”；耦合靠 witness 绑定契约，清单筛选靠 H1–H4 四条硬轴；首步是跑通一个可重放的最小闭环样例。**

——ucif2 SI1语义轨·20261002T104753Z
