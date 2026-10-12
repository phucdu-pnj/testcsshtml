from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Thiết lập đường dẫn gốc
BASE_DIR = Path(__file__).resolve().parent
VIDEO_FILE = BASE_DIR / "static" / "video" / "stock_simulation.gif"

app = FastAPI(title="Mo phong CLT")

# Mount thư mục static
app.mount("/static", StaticFiles(directory="static"), name="static")

# Khởi tạo Jinja2Templates (đặt ở ngoài hàm để dùng chung cho toàn bộ ứng dụng)
templates = Jinja2Templates(directory=BASE_DIR / "templates")

# Duy nhất 1 route cho trang chủ "/"
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"video_available": VIDEO_FILE.is_file()},
    )
@app.get("/health")
async def health():
	return {"status": "ok"}
