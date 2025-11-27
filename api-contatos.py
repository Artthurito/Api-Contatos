import uuid
from datetime import date
from typing import List, Optional
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel, EmailStr, Field, computed_field
from sqlalchemy import create_engine, Column, String, Date
from sqlalchemy.dialects.sqlite import TEXT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

SQLALCHEMY_DATABASE_URL = "sqlite:///./contatos.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class ContatoDB(Base):
    __tablename__ = "contatos"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    nome = Column(String, nullable=False)
    nascimento = Column(Date, nullable=False)
    email = Column(String, nullable=False)
    telefone = Column(String, nullable=True)
    endereco = Column(String, nullable=True)

Base.metadata.create_all(bind=engine)

class ContatoBase(BaseModel):
    nome: str
    nascimento: date
    email: EmailStr
    telefone: Optional[str] = None
    endereco: Optional[str] = None

class ContatoCreate(ContatoBase):
    pass
class ContatoResponse(ContatoBase):
    id: str
  @computed_field
    def idade(self) -> int:
        hoje = date.today()
        return hoje.year - self.nascimento.year - (
            (hoje.month, hoje.day) < (self.nascimento.month, self.nascimento.day)
        )

    class Config:
        from_attributes = True

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

  app = FastAPI(title="API de Gerenciamento de Contatos")

@app.post("/contatos", response_model=ContatoResponse, status_code=status.HTTP_201_CREATED) # 
def criar_contato(contato: ContatoCreate, db: Session = Depends(get_db)):
    novo_contato = ContatoDB(**contato.model_dump())
    db.add(novo_contato)
    db.commit()
    db.refresh(novo_contato)
    return novo_contato

@app.get("/contatos", response_model=List[ContatoResponse])
def listar_contatos(db: Session = Depends(get_db)):
    contatos = db.query(ContatoDB).order_by(ContatoDB.nome.asc()).all()
    return contatos

@app.put("/contatos/{contato_id}", response_model=ContatoResponse)
def atualizar_contato(contato_id: str, dados_atualizados: ContatoCreate, db: Session = Depends(get_db)):
    contato_existente = db.query(ContatoDB).filter(ContatoDB.id == contato_id).first()

    if not contato_existente:
        raise HTTPException(status_code=404, detail="Contato não encontrado")
    
    contato_existente.nome = dados_atualizados.nome
    contato_existente.nascimento = dados_atualizados.nascimento
    contato_existente.email = dados_atualizados.email
    contato_existente.telefone = dados_atualizados.telefone
    contato_existente.endereco = dados_atualizados.endereco
    
    db.commit()
    db.refresh(contato_existente)
    return contato_existente

@app.delete("/contatos/{contato_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_contato(contato_id: str, db: Session = Depends(get_db)):
    contato_existente = db.query(ContatoDB).filter(ContatoDB.id == contato_id).first()
    
    if not contato_existente:
        raise HTTPException(status_code=404, detail="Contato não encontrado")
    
    db.delete(contato_existente)
    db.commit()
    return None
