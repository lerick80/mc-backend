from database import SessionLocal, engine
from models import Base, Guest

Base.metadata.create_all(bind=engine)

db = SessionLocal()

db.query(Guest).delete()
db.commit()

guest1 = Guest(name="Erick", code="ABC123", guests_allowed=3, guests_confirmed=0, guest_names="")
guest2 = Guest(name="Familia Pérez", code="XYZ789", guests_allowed=4, guests_confirmed=0, guest_names="")
guest3 = Guest(name="Karla Gómez", code="TEST456", guests_allowed=2, guests_confirmed=0, guest_names="")

db.add_all([guest1, guest2, guest3])
db.commit()
db.close()

print("Invitados de prueba creados.")