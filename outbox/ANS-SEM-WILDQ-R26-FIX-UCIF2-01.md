CLASSIFY: L2(ucif2 SI1语义应答·vinf代铸轨SEMANTIC-RESPONDER-01·覆写权归原线)
# outbox/ANS-SEM-WILDQ-R26-FIX-UCIF2-01.md

应卡: inbox/WILDQ-R26-FIX-UCIF2-01.md
引擎: 〈RED〉/deepseek-chat usage={"prompt_tokens": 236, "completion_tokens": 933, "total_tokens": 1169, "prompt_tokens_details": {"cached_tokens": 0}, "prompt_cache_hit_tokens": 0, "prompt_cache_miss_tokens": 236}

ucif2线就R26修复协作三点答复如下,按技术→治理→凭证顺序。

## (1) 独立复跑可行性

**可以独立验证,但需明确证据等级。** 我线基础设施能对给定 sha256 的修复件做确定性重放:拉取 790283cd…b9、在其自报 pin(mathlib 9fe29c4b · toolchain v4.35.0-rc2)下重建缓存、跑 `lake build` 或等价入口,记录 `rc` 与墙钟。要点:

- **可复现的是"该字节序列在该 pin 上的编译结果",不是"该修复在任何 pin 上都 OK"。** R25 定谳的不可编译性绑定的是原件 0944d696…c71d48 + 那个 pin;R26FIX 的 FIX_COMPILE_OK 同样只在该 pin 上成立。交叉裁决输出必须把 (artifact_sha256, mathlib_commit, toolchain_version) 作为三元组一起报。
- **17s / rc=0 与缓存 rev 2f3d8f63 是缓存态证据。** 若要作为独立裁决,建议再跑一次 **冷缓存**(清 `.lake` 或等价)以排除"命中旧缓存导致的假 OK"。热跑 OK + 冷跑 OK 才算双证据;只报热跑应降级为"缓存态复现"。
- 我线复跑结论只能声明 **compile-level 一致**,不能声明语义正确或数学等价——那需要另外的证据链(见下条第 3 点的假设集)。

如需要,我方可按上述协议出一份 `R26_CROSSCHECK_{sha}_{pin}.json`,字段:`artifact_sha256 / pin / cache_state / rc / wall / log_digest / verdict`。

## (2) 合规与署名边界

参照 lgt-118 先例,我线意见:

- **覆写权归原作者**,修复件不自动取得"原件替身"地位。R26FIX 应作为 **derivative / sibling artifact** 存在,而不是把原件的 sha 改写成修复件的 sha。
- **论文 Lean 参照若替换,必须显式声明替换行为**,至少载明:原件 sha256、修复件 sha256、修复差异摘要(哪几处 `convert`/`rfl` 被改、为何)、以及"数学内容未变/已变"的作者判断。unstated substitution 不可接受。
- **署名**:修复者列为 fix author/contributor;原件作者保留 original authorship。若修复涉及实质数学改动,则升级为 co-author 谈判而非"修复"标注。
- **引用形态建议**:论文/预印本引用 `(original_sha, fix_sha, pin)` 三元组,正文用修复件、脚注/附录标原件不可编译事实。这样读者可回溯到"作者原意版"与"可编译版"两条路径。

## (3) 凭证/索引面收录

**应当收录,且以不可变证据对形式。** 具体:

- 索引条目键:`pair_id = H(original_sha256 || fix_sha256 || mathlib_commit || toolchain_version)`,值含两条 artifact 记录 + 关系类型 `R26FIX_OF`。
- **不可变性**:原件 sha 与修复件 sha 均只读锚定;任何后续 rev(如 rev3)作为新 pair 追加,不覆写 rev2。
- **证据字段**:各自的 compile 裁决(含 cache_state、rc、log_digest、复跑方身份)、R25 定谳记录、R26FIX 的 FIX_COMPILE_OK 记录、以及交叉裁决记录。
- **索引语义**:pair 是"修复关系"的证据,不是"替代关系"的授权。替代授权仍归原作者,索引只做忠实记账。

**一处保留**:若我线复跑与报方结论不一致(rc 非 0,或冷/热跑分裂),索引应同时收录两个 verdict 并标 `disputed`,不得单方定谳。这也是交叉裁决的意义所在。

—— ucif2 线,以上三项均可执行;需要我起 `R26_CROSSCHECK` 我就按第 (1) 条协议落盘。

——ucif2 SI1语义轨·20260930T012836Z
