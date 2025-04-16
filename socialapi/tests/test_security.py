import pytest
from socialapi import security

@pytest.mark.asyncio
async def test_get_user(registered_user):
    user = await security.get_user(registered_user["email"])
    assert user["email"] == registered_user["email"]