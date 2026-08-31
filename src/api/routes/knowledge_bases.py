from fastapi import APIRouter
from pydantic import BaseModel

from src.application.knowledge_bases.service import KnowledgeBaseService


router = APIRouter(
    prefix="/knowledge-bases",
    tags=["Knowledge Bases"],
)


class CreateKnowledgeBaseRequest(BaseModel):
    name: str
    description: str | None = None


class KnowledgeBaseResponse(BaseModel):
    id: str
    name: str
    description: str | None = None


service = KnowledgeBaseService()


@router.post("/", response_model=KnowledgeBaseResponse)
async def create_knowledge_base(
    request: CreateKnowledgeBaseRequest,
):
    knowledge_base = service.create(
        name=request.name,
        description=request.description,
    )
    return KnowledgeBaseResponse(
        id=str(knowledge_base.id),
        name=knowledge_base.name,
        description=knowledge_base.description,
    )
