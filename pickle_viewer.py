import pickle
import pprint  # 보기 좋게 출력하기 위한 라이브러리

# 파일 경로 설정
# pickle_file = "OpenLane-V/list/datalist_validation.pickle"
pickle_file = "OpenLane-V/label/validation/segment-17065833287841703_2980_000_3000_000_with_camera_labels/155362886424889300.pickle"
# Pickle 파일 열기 (rb: 바이너리 읽기 모드)
with open(pickle_file, "rb") as f:
    data = pickle.load(f)

# 데이터 확인 (출력)
# print(type(data))  # 데이터 타입 확인
# print(data)  # 데이터 내용 출력


# 예제: 딕셔너리 형태일 경우
if isinstance(data, dict):
    pprint.pprint(data)  # 예쁘게 출력

# 예제: 리스트 형태일 경우
elif isinstance(data, list):
    print(f"리스트 길이: {len(data)}")  # 리스트 크기 출력
    print("첫 번째 항목:", data[0])  # 첫 번째 아이템 출력 (너무 길면 일부만 확인)

