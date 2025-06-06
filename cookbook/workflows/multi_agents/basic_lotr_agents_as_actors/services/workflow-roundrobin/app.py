from dapr_agents import RoundRobinOrchestrator
from dotenv import load_dotenv
import asyncio
import logging


async def main():
    try:
        roundrobin_workflow_service = RoundRobinOrchestrator(
            name="Orchestrator",
            message_bus_name="messagepubsub",
            state_store_name="agenticworkflowstate",
            state_key="workflow_state",
            agents_registry_store_name="agentsregistrystore",
            agents_registry_key="agents_registry",
            max_iterations=3,
        ).as_service(port=8004)

        await roundrobin_workflow_service.start()
    except Exception as e:
        print(f"Error starting service: {e}")


if __name__ == "__main__":
    load_dotenv()

    logging.basicConfig(level=logging.INFO)

    asyncio.run(main())
