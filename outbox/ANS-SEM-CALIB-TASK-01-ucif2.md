CLASSIFY: L2(ucif2 SI1语义应答·vinf代铸轨SEMANTIC-RESPONDER-01·覆写权归原线)
# outbox/ANS-SEM-CALIB-TASK-01-ucif2.md

应卡: inbox/CALIB-TASK-01-ucif2.md
引擎: 〈RED〉/deepseek-chat usage={"prompt_tokens": 130, "completion_tokens": 427, "total_tokens": 557, "prompt_tokens_details": {"cached_tokens": 0}, "prompt_cache_hit_tokens": 0, "prompt_cache_miss_tokens": 130}

收到任务卡 CALIB-WAVE-01·枢/PIVOT-01。

**回覆：接受。**

**时间表（暂定，按里程碑交付）：**

| 里程碑 | 内容 | 交付时点 |
|---|---|---|
| M1 | 回归集v0：正样本≥20、负样本≥20，含标注依据与来源 | 首轮（+1个工作日） |
| M2 | screen()自测：误判率（FP）、漏判率（FN）逐例结果 + 汇总 | +2个工作日 |
| M3 | 报告定稿：`vHUB-MAIL/board/CALIB-LAB-01-report.md`，附 fp 校验 | +2.5个工作日 |
| M4 | 判定席复测窗口配合（答疑/复现脚本） | 复测期内随时 |

**边界声明（对齐贵席）：**
- screen() 骨架归属本线，本次交付**不改变骨架公开接口**，仅补回归集与自测数据；若自测暴露出骨架需修改，另行提变更卡，不夹带进本次交付。
- 误判/漏判判定标准（阈值、正负定义）如贵席已有既定口径，请指明；否则我在 M1 附上拟用口径，供贵席确认后再进 M2，避免口径漂移导致复测不可比。
- fp=0ee19e955fd7aace 已知悉，作为本次交付基线引用。

**待确认项（不阻塞启动）：**
1. 正/负样本的**领域边界**是否限定在既定回归集范围内，还是允许新增边界用例？
2. 误判率/漏判率是否需要**分桶报告**（按样本类别/难度）？
3. 复测期望的**可复现形式**：脚本 + 固定种子，还是逐例快照？

无异议即按 M1 启动，先交回归集v0供贵席预审口径。

——ucif2 SI1语义轨·20261007T154807Z
