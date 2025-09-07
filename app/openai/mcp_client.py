import asyncio
import os

from contextlib import asynccontextmanager
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from app.core.config import env_config

class MySQLMCPClient:
    def __init__(self):
        self.session = None
        # MCP 서버 실행 시 필요한 실행 정보를 담는다.
        # 어떤 명령으로, 어떤 인자를 붙여 어떤 환경에서 실행할지?
        self.server_params = StdioServerParameters(
            command="python",   # 실행할 프로그램
            # 실행할 스크립트/파일 경로
            args=[
                os.path.join(os.path.dirname(__file__), "mysql_mcp_server/src/mysql_mcp_server/server.py")
            ],
            # 환경변수
            env={
                "MYSQL_HOST": env_config.mysql_host,
                "MYSQL_PORT": env_config.mysql_port,
                "MYSQL_USER": env_config.mysql_user,
                "MYSQL_PASSWORD": env_config.mysql_password,
                "MYSQL_DATABASE": env_config.mysql_database,
            }
        )

    @asynccontextmanager
    async def create_session(self):
        """MCP 클라이언트 세션 생성"""
        async with stdio_client(self.server_params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                yield session

    async def get_pet_by_id(self, pet_id: int):
        """ID로 펫 정보 조회"""
        async with self.create_session() as session:
            try:
                result = await session.call_tool(
                    "execute_sql",
                    {"query": f"SELECT * FROM pet WHERE id = {pet_id}"}
                )
                return result.content[0].text if result.content else None
            except Exception as e:
                print(f"Error fetching pet by ID: {e}")
                return None

    async def get_pets_by_owner(self, owner_id: int):
        """소유자 ID로 펫 목록 조회"""
        async with self.create_session() as session:
            try:
                result = await session.call_tool(
                    "execute_sql",
                    {"query": f"SELECT * FROM pet WHERE owner_id = {owner_id}"}
                )
                return result.content[0].text if result.content else None
            except Exception as e:
                print(f"Error fetching pets by owner: {e}")
                return None

    async def get_all_pets(self):
        """모든 펫 정보 조회"""
        async with self.create_session() as session:
            try:
                result = await session.call_tool(
                    "execute_sql",
                    {"query": "SELECT * FROM pet"}
                )
                return result.content[0].text if result.content else None
            except Exception as e:
                print(f"Error fetching all pets: {e}")
                return None

    async def search_pets_by_name(self, name: str):
        """이름으로 펫 검색"""
        async with self.create_session() as session:
            try:
                result = await session.call_tool(
                    "execute_sql",
                    {"query": f"SELECT * FROM pet WHERE name LIKE '%{name}%'"}
                )
                return result.content[0].text if result.content else None
            except Exception as e:
                print(f"Error searching pets by name: {e}")
                return None

    def parse_pet_result(self, result_text: str):
        """SQL 결과를 파싱하여 딕셔너리 리스트로 변환"""
        if not result_text:
            return []
        
        lines = result_text.strip().split('\n')
        if len(lines) < 2:
            return []
        
        # 첫 번째 줄은 컬럼명
        headers = lines[0].split(',')
        pets = []
        
        # 나머지 줄들은 데이터
        for line in lines[1:]:
            values = line.split(',')
            if len(values) == len(headers):
                pet = dict(zip(headers, values))
                pets.append(pet)
        
        return pets


# 사용 예제 함수들
async def get_pet_info(pet_id: int):
    """펫 정보를 가져오는 헬퍼 함수"""
    client = MySQLMCPClient()
    result = await client.get_pet_by_id(pet_id)
    
    if result:
        pets = client.parse_pet_result(result)
        return pets[0] if pets else None
    return None

async def get_owner_pets(owner_id: int):
    """소유자의 모든 펫을 가져오는 헬퍼 함수"""
    client = MySQLMCPClient()
    result = await client.get_pets_by_owner(owner_id)
    
    if result:
        return client.parse_pet_result(result)
    return []

# 테스트용 메인 함수
async def main():
    """테스트용 메인 함수"""
    client = MySQLMCPClient()
    
    # 모든 펫 조회
    print("모든 펫 조회:")
    all_pets = await client.get_all_pets()
    if all_pets:
        pets = client.parse_pet_result(all_pets)
        for pet in pets:
            print(f"ID: {pet.get('id')}, 이름: {pet.get('name')}, 나이: {pet.get('age')}")

if __name__ == "__main__":
    asyncio.run(main())