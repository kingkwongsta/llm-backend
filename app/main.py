# .venv\Scripts\Activate.ps1
# .\.venv\Scripts\Activate.ps1
# cd .venv && source bin/activate
# uvicorn main:app --reload
# .venv\Scripts\Activate.ps1; cd backend; uvicorn main:app --reload
# cd .venv && source bin/activate && cd .. && cd app && uvicorn main:app --reload

import uvicorn
from os import getenv
from api import app


if __name__ == "__main__":
    port = int(getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port, reload=True)
