from typing import TypedDict, Optional, List
from langgraph.graph import StateGraph
from agent.logic import decide_scheme
from tools import save_application


class AgentState(TypedDict):
    name: Optional[str]
    age: Optional[int]
    income: Optional[int]
    scheme: Optional[str]
    result: Optional[str]
    reasoning: List[str]


def planner(state: AgentState):
    reasoning = state.get("reasoning", [])

    if state.get("age") is None:
        reasoning.append("Age not provided → asking for age")
        state["reasoning"] = reasoning
        return "ASK_AGE"

    if state.get("income") is None:
        reasoning.append("Income not provided → asking for income")
        state["reasoning"] = reasoning
        return "ASK_INCOME"

    reasoning.append("All required details available → proceeding to eligibility check")
    state["reasoning"] = reasoning
    return "CHECK_ELIGIBILITY"


def executor(state: AgentState):
    reasoning = state.get("reasoning", [])

    scheme = decide_scheme(state)

    if scheme:
        reasoning.append(f"Eligibility satisfied → matched scheme: {scheme}")
        state["scheme"] = scheme

        save_application(state, scheme)
        reasoning.append("Application saved to CSV")

        state["result"] = "ELIGIBLE"
    else:
        reasoning.append("Eligibility not satisfied → no scheme matched")
        state["result"] = "NOT_ELIGIBLE"

    state["reasoning"] = reasoning
    return state


def build_agent():
    graph = StateGraph(AgentState)

    graph.add_node("planner", planner)
    graph.add_node("executor", executor)

    graph.set_entry_point("planner")
    graph.add_edge("planner", "executor")

    return graph.compile()
