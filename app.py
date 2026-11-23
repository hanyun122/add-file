
import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="맞춤형 건강관리",
    page_icon="💚",
    layout="centered"
)

# 제목
st.title("💚 나이별 맞춤형 건강관리")
st.write("나이와 생활습관에 맞는 스트레칭 방법을 추천합니다.")

st.divider()

# 1. 스트레칭 데이터
stretching_data = {
    "눈": [
        "20초 동안 먼 곳 바라보기",
        "눈을 천천히 깜빡이기",
        "화면에서 눈을 떼고 휴식하기"
    ],
    "목": [
        "고개를 좌우로 천천히 기울이기",
        "어깨를 천천히 위아래로 움직이기",
        "목에 힘을 빼고 편안하게 쉬기"
    ],
    "허리": [
        "의자에 앉아 허리를 편안하게 펴기",
        "상체를 좌우로 무리 없이 움직이기",
        "잠시 일어나 가볍게 걷기"
    ]
}

# 2. 나이에 따른 시간 추천 함수
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


# 3. 스마트폰 사용 시간 분석 함수
def check_phone_time(use_time):

    if use_time >= 8:
        return "스마트폰 사용 시간이 긴 편입니다. 중간중간 휴식하세요."

    elif use_time >= 5:
        return "스마트폰 사용 시간을 조절하고 규칙적으로 쉬어 주세요."

    else:
        return "바른 자세와 규칙적인 휴식 습관을 유지하세요."


# 4. 스트레칭 추천 함수
def recommend_stretching(body_parts, stretch_time):

    for part in body_parts:

        st.subheader(f"💪 {part} 스트레칭")

        if part == "눈":
            st.write("추천 시간: 20초")

        else:
            st.write(f"추천 시간: {stretch_time}분")

        for tip in stretching_data[part]:
            st.write("•", tip)


# 5. 사용자 입력 화면
st.header("1. 건강 정보 입력")

age = st.number_input(
    "나이를 입력하세요",
    min_value=1,
    max_value=120,
    value=17
)


body_parts = st.multiselect(
    "스트레칭이 필요한 부위를 선택하세요.",
    ["눈", "목", "허리"]
)

# 6. 분석 버튼
if st.button("건강 상태 분석하기"):

    if len(body_parts) == 0:
        st.warning("스트레칭 부위를 선택해 주세요.")

    else:

        group, stretch_time = recommend_time(age)

        st.divider()
        st.header("2. 건강 분석 결과")

        st.metric("나이", f"{age}세")
        st.success(f"당신은 {group}에 해당합니다.")

        st.write(
            f"추천 스트레칭 시간: {stretch_time}분"
        )

        st.header("3. 스마트폰 사용 습관 분석")

        st.info(check_phone_time(use_time))

        st.header("4. 맞춤형 스트레칭 안내")

        recommend_stretching(
            body_parts,
            stretch_time
        )

        st.divider()
        st.header("5. 건강관리 추가 조언")

        st.write("• 20분마다 20초 동안 먼 곳 바라보기")
        st.write("• 스마트폰을 사용할 때 바른 자세 유지하기")
        st.write("• 장시간 같은 자세로 앉아 있지 않기")
        st.write("• 중간중간 일어나 가볍게 움직이기")

        st.caption(
            "※ 스트레칭 시간은 교육용 예시입니다. "
            "통증이나 어지러움이 발생하면 즉시 중단하세요."
        )
        
def smartphone_advice(hours, minutes):
    total_minutes = hours * 60 + minutes

    if total_minutes < 60:
        advice = "현재 사용 습관을 유지하고 중간중간 휴식하세요."
    elif total_minutes < 120:
        advice = "스마트폰을 오래 연속해서 사용하지 않도록 주의하세요."
    elif total_minutes < 240:
        advice = "20분마다 먼 곳을 바라보고 자세를 점검하세요."
    elif total_minutes < 360:
        advice = "사용 중간에 휴식 시간을 정하고 스트레칭을 해보세요."
    else:
        advice = "사용 목적을 점검하고 규칙적인 휴식과 신체활동을 늘려보세요."

    return total_minutes, advice

st.subheader("📱 하루 스마트폰 사용시간")

hours = st.number_input(
    "사용 시간(시간)",
    min_value=0,
    max_value=24,
    value=2
)

minutes = st.selectbox(
    "추가 사용 시간(분)",
    [0, 10, 20, 30, 40, 50]
)

if st.button("사용시간 분석하기"):
    total, advice = smartphone_advice(hours, minutes)

    st.write(f"하루 사용시간: {total // 60}시간 {total % 60}분")
    st.success(advice)
