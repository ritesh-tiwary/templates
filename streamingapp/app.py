import cv2
import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles



app = FastAPI()
# Mount the 'templates' and 'static' directory as a static directory
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/templates", StaticFiles(directory="templates"), name="templates")

def get_camera_index():
    # Start with index 0 and check for connected cameras
    index = 0
    while True:
        cap = cv2.VideoCapture(index, cv2.CAP_DSHOW)  # Use cv2.CAP_DSHOW for Windows

        if not cap.isOpened():
            # Camera not found at this index, try the next one
            index += 1
            continue

        # Camera found at index, print information and release the capture
        print(f"Camera found at index: {index}")
        cap.release()
        break

    return index

# Replace 'video_source' with the path to your video file or camera index
video_source = get_camera_index() # 'path_to_video_file_or_camera_index'

async def generate_frames():
    cap = cv2.VideoCapture(video_source)  # Video capture from file or camera

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        elif cv2.waitKey(1) & 0xFF == ord('q'):
            print("Quit!!")
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
                   
    frame.release()
    cap.release()
    cv2.destroyAllWindow()

@app.get("/", response_class=HTMLResponse)
async def home():
    return HTMLResponse(content=open("templates/index.html", "r").read())

@app.get("/video_feed")
async def video_feed():
    return StreamingResponse(generate_frames(), media_type="multipart/x-mixed-replace; boundary=frame")



if __name__ == "__main__":
    uvicorn.run(app)
