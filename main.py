from fastapi import FastAPI, HTTPException, Query
import logging
import os

app = FastAPI()

# Loglama yapılandırması: Tüm seviyelerde loglama aktif
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# ========================================
# 10 Adet High Severity Endpoint
# Her biri kasıtlı olarak hata fırlatıp, kritik log kaydı oluşturur.
# ========================================

@app.get("/high-severity1")
async def high_severity_1():
    try:
        raise Exception("Simulated high severity error 1")
    except Exception as e:
        logger.critical(f"High severity error in endpoint 1: {str(e)}")
        raise HTTPException(status_code=500, detail="High severity error in endpoint 1")

@app.get("/high-severity2")
async def high_severity_2():
    try:
        raise Exception("Simulated high severity error 2")
    except Exception as e:
        logger.critical(f"High severity error in endpoint 2: {str(e)}")
        raise HTTPException(status_code=500, detail="High severity error in endpoint 2")

@app.get("/high-severity3")
async def high_severity_3():
    try:
        raise Exception("Simulated high severity error 3")
    except Exception as e:
        logger.critical(f"High severity error in endpoint 3: {str(e)}")
        raise HTTPException(status_code=500, detail="High severity error in endpoint 3")

@app.get("/high-severity4")
async def high_severity_4():
    try:
        raise Exception("Simulated high severity error 4")
    except Exception as e:
        logger.critical(f"High severity error in endpoint 4: {str(e)}")
        raise HTTPException(status_code=500, detail="High severity error in endpoint 4")

@app.get("/high-severity5")
async def high_severity_5():
    try:
        raise Exception("Simulated high severity error 5")
    except Exception as e:
        logger.critical(f"High severity error in endpoint 5: {str(e)}")
        raise HTTPException(status_code=500, detail="High severity error in endpoint 5")

@app.get("/high-severity6")
async def high_severity_6():
    try:
        raise Exception("Simulated high severity error 6")
    except Exception as e:
        logger.critical(f"High severity error in endpoint 6: {str(e)}")
        raise HTTPException(status_code=500, detail="High severity error in endpoint 6")

@app.get("/high-severity7")
async def high_severity_7():
    try:
        raise Exception("Simulated high severity error 7")
    except Exception as e:
        logger.critical(f"High severity error in endpoint 7: {str(e)}")
        raise HTTPException(status_code=500, detail="High severity error in endpoint 7")

@app.get("/high-severity8")
async def high_severity_8():
    try:
        raise Exception("Simulated high severity error 8")
    except Exception as e:
        logger.critical(f"High severity error in endpoint 8: {str(e)}")
        raise HTTPException(status_code=500, detail="High severity error in endpoint 8")

@app.get("/high-severity9")
async def high_severity_9():
    try:
        raise Exception("Simulated high severity error 9")
    except Exception as e:
        logger.critical(f"High severity error in endpoint 9: {str(e)}")
        raise HTTPException(status_code=500, detail="High severity error in endpoint 9")

@app.get("/high-severity10")
async def high_severity_10():
    try:
        raise Exception("Simulated high severity error 10")
    except Exception as e:
        logger.critical(f"High severity error in endpoint 10: {str(e)}")
        raise HTTPException(status_code=500, detail="High severity error in endpoint 10")

# ========================================
# 5 Adet Zafiyet Barındıran (Vulnerable) Endpoint
# Aşağıdaki endpointler, örnek olması amacıyla kullanıcı girdisi üzerinde yeterli kontroller yapmadan
# bazı işlemler gerçekleştirerek zafiyet oluşturma potansiyeli taşır.
# ========================================

@app.get("/vulnerable1")
async def vulnerable_endpoint1(cmd: str = Query(..., description="Çalıştırılacak komut (dikkat: zafiyet içerir)")):
    # Dikkat: Bu kullanım komut enjeksiyonu açığı barındırır.
    os.system(cmd)
    return {"status": "Command executed (vulnerable endpoint 1)"}

@app.get("/vulnerable2")
async def vulnerable_endpoint2(data: str = Query(..., description="İşlenecek veri (zafiyetli)")):
    # Dikkat: Aşağıdaki eval kullanımı zararlı olabilir.
    try:
        result = eval(data)
        return {"result": result}
    except Exception as e:
        return {"error": str(e)}

@app.get("/vulnerable3")
async def vulnerable_endpoint3(query: str = Query(..., description="SQL sorgusu gibi işlenecek veri (örnek zafiyet)") ):
    # Dikkat: Gerçek bir SQL sorgusu olmadığı halde, aşağıdaki string birleştirme yöntemi SQL injection açığına yol açar.
    fake_query = "SELECT * FROM users WHERE name = '" + query + "'"
    return {"query": fake_query}

@app.get("/vulnerable4")
async def vulnerable_endpoint4(filename: str = Query(..., description="Okunacak dosya adı (zafiyet riski)") ):
    # Dikkat: Kullanıcı tarafından belirlenen dosya adını doğrudan açmak Directory Traversal açığı oluşturabilir.
    try:
        with open(filename, "r") as f:
            content = f.read()
        return {"content": content}
    except Exception as e:
        return {"error": str(e)}

@app.get("/vulnerable5")
async def vulnerable_endpoint5(user_input: str = Query(..., description="İşlenecek kullanıcı girdisi (zafiyet içerir)") ):
    # Dikkat: Kullanıcı girdisini doğrudan HTML'e eklemek XSS açığına yol açabilir.
    html_content = f"<html><body>User input: {user_input}</body></html>"
    return {"html": html_content}

# ========================================
# 4 Adet Zafiyetsiz (Güvenli) Endpoint
# Aşağıdaki endpointler, girdilerin doğrulanması, sabit parametre kullanımı gibi tekniklerle daha güvenli bir şekilde yazılmıştır.
# ========================================

@app.get("/secure1")
async def secure_endpoint1():
    return {"status": "This endpoint is secure."}

@app.get("/secure2")
async def secure_endpoint2():
    # Örnek olarak sabit bir mesaj döndüren güvenli endpoint
    message = "Güvenli işlem başarılı."
    return {"message": message}

@app.get("/secure3")
async def secure_endpoint3(number: int = Query(..., description="Sadece tamsayı kabul edilir", gt=0)):
    # Girdi doğrulaması yapılarak güvenli bir hesaplama örneği
    result = number * 2
    return {"input": number, "doubled": result}

@app.get("/secure4")
async def secure_endpoint4():
    # Güvenli endpoint: dış kaynaklara erişim ya da tehlikeli işlemler yapılmaz
    return {"status": "No vulnerabilities here."}

# Uygulamayı çalıştırmak için terminalde: uvicorn main:app --reload
