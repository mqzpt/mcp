# import deps
from mcp.server.fastmcp import FastMCP
import json
import requests
from typing import List

# make server
mcp = FastMCP("churnandburn")

# make tool
@mcp.tool()
def PredictChurn(data: List[dict]) -> str:
    """Predicts churn for a list of employees.

    Args:
        data (List[dict]): employee attributes used for the inference
        [{'YearsAtCompany':10,
        'EmployeeSatisfaction':0.5,
        'Position':'Manager',
        'Salary':100000,}]

    Returns:
        str: 1 for chrun, 0 for not churn
    """
    
    payload = data[0]
    response = requests.post(
        "http://127.0.0.1:8000", 
        headers={"Accept": "application/json", "Content-Type": "application/json"}, 
        data=json.dumps(payload))
    
    return response.json()

if __name__ == "main":
    mcp.run(transport="stdio") # run the server