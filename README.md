# add-file

import streamlit as st
import pandas as pd

# --------------------------------
# 1. 스트레칭 데이터 (리스트)
# --------------------------------

stretching_data = {
    "눈": [
        "20초 동안 약 6m 떨어진 먼 곳 바라보기",
        "눈을 천천히 깜빡이며 휴식하기",
        "화면에서 눈을 떼고 잠시 쉬기"
    ],
    "목": [
        "고개를 좌우로 천천히 기울이기",
        "어깨를 천천히 위아래로 움직이기",
        "목에 힘을 빼고 편안한 자세 유지하기"
    ],
    "허리": [
        "의자에 앉아 허리를 편안하게 펴기",
        "상체를 좌우로 무리 없이 천천히 움직이기",
        "잠시 일어나 가볍게 걷기"
    ]
}

# --------------------------------
# 2. 나이에 따른 시간 추천 함수
# --------------------------------

def recommend_time(age):

    if age < 20:
        group = "청소년"
        stretch_time = 1

    elif age < 40:
        group = "성인"
        stretch_time = 2

    elif age < 60:
        group = "중장년층"
        stretch_time = 2

    else:
        group = "노년층"
        stretch_time = 1

    return group, stretch_time


# --------------------------------
# 3. 스마트폰 사용 습관 분석 함수
# --------------------------------

def check_phone_time(use_time):

    if use_time >= 8:
        return "스마트폰 사용 시간이 긴 편입니다. 중간중간 충분히 쉬어 주세요."

    elif use_time >= 5:
        return "스마트폰 사용 시간을 확인하고 규칙적으로 휴식해 주세요."

    else:
        return "사용 시간뿐 아니라 올바른 자세와 휴식 습관도 중요합니다."


# --------------------------------
# 4. 스트레칭 방법 출력 함수
# --------------------------------

def recommend_stretching(body_parts):

    result = []

    for part in body_parts:
        result.append({
            "신체 부위": part,
            "추천 시간": "20초" if part == "눈" else "1~2분",
            "스트레칭 방법": stretching_data[part]
        })

    return result


# --------------------------------
# 5. 프로그램 화면 구성
# --------------------------------

st.title("💚 나이별 맞춤형 건강관리 프로그램")

st.write("나이와 스마트폰 사용 습관을 입력하면")
st.write("눈, 목, 허리의 스트레칭 방법을 추천해 드립니다.")

st.divider()

# 사용자 정보 입력

st.subheader("1. 사용자 정보 입력")

age = st.number_input(
    "나이를 입력하세요",
    min_value=1,
    max_value=120,
    value=17
)

use_time = st.number_input(
    "하루 스마트폰 사용 시간(시간)",
    min_value=0.0,
    max_value=24.0,
    value=5.0,
    step=0.5
)

body_parts = st.multiselect(
    "스트레칭이 필요한 부위를 선택하세요",
    ["눈", "목", "허리"]
)

# --------------------------------
# 6. 분석 버튼
# --------------------------------

if st.button("건강 상태 분석하기"):

    if len(body_parts) == 0:
        st.warning("스트레칭할 부위를 하나 이상 선택해 주세요.")

    else:
        # 나이 분석
        group, stretch_time = recommend_time(age)

        st.divider()
        st.subheader("2. 건강 분석 결과")

        st.metric("입력 나이", f"{age}세")
        st.write("연령대:", group)
        st.write("연령대별 참고 스트레칭 시간:", f"{stretch_time}분")

        # 스마트폰 사용 습관 분석
        st.subheader("3. 스마트폰 사용 습관")

        phone_result = check_phone_time(use_time)
        st.info(phone_result)

        # 스트레칭 추천
        st.subheader("4. 맞춤형 스트레칭 안내")

        results = recommend_stretching(body_parts)

        for item in results:

            st.markdown(f"### {item['신체 부위']} 스트레칭")

            st.write("추천 시간:", item["추천 시간"])

            for tip in item["스트레칭 방법"]:
                st.write("•", tip)

        # 눈 휴식 안내
        st.subheader("5. 건강관리 추가 조언")

        st.success(
            "눈은 나이와 관계없이 20분마다 "
            "20초 동안 먼 곳을 바라보며 쉬어 주세요."
        )

        st.write("• 스마트폰을 사용할 때 바른 자세 유지하기")
        st.write("• 장시간 같은 자세로 앉아 있지 않기")
        st.write("• 중간중간 일어나 가볍게 움직이기")

        st.caption(
            "※ 스트레칭 시간은 교육용 예시이며 의학적 기준이 아닙니다. "
            "통증이나 어지러움이 생기면 즉시 중단하세요."
        )
