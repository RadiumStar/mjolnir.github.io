# Homework 2

## 习题1 流水线
1. 如果只考虑数据冒险，即不考虑分支错误，那么对于 $n$ 条指令，$p$ 级流水线的运行总时间为（假设时钟周期为 $T$，每 $m$ 条指令停顿 $s$ 个时钟周期，且 $m | n$）
    $$
    \begin{align}
        T_{\text{exec}} &= \overbrace{(n / p) \times p \times T}^{实际运行时间} + \overbrace{(p - 1)\times T}^{开始流水线启动时间} + \overbrace{(\frac{n}{m} - 1) \times s\times T}^{数据冒险停顿时间} \\
        &= (n + p - 1 + \frac{sn}{m} - s)\times T
    \end{align}
    $$
    因此代入数据
    - 对于 5 级流水线，运行时间 $T_{\text{exec1}} = \frac{6}{5}n + 3 \text{ns}$
    - 对于 12 级流水线，运行时间 $T_{\text{exec2}} = \frac{33}{40}n + 4.8 \text{ns}$
    - **故** 12 级流水线相对于 5 级流水线的**加速比**为 $$S = T_{\text{exec1}} / T_{\text{exec2}} = \frac{16n + 40}{11n + 64}$$当 指令数 $n \ge 5$ 条时，12 级流水线比 5 级流水线快
2. 如果考虑数据冒险和分支错误，那么对于 $n$ 条指令，$p$ 级流水线的运行总时间为（假设时钟周期为 $T$，每 $m$ 条指令停顿 $s$ 个时钟周期，且 $m | n$，分支错误预测率为 $q$，预测错误代价为 $r$）
    $$
    \begin{align}
        \text{CPI} &= \left\{\overbrace{(n / p) \times p}^{实际运行周期数} + \overbrace{(p - 1)}^{开始流水线启动周期数} + \overbrace{(\frac{n}{m} - 1) \times s}^{数据冒险停顿周期数} + \overbrace{q \times r}^{分支错误代价}\right\} / n \\
        &= 1 + \frac{s}{m} + \frac{p + qr - s - 1}{n}
    \end{align}
    $$
    因此代入数据
    - 对于 5 级流水线：$\text{CPI}_1 = \frac{6}{5} + \frac{3.1}{n}$
    - 对于 12 级流水线：$\text{CPI}_2 = \frac{11}{8} + \frac{8.25}{n}$

## 习题2 Tomasulo

> 忽略第一条指令

| 迭代 | 指令 | 发射 | 执行 | 访存 | 写CDB | 注释 |
|:---:|:----:|:----:|:---:|:----:|:-----:|:---:|
|  1  |  LD  |  1   |  2  |  2   |   3   |  -  |
|  1  | MULD |  2   | 4-18|  -   |  19   |  F2寄存器RAW   |
|  1  |  LD  |  3   |  4  |  -   |   5   |  -  |
|  1  | ADDD |  4   |20-29|  -   |  30   |  F4，F6寄存器RAW   |
|  1  |  SD  |  5   |  31 |  32  |   -   |  F6寄存器RAW  |
|  1  |DADDIU|  6   |   7 |   -  |   8   |  -  |
|  1  |DADDIU|  7   |   8 |   -  |   9   |  -  |
|  1  |DSLTU |  8   |   9 |   -  |  10   |  -  |
|  1  |BNEZ  |  9   |  11 |  -   |   -   |  R3寄存器RAW   |
|  2  |  LD  | 10   |  12 |  12  |  13   |  等待BNEZ分支指令   |
|  2  | MULD | 11   |19-33|  -   |  34   |  浮点乘功能单元结构性冒险   |
|  2  |  LD  | 12   |  13 |  13  |  14   |  -  |
|  2  | ADDD | 13   |35-44|  -   |  45   |  F4，F6寄存器RAW，浮点加功能单元结构性冒险|
|  2  |  SD  | 14   |  46 |  47  |   -   |  F6寄存器RAW  |
|  2  |DADDIU| 15   |  16 |  -   |  17   |  -  |
|  2  |DADDIU| 16   |  17 |  -   |  18   |  -  |
|  2  |DSLTU | 17   |  18 |  -   |  20   |周期19迭代1的MULD指令正在写CDB，结构性冒险  |
|  2  |BNEZ  | 18   |  21 |  -   |   -   |  R3寄存器RAW   |
|  3  |  LD  | 19   |  22 | 22   |  23   | 等待BNEZ分支指令   |
|  3  | MULD | 20   |34-48|  -   |  49   | 浮点乘功能单元结构性冒险 |
|  3  |  LD  | 21   |  23 |  22  |  24   | 整数功能单元结构性冒险   |
|  3  | ADDD | 22   |50-59|   -  |  60   | F4，F6寄存器RAW，浮点加功能单元结构性冒险|
|  3  |  SD  | 23   |  61 | 62   |   -   |  F6寄存器RAW  |
|  3  |DADDIU| 24   |  25 |  -   |  26   |  -  |
|  3  |DADDIU| 25   |  26 |  -   |  27   |  -  |
|  3  |DSLTU | 26   |  27 |  -   |  28   |  -  |
|  3  |BNEZ  | 27   |  29 |  -   |  -    |  R3寄存器RAW   |

- 第一个循环迭代需要 32 个周期；
- 第二个循环迭代需要 38 个周期；
- 第三个循环迭代需要 44 个周期；



## 习题3 ScoreBoard
1. 请在下表中写出执行指令时每个阶段所属的周期（从 1 开始计数，比如某指令从 a 周期才开始读指令，而执行区间为 b-c 周期）

> 假设 LD 指令执行阶段需要 1 个时钟周期，浮点数乘法执行阶段需要 10 个时钟周期，而浮点数加法执行阶段需要 2 个时钟周期，假设发射、读取、写回只要1个周期

| Op | dest | j | k | Issue | Read Oper | Exec Comp | Write Result |
|:--:|:----:|:-:|:-:|:-----:|:---------:|:---------:|:------------:|
| LD | F6   |34 |R2 |   1   |    2      |     3     |       4      |
| LD | F2   |45 |R3 |   5   |    6      |     7     |       8      |
|MULD| F0   |F5 |F2 |   6   |    9      |   10-19   |      20      |
|MULD| F7   |F2 |F6 |   7   |    9      |   10-19   |      20      |
|ADDD| F6   |F8 |F7 |   8   |   21      |   22-23   |      24      |

2. 在第九个时钟周期时，尝试填写以下功能单元状态图表

| Time |  Name | Busy | Op | Fi | Fj | Fk | Qj | Qk | Rj | Rk |
|:----:|:-----:|:----:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|  -   |Integer|  No  | -  | -  | -  | -  | -  | -  | -  | -  |
| 10   |Mult1  | Yes  |Mult| F0 | F5 | F2 | -  | -  |Yes |Yes |
| 10   |Mult2  | Yes  |Mult| F7 | F2 | F6 | -  | -  |Yes |Yes |
|  -   |Add    |  No  | -  | -  | -  | -  | -  | -  | -  | -  |


## 习题4
1. 数据相关
   1. 从 LD 到 DADDI 有对于寄存器 R1 的RAW相关
   2. 从 LD 到 DADDI 有对于寄存器 R1 的WAW相关
   3. 从 DADDI 到 SD 有对于寄存器 R1 的RAW相关
   4. 从 DADDI 到 DSUB 有对于寄存器 R2 的RAW相关
   5. 从 DSUB 到 BNEZ 有对于寄存器 R4 的RAW相关
2. 这一循环的执行需要 13 个周期

| instr|  1   |  2   |  3   |   4   |  5   |  6   |  7   |  8   |  9   |  10  |  11  |  12  |  13  | 
|:----:|:----:|:----:|:----:|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:| 
|  LD  |  IF  |  ID  |  EX  |  MEM  |  WB  |  -   |  -   |  -   |  -   |  -   |  -   |  -   |  -   |
|DADDI |  -   |  IF  |  ID  | Stall |  EX  |  MEM |  WB  |  -   |  -   |  -   |  -   |  -   |  -   |
|SD    |  -   |   -  |  IF  | Stall |  ID  |  EX  |  MEM |  WB  |  -   |  -   |  -   |  -   |  -   |
|DADDI |  -   |   -  |   -  | Stall |  IF  |  ID  |  EX  |  MEM |  WB  |  -   |  -   |  -   |  -   |
|DSUB  |  -   |   -  |   -  |   -   |   -  |  IF  |  ID  | Stall|  EX  |  MEM |  WB  |  -   |  -   |
|BNEZ  |  -   |   -  |   -  |   -   |   -  |   -  |  IF  | Stall|  ID  | Stall|  Ex  |  MEM |  WB  |

3. 预测未被选中，但是由R2和R3的值的关系，前面98次循环都是分支到循环，只有第99次跳出循环（396 / 4 = 99），因此会导致回滚；这一循环的执行需要 $$\frac{98\times 8 + 10}{99} = \frac{794}{99} = 8.02$$ 个周期

| instr|  1   |  2   |  3   |   4   |  5   |  6   |  7   |  8   |  9   |  10  |  11  |  ... |  794 |
|:----:|:----:|:----:|:----:|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|
|LD(1) |  IF  |  ID  |  EX  |  MEM  |  WB  |  -   |  -   |  -   |  -   |  -   |  -   |  -   |  -   |
|DADDI |  -   |  IF  |  ID  |   EX  |  MEM |  WB  |  -   |  -   |  -   |  -   |  -   |  -   |  -   |
|SD    |  -   |   -  |  IF  |   ID  |  EX  |  MEM |  WB  |  -   |  -   |  -   |  -   |  -   |  -   |
|DADDI |  -   |   -  |   -  |   IF  |  ID  |  EX  |  MEM |  WB  |  -   |  -   |  -   |  -   |  -   |
|DSUB  |  -   |   -  |   -  |   -   |  IF  |  ID  |  EX  |  MEM |  WB  |  -   |  -   |  -   |  -   |
|BNEZ  |  -   |   -  |   -  |   -   |   -  |  IF  |  ID  |  Ex  |  MEM |  WB  |  -   |  -   |  -   |
|LD(2) |  -   |   -  |   -  |   -   |   -  |   -  |   -  |   -  |**IF**|  ID  |  EX  |  ... |  -   |
| ...  |  -   |   -  |   -  |   -   |   -  |   -  |   -  |   -  |  -   |  IF  |  ID  |  ... |  -   |
|BNEZ(99)|-   |   -  |   -  |   -   |   -  |   -  |   -  |   -  |  -   |  -   |  -   |  ... | WB   |

1. 预测被选中，由R2和R3的值的关系，前面98次循环都是分支到循环，只有第99次跳出循环（396 / 4 = 99），因此不会导致回滚；这一循环的执行需要 $$\frac{98\times 6 + 10}{99}=\frac{589}{99} = 6.04$$ 个周期

| instr|  1   |  2   |  3   |   4   |  5   |  6   |  7   |  8   |  9   |  10  |  ... |  598 |
|:----:|:----:|:----:|:----:|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|
|LD(1) |  IF  |  ID  |  EX  |  MEM  |  WB  |  -   |  -   |  -   |  -   |  -   |  -   |  -   |
|DADDI |  -   |  IF  |  ID  |   EX  |  MEM |  WB  |  -   |  -   |  -   |  -   |  -   |  -   |
|SD    |  -   |   -  |  IF  |   ID  |  EX  |  MEM |  WB  |  -   |  -   |  -   |  -   |  -   |
|DADDI |  -   |   -  |   -  |   IF  |  ID  |  EX  |  MEM |  WB  |  -   |  -   |  -   |  -   |
|DSUB  |  -   |   -  |   -  |   -   |  IF  |  ID  |  EX  |  MEM |  WB  |  -   |  -   |  -   |
|BNEZ  |  -   |   -  |   -  |   -   |   -  |  IF  |  ID  |  Ex  |  MEM |  WB  |  -   |  -   |
|LD(2) |  -   |   -  |   -  |   -   |   -  |   -  |**IF**|  ID  |  EX  |  MEM | ...  |  -   |  
| ...  |  -   |   -  |   -  |   -   |   -  |   -  |   -  |  ... | ...  | ...  | ...  |  -   |  
|BNEZ(99)|-   |   -  |   -  |   -   |   -  |   -  |   -  |   -  |  -   |  -   | ...  |  WB  | 

5. 假定在一个 5 级流水线中，最长的流水级需要 0.8ns, 流水线寄存器延迟为 0.1ns。这个 5 级流水线的时钟周期时间为 $$0.8 \times 5 + 0.1\times 3 = 4.3 \text{ns}$$
6. 第4问的 $\text{CPI} = 99\times 6 / 598 \approx 0.9933$
   1. 第一种机器（没有完整转发）的平均指令执行时间为 $$\text{T}_1 = \frac{\frac{4.3}{5} \times (98\times 11 + 13)}{6\times 99} \approx 1.580\text{ns}$$
   2. 第二种机器（有完整转发，预测未选中）的平均指令执行时间为 $$\text{T}_2 = \frac{\frac{4.3}{5} \times 794}{6\times 99} \approx 1.150\text{ns}$$
   3. 第三种机器（有完整转发，预测选中）的平均指令执行时间为 $$\text{T}_3 = \frac{\frac{4.3}{5} \times 598}{6\times 99} \approx 0.866\text{ns}$$

## 习题5 预测器
> update表项解释：entry0: prediction: T表示将entry 0处的prediction表项变更为T

- 对于correlating predictor：最终错误预测率 $33.3\%$

> 初始化假设last outcome 为 T

| Branch PC | Branch | Outcome | Pred | Result | Entry | Update | 
|:---------:|:------:|:-------:|:----:|:------:|:-----:|:------:|
|454        |2       |T        |T     |success |4      |-       |
|543        |3       |NT       |NT    |success |6      |entry6: prediction: NT|
|777        |1       |NT       |T     |fail    |3      |entry3: prediction: T with one misprediction|
|543        |3       |NT       |NT    |success |7      |-       |
|777        |1       |NT       |T     |fail    |3      |entry3: prediction: NT|
|454        |2       |T        |T     |success |5      |-       |
|777        |1       |NT       |NT    |success |2      |-       |
|454        |2       |T        |T     |success |5      |-       |
|543        |3       |T        |NT    |fail    |6      |entry6: prediction: NT with misprediction|

- 对于local predictor：最终错误预测率 $22.2\%$

> 初始化假设0, 1分支的last outcome 都为 T, T

| Branch PC | Branch |last2outcome| Outcome | Pred | Result | Entry | Update | 
|:---------:|:------:|:----------:|:-------:|:----:|:------:|:-----:|:------:|
|454        |0       |T T         |T        |T     |success |0      |entry0: prediction: T|
|543        |1       |T T         |NT       |T     |fail    |4      |entry4: prediction: T with one misprediction|
|777        |1       |T NT        |NT       |T     |fail    |5      |entry5: prediction: NT|
|543        |1       |NT NT       |NT       |NT    |success |7      |-       |
|777        |1       |NT NT       |NT       |NT    |success |7      |-       |
|454        |0       |T T         |T        |T     |success |0      |-       |
|777        |1       |NT NT       |NT       |NT    |success |6      |-       |
|454        |0       |T T         |T        |T     |success |0      |-       |
|543        |1       |NT NT       |NT       |NT    |success |7      |-       |