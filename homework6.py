"""作业 6：TD(λ) 与多步学习；截图转录及独立解答。"""
def get_questions(p, f, ul):
    return [
    (6,1,'λ = 0：一步 TD','在 TD(λ) 算法中，如果 λ = 0，算法是什么？',['Q-learning','SARSA','蒙特卡洛方法','TD(0)'],3,
    p('答案为 D，TD(0)。λ 决定不同步长回报的混合权重；当 λ = 0 时，只保留一步回报目标，因此退化为一步时序差分学习。') +
    f('G<sub>t</sub><sup>λ=0</sup> = G<sub>t:t+1</sub> = R<sub>t+1</sub> + γV(S<sub>t+1</sub>)<br>V(S<sub>t</sub>) ← V(S<sub>t</sub>) + α[G<sub>t:t+1</sub> − V(S<sub>t</sub>)]') +
    p('真正终止时，后继状态价值取 0。TD(0) 中的 0 指 λ = 0，不是“零步更新”：它仍然使用一次转移及其奖励。') +
    ul('A、B：Q-learning 与 SARSA 是动作价值控制算法，不是本题状态价值预测 TD(λ) 在 λ = 0 时的名称。','C：蒙特卡洛使用完整采样回报，对应本题 λ = 1 的前向视角端点。','D：保留一步 TD 目标，正确。'),
    '从资格迹看 λ = 0',p('在表格型、累积资格迹（accumulating traces）的后向实现中，回合开始令 e₋₁(s)=0，每步使用：') +
    f('e<sub>t</sub>(s) = γλe<sub>t−1</sub>(s) + 𝟙{s = S<sub>t</sub>}<br>δ<sub>t</sub> = R<sub>t+1</sub> + γV(S<sub>t+1</sub>) − V(S<sub>t</sub>)<br>V(s) ← V(s) + αδ<sub>t</sub>e<sub>t</sub>(s)') +
    p('𝟙 是指示函数。当 λ = 0 时，旧资格迹全部消失，只有当前状态的迹为 1，所以只更新当前状态，正好得到 TD(0)。')),
    (6,2,'λ = 1：完整回报端点','在 TD(λ) 算法中，λ 取值为 1 时，算法是什么？',['蒙特卡洛方法','SARSA(λ)','Q-learning','TD(0)'],0,
    p('答案为 A，蒙特卡洛方法。按有限回合的经典前向视角，λ = 1 时，λ-return 完全由回合终止前的实际回报构成，不再依赖中途的价值自举。') +
    p('设终止时刻为 T，剩余步数 m = T−t ≥ 1。令 Gₜ:ₜ₊ₙ 为 n 步回报，Gₜ 为完整回报。有限回合的 λ-return 为：') +
    f('G<sub>t</sub><sup>λ</sup> = (1−λ) ∑<sub>n=1</sub><sup>m−1</sup> λ<sup>n−1</sup>G<sub>t:t+n</sub> + λ<sup>m−1</sup>G<sub>t</sub>') +
    p('λ = 1 时，所有未到终点的短步长权重为 0，完整回报的权重为 1。若只剩一步，求和为空，目标直接是完整的一步回报。端点的零次幂权重按 1 处理。') +
    f('G<sub>t</sub><sup>λ=1</sup> = G<sub>t</sub> = ∑<sub>k=0</sub><sup>m−1</sup> γ<sup>k</sup>R<sub>t+k+1</sub>') +
    p('因此常用记忆是“λ = 0 对应 TD(0)，λ = 1 对应 MC”。SARSA(λ) 是带迹的动作价值控制方法，不能由预测算法单靠改变 λ 就变成；Q-learning 也不是该端点。'),
    '目标等价不等于所有在线实现逐步完全一致',p('上述结论针对有限完整回合的前向 λ-return。回合内冻结价值、累积更新的离线条件下，经典累积迹的前后向视角具有对应关系。若传统在线 TD(λ) 在回合中不断改变价值估计，就不能无条件宣称它在每一步都与普通 MC 完全相同。') +
    p('True Online TD(λ) 在其表格或线性函数近似设定下，建立了与特定在线前向视角的精确对应。持续任务中没有有限终点，也不能直接照搬这里的完整回合推导。参考：<a href="https://proceedings.mlr.press/v32/seijen14.pdf">van Seijen 与 Sutton，True Online TD(λ)</a>。')),
    (6,3,'λ 的取值范围','TD(λ) 算法中的 λ 参数的取值范围是：',['[0,1]','(0,1]','[0,1)','(0,1)'],0,
    p('答案为 A，[0,1]。标准 TD(λ) 同时包含 λ = 0 与 λ = 1 两个端点，另外三个选项分别排除了至少一个端点。') +
    f('0 ≤ λ ≤ 1') +
    ul('λ = 0：仅使用一步 TD 目标。','0 &lt; λ &lt; 1：混合不同步长的目标。','λ = 1：有限回合前向目标是完整 MC 回报。') +
    p('以剩余 3 步的回合为例，1 步、2 步、完整 3 步目标的权重分别是 1−λ、(1−λ)λ、λ²。它们非负且总和为 1。取 λ = 0.5，得到 0.5、0.25、0.25。'),
    '不要混淆 λ、γ 与 α',
    '<table><caption>三个参数分别控制什么？</caption><thead><tr><th>参数</th><th>含义</th><th>作用</th></tr></thead><tbody><tr><td>λ</td><td>迹衰减 / 回报混合参数</td><td>控制不同备份长度的权重</td></tr><tr><td>γ</td><td>折扣因子</td><td>控制未来奖励的折扣</td></tr><tr><td>α</td><td>学习率</td><td>控制每次参数更新的幅度</td></tr></tbody></table>' +
    p('在累积资格迹中，旧迹的单步衰减系数是 γλ，而不是仅 λ。因此即使 λ = 1，只要 γ &lt; 1，未再次访问状态的旧迹仍会衰减。λ 较大通常更偏重长回报，但不保证误差一定更小；表现取决于采样方差、自举误差、步长与任务。')),
    (6,4,'TD(λ) 与 n-step TD','TD(λ) 和 n-step TD 是同一个算法的不同名称。',['对','错'],1,
    p('答案为 B，错。二者有关联，但不是同一个算法的别名。固定 n-step TD 选择一个步长 n；TD(λ) 的前向视角将多个步长回报按 λ 加权混合。') +
    f('n 步目标（t+n &lt; T）：<br>G<sub>t:t+n</sub> = ∑<sub>k=0</sub><sup>n−1</sup> γ<sup>k</sup>R<sub>t+k+1</sub> + γ<sup>n</sup>V(S<sub>t+n</sub>)') +
    p('若在 n 步之内终止，则只累加到终止，不再加终止后的价值。TD(λ) 则使用第 2 题给出的 λ-return，而不是单独选取一个固定 n。') +
    '<table><caption>两种多步学习方式</caption><thead><tr><th>维度</th><th>固定 n-step TD</th><th>TD(λ)</th></tr></thead><tbody><tr><td>主要参数</td><td>步数 n</td><td>混合系数 λ</td></tr><tr><td>前向目标</td><td>一个指定步长的回报</td><td>多个步长回报的加权组合</td></tr><tr><td>典型实现</td><td>保存所需的近期转移</td><td>使用资格迹向过去分配当前 TD 误差</td></tr><tr><td>共同端点</td><td>n = 1 是一步 TD</td><td>λ = 0 是一步 TD</td></tr></tbody></table>' +
    p('例如剩余 3 步，三个目标分别为 2、4、8。固定 2-step TD 的目标是 4；λ = 0.5 的前向混合目标为 0.5×2 + 0.25×4 + 0.25×8 = 4。这次碰巧相等，并不说明算法相同；若完整回报改成 12，混合目标就变为 5，而固定 2-step 目标仍是 4。'),
    '前向视角与后向视角',p('前向视角从当前时刻向未来看，描述“用什么目标学习”；后向视角利用资格迹，将当前 TD 误差分配给近期访问过的状态，描述一种可在线执行的机制。') +
    p('因此不能把“TD(λ) 融合多步信息”误解为“它就是某个固定 n-step TD”。λ 接近 1 会提高较长回报的相对权重，但不存在对任意任务都能把一个 λ 精确替换成一个固定 n 的通用公式。')),
    ]

RECAP = '''<section id="lambda-recap"><div class="eyebrow">ELIGIBILITY TRACES / 复习卡</div><h2>λ 把一步 TD 与完整回报连起来</h2><div class="concepts"><p><b>λ = 0</b><br>TD(0)：只保留一步目标</p><p><b>0 &lt; λ &lt; 1</b><br>混合不同步长回报</p><p><b>λ = 1</b><br>有限回合前向目标为 MC 回报</p></div><table><caption>第 6 次作业 · 易考判断</caption><thead><tr><th>说法</th><th>判断与条件</th></tr></thead><tbody><tr><td>标准 λ 范围包含 0 与 1</td><td>对，[0,1]</td></tr><tr><td>TD(0) 表示不需要任何转移信息</td><td>错；它是一步 TD</td></tr><tr><td>λ = 1 时有限回合的前向 λ-return 等于完整回报</td><td>对</td></tr><tr><td>所有在线 TD(1) 实现都与普通 MC 逐步完全相同</td><td>错；需区分视角、实现和更新条件</td></tr><tr><td>TD(λ) 是固定 n-step TD 的另一个名称</td><td>错</td></tr><tr><td>累积资格迹的旧迹按 γλ 衰减</td><td>对</td></tr><tr><td>λ 越大，学习效果必然越好</td><td>错；需要按任务权衡</td></tr></tbody></table><p>题目来源：用户提供的四张截图，按顺序标记选项；答案与解析为独立解答，并非官方答案。参考：<a href="https://www.incompleteideas.net/book/bookdraft2018mar21.pdf">Sutton &amp; Barto，第 7 章 n-step Bootstrapping、第 12 章 Eligibility Traces</a>。在线等价性的边界可进一步阅读 <a href="https://proceedings.mlr.press/v32/seijen14.pdf">True Online TD(λ)</a>。</p></section>'''
