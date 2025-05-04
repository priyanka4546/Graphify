
from neo4j import GraphDatabase
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
import os
from dotenv import load_dotenv

load_dotenv()

driver = GraphDatabase.driver(os.getenv("URI"), auth=(os.getenv("USER"), os.getenv("PASSWORD")))

app = FastAPI()

def test_connection(tx):
    result = tx.run("RETURN 'Connected to Neo4j' AS message")
    for record in result:
        print(record["message"])

with driver.session() as session:
    session.execute_read(test_connection)
    
    
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/api/get-all")
def get_all():
    with driver.session() as session:
        result = session.run("MATCH (n) RETURN n")
        nodes = [record["n"] for record in result]
    return {"nodes": nodes}

driver.close()
