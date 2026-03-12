import seaborn as sns
import pandas as pd
import numpy as np

# 데이터 불러오기
tips = sns.load_dataset("tips")

print("전체 데이터 개수:", len(tips))

# 1. 단순 임의 추출 (Random Sampling)
sample_random = tips.sample(frac=0.2, random_state=1)
print("\nRandom Sampling:")
print(sample_random.head())

# 2. 층화 추출 (Stratified Sampling)
sample_stratified = tips.groupby("sex", group_keys=False).apply(lambda x: x.sample(frac=0.2))
print("\nStratified Sampling:")
print(sample_stratified.head())

# 3. 체계적 추출 (Systematic Sampling)
k = 5
sample_systematic = tips.iloc[::k]
print("\nSystematic Sampling:")
print(sample_systematic.head())
