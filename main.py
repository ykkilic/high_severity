from fastapi import FastAPI, HTTPException
import logging

app = FastAPI()

# Loglama yapılandırması: kritik (CRITICAL) seviyesindeki loglar yakalanır
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

@app.get("/high-severity")
async def high_severity_endpoint():
    try:
        # İşlem sırasında gerçekleşmesi beklenen kritik hata simülasyonu
        raise Exception("Simulated high severity error")
    except Exception as e:
        # Yüksek öncelikli hata durumunu kritik olarak logla
        logger.critical(f"High severity error occurred: {str(e)}")
        # İstemciye HTTP 500 (Internal Server Error) ile dön
        raise HTTPException(status_code=500, detail="High severity error occurred")
