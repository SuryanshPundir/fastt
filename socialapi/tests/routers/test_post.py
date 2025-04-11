import pytest
from https import AsyncClient
async def create_post(body:str, async_client:AsyncClient)->dict:
    response = await async_client.post("/post", json={"body":body})
    return response.json()


@pytest.fixture()
async def created_post(async_client:AsyncClient)->dict:
    return await create_post("test post", async_client)

@pytest.mark.anyio
async def test_create_post(async_client:AsyncClient):
    name= "test post"
    response = await async_client.post("/post", json={"body":body})
    assert response.status_code == 201
    assert {"id": 1, "body": body}.items() >= response.json().items()

@pytest.mark.anyio
async def test_create_post_with_comment(async_client:AsyncClient, created_post:dict):
    body = "test comment"
    response = await async_client.post(f"/post/{created_post['id']}/comment", json={"body": body})
    assert response.status_code == 201
    assert {"id": 1, "body": body}.items() >= response.json().items()