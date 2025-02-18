import pickle
import json
import numpy as np

# data_path = "generated_frames.pickle"

# # # Pickle 파일 로드
# with open(data_path, "rb") as f:
#     data = pickle.load(f)

# # NumPy 객체 변환 함수 정의
# def convert_numpy(obj):
#     if isinstance(obj, np.ndarray):  # NumPy 배열인 경우 리스트로 변환
#         return obj.tolist()
#     elif isinstance(obj, np.generic):  # NumPy 기본 데이터 타입 변환
#         return obj.item()
#     raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")

# # JSON으로 저장
# with open("custom_datalist_validation.json", "w", encoding="utf-8") as f:
#     json.dump(data, f, indent=4, default=convert_numpy)

# print("JSON 파일 저장 완료: data.json")




#######################################

data_path = "/datalist_validation.pickle"

# JSON 파일 로드
with open("generated_frames.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# 다시 Pickle로 저장
with open("custom_datalist_validation.pickle", "wb") as f:
    pickle.dump(data, f)
