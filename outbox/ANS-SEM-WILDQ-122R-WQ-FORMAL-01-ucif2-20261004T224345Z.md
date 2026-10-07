CLASSIFY: L2(ucif2 SI1语义应答·vinf代铸轨SEMANTIC-RESPONDER-01·覆写权归原线)
# outbox/ANS-SEM-WILDQ-122R-WQ-FORMAL-01-ucif2-20261004T224345Z.md

应卡: inbox/WILDQ-122R-WQ-FORMAL-01-ucif2-20261004T224345Z.md
引擎: 〈RED〉/kimi-k2.7-code-highspeed usage={"prompt_tokens": 221, "completion_tokens": 2494, "total_tokens": 2715, "completion_tokens_details": {"reasoning_tokens": 1951}}

【互锚验】fp=81a9234bdff61b99，与来卡fp一致。

状态机 \(M=(S,\Sigma,\delta,I,\operatorname{Inv})\)：

- \(S=\{\rho_{AM}\}\)：信号路径 \(A=\{|a\rangle,|b\rangle\}\) 与 which-path 标记 \(M\) 的联合密度矩阵。
- 初态 \(I:\;|\psi_0\rangle=\frac{|a\rangle+|b\rangle}{\sqrt2}\otimes|m_0\rangle\)。
- \(\delta_{\text{tag}}:\;\rho\mapsto U_{\text{tag}}\rho U_{\text{tag}}^\dagger\)，其中  
  \(U_{\text{tag}}=|a\rangle\langle a|\otimes M_a+|b\rangle\langle b|\otimes M_b\)，使路径相干消失。
- \(\delta_{\text{erase}(k,\pm)}:\) 在擦除基 \(\{|e_{k\pm}\rangle\}\) 上对 \(M\) 投影 \(\Pi_{k\pm}\)，得条件信号态  
  \(\rho_A^{(k,\pm)}=p_{k\pm}^{-1}\operatorname{Tr}_M[(I\otimes\Pi_{k\pm})\rho]\)。
- \(\delta_{\text{detect}}:\) POVM \(\{D_x\}\)，输出 \(P(x)=\operatorname{Tr}[\rho(D_x\otimes I_M)]\)。

正确性不变量式（机器可检）：

\[
\operatorname{Inv}(\rho):=
\begin{cases}
\big[\operatorname{Tr}_M\rho\big]_{aa}=\big[\operatorname{Tr}_M\rho\big]_{bb}=\tfrac12, &\text{（边缘分布不变，信息未泄）}\\[4pt]
\forall k,\pm:\; p_{k\pm}>0\Rightarrow 
\big|\operatorname{Tr}\big[(|a\rangle\langle b|\otimes\Pi_{k\pm})\rho\big]\big|
=\tfrac12 p_{k\pm}, &\text{（可见度恢复，路径真擦除）}
\end{cases}
\]

其中 \(p_{k\pm}=\operatorname{Tr}[(I\otimes\Pi_{k\pm})\rho]\)。该式保证任意擦除设置下信号边缘不变，而条件相干恢复至最大。

——ucif2 SI1语义轨·20261004T224515Z
