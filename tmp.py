
# 시작과 끝 숫자
start_num = 0
end_num = 2581

# 50 단위로 값 추가
step = 1
new_frames = [
    f"1128_corner_speed/{i:06d}"
    for i in range(start_num, end_num + 1, step)
]


import json

# JSON 파일 저장
json_filename = "generated_frames.json"
with open(json_filename, "w", encoding="utf-8") as f:
    json.dump(new_frames, f, indent=4)
