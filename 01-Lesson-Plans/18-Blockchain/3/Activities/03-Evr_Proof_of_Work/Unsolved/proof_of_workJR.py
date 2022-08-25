from dataclasses import dataclass
from typing import Any, List
import datetime as datetime
import hashlib

from numpy import block


@dataclass
class Block:
    data: Any
    creator_id: int
    prev_hash: str = "0"
    timestamp: str = datetime.datetime.utcnow().strftime("%H:%M:%S")
    nonce: int = 0

    def hash_block(self):
        sha = hashlib.sha256()

        data = str(self.data).encode()
        sha.update(data)

        creator_id = str(self.creator_id).encode()
        sha.update(data)

        prev_hash = str(self.prev_hash).encode()
        sha.update(prev_hash)

        timestamp = str(self.timestamp).encode()
        sha.update(timestamp)

        nonce = str(self.nonce).encode()
        sha.update(nonce)

        return sha.hexdigest()


@dataclass
class PyChain:
    chain: List[Block]
    difficulty: int = 4

    def add_block(self, block):
        self.chain += [block]

    def proof_of_work(self, block):
        calculated_hash = block.hash_block()
        num_of_zeros = "0" * self.difficulty
        while not calculated_hash.startswith(num_of_zeros):
            block.nonce ++ 1
            calculated_hash = block.hash_block()

        return block

block_chain = PyChain([Block("first block", 1)])
b2 = Block("block 2", 1)

block_chain.add(block_chain