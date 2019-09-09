import numpy as np
import pandas as pd

gs = pd.read_excel(r"2019研究生录取表.xls")
cols = ["姓名","录取专业代码","录取专业名称","总成绩"]
gs = gs[cols]
gs.sort_values("录取专业代码",inplace=True)
students_selected = gs.pivot_table(index="录取专业名称",values='总成绩',aggfunc=[np.mean,np.max,np.min])
print(students_selected)

