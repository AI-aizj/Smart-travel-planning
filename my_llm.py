from langchain_openai import ChatOpenAI
from env_utils import DASHSCOPE_API_KEY, DASHSCOPE_API_URL

llm = ChatOpenAI(
    # model='qwen-max',
    model='qwen3-max',
    # model='qwen3.5-plus',
    temperature=0.5,
    # extra_body={"enable_search": True},
    extra_body={"enable_search": False},
    api_key=DASHSCOPE_API_KEY,
    base_url=DASHSCOPE_API_URL
    )

# llm1 = ChatOpenAI(
#     model='deepseek-r1',
#     temperature=0.5,
#     api_key=DASHSCOPE_API_KEY,
#     base_url=DASHSCOPE_API_URL
# )