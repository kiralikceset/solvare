"""
db.py - SQLAlchemy veritaban\u0131 ayarlar\u0131

Bu dosya veritaban\u0131 nesnesini tan\u0131mlar ve tablolar\u0131 olu\u015fturmak i\u00e7in
`init_db()` fonksiyonunu sa\u011flar.
"""

from flask_sqlalchemy import SQLAlchemy

# SQLAlchemy nesnesi
# Flask uygulamas\u0131 app.py'de bu nesneyi kullanarak veritaban\u0131na ba\u011flan\u0131r

db = SQLAlchemy()


def init_db():
    """Tablolar\u0131 olu\u015fturur."""
    db.create_all()

