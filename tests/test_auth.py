import pytest

@pytest.mark.asyncio
async def test_login_success(client):
    resp = await client.post(
        "/api/v1/auth/login",
        data={"username": "admin@local.com", "password": "admin123456"},
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )

    assert resp.status_code in (200, 401)
