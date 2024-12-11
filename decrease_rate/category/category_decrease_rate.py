import pandas as pd

# 2019 데이터
data_2019 = {
    "업종": ["소매", "숙박", "스포츠", "오락", "음식", "합계"],
    "합계": [396696, 14451, 7284, 36246, 408035, 862712]
}

# 2021 데이터
data_2021 = {
    "업종": ["소매", "숙박", "스포츠", "오락", "음식", "합계"],
    "합계": [305640, 12349, 9723, 21272, 380083, 729067]
}

# 데이터프레임 생성
df_2019 = pd.DataFrame(data_2019).set_index("업종")
df_2023 = pd.DataFrame(data_2021).set_index("업종")

# 감소율 계산
decrease_rate = ((df_2019["합계"] - df_2023["합계"]) / df_2019["합계"] * 100).round(2)

# 결과 데이터프레임 생성
decrease_rate_df = pd.DataFrame({
    "업종": df_2019.index,
    "2019 합계": df_2019["합계"],
    "2021 합계": df_2023["합계"],
    "감소율 (%)": decrease_rate
}).reset_index(drop=True)