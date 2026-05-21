from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import uvicorn
import os
from trip_planner.schemas定义所有数据模型 import TripPlanResponse, TripRequest
from trip_planner.trip_planner_agent多智能体系统核心实现 import get_trip_planner_agent

app = FastAPI(title="AI旅行助手", version="1.0")

@app.get("/favicon.ico")
async def favicon():
    return None

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

planner = get_trip_planner_agent()

@app.post("/api/v1/trip/plan", response_model=TripPlanResponse)
async def plan_trip(request: TripRequest):
    try:
        await planner.initialize()
        plan = await planner.plan_trip(request)
        return TripPlanResponse(success=True, message="规划成功", data=plan)
    except Exception as e:
        return TripPlanResponse(success=False, message=str(e))

@app.get("/")
async def root():
    # 获取当前文件的目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # 返回index.html文件
    return FileResponse(os.path.join(current_dir, "index.html"))

if __name__ == "__main__":
    uvicorn.run("trip_planner.main:app", host="127.0.0.1", port=8000, reload=True)