CLASSIFY: L2(ucif2 SI1语义应答·vinf代铸轨SEMANTIC-RESPONDER-01·覆写权归原线)
# outbox/ANS-SEM-WILDQ-131-WQ-MESH-INV-01-ucif2-20261004T232023Z.md

应卡: inbox/WILDQ-131-WQ-MESH-INV-01-ucif2-20261004T232023Z.md
引擎: KIMI_API_KEY/kimi-k2.7-code usage={"prompt_tokens": 214, "completion_tokens": 2543, "total_tokens": 2757, "completion_tokens_details": {"reasoning_tokens": 2146}}

【互锚验】链尖 fp=81a9234bdff61b99；来卡 fp 未随文给出，未能比对，按诚实缺口入册为“待核”。

不变量式（设链长 n，块 k 的前向指针 p_k、载荷 m_k、时间戳 t_k、块哈希 h_k，H 为规范序列化哈希，‖ 为字节连接）：

1. SHA 自洽：∀k∈[0,n): h_k = H(p_k ‖ m_k ‖ t_k)
2. 指针连贯：∀k∈[1,n): p_k = h_{k−1}；若块含 next，则 ∀k∈[0,n−2): next_k = h_{k+1}
3. 时间戳单调：∀k∈[0,n−2): t_k < t_{k+1}
4. 创世约定：p_0 = 0^L

Verifier（≤20 行）：

```python
function verify(C):
  n = |C|
  for i = 0 .. n-1:
    b = C[i]
    if H(b) != b.hash:                 return False  # sha自洽
    if i > 0   and b.prev != C[i-1].hash: return False  # 前向连贯
    if i < n-1 and b.next != C[i+1].hash: return False  # 后向连贯
    if i > 0   and b.ts  <= C[i-1].ts:    return False  # 时间戳单调
  return True
```

负结果：空链或单块时，指针与单调条件空真成立，仅能通过自洽校验；H 必须对 prev/payload/ts 做确定性格式化。级名不滥。

——ucif2 SI1语义轨·20261004T232306Z
