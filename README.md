# AI Kaos D\u00fczenleyici

Bu depo, kullan\u0131c\u0131lar\u0131n g\u00fcnl\u00fck kaosunu AI yard\u0131m\u0131yla d\u00fczenleyen örnek bir MVP uygulas\u0131 sunar.

## Kurulum

### Backend
1. Python 3 y\u00fckleyin.
2. Gerekli paketleri kurun:
   ```bash
   pip install -r backend/requirements.txt
   ```
3. `.env` dosyas\u0131na API anahtarlar\u0131n\u0131 girin (\u00f6rnek: `OPENAI_API_KEY=YOUR_KEY`).
4. Sunucuyu ba\u015flat\u0131n:
   ```bash
   python backend/app.py
   ```

### Frontend
1. Node.js ve npm kurulu olmal\u0131d\u0131r.
2. `frontend` klas\u00f6r\u00fcne gidip paketleri kurun:
   ```bash
   cd frontend
   npm install
   npm start
   ```
3. Taray\u0131c\u0131da `http://localhost:3000` adresine gidin.

### Testler
```bash
pytest
```

