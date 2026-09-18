from fastmcp.server.auth import TokenVerifier, AccessToken

class KeyVerifier(TokenVerifier):
    async def verify_token(self, token: str) -> AccessToken | None:
        print("verify_token",token)
        # 允许访问
        if token == "130806":
            return AccessToken(
                token=token,
                client_id="1108",
                scopes=[],
                # scopes=["read", "write"],   # 允许访问的权限信息
            )
        else:
            return None