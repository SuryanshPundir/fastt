import pytest
from httpx import AsyncClient
@pytest.mark.anyio
async def test_create_post(async_client: AsyncClient):
    body = "test post"
    response = await async_client.post("/post", json={"body": body})
    assert response.status_code == 201
    data = response.json()
    assert data["body"] == body
    assert "id" in data

@pytest.mark.anyio
async def test_create_post_with_comment(async_client: AsyncClient, created_post: dict):
    body = "test comment"
    response = await async_client.post("/comment", json={
        "post_id": created_post["id"],
        "body": body
    })
    assert response.status_code == 201
    data = response.json()
    assert data["body"] == body
    assert "id" in data
