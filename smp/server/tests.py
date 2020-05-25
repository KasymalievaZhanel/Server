import pytest

@pytest.mark.asyncio
async def test_invalid_going(cli):
    resp = await cli.get('/ciphers')
    assert resp.status == 405