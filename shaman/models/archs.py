from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from shaman.models import Base


class Arch(Base):

    __tablename__ = "archs"
    id = Column(Integer, primary_key=True)
    name = Column(String(256), index=True)
    repo_id = Column(Integer, ForeignKey("repos.id"))
    repo = relationship("Repo", back_populates="archs")

    def __init__(self, name, repo):
        self.name = name
        self.repo = repo

