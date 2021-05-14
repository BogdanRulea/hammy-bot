import collections
import logging
class Document:
    def __init__(self, connection, document_name):
        self.db = connection[document_name]
        self.logger = logging.getLogger(__name__)

    async def update(self, dict):
        await self.update_by_id(dict)
    
        