from neo4j import GraphDatabase

class HelloWorldExample:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def creat_log(self):
        with self.driver.session() as session:
            greeting = session.execute_write(self._creat_log_action)
            print(greeting)

    @staticmethod
    def _creat_log_action(tx):
        historyId="635237545b323455e1b42dc2"
        actionDisplayName="Login"
        sourceIp="211.108.30.234"
        productDisplayName="Sub Account"
        actionSubAccountNo="11111"
        productName="BOTH"

        result = tx.run("CREATE (a:Log) "
                        "SET a.name = $historyId,"
                        "a.actionDisplayName=$actionDisplayName,"
                        "a.sourceIp=$sourceIp, "
                        "a.productDisplayName=$productDisplayName,"
                        "a.actionSubAccountNo=$actionSubAccountNo, "
                        "a.productName=$productName "
                        "RETURN a.message", 
                        historyId=historyId,
                        actionDisplayName=actionDisplayName,
                        sourceIp=sourceIp,
                        productDisplayName=productDisplayName,
                        actionSubAccountNo=actionSubAccountNo,
                        productName=productName,
                        ) 
        return result.single()[0]


if __name__ == "__main__":
    greeter = HelloWorldExample("bolt://localhost:7687", "neo4j", "Tkekrtus123!")
    greeter.creat_log()
    greeter.close()