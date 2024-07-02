def chatopenai(region,theme,datediff):
    from langchain.chat_models import ChatOpenAI
    from langchain.prompts import PromptTemplate
    import os
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    api_key = OPENAI_API_KEY
    chat_model = ChatOpenAI(openai_api_key=api_key)
    # 지역, 테마
    # 최대 20개  관광지명, 주소, 설명
    template = """
    너는 여행 계획을 짜주는 AI야.
    사용자가 특정 지역으로 어느 기간 동안 여행 계획을 짜달라고 <질문>을 하면
    날짜별로 추천 관광지와 해당 주소를 4개씩 나열해야해.
    같은 날에 비슷한 테마의 관광지는 안겹치게 해줘
    관광지는 중복되면 안돼
    이때 '관광지 : 도로명 주소 : 설명', 형태로 대답해주고, 각 관광지는 반드시 comma(,)로 분리해서 대답해주고, 날짜별로 줄바꿈해줘. 이때 중복되는 단어는 제외해줘. 이외의 말은 하지 마.
    아래와 같은 형식으로 대답해줘
    1일차
    관광지명 : 도로명 주소 : 설명, 관광지명 : 도로명 주소 : 설명, 관광지명 : 도로명 주소 : 설명, 관광지명 : 도로명 주소 : 설명
    2일차
    관광지명 : 도로명 주소 : 설명, 관광지명 : 도로명 주소 : 설명, 관광지명 : 도로명 주소 : 설명, 관광지명 : 도로명 주소 : 설명
    3일차
    관광지명 : 도로명 주소 : 설명, 관광지명 : 도로명 주소 : 설명, 관광지명 : 도로명 주소 : 설명, 관광지명 : 도로명 주소 : 설명
    ...
    n일차
    관광지명 : 도로명 주소 : 설명, 관광지명 : 도로명 주소 : 설명, 관광지명 : 도로명 주소 : 설명, 관광지명 : 도로명 주소 : 설명
    질문:{question}"""
    prompt = PromptTemplate.from_template(template)

    answer = chat_model.predict(prompt.format(question="{} {}의 {}일 여행 계획을 짜줘".format(region,theme,datediff)))
    return answer
    pass
# region = '부산'
# theme = '역사와 문화'
# datediff = 4
# dict_answer = chatopenai(region,theme,datediff)