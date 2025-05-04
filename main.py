
from neo4j import GraphDatabase

# Update with your credentials
uri = "bolt://localhost:7687"
user = "neo4j"
password = "12345678"

driver = GraphDatabase.driver(uri, auth=(user, password))

def test_connection(tx):
    result = tx.run("RETURN 'Connected to Neo4j' AS message")
    for record in result:
        print(record["message"])

with driver.session() as session:
    session.execute_read(test_connection)

driver.close()
